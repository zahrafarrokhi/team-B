# Generated by Django 3.2.2 on 2021-05-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0011_follower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted'], 'verbose_name': 'دیدگاه', 'verbose_name_plural': 'دیدگاه'},
        ),
        migrations.AlterModelOptions(
            name='reaction',
            options={'verbose_name': 'پاسخ به دیدگاه ها', 'verbose_name_plural': 'پاسخ به دیدگاه ها'},
        ),
        migrations.AlterModelOptions(
            name='reactioninstance',
            options={'verbose_name': 'پاسخ به دیدگاه ها', 'verbose_name_plural': 'پاسخ به دیدگاه ها'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flaginstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reactioninstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
