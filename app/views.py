from django.shortcuts import render, redirect
from .forms import MedicineCraeteForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User,Medicines

def home(request):
    data = Medicines.objects.all()
    context = {"data":data}

    return render(request, "app/showMedicines.html",context)
def nonhome(request):
    data = Medicines.objects.all()
    context = {"data":data}

    return render(request, "app/nonhome.html",context)

def AddMedicine(request):
    form = MedicineCraeteForm()
    if request.method == 'POST':
        data = MedicineCraeteForm(request.POST)
        if data.is_valid():
            print("valid")
            user = data.save(commit=False)
            user.host = request.user
            user.save()
            return redirect('home')
    context = {"form":form}
    return render(request, "app/AddMedicine.html", context)

def UpdateMedicine(request, medicine_id):
    medicine_instance = Medicines.objects.get( id=medicine_id)
    form = MedicineCraeteForm(instance=medicine_instance)
    if request.method == 'POST':
        data = MedicineCraeteForm(request.POST, instance=medicine_instance)
        print(data)
        # if form.is_valid():
        updated_medicine = data.save(commit=False)
        updated_medicine.host = request.user
        updated_medicine.save()

        return redirect('home')
    context = {"form": form, "medicine_instance": medicine_instance}
    return render(request, "app/AddMedicine.html", context)
def DeleteMedicine(request,medicine_id):
    
    medicine_instance = Medicines.objects.get( id=medicine_id)
    Medicines.delete(medicine_instance)
    return redirect('home')