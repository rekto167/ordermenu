from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class MenuModel(models.Model):
    name_menu = models.CharField(max_length=100)
    img_menu = models.ImageField(null=True, blank=True, upload_to='media')
    cat_menu = models.CharField(max_length=100)
    price_menu = models.DecimalField(max_digits=6, decimal_places=0)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(f"{self.name_menu}")
        super().save()

    def delete(self):
        self.img_menu.storage.delete(self.img_menu.name)
        super().delete()

    def get_absolute_url(self):
        return reverse('restoran:managemenu')

    def __str__(self):
        return "{}. {}".format(self.id, self.name_menu)
