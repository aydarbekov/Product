# Generated by Django 2.2.5 on 2019-09-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('food', 'Еда'), ('drink', 'Вода'), ('cloth', 'Одежда'), ('electronics', 'Электроника')], default='other', max_length=20, verbose_name='Категория')),
                ('amount', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
        ),
    ]
