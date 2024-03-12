from django.urls import path
from . import views
from .views import MyWizardView

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer_record, name='customer'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    path('add_customer/', MyWizardView.as_view(), name='add_customer'),
    #path('add_customer/', views.add_customer, name='add_customer'),
    path('add_supplier/', MyWizardView.as_view(), name='add_supplier'),
    path('add_detail/', MyWizardView.as_view(), name='add_detail'),
    path('add_exclusion/', MyWizardView.as_view(), name='add_exclusion'),
 ]
