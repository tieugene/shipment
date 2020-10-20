import hashlib
import os
import uuid, mimetypes

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


def my_upload_to(instance, filename):
    """
    Generates upload path for FileField
    """
    instance.name = filename
    # return u'temp/%s' % filename
    return 'temp/%s' % uuid.uuid4().hex.upper()


def file_md5(file, block_size=1024 * 14):
    """
    file_md5(file, use_system = False) -> md5sum of "file" as hexdigest string.
    "file" may be a file name or file object, opened for read.
    If "use_system" is True, if possible use system specific program. This ignore, if file object given.
    "block_size" -- size in bytes buffer for calc md5. Used with "use_system=False".
    """
    if isinstance(file, basestring):
        file = open(file, 'rb')
    h = hashlib.md5()
    block = file.read(block_size)
    while block:
        h.update(block)
        block = file.read(block_size)
    return h.hexdigest()


class File(models.Model):
    """
    """
    file = models.FileField(upload_to=my_upload_to, verbose_name=_('File'))
    name = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('File name'))
    mime = models.CharField(db_index=True, blank=False, max_length=255, verbose_name=_('MIME type'))
    ctime = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name=_('Created'))
    size = models.PositiveIntegerField(db_index=True, verbose_name=_('Size'))
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
    print("File pre-save start")
    f = instance.file
    instance.size = f.size
    # mimetypes.guess_type(f.name)
    instance.mime = "application/pdf"
    instance.crc = file_md5(f.file)
    print("File pre-save end")
