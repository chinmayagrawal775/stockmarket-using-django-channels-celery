from django.contrib import admin
from .models import UserSessionId, StockDetail

# Register your models here.
@admin.register(UserSessionId)
class UserSessionIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_id')

admin.site.register(StockDetail)
# @admin.register(StockDetail)
# class StockDetailAdmin(admin.ModelAdmin):
#     list_display = ('id', 'stock', 'user')