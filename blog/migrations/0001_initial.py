# Generated by Django 2.0.1 on 2018-01-13 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('main_text', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('facebook_id', models.CharField(max_length=30)),
                ('instagram_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WeightWorkOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle', models.CharField(choices=[('che', '가슴'), ('bac', '등'), ('shd', '어깨'), ('arm', '팔'), ('leg', '다리'), ('abd', '복부'), ('com', '복합')], max_length=3)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnail')),
            ],
        ),
        migrations.AddField(
            model_name='mainimages',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.PersonalInfo'),
        ),
    ]
