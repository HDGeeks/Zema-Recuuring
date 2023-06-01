from rest_framework.viewsets import ModelViewSet
from .models import Mandate,DirectDebitTransaction
from .serializers import MandateSerializer,DirectDebitTransactionSerializer

class CreateDebitMandateViewSet(ModelViewSet):
    queryset=Mandate.objects.all()
    serializer_class=MandateSerializer

class DirectDebitTransactionViewSet(ModelViewSet):
    queryset=DirectDebitTransaction.objects.all()
    serializer_class=DirectDebitTransactionSerializer