# Generated by Django 3.1.2 on 2020-10-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=2048)),
                ('citation_url', models.CharField(max_length=512)),
                ('citation_title', models.CharField(max_length=512)),
                ('citation_image_url', models.CharField(max_length=512)),
            ],
        ),
    ]
