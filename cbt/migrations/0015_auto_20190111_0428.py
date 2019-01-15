# Generated by Django 2.0.7 on 2019-01-11 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbt', '0014_auto_20190111_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(help_text='Generate Token for User.', on_delete=django.db.models.deletion.CASCADE, related_name='user_token', to='cbt.UserDetail'),
        ),
    ]