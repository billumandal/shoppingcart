from django.contrib import admin
from models import FourthTry, CustomerProfile, UploadFile, Picture

# class FourthTryInline(admin.TabularInline):
#     model = FourthTry

class FourthTryAdmin(admin.ModelAdmin):
    fields = ('picture_name', 'picture')
    list_display = ('picture_name', 'picture')
    # inlines = [FourthTryInline]

admin.site.register(FourthTry, FourthTryAdmin)