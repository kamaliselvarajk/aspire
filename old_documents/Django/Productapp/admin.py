from django.contrib import admin

# Register your models here.
#from django.apps import apps
from .models import *
# from .views import *

admin.site.register(Product)
#admin.site.register(display())