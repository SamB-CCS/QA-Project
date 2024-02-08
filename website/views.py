from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddCustomerForm
from .models import Customer



def home(request):
    customers = Customer.objects.all()


    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('home')
        else:
            messages.success(request, "Incorrect email or password, please try again...")
            return redirect('home')
    else:    
        return render(request, 'home.html', {'customers':customers})


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate & Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered your details!")
            return redirect ('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form':form})
        
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view details")
        return redirect ('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_cust = Customer.objects.get(id=pk)
        delete_cust.delete()
        messages.success(request, "This has been successfully deleted")
        return redirect ('home')
    else:
        messages.success(request, "You must be logged in to view details")
        return redirect ('home')

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_customer.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

def update_customer(request, pk):
    if request.user.is_authenticated:
        update_cust = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=update_cust)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been updated!")
            return redirect('home')
        return render(request, 'update_customer.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')