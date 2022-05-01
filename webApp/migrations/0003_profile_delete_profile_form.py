# Generated by Django 4.0.3 on 2022-04-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_alter_profile_form_activitylevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=5, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('activitylevel', models.CharField(blank=True, choices=[('Sedentary: little or no exercise', 'Sedentary: little or no exercise'), ('Exercise 1-3 times/week', 'Exercise 1-3 times/week'), ('xercise 4-5 times/week', 'Exercise 4-5 times/week'), ('Daily exercise or intense exercise 3-4 times/week', 'Daily exercise or intense exercise 3-4 times/week')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='profile_form',
        ),
    ]