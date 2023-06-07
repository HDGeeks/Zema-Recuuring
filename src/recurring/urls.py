from rest_framework import routers
from .views import DirectDebitTransactionViewSet
from recurring.viewsets.create import CreateDebitMandateViewSet

router = routers.DefaultRouter(trailing_slash=False)


router.register(r"create-mandate", CreateDebitMandateViewSet, basename="mandate")
router.register(r"transaction", DirectDebitTransactionViewSet, basename="transaction")

urlpatterns = []
urlpatterns += router.urls
