# Generated by Django 3.2.12 on 2022-05-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0002_alter_obra_valor_previsto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota_fiscal',
            name='url',
            field=models.CharField(default='#', max_length=300, verbose_name='Link da nota'),
        ),
    ]