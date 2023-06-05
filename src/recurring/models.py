from django.db import models

# Create your models here.

class Abstarct(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Mandate(Abstarct):
    """
    A model representing a direct debit mandate.
    """

    mandate_id = models.CharField(max_length=18, primary_key=True)
    agreed_tc = models.BooleanField()
    payer_account_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Direct Debit Mandate"
        verbose_name_plural = "Direct Debit Mandates"

class DirectDebitMandate(Abstarct):
    payer_reference_number = models.CharField(max_length=255)
    agreed_tc = models.IntegerField()
    payee_account_name = models.CharField(max_length=255)
    payer_account_name = models.CharField(max_length=255)
    first_payment_date = models.DateField()
    frequency = models.CharField(max_length=2)
    start_range_of_days = models.IntegerField()
    end_range_of_days = models.IntegerField()
    expiry_date = models.DateField()
    identifier_type = models.IntegerField()
    identifier_value = models.CharField(max_length=255)
    security_credential = models.CharField(max_length=255)
    receiver_identifier_type = models.IntegerField()
    receiver_identifier = models.CharField(max_length=255)
    # Add any additional fields you may need for your application

    def __str__(self):
        return self.payer_reference_number
    
class DirectDebitTransaction(Abstarct):
    """
    A model representing a direct debit transaction.
    """

    mandate = models.ForeignKey(Mandate, on_delete=models.CASCADE)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    request_timestamp = models.DateTimeField()
    status = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Direct Debit Transaction"
        verbose_name_plural = "Direct Debit Transactions"
