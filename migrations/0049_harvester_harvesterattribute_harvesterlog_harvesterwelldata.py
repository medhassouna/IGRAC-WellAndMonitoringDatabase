# Generated by Django 2.2.16 on 2021-08-09 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0048_welllevelmeasurement_value_in_m'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvester_class', models.CharField(help_text='The type of harvester that will be used.Use class with full package.', max_length=100, unique=True)),
                ('name', models.CharField(help_text='Name of harvester that.', max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, help_text='Make this harvester ready to be harvested periodically.')),
                ('is_run', models.BooleanField(default=False, help_text='Is the harvester running.')),
                ('public', models.BooleanField(default=True, help_text='Default indicator for : well can be viewed by non organisation user.')),
                ('downloadable', models.BooleanField(default=True, help_text='Default indicator : well can be downloaded.')),
                ('feature_type', models.ForeignKey(blank=True, help_text='Default feature type for the extracted wells.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermFeatureType')),
                ('organisation', models.ForeignKey(blank=True, help_text="Organisation for this harvester. It will be used as default of well's organisation", null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Organisation')),
            ],
            options={
                'db_table': 'harvester',
            },
        ),
        migrations.CreateModel(
            name='HarvesterWellData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurements_found', models.IntegerField(default=0, help_text='Number of measurements found.')),
                ('from_time_data', models.DateTimeField(blank=True, help_text='The time of oldest measurement that are harvested.', null=True)),
                ('to_time_data', models.DateTimeField(blank=True, help_text='The time of newest measurement that are harvested.', null=True)),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Harvester')),
                ('well', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Well')),
            ],
            options={
                'db_table': 'harvester_well_data',
            },
        ),
        migrations.CreateModel(
            name='HarvesterLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, help_text='This is when the harvester is started.')),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Done', 'Done'), ('Error', 'Error')], default='Running', max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Harvester')),
            ],
            options={
                'db_table': 'harvester_log',
                'ordering': ('-start_time',),
            },
        ),
        migrations.CreateModel(
            name='HarvesterAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of attribute', max_length=100)),
                ('value', models.CharField(default=True, help_text='The value of attribute', max_length=100, null=True)),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Harvester')),
            ],
            options={
                'db_table': 'harvester_attribute',
                'unique_together': {('harvester', 'name')},
            },
        ),
    ]
