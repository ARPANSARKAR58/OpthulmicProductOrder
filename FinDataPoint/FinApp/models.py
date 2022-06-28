from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True,blank=True)
    address = models.CharField(max_length=200, null=True,blank=True)
    pincode = models.CharField(max_length=20, null=True,blank=True)
    city = models.CharField(max_length=20, null=True,blank=True)
    state = models.CharField(max_length=20, null=True,blank=True)
    custcode = models.CharField(max_length=200, null=True,blank=True)
    country = models.CharField(max_length=20, null=True,blank=True)
    coord_lat= models.CharField(max_length=20, null=True,blank=True)
    coord_lon= models.CharField(max_length=20, null=True,blank=True)
    GSTNO= models.CharField(max_length=200, null=True,blank=True)
    GSTDATE = models.CharField(max_length=20, null=True,blank=True)
    Pan_NO = models.CharField(max_length=20, null=True,blank=True)
    Cust_Type = models.CharField(max_length=20, null=True,blank=True)
    Contact_member_Firstname = models.CharField(max_length=20, null=True,blank=True)
    Contact_member_LastName = models.CharField(max_length=20, null=True,blank=True)
    billing_Cycle = models.CharField(max_length=20, null=True,blank=True)
    EMPID = models.CharField(max_length=20, null=True,blank=True)
    consaltant_Id = models.CharField(max_length=20, null=True,blank=True)
    pic = models.ImageField(default="Adherdoc.png", null=True, blank=True)
    # phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(max_length=17, blank=True, null=True)
    email= models.CharField(max_length=200, null=True,blank=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.custcode}: {self.email}:{self.date_created}"



class OrderRegistration(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    application_name = models.CharField(max_length=200, null=True)
    castomer_code = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.custcode}: {self.email}:{self.date_created}"
    


class accounts(models.Model):
    CustomerCode = models.CharField(max_length=15, null=False)
    CustomerName = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    PinCode = models.CharField(max_length=15, null=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=45, null=True)
    State = models.CharField(max_length=45, null=True)
    Country = CountryField(blank=True, null=True)
    continent = CountryField(max_length=45, null=True)
    coord_lat = models.CharField(max_length=9, null=True)
    coord_long = models.CharField(max_length=9, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
    noPhone = models.CharField(validators=[phone_regex], verbose_name=_("Land phone"), max_length=50, blank=True, null=True)
    noMobile = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=50, blank=True, null=True)
    noFax = models.CharField(validators=[phone_regex], verbose_name=_("Fax no"), max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, null=True)
    GSTINNO = models.CharField(max_length=45, null=True)
    GSTINDate = models.DateTimeField(auto_now_add=True, null=True)
    RegistrationNo = models.CharField(max_length=45, null=True)
    TypeCustomer = models.CharField(max_length=45, null=True)
    ContactFirstName = models.CharField(max_length=45, null=True)
    ContactLastName = models.CharField(max_length=45, null=True)
    billingCycle = models.CharField(max_length=20, null=True,blank=True)
    employeeId = models.CharField(max_length=45, null=False)
    consultantId = models.CharField(max_length=45, null=False)

    # class Meta:
    #     db_table = 'accounts'

    def __str__(self):
        return f"{self.name}: {self.custcode}: {self.email}:{self.date_created}"


class Marketing(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    application_name = models.CharField(max_length=200, null=True)
    castomer_code = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=_("Enter a valid international mobile phone number starting with +(country code)"))
    mobile_phone = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.custcode}: {self.email}:{self.date_created}"


class Sales(models.Model):
    invoiceId = models.CharField(max_length=255, null=False)
    invoiceDate = models.DateTimeField(auto_now_add=True, null=True)
    customerId = models.CharField(max_length=255, null=True)
    Country = CountryField(max_length=45, null=True)
    tsds = models.CharField(max_length=255, null=True)
    lensIndex = models.CharField(max_length=40, null=True, blank=True)
    lensFocality = models.CharField(max_length=255, null=True)
    prodBrand = models.CharField(max_length=255, null=True)
    prodSubBrand = models.CharField(max_length=255, null=True)
    itemGroupId = models.CharField(max_length=255, null=False)
    lensSold = models.CharField(max_length=255, null=False)
    coating = models.CharField(max_length=255, null=False)
    soldQuantity = models.CharField(max_length=255, null=True)
    lensSoldValue = models.CharField(max_length=30, null=True)
    discount = models.CharField(max_length=30, null=True)
    lensNetSaleValue = models.CharField(max_length=30, null=True)
    

    # class Meta:
    #     db_table = 'Sales'


    def __str__(self):
        return f"{self.name}: {self.custcode}: {self.email}:{self.date_created}"



