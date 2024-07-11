# Generated by Django 5.0.6 on 2024-06-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='imageby',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]