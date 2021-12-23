# Generated by Django 4.0 on 2021-12-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('alt_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('symbol', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='core.portfoliogroup')),
                ('images', models.ManyToManyField(to='core.Image')),
                ('tags', models.ManyToManyField(to='core.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='core.image')),
                ('tags', models.ManyToManyField(to='core.Tag')),
            ],
        ),
    ]
