# Generated by Django 2.2.3 on 2019-07-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_barang_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='test',
            field=models.FileField(default='a', upload_to=''),
        ),
    ]
