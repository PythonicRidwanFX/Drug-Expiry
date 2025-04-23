from django.utils import timezone
from datetime import datetime, timedelta
from .models import Drug
from django.db.models import Q
from .mailer.utils.sendmail import send_drug_expiry_email_alert
import time

def send_expiring_notification():
    today = timezone.now().date()
    expiration_dates = [today + timedelta(days=i) for i in [30, 60, 90]]
    # print(expiration_dates)
    
    # expiration_dates = today + timedelta(days=30)
    # print(expiration_dates)
    
    
    expiring_drugs = Drug.objects.filter(
            Q(exp_date__lte=expiration_dates[0]) |  
            Q(exp_date__lte=expiration_dates[1]) | 
            Q(exp_date__lte=expiration_dates[2])
        )
    
    
    for drug in expiring_drugs:
       
        send_drug_expiry_email_alert('michaelmercy0208@gmail.com', drug_name=drug.drug_name, expiry_date=drug.exp_date)
        drug.has_been_alerted = True
        drug.save()
        time.sleep(11110) # wait for 1 seconds before the next mail is sent
        print(f"Email Sent for {drug.drug_name}")
        
 
 # send_mail(
        #     f'Expiry Alert for {drug.drug_name}',
        #     f'The drug {drug.drug_name} is expiring on {drug.exp_date}.',
        #     ['akintunderidwan113@outlook.com'],  # from email
        #     'akintunderidwan113@gmail.com',  # to email
        #     fail_silently=False,
        # )
        