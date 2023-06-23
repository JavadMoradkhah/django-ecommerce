from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'Category', on_delete=models.PROTECT,
        related_name='children', null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    shippable = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class FaqCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'FAQ Category'
        verbose_name_plural = 'FAQ Categories'


class FAQ(models.Model):
    category = models.ForeignKey(
        FaqCategory, on_delete=models.PROTECT, related_name='faqs'
    )
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class ShippingMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    value = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.value


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = ColorField(default='#FFFFFF', format='hexa',
                      max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='products'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='products'
    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='store/images/products')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    order_limit = models.PositiveSmallIntegerField(null=True, blank=True)
    orderable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
