# Generated by Django 4.1.3 on 2022-12-21 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geacexdb', '0007_rename_plazo_preinscripcion_calendario_plazo_inscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='centro',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='geacexdb.centro'),
            preserve_default=False,
        ),
    ]
