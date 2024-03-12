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

class Supplier(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    supplier_name = models.CharField(max_length=50)
    supplier_email = models.CharField(max_length=100)
    supllier_phone = models.CharField(max_length=15) 
    supplier_address = models.CharField(max_length=100) 
    supplier_city = models.CharField(max_length=50)
    supplier_country = models.CharField(max_length=50)
    supplier_postcode = models.CharField(max_length=20)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str_(self):
        return f"{self.supplier_name}"

class Detail(models.Model):
    COMPANY_TYPE = (
			('Agricultural', 'Agricultural'),
			('Clothing & Accessories', 'Clothing & Accessories'),
            ('Construction Materials', 'Construction Materials'),
            ('Education & Training', 'Education & Training'),
            ('Financial Services', 'Financial Services'),
            ('Hospitality', 'Hospitality'),
            ('IT Services', 'IT Services'),
            ('Medical Eqipment', 'Medical Eqipment'),
            ('Office Supplies', 'Office Supplies'),
            ('Financial Services', 'Financial Services'),
			)
    LEGAL_FORM = (
			('Sole Trader', 'Sole Trader'),
			('Limited Company', 'Limited Company'),
            ('Charity', 'Charity'),
			)
    created_at = models.DateTimeField(auto_now_add=True)
    company_type = models.CharField(max_length=50, choices=COMPANY_TYPE) 
    legal_form = models.CharField(max_length=50, choices=LEGAL_FORM)
    vat_no = models.CharField(max_length=100) 
    supplier_id = models.OneToOneField(Supplier, on_delete=models.CASCADE)

    def __str_(self):
        return f"{self}"

class Exclusion(models.Model):
    MANDATORY = (
			('Theft', 'Theft'),
			('Fraud', 'Fraud'),
            ('Bribery', 'Bribery'),
			)
    DISCRETIONARY = (
			('Bankruptcy', 'Bankruptcy'),
			('Improper Procurement', 'Improper Procurement'),
            ('Breach of Contract', 'Breach of Contract'),
			)
    created_at = models.DateTimeField(auto_now_add=True)
    mandatory = models.CharField(max_length=50, choices=MANDATORY)
    discretionary = models.CharField(max_length=50, choices=DISCRETIONARY)
    exclusion_date = models.DateField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str_(self):
        return f"{self}"