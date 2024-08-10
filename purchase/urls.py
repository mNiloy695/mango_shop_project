from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
# router.register('purchase',views.PurchaseSerializerViewSet)
router.register('review',views.ReviewSerializerViewSet)
router.register('user/addresses',views.AddressViewSet)

urlpatterns = [
   
    path('',include(router.urls)),
    path('purchase/',views.PurchaseSerializerViewSet.as_view(),name="purchase"),
    path('purchase/<int:pk>/',views.PurchaseDetails.as_view(),name="purchase"),

]

# urlpatterns = [
#     path('purchase',views.PurchaseSerializerViewSet.as_view()),
# ]
