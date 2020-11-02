from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import gettext as _

from core.models import File


class Shipper(models.Model):
    """
    Own
    """
    name = models.CharField(unique=True, max_length=16, db_index=True, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('Shipper')
        verbose_name_plural = _('Shippers')


class Org(models.Model):
    """
    Partner
    """
    name = models.CharField(unique=True, max_length=32, verbose_name=_('Short name'))
    fullname = models.CharField(null=True, blank=True, db_index=True, max_length=64, verbose_name=_('Full name'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('org_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name',)
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


class DocType(models.Model):
    """
    Shipment document type
    """
    name = models.CharField(unique=True, max_length=16, db_index=True, verbose_name=_('Name'))
    fullname = models.CharField(null=True, blank=True, db_index=True, max_length=64, verbose_name=_('Full name'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('Document type')
        verbose_name_plural = _('Document types')


class Document(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE, primary_key=True, verbose_name=_('File'))
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, related_name='shipper_document', db_index=True,
                                verbose_name=_('Shipper'))
    org = models.ForeignKey(Org, on_delete=models.CASCADE, related_name='org_document', db_index=True,
                            verbose_name=_('Customer'))
    date = models.DateField(db_index=True, verbose_name=_('Date'))
    doctype = models.ForeignKey(DocType, on_delete=models.CASCADE, null=True, blank=True, related_name='doctype_document',
                                db_index=True, verbose_name=_('Type'))
    comments = models.CharField(null=True, blank=True, db_index=True, max_length=255, verbose_name=_('Note'))

    def __str__(self):
        return "{} => {} {} {} ({})".format(self.shipper, self.org, self.date, self.doctype, self.comments)

    def get_absolute_url(self):
        return reverse('doc_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-date', 'shipper', 'org')
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')


@receiver(post_delete, sender=Document)
def _doc_post_delete(sender, instance, **kwargs):
    File.objects.get(pk=instance.pk).delete()
