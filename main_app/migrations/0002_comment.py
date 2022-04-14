# Generated by Django 4.0.3 on 2022-04-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=300)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.art')),
            ],
        ),
    ]