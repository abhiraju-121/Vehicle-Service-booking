from django.contrib import admin
from . models import Vehicle,Cars
# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=['name','price','brand','created_at','is_available','description']
    search_fields=['name','brand']

admin.site.register(Cars)
