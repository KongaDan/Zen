# Generated by Django 4.2.7 on 2023-11-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cool.promotion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cool.section'),
        ),
    ]
