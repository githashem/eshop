from django import template

register = template.Library()


@register.simple_tag()
def get_image_first(product):
    return product.picture_set.all().first().image.url
