# Generated by Django 2.1.7 on 2019-05-12 17:59

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import univoting.models.degree


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(help_text='Write your opinion here', max_length=250)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.SmallIntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')])),
            ],
            options={
                'ordering': ['course'],
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, validators=[univoting.models.degree.validate_title])),
                ('ects', models.PositiveSmallIntegerField(default=240, validators=[django.core.validators.MaxValueValidator(600)])),
                ('description', models.TextField(default='No description for now.')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('lat', models.FloatField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='Latitude')),
                ('long', models.FloatField(validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Subject', max_length=64)),
                ('ects', models.PositiveSmallIntegerField(default=6, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(default='No description added yet', max_length=250)),
                ('_course', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('_degree', models.PositiveIntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('difficulty', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('work_score', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('workVolume', models.PositiveSmallIntegerField(choices=[(0, 'LOW'), (1, 'MEDIUM'), (2, 'A LOT')], default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('picture', models.ImageField(default='noimage.png', upload_to='university_pics')),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=12, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('country', models.CharField(blank=True, max_length=32, null=True)),
                ('lat', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='Latitude')),
                ('long', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='Longitude')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='univoting.Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('univoting.comment',),
        ),
        migrations.AddField(
            model_name='subject',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='univoting.SubjectReview'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('lat', 'long')},
        ),
        migrations.AddField(
            model_name='degree',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univoting.University'),
        ),
        migrations.AddField(
            model_name='course',
            name='degree_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univoting.Degree'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univoting.Subject'),
        ),
        migrations.AddField(
            model_name='subjectcomment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univoting.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('degree_id', 'subject_id')},
        ),
    ]
