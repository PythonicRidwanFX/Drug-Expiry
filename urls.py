from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='dashboard-front_page'),
    path('index/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('addstaff/', views.addstaff, name='dashboard-addstaff'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='dashboard-staff-delete'),
    path('staff/update/<int:pk>/', views.staff_update, name='dashboard-staff-update'),
    path('drug/delete/<int:pk>/', views.drug_delete, name='dashboard-drug-delete'),
    path('drug/update/<int:pk>/', views.drug_update, name='dashboard-drug-update'),
    path('drug/', views.drug, name='dashboard-drug'),
    path('adddrug/', views.adddrug, name='dashboard-adddrug'),
    path('print-drug-records/', views.print_drug_records, name='print_drug_records'),
    path('purchase/', views.purchase_name, name='purchase_name'),
    path('add-purchase/', views.add_purchase, name='dashboard-add_purchase'),
    path('drug-price/', views.price_record, name='price_record'),
    path('update-drug-price/<int:pk>/', views.update_drug_price, name='dashboard-update-drug'),
    path('delete-drug-price/<int:pk>/', views.delete_drug_price, name='dashboard-delete-drug'),
    path('drug-report/', views.drug_report, name='drug_report'),
    path('support/', views.support_page, name='support_page'),
    
]
