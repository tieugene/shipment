from django.db import models

class Shipper(models.Model):
    '''
    Own 
    '''
    name = models.CharField(unique=True, max_length=16, db_index=True, verbose_name='Name')

    def __unicode__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('shipper_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name', )
        verbose_name = 'Shipper'
        verbose_name_plural = 'Shippers'


class Org(models.Model):
    '''
    Partner
    '''
    name = models.CharField(unique=True, max_length=32, verbose_name='Short name')
    fullname = models.CharField(null=False, blank=False, db_index=True, max_length=64, verbose_name='Full name')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('org_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class DocType(models.Model):
    '''
    Shipment document type 
    '''
    name = models.CharField(unique=True, max_length=16, db_index=True, verbose_name='Name')

    def __unicode__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('shipper_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('name', )
        verbose_name = 'Document type'
        verbose_name_plural = 'Document types'


class Document(models.Model):
    file = models.OneToOneField(File, primary_key=True, verbose_name='File')
    shipper = models.ForeignKey(Shipper, related_name='shipper_document', db_index=True, verbose_name='Shipper')
    org = models.ForeignKey(Org, related_name='org_document', db_index=True, verbose_name='Customer')
    doctype = models.ForeignKey(DocType, null=True, related_name='doctype_document', db_index=True, verbose_name='DocType')
    date = models.DateField(db_index=True, verbose_name='Date')

    def __unicode__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('document_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('date', 'shipper', 'payer')
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
