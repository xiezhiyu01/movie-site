from django.urls import path

from . import views

urlpatterns = [
    path('', views.exploremovie),
    path('explorecelebrity/', views.explorecelebrity),
    path('search/', views.search, name='search'),
    path('movie/<int:movieid>/', views.movie),
    path('celebrity/<int:celebrityid>/', views.celebrity),
]
