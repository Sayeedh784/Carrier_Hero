# Generated by Django 4.0.3 on 2022-03-10 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_appoinments_status_appoinment_appoinment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='req_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
