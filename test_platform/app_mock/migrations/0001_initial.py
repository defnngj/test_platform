# Generated by Django 2.2.2 on 2019-08-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MockData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=200, verbose_name='uri')),
                ('env', models.CharField(default='', max_length=20, verbose_name='env')),
                ('method', models.CharField(default='get', max_length=10, verbose_name='方法')),
                ('desc', models.TextField(default='', verbose_name='描述')),
                ('header', models.TextField(default='{}', verbose_name='请求头')),
                ('request_type', models.TextField(default='', verbose_name='请求参数类型')),
                ('request', models.TextField(default='{}', verbose_name='请求参数')),
                ('response', models.TextField(default='', verbose_name='返回参数')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]