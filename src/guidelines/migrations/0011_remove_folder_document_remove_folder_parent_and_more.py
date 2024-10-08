# Generated by Django 4.1.13 on 2024-07-13 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guidelines', '0010_remove_folder_content_folder_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='document',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='guideline',
            name='folder',
        ),
        migrations.AddField(
            model_name='document',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='guidelines.folder'),
        ),
        migrations.AddField(
            model_name='folder',
            name='guideline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='guidelines.guideline'),
        ),
    ]
