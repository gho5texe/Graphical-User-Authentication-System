# Generated by Django 4.1.5 on 2023-01-14 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_delete_auth_user_delete_default_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_img',
        ),
    ]