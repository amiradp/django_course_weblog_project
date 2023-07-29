# Generated by Django 4.2.3 on 2023-07-08 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_title', models.CharField(max_length=100)),
                ('user_text', models.TextField()),
                ('user_date_created', models.DateTimeField(auto_now_add=True)),
                ('user_datetime_modified', models.DateTimeField(auto_now=True)),
                ('user_status', models.CharField(choices=[('pub', 'Published'), ('drf', 'Draft')], max_length=3)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
