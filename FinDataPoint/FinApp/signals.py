from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Customer
from .models import OrderRegistration
from .models import accounts
from .models import Marketing
from .models import Sales

def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			mobile_phone=instance.username,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)


def registration_form(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.post(name='OrderRegistration')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			mobile_phone=instance.username,
			)
		print('Profile created!')

post_save.connect(registration_form, sender=User)


def accounts_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='accounts')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			mobile_phone=instance.username,
			)
		print('Profile created!')

post_save.connect(accounts_profile, sender=User)


