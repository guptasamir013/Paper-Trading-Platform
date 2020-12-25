# Generated by Django 3.1.3 on 2020-12-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_pendingorder_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='executedorder',
            name='type',
            field=models.CharField(choices=[('buy-sell', 'buy-sell'), ('sell-buy', 'sell-buy')], default='buy-sell', max_length=10),
        ),
    ]
