# Generated by Django 2.2.12 on 2020-10-15 03:37

import datetime
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pump_installer', models.CharField(blank=True, help_text='Name of the company or person who installed the pump.', max_length=512, null=True)),
                ('pump_description', models.TextField(blank=True, help_text='Any relevant information on the pump (e.g. model, capacity, energy supply, depth).', null=True)),
            ],
            options={
                'db_table': 'construction',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('code', models.CharField(max_length=126)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'country',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Drilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driller', models.CharField(blank=True, help_text='Name of the drilling company or responsible person.', max_length=512, null=True)),
                ('successful', models.BooleanField(blank=True, null=True)),
                ('cause_of_failure', models.TextField(blank=True, help_text='Explain why the drilling was not successful.', null=True)),
            ],
            options={
                'db_table': 'drilling',
            },
        ),
        migrations.CreateModel(
            name='Geology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'geology',
            },
        ),
        migrations.CreateModel(
            name='HydrogeologyParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aquifer_name', models.CharField(blank=True, max_length=512, null=True)),
                ('aquifer_material', models.CharField(blank=True, max_length=512, null=True)),
                ('degree_of_confinement', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hydrogeology_parameter',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=512, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, help_text='Explain what the license entails.', null=True)),
            ],
            options={
                'db_table': 'license',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(blank=True, help_text='Name of the manager or owner of the groundwater point. This can be a single person, a group of persons or an organisation.', max_length=512, null=True, verbose_name='Manager / owner')),
                ('description', models.TextField(blank=True, help_text='Explain how the groundwater point is managed.', null=True)),
                ('number_of_users', models.IntegerField(blank=True, help_text='Indicate how many people use the groundwater.', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Number of people served')),
            ],
            options={
                'db_table': 'management',
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
            options={
                'db_table': 'quantity',
            },
        ),
        migrations.CreateModel(
            name='ReferenceElevation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reference_elevation',
            },
        ),
        migrations.CreateModel(
            name='ReferenceElevationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reference_elevation_type',
            },
        ),
        migrations.CreateModel(
            name='TermAquiferType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_aquifer_type',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermConfinement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_confinement',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermDrillingMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_drilling_method',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermFeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_feature_type',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermGroundwaterUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_groundwater_use',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermMeasurementParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_measurement_parameter',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermWellPurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_well_purpose',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TermWellStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_well_status',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('html', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'db_table': 'unit',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text='Location of the feature.', srid=4326, verbose_name='location')),
                ('address', models.TextField(blank=True, null=True)),
                ('photo', models.FileField(blank=True, help_text='A photo of the groundwater point. More photos can be added in annex. ', null=True, upload_to='gwml2/photos/')),
                ('description', models.TextField(blank=True, help_text='A general description of the groundwater point.', null=True)),
                ('original_id', models.CharField(help_text='As recorded in the original database.', max_length=256, unique=True)),
                ('construction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Construction')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Country')),
                ('drilling', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Drilling')),
                ('feature_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermFeatureType')),
                ('geology', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Geology')),
                ('ground_surface_elevation', models.OneToOneField(blank=True, help_text='Ground Surface Elevation Above Sea Level.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ground_surface_elevation', to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'well',
                'ordering': ['original_id'],
            },
        ),
        migrations.CreateModel(
            name='WellGroundwaterLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_elevation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevation')),
            ],
            options={
                'db_table': 'well_groundwater_level',
            },
        ),
        migrations.CreateModel(
            name='WellYieldMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('methodology', models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=512, null=True)),
                ('parameter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermMeasurementParameter', verbose_name='parameter')),
                ('value', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Well')),
            ],
            options={
                'db_table': 'well_yield_measurement',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='WellQualityMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('methodology', models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=512, null=True)),
                ('parameter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermMeasurementParameter', verbose_name='parameter')),
                ('value', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Well')),
            ],
            options={
                'db_table': 'well_quality_measurement',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='WellGroundwaterLevelMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('methodology', models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=512, null=True)),
                ('groundwater_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.WellGroundwaterLevel')),
                ('parameter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermMeasurementParameter', verbose_name='parameter')),
                ('value', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'well_groundwater_level_measurement',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='WellDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('file', models.FileField(blank=True, null=True, upload_to='gwml2/document/')),
                ('file_path', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, help_text='Description of the feature.', null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Well')),
            ],
            options={
                'db_table': 'well_document',
            },
        ),
        migrations.AddField(
            model_name='well',
            name='groundwater_level',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.WellGroundwaterLevel'),
        ),
        migrations.AddField(
            model_name='well',
            name='hydrogeology_parameter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.HydrogeologyParameter'),
        ),
        migrations.AddField(
            model_name='well',
            name='management',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Management'),
        ),
        migrations.AddField(
            model_name='well',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermWellPurpose'),
        ),
        migrations.AddField(
            model_name='well',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermWellStatus'),
        ),
        migrations.AddField(
            model_name='well',
            name='top_borehole_elevation',
            field=models.OneToOneField(blank=True, help_text='Elevation of Top of Borehole Above Sea Level.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_borehole_elevation', to='gwml2.Quantity'),
        ),
        migrations.CreateModel(
            name='WaterStrike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevation')),
                ('drilling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Drilling')),
            ],
            options={
                'db_table': 'drilling_water_strike',
            },
        ),
        migrations.CreateModel(
            name='UnitGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('units', models.ManyToManyField(blank=True, null=True, to='gwml2.Unit')),
            ],
            options={
                'db_table': 'unit_group',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StratigraphicLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=512, null=True)),
                ('stratigraphic_unit', models.CharField(blank=True, max_length=256, null=True)),
                ('bottom_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stratigraphic_log_bottom_depth', to='gwml2.Quantity')),
                ('drilling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwml2.Drilling')),
                ('reference_elevation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevationType')),
                ('top_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stratigraphic_log_top_depth', to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'drilling_stratigraphic_log',
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('bottom_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='screening_bottom_depth', to='gwml2.Quantity')),
                ('construction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Construction')),
                ('diameter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='screening_diameter', to='gwml2.Quantity')),
                ('reference_elevation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevationType')),
                ('top_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='screening_top_depth', to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'construction_screen',
            },
        ),
        migrations.AddField(
            model_name='referenceelevation',
            name='reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevationType'),
        ),
        migrations.AddField(
            model_name='referenceelevation',
            name='value',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Unit'),
        ),
        migrations.CreateModel(
            name='PumpingTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porosity', models.FloatField(blank=True, null=True)),
                ('specific_yield', models.FloatField(blank=True, null=True)),
                ('storativity', models.FloatField(blank=True, help_text='In confined aquifers, storativity is the integrated specific storage over the thickness of the aquifer. In unconfined aquifer, storativity is equivalent to specific yield.', null=True)),
                ('test_type', models.CharField(blank=True, help_text='Provide information on the test(s) performed to estimate the hydraulic properties.', max_length=512, null=True)),
                ('hydraulic_conductivity', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pumping_test_hydraulic_conductivity', to='gwml2.Quantity')),
                ('specific_capacity', models.OneToOneField(blank=True, help_text='Specific capacity is the pumping rate divided by the drawdown. It gives an indication of the yield of a well.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pumping_test_specific_capacity', to='gwml2.Quantity')),
                ('specific_storage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pumping_test_specific_storage', to='gwml2.Quantity')),
                ('transmissivity', models.OneToOneField(blank=True, help_text='Transmissivity is the hydraulic conductivity integrated over the thickness of the aquifer.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pumping_test_transmissivity', to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'pumping_test',
            },
        ),
        migrations.AddField(
            model_name='management',
            name='groundwater_use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermGroundwaterUse'),
        ),
        migrations.AddField(
            model_name='management',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.License'),
        ),
        migrations.AddField(
            model_name='hydrogeologyparameter',
            name='aquifer_thickness',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity'),
        ),
        migrations.AddField(
            model_name='hydrogeologyparameter',
            name='aquifer_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermAquiferType'),
        ),
        migrations.AddField(
            model_name='hydrogeologyparameter',
            name='confinement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermConfinement'),
        ),
        migrations.AddField(
            model_name='hydrogeologyparameter',
            name='pumping_test',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.PumpingTest'),
        ),
        migrations.AddField(
            model_name='geology',
            name='total_depth',
            field=models.OneToOneField(blank=True, help_text='Depth of the well below the ground surface.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity'),
        ),
        migrations.AddField(
            model_name='drilling',
            name='drilling_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TermDrillingMethod'),
        ),
        migrations.AddField(
            model_name='drilling',
            name='reference_elevation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevation'),
        ),
        migrations.AddField(
            model_name='drilling',
            name='total_depth',
            field=models.OneToOneField(blank=True, help_text='Total depth of stratigraphic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity'),
        ),
        migrations.CreateModel(
            name='Casing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('bottom_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casing_bottom_depth', to='gwml2.Quantity')),
                ('construction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Construction')),
                ('diameter', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casing_diameter', to='gwml2.Quantity')),
                ('reference_elevation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ReferenceElevationType')),
                ('top_depth', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casing_top_depth', to='gwml2.Quantity')),
            ],
            options={
                'db_table': 'construction_casing',
            },
        ),
    ]
