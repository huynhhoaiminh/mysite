# Generated by Django 3.1.4 on 2020-12-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Mới', 'Mới'), ('Chấp nhận', 'Chấp nhận'), ('Đang chuẩn bị', 'Đang chuẩn bị'), ('Đang Ship', 'Đang Ship'), ('Hoàn Thành', 'Hoàn Thành'), ('Đã hủy', 'Đã hủy')], default='New', max_length=15),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('Mới', 'Mới'), ('Chấp Nhận', 'Chấp Nhận'), ('Đã hủy', 'Đã hủy')], default='New', max_length=10),
        ),
    ]