# Generated by Django 4.1 on 2022-12-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_tidings_delete_hall_layout_delete_order_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tidings',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='tidings',
            name='username',
            field=models.CharField(max_length=250, null=True, verbose_name='Имя пользователя'),
        ),
    ]
