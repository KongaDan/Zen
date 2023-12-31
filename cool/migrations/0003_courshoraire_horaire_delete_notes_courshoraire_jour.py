# Generated by Django 4.2.7 on 2023-11-29 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cool', '0002_alter_user_promotion_alter_user_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursHoraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.BooleanField(default=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cool.cours')),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=50, null=True)),
                ('cours', models.ManyToManyField(through='cool.CoursHoraire', to='cool.cours')),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.AddField(
            model_name='courshoraire',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cool.horaire'),
        ),
    ]
