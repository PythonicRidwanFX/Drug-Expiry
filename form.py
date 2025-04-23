from django import forms
from .models import Drug, Staff
from django import forms
from .models import DrugPurchase, DrugPrice


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields =['drug_name', 'dosage', 'nafdac_reg_n', 'batch_n', 'quantity_in_stock', 'mfg_date', 'exp_date']
        

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'phone_number', 'gender')



class PurchaseForm(forms.ModelForm):
    class Meta:
        model = DrugPurchase
        fields = ['customer_name', 'drug_name', 'dosage', 'price_per_unit', 'quantity']

class DrugPriceForm(forms.ModelForm):
    class Meta:
        model = DrugPrice
        fields = ['drug_name', 'dosage', 'price']