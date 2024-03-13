from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, admin
from .forms import SignupForm, AddCustomerForm, AddSupplierForm, AddDetailForm, AddExclusionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from formtools.wizard.views import SessionWizardView
from .models import Customer, Supplier, Detail, Exclusion


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
    if request.method == 'POST':
        if 'confirm_logout' in request.POST:
            logout(request)
            messages.success(request, "You have been logged out...")
            return redirect('home')
    
    return render(request, 'logout_confirm.html')


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
        suppliers = Supplier.objects.filter(customer_id=customer_record)
        details = []
        exclusions = []
        for supplier in suppliers:
            detail = Detail.objects.filter(supplier_id=supplier).first()
            exclusion = Exclusion.objects.filter(supplier_id=supplier).first()
            details.append(detail)
            exclusions.append(exclusion)
        return render(request, 'customer.html', {
            'customer_record': customer_record,
            'suppliers': suppliers,
            'details': details,
            'exclusions': exclusions,
        })
    else:
        messages.success(request, "You must be logged in to view details")
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
    
def update_supplier(request, pk):
    if request.user.is_authenticated:
        update_supp = Supplier.objects.get(id=pk)  
        form = AddSupplierForm(request.POST or None, instance=update_supp)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier has been updated!")
            session_keys_to_remove = ['customer', 'supplier']
            session = request.session
            for key in session_keys_to_remove:
                if key in session:
                    del session[key]
            session.modified = True
            return redirect('home')
        return render(request, 'update_supplier.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def update_detail(request, pk):
    if request.user.is_authenticated:
        update_det = Detail.objects.get(id=pk)  
        form = AddDetailForm(request.POST or None, instance=update_det)
        if form.is_valid():
            form.save()
            messages.success(request, "Details have been updated!")
            return redirect('home')
        return render(request, 'update_detail.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def update_exclusion(request, pk):
    if request.user.is_authenticated:
        update_excl = Exclusion.objects.get(id=pk)  
        form = AddExclusionForm(request.POST or None, instance=update_excl)
        if form.is_valid():
            form.save()
            messages.success(request, "Exclusions have been updated!")
            return redirect('home')
        return render(request, 'update_exclusion.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
FORMS = [("customer", AddCustomerForm),
        ("supplier", AddSupplierForm),
        ("detail", AddDetailForm),
        ("exclusion", AddExclusionForm)]

TEMPLATES = {"customer": "add_customer.html",
            "supplier": "add_supplier.html",
            "detail": "add_detail.html",
            "exclusion": "add_exclusion.html"}

class MyWizardView(LoginRequiredMixin, SessionWizardView):

    form_list = FORMS
    templates = TEMPLATES  

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    
    def done(self, form_list, **kwargs):
                customer_instance = None
                for form in form_list:
                    if form.prefix == 'customer':
                        customer_instance = form.save()
                        self.request.session['customer'] = customer_instance
                        messages.success(self.request, f"{form.prefix} Added...")
                    elif form.prefix == 'supplier':  
                        customer = self.request.session.get('customer')
                        if customer: 
                            form.instance.customer_id = customer
                            customer_instance = form.save()
                            self.request.session['supplier'] = customer_instance
                            messages.success(self.request, f"{form.prefix} Added...")
                    elif form.prefix == 'detail' or 'exclusion':
                        supplier = self.request.session.get('supplier')
                        if supplier: 
                            form.instance.supplier_id = supplier
                            customer_instance = form.save()
                            messages.success(self.request, f"{form.prefix} Added...")                            
                    else:
                        messages.error(self.request, f"{form.prefix} form has errors.")
                        return self.render_goto_step(step=self.steps.current)
                            #pass
                
                session_keys_to_remove = ['customer', 'supplier']
                session = self.request.session
                for key in session_keys_to_remove:
                    if key in session:
                        del session[key]
                session.modified = True
                return redirect('home')           
