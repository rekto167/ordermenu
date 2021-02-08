from django import forms
from .models import MenuModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = (
            'name_menu',
            'img_menu',
            'cat_menu',
            'price_menu',
        )
