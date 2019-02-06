# Generated by Django 2.1.5 on 2019-02-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='languages',
            field=models.ManyToManyField(to='example.Language'),
        ),
    ]
