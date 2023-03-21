from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.user),
    path('/<int:id>', views.user_detail),
    path('/<str:nome>', views.user_name),
    
]

