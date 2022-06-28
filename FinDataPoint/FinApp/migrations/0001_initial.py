# Generated by Django 3.0 on 2022-06-21 09:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerCode', models.CharField(max_length=15)),
                ('CustomerName', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('PinCode', models.CharField(max_length=15, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('District', models.CharField(max_length=45, null=True)),
                ('State', models.CharField(max_length=45, null=True)),
                ('Country', django_countries.fields.CountryField(max_length=45, null=True)),
                ('continent', django_countries.fields.CountryField(max_length=45, null=True)),
                ('coord_lat', models.CharField(max_length=9, null=True)),
                ('coord_long', models.CharField(max_length=9, null=True)),
                ('noPhone', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Land phone')),
                ('noMobile', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone')),
                ('noFax', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Fax no')),
                ('email', models.CharField(max_length=50, null=True)),
                ('GSTINNO', models.CharField(max_length=45, null=True)),
                ('GSTINDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('RegistrationNo', models.CharField(max_length=45, null=True)),
                ('TypeCustomer', models.CharField(max_length=45, null=True)),
                ('ContactFirstName', models.CharField(max_length=45, null=True)),
                ('ContactLastName', models.CharField(max_length=45, null=True)),
                ('billingCycle', models.CharField(blank=True, max_length=20, null=True)),
                ('employeeId', models.CharField(max_length=45)),
                ('consultantId', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('application_name', models.CharField(max_length=200, null=True)),
                ('castomer_code', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('application_name', models.CharField(max_length=200, null=True)),
                ('castomer_code', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceId', models.CharField(max_length=255)),
                ('invoiceDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('customerId', models.CharField(max_length=255, null=True)),
                ('tsds', models.CharField(max_length=255, null=True)),
                ('lensIndex', models.CharField(blank=True, max_length=40, null=True)),
                ('lensFocality', models.CharField(max_length=255, null=True)),
                ('prodBrand', models.CharField(max_length=255, null=True)),
                ('prodSubBrand', models.CharField(max_length=255, null=True)),
                ('itemGroupId', models.CharField(max_length=255)),
                ('lensSold', models.CharField(max_length=255)),
                ('coating', models.CharField(max_length=255)),
                ('soldQuantity', models.CharField(max_length=255, null=True)),
                ('lensSoldValue', models.CharField(max_length=30, null=True)),
                ('discount', models.CharField(max_length=30, null=True)),
                ('lensNetSaleValue', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('custcode', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('coord_lat', models.CharField(blank=True, max_length=20, null=True)),
                ('coord_lon', models.CharField(blank=True, max_length=20, null=True)),
                ('GSTNO', models.CharField(blank=True, max_length=200, null=True)),
                ('GSTDATE', models.CharField(blank=True, max_length=20, null=True)),
                ('Pan_NO', models.CharField(blank=True, max_length=20, null=True)),
                ('Cust_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('Contact_member_Firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('Contact_member_LastName', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_Cycle', models.CharField(blank=True, max_length=20, null=True)),
                ('EMPID', models.CharField(blank=True, max_length=20, null=True)),
                ('consaltant_Id', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.ImageField(blank=True, default='Adherdoc.png', null=True, upload_to='')),
                ('mobile_phone', models.CharField(blank=True, max_length=17, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]