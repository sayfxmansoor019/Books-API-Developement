from django.contrib import admin
from .models import Books      #importing the created model

admin.site.register(Books)  #registering model to be displayed on database/site in form of tables