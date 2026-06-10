from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_name",
            "product_code",
            "product_type",
            "description",
            "price",
            "tax",
            "mrp",
            "stock",
            "status",
            "video_url",
        ]

    def clean(self):
        cleaned_data = super().clean()
        product_type = cleaned_data.get("product_type")
        video_url = (cleaned_data.get("video_url") or "").strip()

        if product_type == Product.VIDEO and not video_url:
            self.add_error("video_url", "Video URL is required for video products.")

        if product_type == Product.PRODUCT:
            cleaned_data["video_url"] = ""

        return cleaned_data
