# Generated by Django 2.2.5 on 2019-09-26 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyBlogDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=5000)),
                ('myblog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.MyBlog')),
            ],
        ),
    ]
