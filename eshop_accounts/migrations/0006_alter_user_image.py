# Generated by Django 3.2.2 on 2021-05-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_accounts', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile/profile.jfif', upload_to='profile/', verbose_name='تصویر'),
        ),
    ]