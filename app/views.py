from django.shortcuts import render, redirect
from .forms import MedicineCraeteForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User,Medicines
from django.urls import reverse
from django.db import IntegrityError



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

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Authenticate against MedicineUser model
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            
            if username == "Manager":
                login(request, user)
                return render(request, "app/addMedicine.html")
            else:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "logins/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "logins/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "logins/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "logins/register.html")