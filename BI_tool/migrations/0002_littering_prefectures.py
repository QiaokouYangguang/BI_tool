# Generated by Django 3.1.1 on 2021-09-21 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BI_tool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='都道府県名')),
            ],
        ),
        migrations.CreateModel(
            name='Littering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Collection_date', models.DateField(verbose_name='回収日')),
                ('Bottles', models.IntegerField(default=0, verbose_name='ペットボトル')),
                ('Tobacco', models.IntegerField(default=0, verbose_name='タバコ')),
                ('Can', models.IntegerField(default=0, verbose_name='空き缶')),
                ('Prefectures', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BI_tool.prefectures')),
            ],
        ),
    ]