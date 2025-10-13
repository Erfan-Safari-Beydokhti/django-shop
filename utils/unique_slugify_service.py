from django.utils.text import slugify
def unique_slugify(instance, value, slug_field_name='slug', queryset=None, slug_separator='-'):
    slug = slugify(value)

    if queryset is None:
        queryset = instance.__class__.objects.all()

    original_slug = slug
    index = 1

    while queryset.filter(**{slug_field_name: slug}).exclude(pk=instance.pk).exists():
        slug = original_slug + slug_separator + str(index)
        index += 1

    return slug