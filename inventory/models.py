from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

   


class Order(models.Model):
    customer_name  = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return self.drug.price * self.quantity

    def __str__(self):
        return f"{self.customer_name} ordered {self.quantity} pack/packs of {self.drug} for {self.get_total_price()}"
    


    

    
    