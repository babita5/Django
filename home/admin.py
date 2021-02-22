from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Contact)
admin.site.register(ContactInformation)
admin.site.register(HomeInformation)
admin.site.register(Testimonial)