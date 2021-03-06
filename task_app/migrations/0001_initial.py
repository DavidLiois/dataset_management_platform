# Generated by Django 3.2.6 on 2021-08-12 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('BookedByUser', models.CharField(max_length=500)),
                ('UploadDate', models.DateTimeField(verbose_name='Uploaded At')),
                ('Deleted', models.BooleanField(verbose_name='Is Deleted')),
            ],
        ),
        migrations.CreateModel(
            name='TasksZipFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZIPFile', models.FileField(upload_to='ZIPFiles/%Y-%m')),
                ('TaskTitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.tasks')),
            ],
        ),
    ]
