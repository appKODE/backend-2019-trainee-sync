# Generated by Django 2.2.7 on 2019-11-18 13:16

from django.db import migrations, models
import pitter.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(default=pitter.models.base.default_uuid_id, editable=False, max_length=256, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fake_id', models.CharField(default='', max_length=50)),
                ('message', models.CharField(max_length=256)),
                ('user_comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
