# Generated by Django 4.0.2 on 2022-02-15 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('houses', '0003_alter_house_exit_alter_house_trap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
