from django.urls import include,path

from .views import UserCreationViewSet,activate
from . import views
urlpatterns = [
    path('registration/',UserCreationViewSet.as_view(),name='registration'),
    path('activate/<uid64>/<token>/',activate,name='activate'),
    path('login/',views.UserLoginViewSet.as_view(),name='login'),
    path('logout/',views.UserLogoutViewSet.as_view(),name='logout'),
    path('list/',views.UserSerializerViewSetForChecking.as_view(),name='user_list'),
]
