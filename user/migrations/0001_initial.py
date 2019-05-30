# Generated by Django 2.0.6 on 2019-05-11 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recv_name', models.CharField(max_length=20, verbose_name='联系人')),
                ('liaison', models.IntegerField(verbose_name='联系方式')),
                ('address_detailed', models.CharField(max_length=50, verbose_name='收货地址')),
                ('address_number', models.CharField(max_length=20, verbose_name='门牌号')),
                ('address_type', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, verbose_name='创建时间')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='用户名')),
                ('_password', models.CharField(max_length=128, verbose_name='密码')),
                ('user_status', models.SmallIntegerField(choices=[(0, '管理员'), (1, '普通用户')], default=1)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]
