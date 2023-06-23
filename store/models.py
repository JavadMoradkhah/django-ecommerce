from django.db import models


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

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class ShippingMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)


class Size(models.Model):
    value = models.CharField(max_length=50, unique=True)
