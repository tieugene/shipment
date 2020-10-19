import hashlib
import os
import uuid

from django.db import models


def my_upload_to(instance, filename):
    '''
    Generates upload path for FileField
    '''
    instance.name = filename
    # return u'temp/%s' % filename
    return 'temp/%s' % uuid.uuid4().hex.upper()


def file_md5(file, block_size=1024 * 14):
    '''
    file_md5(file, use_system = False) -> md5sum of "file" as hexdigest string.
    "file" may be a file name or file object, opened for read.
    If "use_system" is True, if possible use system specific program. This ignore, if file object given.
    "block_size" -- size in bytes buffer for calc md5. Used with "use_system=False".
    '''
    if isinstance(file, basestring):
        file = open(file, 'rb')
    h = hashlib.md5()
    block = file.read(block_size)
    while block:
        h.update(block)
        block = file.read(block_size)
    return h.hexdigest()

class File(models.Model):
    '''
    '''
    file = models.FileField(upload_to=my_upload_to, verbose_name='File')
    name = models.CharField(db_index=True, blank=False, max_length=255, verbose_name='File name')    # max=130
    mime = models.CharField(db_index=True, blank=False, max_length=255, verbose_name='MIME type')    # max=10
    ctime = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Created')
    size = models.PositiveIntegerField(db_index=True, verbose_name='Size')
    crc = models.UUIDField(db_index=True, verbose_name='CRC')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
