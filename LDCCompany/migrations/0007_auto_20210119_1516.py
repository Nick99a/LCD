# Generated by Django 3.1.5 on 2021-01-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LDCCompany', '0006_remove_telephoneconversation_id_conversation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id_receipt',
        ),
        migrations.AddField(
            model_name='receipt',
            name='id_client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='LDCCompany.client'),
            preserve_default=False,
        ),
    ]
