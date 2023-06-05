from rest_framework.viewsets import ModelViewSet
from .models import Mandate, DirectDebitTransaction
from .serializers import MandateSerializer, DirectDebitTransactionSerializer


class DirectDebitTransactionViewSet(ModelViewSet):
    queryset = DirectDebitTransaction.objects.all()
    serializer_class = DirectDebitTransactionSerializer
