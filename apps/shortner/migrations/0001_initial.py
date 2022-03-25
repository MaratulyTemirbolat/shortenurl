# Generated by Django 3.0 on 2022-03-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время удаления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('link', models.CharField(max_length=10000, verbose_name='url link')),
                ('uuid', models.CharField(max_length=10, unique=True, verbose_name='shortened link')),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Ulr(ы)',
            },
        ),
    ]
