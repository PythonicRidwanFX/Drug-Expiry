from django.urls import path
from .views import print_drug_records
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('addstaff/', views.addstaff, name='dashboard-addstaff'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='dashboard-staff-delete'),
    path('staff/update/<int:pk>/', views.staff_update, name='dashboard-staff-update'),
    path('drug/delete/<int:pk>/', views.drug_delete, name='dashboard-drug-delete'),
    path('drug/update/<int:pk>/', views.drug_update, name='dashboard-drug-update'),
    path('drug/', views.drug, name='dashboard-drug'),
    path('adddrug/', views.adddrug, name='dashboard-adddrug'),
    path('print-drug-records/', print_drug_records, name='print-drug-records'),
]
