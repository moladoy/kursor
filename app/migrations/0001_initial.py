# Generated by Django 4.2.1 on 2023-05-31 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/')),
                ('title', models.CharField(max_length=155)),
                ('review', models.IntegerField(blank=True, default=1, null=True)),
                ('price', models.FloatField()),
                ('text', models.TextField()),
                ('choice', models.CharField(choices=[('xs', 'Xs'), ('x', 'X'), ('m', 'M'), ('l', 'L'), ('xl', 'Xl')], default='xl', max_length=55)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], default='White', max_length=25)),
                ('quantity', models.IntegerField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
