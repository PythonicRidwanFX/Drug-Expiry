from django.db import models
from django.contrib.auth.models import User




class Staff(models.Model):
    first_name =models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    gender = models.CharField(max_length=55, null=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.phone_number + " " + self.gender
    

class Drug(models.Model):
    drug_name = models.CharField(max_length=100, null=True)
    dosage = models.CharField(max_length=20, null=True)
    nafdac_reg_n = models.CharField(max_length=20, null=True)
    batch_n = models.CharField(max_length=20, null=True)
    quantity_in_stock = models.CharField(max_length=20, null=True)
    mfg_date = models.DateField(max_length=20, null=True)
    exp_date = models.DateField(max_length=20, null=True)

    
    
    def __str__(self):
        return self.drug_name + "  " + self.dosage + "  " + self.nafdac_reg_n + "  " + self.batch_n + "  " + self.quantity_in_stock 
    

class DrugPurchase(models.Model):
    customer_name = models.CharField(max_length=200)
    drug_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.price_per_unit * self.quantity
        super().save(*args, **kwargs)
   
        
        
    def __str__(self):
        return f"{self.customer_name} - {self.drug_name}"

class DrugPrice(models.Model):
    drug_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
