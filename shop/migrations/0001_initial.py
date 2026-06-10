from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("product_name", models.CharField(max_length=200)),
                ("product_code", models.CharField(max_length=100, unique=True)),
                ("product_type", models.CharField(choices=[("product", "Product"), ("video", "Video Product")], default="product", max_length=20)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("tax", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ("mrp", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock", models.PositiveIntegerField(default=0)),
                ("status", models.CharField(choices=[("active", "Active"), ("draft", "Draft"), ("out_of_stock", "Out of Stock")], default="active", max_length=20)),
                ("video_url", models.URLField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
