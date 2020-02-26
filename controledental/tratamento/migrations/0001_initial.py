# Generated by Django 3.0.3 on 2020-02-26 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastrotratamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dente', models.CharField(choices=[('0-TODOS', 'TODOS'), ('11-INCISIVO CENTRAL SUPERIOR', '11-INCISIVO CENTRAL SUPERIOR'), ('21-INCISIVO CENTRAL SUPERIOR', '21-INCISIVO CENTRAL SUPERIOR'), ('12-INCISIVO LATERAL SUPERIOR', '12-INCISIVO LATERAL SUPERIOR'), ('22-INCISIVO LATERAL SUPERIOR', '22-INCISIVO LATERAL SUPERIOR'), ('13-CANINO SUPERIOR', '13-CANINO SUPERIOR'), ('23-CANINO SUPERIOR', '23-CANINO SUPERIOR'), ('14-PRE-MOLAR SUPERIOR', '14-PRE-MOLAR SUPERIOR'), ('15-PRE-MOLAR SUPERIOR', '15-PRE-MOLAR SUPERIOR'), ('24-PRE-MOLAR SUPERIOR', '24-PRE-MOLAR SUPERIOR'), ('25-PRE-MOLAR SUPERIOR', '25-PRE-MOLAR SUPERIOR'), ('16-MOLAR SUPERIOR', '16-MOLAR SUPERIOR'), ('17-MOLAR SUPERIOR', '17-MOLAR SUPERIOR'), ('18-MOLAR SUPERIOR', '18-MOLAR SUPERIOR'), ('26-MOLAR SUPERIOR', '26-MOLAR SUPERIOR'), ('27-MOLAR SUPERIOR', '27-MOLAR SUPERIOR'), ('28-MOLAR SUPERIOR', '28-MOLAR SUPERIOR'), ('31-INCISIVO CENTRAL INFERIOR', '31-INCISIVO CENTRAL INFERIOR'), ('41-INCISIVO CENTRAL INFERIOR', '41-INCISIVO CENTRAL INFERIOR'), ('32-INCISIVO LATERAL INFERIOR', '32-INCISIVO LATERAL INFERIOR'), ('42-INCISIVO LATERAL INFERIOR', '42-INCISIVO LATERAL INFERIOR'), ('33-CANINO INFERIOR', '33-CANINO INFERIOR'), ('43-CANINO INFERIOR', '43-CANINO INFERIOR'), ('34-PRE MOLAR INFERIOR', '34-PRE MOLAR INFERIOR'), ('35-PRE MOLAR INFERIOR', '35-PRE MOLAR INFERIOR'), ('44-PRE MOLAR INFERIOR', '44-PRE MOLAR INFERIOR'), ('45-PRE MOLAR INFERIOR', '45-PRE MOLAR INFERIOR'), ('36-MOLAR INFERIOR', '36-MOLAR INFERIOR'), ('37-MOLAR INFERIOR', '37-MOLAR INFERIOR'), ('38-MOLAR INFERIOR', '38-MOLAR INFERIOR'), ('46-MOLAR INFERIOR', '46-MOLAR INFERIOR'), ('47-MOLAR INFERIOR', '47-MOLAR INFERIOR'), ('48-MOLAR INFERIOR', '48-MOLAR INFERIOR')], max_length=60, verbose_name='Dente')),
                ('observacao', models.CharField(max_length=5000, verbose_name='Observação')),
                ('valor_tratamento', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='valor')),
                ('data_tratamento', models.DateField(default=django.utils.timezone.now, verbose_name='Data Tratamento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tratamento', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cadastrotratamento.CadastroTratamento', verbose_name='Tratamento')),
            ],
            options={
                'verbose_name': 'Tratamento',
                'verbose_name_plural': 'Tratamentos',
            },
        ),
    ]
