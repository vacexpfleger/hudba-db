# Generated by Django 4.0.4 on 2022-05-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0004_review_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='about',
            field=models.CharField(default='Penis', max_length=500),
            preserve_default=False,
        ),
    ]
