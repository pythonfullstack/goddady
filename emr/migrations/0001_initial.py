# Generated by Django 3.2.13 on 2022-04-29 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentInstance',
            fields=[
                ('sku', models.CharField(help_text='Environment Instance SKU', max_length=50, primary_key=True, serialize=False)),
                ('stage', models.CharField(choices=[('dev', 'Dev'), ('staging', 'Staging'), ('prod', 'Prod')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='environment_instance', to='emr.environment')),
            ],
        ),
        migrations.CreateModel(
            name='EMR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('terminated', 'Terminated')], db_index=True, default='pending', help_text='EMR Instance Status', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('environment_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emr', to='emr.environmentinstance')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emr', to='emr.team')),
            ],
        ),
        migrations.CreateModel(
            name='TaskQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(db_index=True, max_length=128)),
                ('task', models.CharField(choices=[('create_emr', 'Create EMR'), ('update_emr', 'Update EMR'), ('delete_emr', 'Delete EMR')], db_index=True, max_length=16)),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('processing', 'Processing'), ('failed', 'Failed')], db_index=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_queue', to='emr.team')),
            ],
            options={
                'unique_together': {('team', 'content_type', 'object_id', 'task')},
            },
        ),
    ]
