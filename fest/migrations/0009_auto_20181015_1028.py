# Generated by Django 2.0.5 on 2018-10-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest', '0008_auto_20181008_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrie',
            name='icon',
            field=models.CharField(choices=[('icon fas fa-home', 'Home'), ('icon fas fa-flag-checkered', 'Flag'), ('icon fas fa-fire', 'Fire'), ('icon fas fa-utensils', 'Cutlery'), ('icon fas fa-cogs', 'Cogs'), ('icon fas fa-om', 'Om'), ('icon fas fa-snowflake', 'Snow'), ('icon fas fa-magic', 'Magic')], max_length=25),
        ),
    ]
