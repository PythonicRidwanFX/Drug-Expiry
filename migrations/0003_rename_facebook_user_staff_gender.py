# Generated by Django 5.1.3 on 2024-11-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_drug_batch_n_alter_drug_dosage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='facebook_user',
            new_name='gender',
        ),
    ]
