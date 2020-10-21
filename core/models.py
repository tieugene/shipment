import hashlib
import os
import uuid, mimetypes
import magic

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext as _


def my_upload_to(instance, filename):
    """
    Generates upload path for FileField
    """
    instance.name = filename
    # return u'temp/%s' % filename
    return 'temp/%s' % uuid.uuid4().hex.upper()


def __get_file_md5(file, block_size=1024 * 14):
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
    block = file.read(block_size)
    while block:
        h.update(block)
        block = file.read(block_size)
    # TODO: iterate over file.chunks() if (file.multiple_chunks())
    # h.update(file.read())  # for InMemoryUploadedFile
    return h.hexdigest()


def __get_file_mime(file):
    """
    @param file:
    - new/replace - django.core.files.uploadedfile.InMemoryUploadedFile (for newly created)
    - edit (w/o changing file itself) - django.core.files.base.File
    From https://stackoverflow.com/questions/4853581/django-get-uploaded-file-type-mimetype
    initial_pos = file.tell()
    file.seek(0)
    mime_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(initial_pos)
    return mime_type
    """
    mime = magic.from_buffer(file.read(), mime=True)
    return mime


class File(models.Model):
    """
    """
    file = models.FileField(upload_to=my_upload_to, verbose_name=_('File'))
    name = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('File name'))
    mime = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('MIME type'))    # option?
    ctime = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name=_('Created'))   # option?
    size = models.PositiveIntegerField(db_index=True, verbose_name=_('Size'))  # option?
    crc = models.UUIDField(db_index=True, verbose_name='CRC')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('file_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')


@receiver(pre_save, sender=File)
def _file_pre_save(sender, instance, **kwargs):
    """
    Define mime, size, crc
    Mime for django: https://medium.com/@ajrbyers/file-mime-types-in-django-ee9531f3035b

    """
    # print("File pre-save start")
    f = instance.file  # FieldFile; f.file = django.core.files.uploadedfile.TemporaryUploadedFile
    # print("File type: {}".format(type(f.file)))
    if isinstance(f.file, InMemoryUploadedFile):
        # instance.name = f.name
        instance.size = f.size
        # mimetypes.guess_type(f.name)
        instance.mime = __get_file_mime(f.file)
        instance.crc = __get_file_md5(f.file)
    # print("File pre-save end")
