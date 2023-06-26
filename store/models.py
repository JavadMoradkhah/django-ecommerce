from django.db import models
from django.contrib.auth import get_user_model
from colorfield.fields import ColorField

User = get_user_model()


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
    discount = models.PositiveSmallIntegerField(null=True, blank=True)
    order_limit = models.PositiveSmallIntegerField(null=True, blank=True)
    orderable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Promotion(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='promotion', unique=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    discount_rate = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Variation(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='variations'
    )
    color = models.ForeignKey(
        Color, on_delete=models.PROTECT, related_name='variations'
    )
    size = models.ForeignKey(
        Size, on_delete=models.PROTECT, related_name='variations'
    )
    quantity_in_stock = models.PositiveSmallIntegerField()


class ProductTag(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='tags'
    )
    tag = models.ForeignKey(
        Tag, on_delete=models.PROTECT, related_name='product_tags'
    )

    class Meta:
        unique_together = ('product', 'tag')


class Review(models.Model):
    REVIEW_STATUS_PENDING = 'pending'
    REVIEW_STATUS_CONFIRMED = 'confirmed'
    REVIEW_STATUS_REJECTED = 'rejected'

    REVIEW_STATUS_CHOICES = (
        ('PENDING', REVIEW_STATUS_PENDING),
        ('CONFIRMED', REVIEW_STATUS_CONFIRMED),
        ('REJECTED', REVIEW_STATUS_REJECTED)
    )

    status = models.CharField(
        max_length=50, choices=REVIEW_STATUS_CHOICES, default=REVIEW_STATUS_PENDING
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart', unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items'
    )
    variation = models.ForeignKey(
        Variation, on_delete=models.PROTECT, related_name='cart_items'
    )
    quantity = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist, on_delete=models.CASCADE, related_name='items'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wishlist_items'
    )

    class Meta:
        unique_together = ('wishlist', 'product')


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='addresses'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name='addresses'
    )
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    unit_number = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
