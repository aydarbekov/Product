from django import forms
from django.forms import widgets
# from product.models import PRODUCT_OTHER_CHOICE, PRODUCT_CATEGORY_CHOICES

PRODUCT_OTHER_CHOICE = 'other'
PRODUCT_CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'Разное'),
    ('food', 'Еда'),
    ('drink', 'Вода'),
    ('cloth', 'Одежда'),
    ('electronics', 'Электроника')
)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование')
    description = forms.CharField(max_length=2000, required=True, label='Описание', widget=forms.Textarea)
    category = forms.ChoiceField(required=False, widget=forms.Select, choices=PRODUCT_CATEGORY_CHOICES, label='Категория')
    amount = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')



