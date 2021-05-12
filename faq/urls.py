from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq, name='faq'),
    path('add/', views.add_faq, name='add_faq'),
    path('delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),
]
