from django.db import models

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) 
    address = models.CharField(max_length=100) 
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

# class Supplier(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     supplier_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15) 
#     address = models.CharField(max_length=100) 
#     city = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     postcode = models.CharField(max_length=20)
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

# def __str_(self):
#     return(f"{self.supplier_name}")

# class   Details(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     company_type = models.CharField(max_length=15) 
#     legal_form = models.CharField(max_length=50)
#     vat_no = models.CharField(max_length=100) 
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

# def __str_(self):
#     return(f"{self}")

# class   Exclusions(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     mandatory = models.CharField(max_length=50)
#     discretionary = models.CharField(max_length=100)
#     exclusion_date = models.DateField()
#     company_type = models.CharField(max_length=15) 
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

# def __str_(self):
#     return(f"{self}")