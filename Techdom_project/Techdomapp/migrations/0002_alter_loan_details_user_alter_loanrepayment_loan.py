# Generated by Django 5.0.4 on 2024-05-03 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Techdomapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_details',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loanrepayment',
            name='loan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Techdomapp.loan_details'),
        ),
    ]