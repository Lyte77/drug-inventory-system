from django.contrib import admin
from .models import (
    Drug,
    Order
    
)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'drug', 'quantity')
    search_fields = ('customer_name', 'drug')
    list_filter = ['drug']

    def customer_total(self,obj):
        orders = Order.objects.filter(customer_name=obj.customer_name)
        return sum(order.get_total_price() for order in orders)

        customer_total.short_description = "Total Order Amount"


admin.site.register(Drug)
admin.site.register(Order,OrderAdmin)

