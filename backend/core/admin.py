from django.contrib import admin
from .models import JobCategory, Vacancy, Employer, Area
# Register your models here.

admin.site.register(JobCategory)
admin.site.register(Vacancy)
admin.site.register(Employer)
admin.site.register(Area)
