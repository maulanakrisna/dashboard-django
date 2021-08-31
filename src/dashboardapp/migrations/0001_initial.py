# Generated by Django 3.2.1 on 2021-08-14 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=32)),
                ('fax', models.CharField(max_length=32)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Sti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=32)),
                ('brand', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.office')),
            ],
        ),
        migrations.AddField(
            model_name='office',
            name='sti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.sti'),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=32)),
                ('bandwidth', models.CharField(max_length=32)),
                ('ip_address', models.CharField(max_length=64)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.office')),
            ],
        ),
        migrations.CreateModel(
            name='Itsupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('jobdescription', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.office')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=32)),
                ('monitor', models.CharField(max_length=256)),
                ('processor', models.CharField(max_length=256)),
                ('memory', models.CharField(max_length=256)),
                ('storage', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.office')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=256)),
                ('address2', models.CharField(max_length=256)),
                ('zipcode', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboardapp.office')),
            ],
        ),
    ]