# Generated by Django 4.1.4 on 2023-01-04 15:26

from django.db import migrations, models
import subscription_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='id',
        ),
        migrations.AlterField(
            model_name='code',
            name='msisdncode',
            field=models.CharField(default=subscription_app.models._campaignId, max_length=32, primary_key=True, serialize=False),
        ),
    ]