from django.contrib import admin
from .models import Drug, Staff, DrugPurchase
from django.contrib.auth.models import Group

# Register your models here.
admin.site.unregister(Group)

admin.site.site_header = "Olayiwola Pharmacy Dashboard"

class StaffAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "gender")
    
    
class DrugAdmin(admin.ModelAdmin):
    list_display = ("drug_name", "dosage", "nafdac_reg_n", "batch_n", "quantity_in_stock", "mfg_date", "exp_date")
    
    
admin.site.register(Staff, StaffAdmin)


admin.site.register(Drug, DrugAdmin)

class DrugPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'drug_name', 'dosage', 'price_per_unit', 'quantity')
    
admin.site.register(DrugPurchase, DrugPurchaseAdmin)
