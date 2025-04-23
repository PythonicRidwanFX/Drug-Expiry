from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Drug, Staff
from django.contrib.auth.models import User
from .form import DrugForm, StaffForm
from django.contrib import messages
from django.http import HttpResponse
from .models import DrugPurchase as Purchase
import logging
from .form import PurchaseForm

logger = logging.getLogger(__name__)

# Create your views here.

@login_required
def index(request):
    staff_count  = Staff.objects.all().count()
    items_count = Drug.objects.all().count()
    
    
    context = {
        
        'staff_count': staff_count,
        "items_count": items_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    #staff_view = Staff.objects.raw('SELECT * FROM dashboard_staff')
    staff_view  = Staff.objects.all()
    staff_count = staff_view.count()
    items_count = Drug.objects.all().count()
    context = {
        'staff_view': staff_view,
        'staff_count': staff_count,
        "items_count": items_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def addstaff(request):
    staff_count  = Staff.objects.all().count()
    items_count = Drug.objects.all().count()
    if request.method=='POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            staff_name = form.cleaned_data.get("first_name")
            messages.success(request, f'{staff_name} has been added')
            return redirect('dashboard-addstaff')
    else:
        form = StaffForm()
        context = {
            'form': form,
            'staff_count': staff_count,
            "items_count": items_count,
        }
    return render(request, 'dashboard/addstaff.html', context)

def staff_delete(request, pk):
    item = Staff.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('dashboard-staff')
    return render(request, 'dashboard/staff_delete.html')

def staff_update(request, pk):
    item = Staff.objects.get(id=pk)
    if request.method == 'POST':
        form =StaffForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staff')
    else:
        form = StaffForm(instance=item)
    context ={
        'form': form,
    }
    return render(request, 'dashboard/staff_update.html', context)

@login_required
def drug(request):
    #items = Drug.objects.raw('SELECT * FROM dashboard_drug')
    items = Drug.objects.all()
    items_count = items.count()
    staff_count  = Staff.objects.all().count()
    context = {
        'items': items,
        'staff_count': staff_count,
        "items_count": items_count,
    }
    return render(request, 'dashboard/drug.html', context)

@login_required
def adddrug(request):
    staff_count  = Staff.objects.all().count()
    items_count = Drug.objects.all().count()
    if request.method=='POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            drug_name = form.cleaned_data.get("drug_name")
            messages.success(request, f'{drug_name} has been added')
            return redirect('dashboard-adddrug')
    else:
        form = DrugForm()
        context = {
            'form': form,
            'staff_count': staff_count,
            "items_count": items_count,
        }
    return render(request, 'dashboard/adddrug.html', context)

def drug_delete(request, pk):
    item = Drug.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('dashboard-drug')
    return render(request, 'dashboard/drug_delete.html')

def drug_update(request, pk):
    item = Drug.objects.get(id=pk)
    if request.method == 'POST':
        form =DrugForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-drug')
    else:
        form = DrugForm(instance=item)
    context ={
        'form': form,
    }
    return render(request, 'dashboard/drug_update.html', context)




# asert/views.py


# Initialize the Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def my_view(request):
    # Set a key-value pair in Redis
    redis_client.set('foo', 'bar')

    # Retrieve the value
    value = redis_client.get('foo')

    # Return a response
    return HttpResponse(f"The value of 'foo' is: {value.decode('utf-8')}")


def print_drug_records(request):
    drugs = Drug.objects.all()
    print(drugs)
    return render(request, 'dashboard/print_drug_records.html', {'drugs': drugs})



def purchase_name(request):
    purchases = Purchase.objects.all()
    return render(request, 'dashboard/purchase_name.html', {'purchases': purchases})

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data.get('customer_name')
            messages.success(request, f'{customer_name} has made a purchase.')
            return redirect('dashboard-add_purchase')  # Redirect to the same page
    else:
        form = PurchaseForm()

    return render(request, 'dashboard/add_purchase.html', {'form': form})