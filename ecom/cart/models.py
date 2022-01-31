from django.db import models

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="media",max_length=5000, null=True, blank=True)

    """def __str__(self):
        return self.productname,self.price,self.description"""

    def __str__(self):
        template = '{0.productname} {0.price} {0.description}{0.image}'
        return template.format(self)
class contacts(models.Model):
    name=models.CharField(max_length=100,null=True)
    Email=models.EmailField(max_length=100,null=True)
    mobile=models.BigIntegerField()
    message=models.TextField()

class Cart(models.Model):
    #user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE,null=True)
    #productname=models.ForeignKey(Product,verbose_name="product", on_delete=models.CASCADE)
    #productname = models.CharField(max_length=200,null=True)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    #description = models.TextField()
    #image = models.ImageField(upload_to="media",max_length=5000, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    def __str__(self):
        template = '{0.product_id}'
        return template.format(self)

    