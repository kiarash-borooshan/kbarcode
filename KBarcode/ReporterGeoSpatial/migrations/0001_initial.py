# Generated by Django 4.2.4 on 2023-08-21 15:50

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HealthStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IRN_adm1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_0', models.BigIntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.BigIntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('type_1', models.CharField(max_length=50)),
                ('engtype_1', models.CharField(max_length=50)),
                ('nl_name_1', models.CharField(blank=True, max_length=50, null=True)),
                ('varname_1', models.CharField(blank=True, max_length=150, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name': 'countie',
            },
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('geo_tag_photo', models.ImageField(blank=True, null=True, upload_to='geoTag_Image')),
                ('Date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=20)),
                ('variety', models.CharField(blank=True, max_length=255, null=True)),
                ('disease_name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('health_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_status', to='ReporterGeoSpatial.healthstatus')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='em_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Feature',
            },
        ),
    ]
