from django.urls import path
from tutorials import views

urlpatterns = [
    path('api/vetofficers/', views.vetofficers_list),
    path('api/vetofficers/<int:pk>/', views.vetofficer_detail),
    path('api/vetofficers/published/', views.vetofficers_list_published),
]
