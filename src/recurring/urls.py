from rest_framework import routers
from .views import CreateDebitMandateViewSet, DirectDebitTransactionViewSet
from recurring.
router = routers.DefaultRouter(trailing_slash=False)


router.register(r"mandate", CreateDebitMandateViewSet, basename="mandate")
router.register(r"transaction", DirectDebitTransactionViewSet, basename="transaction")

urlpatterns = []
urlpatterns += router.urls
