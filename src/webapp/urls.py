from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls')),
    path('profile/', views.profile),
    path('logout/', views.logout),
]