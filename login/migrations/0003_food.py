# Generated by Django 4.2.8 on 2024-03-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_customuser_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='foods/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
