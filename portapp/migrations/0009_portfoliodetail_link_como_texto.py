# Generated by Django 4.0.2 on 2022-05-04 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0008_alter_portfoliodetail_img_prev'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliodetail',
            name='link_como_texto',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
