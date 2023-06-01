from django.db import models

# Create your models here.

class Mandate(models.Model):
    """
    A model representing a direct debit mandate.
    """

    mandate_id = models.CharField(max_length=18, primary_key=True)
    agreed_tc = models.BooleanField()
    payer_account_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Direct Debit Mandate"
        verbose_name_plural = "Direct Debit Mandates"


class DirectDebitTransaction(models.Model):
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
