# Generated by Django 4.1.13 on 2024-01-13 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guidelines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='guidelines.folder'),
        ),
        migrations.AlterField(
            model_name='guideline',
            name='folderId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='guidelines.folder'),
        ),
    ]
