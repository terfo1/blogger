# Generated by Django 5.0.6 on 2024-06-27 14:46

import blogapp.models
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('IT & Startups', 'IT & Startups'), ('Finance', 'Finance')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', django_ckeditor_5.fields.CKEditor5Field()),
                ('short_description', models.TextField(validators=[blogapp.models.validate_word_count])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
            ],
        ),
    ]
