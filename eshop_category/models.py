from django.db import models
from django.urls import reverse
import itertools


def grouped_by(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(blank=True, verbose_name="عنوان در url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_absolute_url(self):
        return reverse('category', kwargs={'name_category': self.slug})

    def get_products(self):
        return grouped_by(4, self.product_set.order_by('-id')[:8])


