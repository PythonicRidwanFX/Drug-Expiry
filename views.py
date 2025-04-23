from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Drug, Staff, DrugPurchase
from django.contrib.auth.models import User
from .form import DrugForm, StaffForm, PurchaseForm
from django.contrib import messages
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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

from django.shortcuts import render

def front_page(request):
    return render(request, 'dashboard/front_page.html')

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
        drugs = Drug.objects.all()
        context = {
            'form': form,
            'drugs': drugs,
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



def print_drug_records(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="drug_records.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Drug Report Olayiwola Pharmacy")

    p.setFont("Helvetica-Bold", 10)
    y_position = height - 100
    p.drawString(50, y_position, "Drug Name")
    p.drawString(170, y_position, "NAFDAC REG. NO")
    p.drawString(270, y_position, "BATCH NO")
    p.drawString(370, y_position, "Quantity")
    p.drawString(450, y_position, "MFG.Date")
    p.drawString(530, y_position, "Expiry Date")
    y_position -= 20

    drugs = Drug.objects.all()

    p.setFont("Helvetica", 10)
    for drug in drugs:
        if y_position < 50:  # Check if a new page is needed
            p.showPage()
            y_position = height - 100
            p.setFont("Helvetica-Bold", 10)
            p.drawString(50, y_position, "Drug Name")
            p.drawString(200, y_position, "NAFDAC REG. NO")
            p.drawString(280, y_position, "BATCH NO")
            p.drawString(370, y_position, "Quantity")
            p.drawString(450, y_position, "MFG. DATE")
            p.drawString(530, y_position, "Expiry Date")
            y_position -= 20
            p.setFont("Helvetica", 10)

        p.drawString(50, y_position, drug.drug_name)
        p.drawString(200, y_position, str(drug.nafdac_reg_n))
        p.drawString(280, y_position, str(drug.batch_n))
        p.drawString(370, y_position, str(drug.quantity_in_stock))
        p.drawString(450, y_position, drug.mfg_date.strftime('%Y-%m-%d'))
        p.drawString(530, y_position, drug.exp_date.strftime('%Y-%m-%d'))
        y_position -= 20

    p.save()
    return response


def purchase_name(request):
    return render(request, 'dashboard/purchase_name.html')

def purchase_name(request):
    purchases = DrugPurchase.objects.all()
    context = {'purchases': purchases}
    return render(request, 'dashboard/purchase_name.html', context)



def add_purchase(request):
    staff_count  = Staff.objects.all().count()
    items_count = Drug.objects.all().count()
    if request.method=='POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data.get("customer_name")
            messages.success(request, f'{customer_name} has been added')
            return redirect('dashboard-add_purchase')
    else:
        form = PurchaseForm()
        context = {
            'form': form,
            'staff_count': staff_count,
            "items_count": items_count,
        }
    return render(request, 'dashboard/add_purchase.html', context)



def price_record(request):
    return render(request, 'dashboard/price_record.html')

def drug_report(request):
    return render(request, 'dashboard/drug_report.html')

def support_page(request):
    return render(request, 'dashboard/support.html')


def update_drug_price(request, pk):
    item = DrugPrice.objects.get(id=pk)
    if request.method == 'POST':
        form =DrugPriceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('price_record')
    else:
        form = DrugPriceForm(instance=item)
    context ={
        'form': form,
    }
    return render(request, 'dashboard/update_drug_price.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Drug
from .form import DrugPriceForm, DrugPrice

def price_record(request):
    if request.method == 'POST':
        form = DrugPriceForm(request.POST)
        if form.is_valid():
            form.save()
            drug_name = form.cleaned_data.get("drug_name")
            messages.success(request, f"{drug_name} has been added successfully!")
            return redirect('price_record') 
    else:
        form = DrugPriceForm()

    price_view = DrugPrice.objects.all()

    context = {
        'form': form,
        'price_view': price_view,
    }
    return render(request, 'dashboard/price_record.html', context)

def delete_drug_price(request, pk):
    item = DrugPrice.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('price_record')
    return render(request, 'dashboard/delete_price.html')