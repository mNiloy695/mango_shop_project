from django.urls import path,include

from rest_framework.routers import DefaultRouter

from . import views
router=DefaultRouter()

router.register('categories',views.CategorySerializerViewSet)
# router.register('categories',views.CategorySerializerViewSet)
router.register('list',views.MangoSerializerViewSet)
urlpatterns = [
    path('mango/',include(router.urls)),

]

