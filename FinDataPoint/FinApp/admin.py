from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import OrderRegistration
from .models import accounts
from .models import Marketing
from .models import Sales


admin.site.register(Customer)
admin.site.register(OrderRegistration)
admin.site.register(accounts)
admin.site.register(Marketing)
admin.site.register(Sales)



