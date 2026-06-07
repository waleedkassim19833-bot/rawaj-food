from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/', verbose_name="الصورة")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="الفئة")
    available = models.BooleanField(default=True, verbose_name="متوفر")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"