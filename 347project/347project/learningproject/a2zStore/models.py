from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, default="", null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    desc = models.TextField(max_length=800,blank=True)
    book_url = models.URLField(verbose_name='Book link', default="",null=False, blank=False)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="book_images/", default="", null=False, blank=False)

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90, null=False, blank=False)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111, null=False, blank=False)
    city = models.CharField(max_length=111, null=False, blank=False)
    state = models.CharField(max_length=111, null=False, blank=False)
    zip_code = models.CharField(max_length=111, null=False, blank=False)
    phone = models.CharField(max_length=111, null=False, blank=False)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."