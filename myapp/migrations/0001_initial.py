# Generated by Django 4.1.4 on 2022-12-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_image', models.URLField()),
                ('title_proyecto', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('url_github', models.URLField()),
                ('tag_html', models.CharField(max_length=50)),
                ('tag_css', models.CharField(max_length=50)),
                ('tag_script', models.CharField(max_length=50)),
                ('tag_php', models.CharField(max_length=50)),
                ('tag_python', models.CharField(max_length=50)),
                ('tag_photo', models.CharField(max_length=50)),
            ],
        ),
    ]