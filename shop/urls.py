from django.urls import path

from shop import views
from shop.views import index, create, modal, testing, RegisterUser, LoginUser, logout_user, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='home'),
    path('home',index,name='home'),
    path('home/filter',index,name='filter'),
    path('create',create,name='create'),
    path('modal',modal,name='modal'),
    path('home/<int:pk>/update',views.NewsUpdateView.as_view(),name='update'),
    path('home/<int:pk>/delete',views.DeleteForm.as_view(),name='delete'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',logout_user,name='logout'),
    path('profile',profile,name='profile'),
    path('testing',testing),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)