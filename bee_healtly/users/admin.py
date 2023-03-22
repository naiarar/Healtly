from django.contrib import admin
from .models import User, Measurements, Training_level

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'training_level')
    list_filter = ('training_level',)
    search_fields = ('name',)



admin.site.register(User, UserAdmin)
admin.site.register(Measurements)
admin.site.register(Training_level)
