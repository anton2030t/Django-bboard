# Generated by Django 2.0.5 on 2018-08-29 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Надрубрика',
                'verbose_name_plural': 'Надрубрики',
                'ordering': ('order', 'name'),
                'proxy': True,
                'indexes': [],
            },
            bases=('main.rubric',),
        ),
    ]
