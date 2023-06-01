from gift import serializers
from .models import *

class MandateSerializer(serializers.ModelSerializer):
    """
    A serializer for the Mandate model.
    """

    class Meta:
        model = Mandate
        fields = (
            "mandate_id",
            "agreed_tc",
            "payer_account_name",
        )


class DirectDebitTransactionSerializer(serializers.ModelSerializer):
    """
    A serializer for the DirectDebitTransaction model.
    """

    class Meta:
        model = DirectDebitTransaction
        fields = (
            "mandate",
            "fee_amount",
            "request_timestamp",
            "status",
        )