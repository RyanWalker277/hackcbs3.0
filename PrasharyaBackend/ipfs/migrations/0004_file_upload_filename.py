# Generated by Django 3.2.15 on 2022-09-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfs', '0003_rename_aadhaar_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_upload',
            name='FileName',
            field=models.CharField(default='sample', max_length=255),
            preserve_default=False,
        ),
    ]