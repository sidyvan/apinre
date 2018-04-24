# URLconf
from django.urls import path

from website import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #path('blog/page<int:num>/', views.page),
]
