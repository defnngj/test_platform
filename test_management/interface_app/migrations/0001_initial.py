# Generated by Django 2.1.1 on 2018-10-05 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('status', models.IntegerField(default=True, verbose_name='状态：')),
                ('url', models.CharField(default='', max_length=100, verbose_name='URL')),
                ('mothod', models.CharField(default='', max_length=100, verbose_name='方法')),
                ('header', models.CharField(blank=True, default='', max_length=100, verbose_name='Header')),
                ('parameter_type', models.CharField(blank=True, default='', max_length=10, verbose_name='参数类型')),
                ('parameter_body', models.CharField(blank=True, default='', max_length=1000, verbose_name='参数体')),
                ('response_assert', models.CharField(blank=True, default='', max_length=1000, verbose_name='返回值断言')),
                ('user', models.CharField(blank=True, default='', max_length=50, verbose_name='用户')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('belong_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.Module')),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.Project')),
            ],
        ),
    ]