# Generated by Django 5.0.2 on 2024-03-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_medicineuser_delete_product'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicineUser',
            new_name='User',
        ),
    ]