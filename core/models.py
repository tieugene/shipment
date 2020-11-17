"""
core.models
"""
import hashlib
import os
import magic

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.utils.translation import gettext as _

DEFAULT_SORT_FILE = '-pk'

def my_upload_to(instance, filename):
    """
    Generates upload path for FileField
    """
    import uuid
    instance.name = filename
    # return 'temp/%s' % filename
    return 'temp/%s' % uuid.uuid4().hex.upper()


class File(models.Model):
    """
    """
    file = models.FileField(upload_to=my_upload_to, verbose_name=_('File'))  # ...
    name = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('Name'))
    mime = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('MIME type'))  # option?
    ctime = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name=_('Created'))  # option?
    size = models.PositiveIntegerField(db_index=True, editable=False, verbose_name=_('Size'))  # option?
    crc = models.UUIDField(unique=True, max_length=32, blank=False, editable=False, verbose_name='CRC')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('file_view', kwargs={'pk': self.pk})

    def get_filename(self):
        s = '%09d' % self.pk
        return os.path.join(s[:3], s[3:6], s[6:])

    def get_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.get_filename())

    class Meta:
        ordering = (DEFAULT_SORT_FILE,)
        verbose_name = _('File')
        verbose_name_plural = _('Files')


def get_file_crc(file, block_size=1024 * 14):
    """
    file_md5(file, use_system = False) -> md5sum of "file" as hexdigest string.
    "file" may be a file name or file object, opened for read.
    If "use_system" is True, if possible use system specific program. This ignore, if file object given.
    "block_size" -- size in bytes buffer for calc md5. Used with "use_system=False".
    @param file: in admin
    - new/replace - django.core.files.uploadedfile.InMemoryUploadedFile (for newly created)
    - edit (w/o changing file itself) - django.core.files.base.File
    """
    h = hashlib.md5()
    # if isinstance(file, basestring):
    #    file = open(file, 'rb')
    pos = file.tell()
    file.seek(0)
    block = file.read(block_size)
    while block:
        h.update(block)
        block = file.read(block_size)
    file.seek(pos)
    # TODO: iterate over file.chunks() if (file.multiple_chunks())
    # h.update(file.read())  # for InMemoryUploadedFile
    return h.hexdigest()


def get_file_mime(fobj):
    """
    @param fobj:InMemoryUploadedFile
    - new/replace - django.core.files.uploadedfile.InMemoryUploadedFile (for newly created)
    - edit (w/o changing file itself) - django.core.files.base.File
    From https://stackoverflow.com/questions/4853581/django-get-uploaded-file-type-mimetype
    initial_pos = file.tell()
    file.seek(0)
    mime_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(initial_pos)
    return mime_type
    """
    pos = fobj.tell()
    fobj.seek(0)
    # depricated (python3-magic)
    # mime = magic.from_buffer(fobj.read(), mime=True)
    # new (python3-file-magic)
    mime = magic.detect_from_content(fobj.read(1024)).mime_type
    fobj.seek(pos)
    return mime


@receiver(pre_save, sender=File)
def _file_pre_save(sender, instance, **kwargs):
    """
    Define mime, size, crc
    Mime for django: https://medium.com/@ajrbyers/file-mime-types-in-django-ee9531f3035b
    Uploaded is django.core.files.uploadedfile.InMemoryUploadedFile (small)/ TemporaryUploadedFile (3MB+)
    """
    # print("File pre-save start")
    f = instance.file  # FieldFile; f.file = django.core.files.uploadedfile.TemporaryUploadedFile
    # print("File type: {}".format(type(f.file)))
    if isinstance(f.file, InMemoryUploadedFile) or isinstance(f.file, TemporaryUploadedFile):
        instance.name = f.name
        instance.size = f.size
        # mimetypes.guess_type(f.name)
        instance.mime = get_file_mime(f.file)
        instance.crc = get_file_crc(f.file)
    # print("File pre-save end")


@receiver(post_save, sender=File)
def _file_post_save(sender, instance, created, **kwargs):
    """
    Powered by https://dev.retosteffen.ch/2017/09/django-uploading-image-post_save/
    """
    if created:
        file = instance.file
        old_name = file.name
        if not old_name:    # ?
            return
        new_name = instance.get_filename()
        new_path = instance.get_path()
        new_dir = os.path.dirname(new_path)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        os.rename(file.path, new_path)
        # print("File renamed from {} to {}".format(file.path, new_path))
        instance.file.name = new_name
        instance.save()


@receiver(pre_delete, sender=File)
def _file_delete(sender, instance, **kwargs):
    # p = instance.get_path()
    p = os.path.join(settings.MEDIA_ROOT, instance.file.name)
    if os.path.exists(p):
        os.unlink(p)
