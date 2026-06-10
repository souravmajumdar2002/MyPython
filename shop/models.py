from django.db import models


class Product(models.Model):
    PRODUCT = "product"
    VIDEO = "video"
    PRODUCT_TYPE_CHOICES = [
        (PRODUCT, "Product"),
        (VIDEO, "Video Product"),
    ]

    ACTIVE = "active"
    DRAFT = "draft"
    OUT_OF_STOCK = "out_of_stock"
    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (DRAFT, "Draft"),
        (OUT_OF_STOCK, "Out of Stock"),
    ]

    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=100, unique=True)
    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE_CHOICES,
        default=PRODUCT,
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.product_name} ({self.product_code})"
