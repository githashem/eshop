from django.contrib import admin
from . import models


class PictureInline(admin.StackedInline):
    model = models.Picture


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "price", "active"]
    inlines = [PictureInline]

    class Meta:
        model = models.Product
