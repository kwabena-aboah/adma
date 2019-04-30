# Generated by Django 2.1.7 on 2019-04-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cover_pic',
            field=models.FileField(default=1, help_text='Cover image for entry.', upload_to='Uploads/entries'),
            preserve_default=False,
        ),
    ]
