from django.contrib import admin
from home.models import img
# Register your models here.
class imageadmin(admin.ModelAdmin):
  list_display=("id","name")

admin.site.register(img,imageadmin)