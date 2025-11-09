from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=120)
    sku = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.sku})"


class ProductEvent(models.Model):

    class EventType(models.TextChoices):
        MANUFACTURED = "manufactured", "Manufactured"
        IN_TRANSIT = "in_transit", "In transit"
        STORED = "stored", "Stored"
        DELIVERED = "delivered", "Delivered"
        CUSTOM = "custom", "Custom"

    product = models.ForeignKey(
        Product, related_name="events", on_delete=models.CASCADE
    )
    event_type = models.CharField(
        max_length=32, choices=EventType.choices, default=EventType.CUSTOM
    )
    title = models.CharField(max_length=120)
    notes = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    occurred_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-occurred_at"]

    def __str__(self):
        return f"{self.product.name}: {self.title}"
