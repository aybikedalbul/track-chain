from django import forms

from .models import Product, ProductEvent


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "description"]


class ProductEventForm(forms.ModelForm):
    occurred_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        help_text="Olay ne zaman gerçekleşti? (UTC formatında gir)"
    )

    class Meta:
        model = ProductEvent
        fields = ["product", "event_type", "title", "notes", "location", "occurred_at"]
