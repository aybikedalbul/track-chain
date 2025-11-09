from django.forms import HiddenInput
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductEventForm, ProductForm
from .models import Product, ProductEvent


class ProductListView(ListView):
    model = Product
    template_name = "tracker/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("events")


class ProductDetailView(DetailView):
    model = Product
    template_name = "tracker/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "tracker/product_form.html"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "tracker/product_form.html"

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "tracker/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")


class ProductEventCreateView(CreateView):
    model = ProductEvent
    form_class = ProductEventForm
    template_name = "tracker/event_form.html"

    def get_initial(self):
        initial = super().get_initial()
        product_id = self.kwargs.get("product_pk")
        if product_id:
            initial["product"] = product_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if "product" in form.fields and self.kwargs.get("product_pk"):
            form.fields["product"].widget = HiddenInput()
            form.initial["product"] = self.kwargs["product_pk"]
        return form

    def form_valid(self, form):
        if self.kwargs.get("product_pk"):
            form.instance.product_id = self.kwargs["product_pk"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product_id})


class ProductEventUpdateView(UpdateView):
    model = ProductEvent
    form_class = ProductEventForm
    template_name = "tracker/event_form.html"

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product_id})


class ProductEventDeleteView(DeleteView):
    model = ProductEvent
    template_name = "tracker/event_confirm_delete.html"

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.object.product_id})
