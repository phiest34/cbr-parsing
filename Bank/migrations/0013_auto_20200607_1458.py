# Generated by Django 3.0.4 on 2020-06-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Bank', '0012_auto_20200606_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='banks_b',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGN', models.CharField(default='None', max_length=4, null=True)),
                ('OKATO', models.CharField(default='0', max_length=2, null=True)),
                ('OKPO', models.CharField(default='0', max_length=8, null=True)),
                ('OGRN', models.CharField(default='0', max_length=13, null=True)),
                ('REGN_S', models.CharField(default='0', max_length=10, null=True)),
                ('BIC', models.CharField(default='0', max_length=9, null=True)),
                ('DT', models.CharField(default='None', max_length=10, null=True)),
                ('NAME_B', models.CharField(default='0', max_length=60, null=True)),
                ('ADR', models.CharField(default='0', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='banks_d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT', models.CharField(default='None', max_length=10, null=True)),
                ('REGN', models.CharField(default='None', max_length=4, null=True)),
                ('C1', models.CharField(default='None', max_length=15, null=True)),
                ('C3', models.CharField(default='None', max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='banks_n',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT', models.CharField(default='None', max_length=10, null=True)),
                ('C1', models.CharField(default='None', max_length=15, null=True)),
                ('C2_1', models.CharField(default='None', max_length=240, null=True)),
                ('C2_2', models.CharField(default='None', max_length=240, null=True)),
                ('C2_3', models.CharField(default='None', max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='banks_s',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT', models.CharField(default='None', max_length=10, null=True)),
                ('REGN', models.CharField(default='None', max_length=4, null=True)),
                ('C1_S', models.CharField(default='0', max_length=20, null=True)),
                ('C2_S', models.CharField(default='0', max_length=20, null=True)),
                ('C31_S', models.CharField(default='0', max_length=20, null=True)),
                ('C32_S', models.CharField(default='0', max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='bank012014_b',
        ),
        migrations.DeleteModel(
            name='bank012014_d',
        ),
        migrations.DeleteModel(
            name='bank012014_n',
        ),
        migrations.DeleteModel(
            name='bank012015_b',
        ),
        migrations.DeleteModel(
            name='bank012015_d',
        ),
        migrations.DeleteModel(
            name='bank012015_n',
        ),
        migrations.DeleteModel(
            name='bank012016_b',
        ),
        migrations.DeleteModel(
            name='bank012016_d',
        ),
        migrations.DeleteModel(
            name='bank012016_n',
        ),
        migrations.DeleteModel(
            name='bank012016_s',
        ),
        migrations.DeleteModel(
            name='bank012017_b',
        ),
        migrations.DeleteModel(
            name='bank012017_d',
        ),
        migrations.DeleteModel(
            name='bank012017_n',
        ),
        migrations.DeleteModel(
            name='bank012017_s',
        ),
        migrations.DeleteModel(
            name='bank012018_b',
        ),
        migrations.DeleteModel(
            name='bank012018_d',
        ),
        migrations.DeleteModel(
            name='bank012018_n',
        ),
        migrations.DeleteModel(
            name='bank012018_s',
        ),
        migrations.DeleteModel(
            name='bank012019_b',
        ),
        migrations.DeleteModel(
            name='bank012019_d',
        ),
        migrations.DeleteModel(
            name='bank012019_n',
        ),
        migrations.DeleteModel(
            name='bank012019_s',
        ),
        migrations.DeleteModel(
            name='bank012020_b',
        ),
        migrations.DeleteModel(
            name='bank012020_d',
        ),
        migrations.DeleteModel(
            name='bank012020_n',
        ),
        migrations.DeleteModel(
            name='bank012020_s',
        ),
        migrations.DeleteModel(
            name='bank022014_b',
        ),
        migrations.DeleteModel(
            name='bank022014_d',
        ),
        migrations.DeleteModel(
            name='bank022014_n',
        ),
        migrations.DeleteModel(
            name='bank022015_b',
        ),
        migrations.DeleteModel(
            name='bank022015_d',
        ),
        migrations.DeleteModel(
            name='bank022015_n',
        ),
        migrations.DeleteModel(
            name='bank022016_b',
        ),
        migrations.DeleteModel(
            name='bank022016_d',
        ),
        migrations.DeleteModel(
            name='bank022016_n',
        ),
        migrations.DeleteModel(
            name='bank022016_s',
        ),
        migrations.DeleteModel(
            name='bank022017_b',
        ),
        migrations.DeleteModel(
            name='bank022017_d',
        ),
        migrations.DeleteModel(
            name='bank022017_n',
        ),
        migrations.DeleteModel(
            name='bank022017_s',
        ),
        migrations.DeleteModel(
            name='bank022018_b',
        ),
        migrations.DeleteModel(
            name='bank022018_d',
        ),
        migrations.DeleteModel(
            name='bank022018_n',
        ),
        migrations.DeleteModel(
            name='bank022018_s',
        ),
        migrations.DeleteModel(
            name='bank022019_b',
        ),
        migrations.DeleteModel(
            name='bank022019_d',
        ),
        migrations.DeleteModel(
            name='bank022019_n',
        ),
        migrations.DeleteModel(
            name='bank022019_s',
        ),
        migrations.DeleteModel(
            name='bank022020_b',
        ),
        migrations.DeleteModel(
            name='bank022020_d',
        ),
        migrations.DeleteModel(
            name='bank022020_n',
        ),
        migrations.DeleteModel(
            name='bank022020_s',
        ),
        migrations.DeleteModel(
            name='bank032014_b',
        ),
        migrations.DeleteModel(
            name='bank032014_d',
        ),
        migrations.DeleteModel(
            name='bank032014_n',
        ),
        migrations.DeleteModel(
            name='bank032015_b',
        ),
        migrations.DeleteModel(
            name='bank032015_d',
        ),
        migrations.DeleteModel(
            name='bank032015_n',
        ),
        migrations.DeleteModel(
            name='bank032016_b',
        ),
        migrations.DeleteModel(
            name='bank032016_d',
        ),
        migrations.DeleteModel(
            name='bank032016_n',
        ),
        migrations.DeleteModel(
            name='bank032016_s',
        ),
        migrations.DeleteModel(
            name='bank032017_b',
        ),
        migrations.DeleteModel(
            name='bank032017_d',
        ),
        migrations.DeleteModel(
            name='bank032017_n',
        ),
        migrations.DeleteModel(
            name='bank032017_s',
        ),
        migrations.DeleteModel(
            name='bank032018_b',
        ),
        migrations.DeleteModel(
            name='bank032018_d',
        ),
        migrations.DeleteModel(
            name='bank032018_n',
        ),
        migrations.DeleteModel(
            name='bank032018_s',
        ),
        migrations.DeleteModel(
            name='bank032019_b',
        ),
        migrations.DeleteModel(
            name='bank032019_d',
        ),
        migrations.DeleteModel(
            name='bank032019_n',
        ),
        migrations.DeleteModel(
            name='bank032019_s',
        ),
        migrations.DeleteModel(
            name='bank032020_b',
        ),
        migrations.DeleteModel(
            name='bank032020_d',
        ),
        migrations.DeleteModel(
            name='bank032020_n',
        ),
        migrations.DeleteModel(
            name='bank032020_s',
        ),
        migrations.DeleteModel(
            name='bank042014_b',
        ),
        migrations.DeleteModel(
            name='bank042014_d',
        ),
        migrations.DeleteModel(
            name='bank042014_n',
        ),
        migrations.DeleteModel(
            name='bank042015_b',
        ),
        migrations.DeleteModel(
            name='bank042015_d',
        ),
        migrations.DeleteModel(
            name='bank042015_n',
        ),
        migrations.DeleteModel(
            name='bank042016_b',
        ),
        migrations.DeleteModel(
            name='bank042016_d',
        ),
        migrations.DeleteModel(
            name='bank042016_n',
        ),
        migrations.DeleteModel(
            name='bank042016_s',
        ),
        migrations.DeleteModel(
            name='bank042017_b',
        ),
        migrations.DeleteModel(
            name='bank042017_d',
        ),
        migrations.DeleteModel(
            name='bank042017_n',
        ),
        migrations.DeleteModel(
            name='bank042017_s',
        ),
        migrations.DeleteModel(
            name='bank042018_b',
        ),
        migrations.DeleteModel(
            name='bank042018_d',
        ),
        migrations.DeleteModel(
            name='bank042018_n',
        ),
        migrations.DeleteModel(
            name='bank042018_s',
        ),
        migrations.DeleteModel(
            name='bank042019_b',
        ),
        migrations.DeleteModel(
            name='bank042019_d',
        ),
        migrations.DeleteModel(
            name='bank042019_n',
        ),
        migrations.DeleteModel(
            name='bank042019_s',
        ),
        migrations.DeleteModel(
            name='bank042020_b',
        ),
        migrations.DeleteModel(
            name='bank042020_d',
        ),
        migrations.DeleteModel(
            name='bank042020_n',
        ),
        migrations.DeleteModel(
            name='bank042020_s',
        ),
        migrations.DeleteModel(
            name='bank052014_b',
        ),
        migrations.DeleteModel(
            name='bank052014_d',
        ),
        migrations.DeleteModel(
            name='bank052014_n',
        ),
        migrations.DeleteModel(
            name='bank052015_b',
        ),
        migrations.DeleteModel(
            name='bank052015_d',
        ),
        migrations.DeleteModel(
            name='bank052015_n',
        ),
        migrations.DeleteModel(
            name='bank052016_b',
        ),
        migrations.DeleteModel(
            name='bank052016_d',
        ),
        migrations.DeleteModel(
            name='bank052016_n',
        ),
        migrations.DeleteModel(
            name='bank052016_s',
        ),
        migrations.DeleteModel(
            name='bank052017_b',
        ),
        migrations.DeleteModel(
            name='bank052017_d',
        ),
        migrations.DeleteModel(
            name='bank052017_n',
        ),
        migrations.DeleteModel(
            name='bank052017_s',
        ),
        migrations.DeleteModel(
            name='bank052018_b',
        ),
        migrations.DeleteModel(
            name='bank052018_d',
        ),
        migrations.DeleteModel(
            name='bank052018_n',
        ),
        migrations.DeleteModel(
            name='bank052018_s',
        ),
        migrations.DeleteModel(
            name='bank052019_b',
        ),
        migrations.DeleteModel(
            name='bank052019_d',
        ),
        migrations.DeleteModel(
            name='bank052019_n',
        ),
        migrations.DeleteModel(
            name='bank052019_s',
        ),
        migrations.DeleteModel(
            name='bank052020_b',
        ),
        migrations.DeleteModel(
            name='bank052020_d',
        ),
        migrations.DeleteModel(
            name='bank052020_n',
        ),
        migrations.DeleteModel(
            name='bank052020_s',
        ),
        migrations.DeleteModel(
            name='bank062014_b',
        ),
        migrations.DeleteModel(
            name='bank062014_d',
        ),
        migrations.DeleteModel(
            name='bank062014_n',
        ),
        migrations.DeleteModel(
            name='bank062015_b',
        ),
        migrations.DeleteModel(
            name='bank062015_d',
        ),
        migrations.DeleteModel(
            name='bank062015_n',
        ),
        migrations.DeleteModel(
            name='bank062016_b',
        ),
        migrations.DeleteModel(
            name='bank062016_d',
        ),
        migrations.DeleteModel(
            name='bank062016_n',
        ),
        migrations.DeleteModel(
            name='bank062016_s',
        ),
        migrations.DeleteModel(
            name='bank062017_b',
        ),
        migrations.DeleteModel(
            name='bank062017_d',
        ),
        migrations.DeleteModel(
            name='bank062017_n',
        ),
        migrations.DeleteModel(
            name='bank062017_s',
        ),
        migrations.DeleteModel(
            name='bank062018_b',
        ),
        migrations.DeleteModel(
            name='bank062018_d',
        ),
        migrations.DeleteModel(
            name='bank062018_n',
        ),
        migrations.DeleteModel(
            name='bank062018_s',
        ),
        migrations.DeleteModel(
            name='bank062019_b',
        ),
        migrations.DeleteModel(
            name='bank062019_d',
        ),
        migrations.DeleteModel(
            name='bank062019_n',
        ),
        migrations.DeleteModel(
            name='bank062019_s',
        ),
        migrations.DeleteModel(
            name='bank072014_b',
        ),
        migrations.DeleteModel(
            name='bank072014_d',
        ),
        migrations.DeleteModel(
            name='bank072014_n',
        ),
        migrations.DeleteModel(
            name='bank072015_b',
        ),
        migrations.DeleteModel(
            name='bank072015_d',
        ),
        migrations.DeleteModel(
            name='bank072015_n',
        ),
        migrations.DeleteModel(
            name='bank072016_b',
        ),
        migrations.DeleteModel(
            name='bank072016_d',
        ),
        migrations.DeleteModel(
            name='bank072016_n',
        ),
        migrations.DeleteModel(
            name='bank072016_s',
        ),
        migrations.DeleteModel(
            name='bank072017_b',
        ),
        migrations.DeleteModel(
            name='bank072017_d',
        ),
        migrations.DeleteModel(
            name='bank072017_n',
        ),
        migrations.DeleteModel(
            name='bank072017_s',
        ),
        migrations.DeleteModel(
            name='bank072018_b',
        ),
        migrations.DeleteModel(
            name='bank072018_d',
        ),
        migrations.DeleteModel(
            name='bank072018_n',
        ),
        migrations.DeleteModel(
            name='bank072018_s',
        ),
        migrations.DeleteModel(
            name='bank072019_b',
        ),
        migrations.DeleteModel(
            name='bank072019_d',
        ),
        migrations.DeleteModel(
            name='bank072019_n',
        ),
        migrations.DeleteModel(
            name='bank072019_s',
        ),
        migrations.DeleteModel(
            name='bank082014_b',
        ),
        migrations.DeleteModel(
            name='bank082014_d',
        ),
        migrations.DeleteModel(
            name='bank082014_n',
        ),
        migrations.DeleteModel(
            name='bank082015_b',
        ),
        migrations.DeleteModel(
            name='bank082015_d',
        ),
        migrations.DeleteModel(
            name='bank082015_n',
        ),
        migrations.DeleteModel(
            name='bank082016_b',
        ),
        migrations.DeleteModel(
            name='bank082016_d',
        ),
        migrations.DeleteModel(
            name='bank082016_n',
        ),
        migrations.DeleteModel(
            name='bank082016_s',
        ),
        migrations.DeleteModel(
            name='bank082017_b',
        ),
        migrations.DeleteModel(
            name='bank082017_d',
        ),
        migrations.DeleteModel(
            name='bank082017_n',
        ),
        migrations.DeleteModel(
            name='bank082017_s',
        ),
        migrations.DeleteModel(
            name='bank082018_b',
        ),
        migrations.DeleteModel(
            name='bank082018_d',
        ),
        migrations.DeleteModel(
            name='bank082018_n',
        ),
        migrations.DeleteModel(
            name='bank082018_s',
        ),
        migrations.DeleteModel(
            name='bank082019_b',
        ),
        migrations.DeleteModel(
            name='bank082019_d',
        ),
        migrations.DeleteModel(
            name='bank082019_n',
        ),
        migrations.DeleteModel(
            name='bank082019_s',
        ),
        migrations.DeleteModel(
            name='bank092014_b',
        ),
        migrations.DeleteModel(
            name='bank092014_d',
        ),
        migrations.DeleteModel(
            name='bank092014_n',
        ),
        migrations.DeleteModel(
            name='bank092015_b',
        ),
        migrations.DeleteModel(
            name='bank092015_d',
        ),
        migrations.DeleteModel(
            name='bank092015_n',
        ),
        migrations.DeleteModel(
            name='bank092016_b',
        ),
        migrations.DeleteModel(
            name='bank092016_d',
        ),
        migrations.DeleteModel(
            name='bank092016_n',
        ),
        migrations.DeleteModel(
            name='bank092016_s',
        ),
        migrations.DeleteModel(
            name='bank092017_b',
        ),
        migrations.DeleteModel(
            name='bank092017_d',
        ),
        migrations.DeleteModel(
            name='bank092017_n',
        ),
        migrations.DeleteModel(
            name='bank092017_s',
        ),
        migrations.DeleteModel(
            name='bank092018_b',
        ),
        migrations.DeleteModel(
            name='bank092018_d',
        ),
        migrations.DeleteModel(
            name='bank092018_n',
        ),
        migrations.DeleteModel(
            name='bank092018_s',
        ),
        migrations.DeleteModel(
            name='bank092019_b',
        ),
        migrations.DeleteModel(
            name='bank092019_d',
        ),
        migrations.DeleteModel(
            name='bank092019_n',
        ),
        migrations.DeleteModel(
            name='bank092019_s',
        ),
        migrations.DeleteModel(
            name='bank102014_b',
        ),
        migrations.DeleteModel(
            name='bank102014_d',
        ),
        migrations.DeleteModel(
            name='bank102014_n',
        ),
        migrations.DeleteModel(
            name='bank102015_b',
        ),
        migrations.DeleteModel(
            name='bank102015_d',
        ),
        migrations.DeleteModel(
            name='bank102015_n',
        ),
        migrations.DeleteModel(
            name='bank102016_b',
        ),
        migrations.DeleteModel(
            name='bank102016_d',
        ),
        migrations.DeleteModel(
            name='bank102016_n',
        ),
        migrations.DeleteModel(
            name='bank102016_s',
        ),
        migrations.DeleteModel(
            name='bank102017_b',
        ),
        migrations.DeleteModel(
            name='bank102017_d',
        ),
        migrations.DeleteModel(
            name='bank102017_n',
        ),
        migrations.DeleteModel(
            name='bank102017_s',
        ),
        migrations.DeleteModel(
            name='bank102018_b',
        ),
        migrations.DeleteModel(
            name='bank102018_d',
        ),
        migrations.DeleteModel(
            name='bank102018_n',
        ),
        migrations.DeleteModel(
            name='bank102018_s',
        ),
        migrations.DeleteModel(
            name='bank102019_b',
        ),
        migrations.DeleteModel(
            name='bank102019_d',
        ),
        migrations.DeleteModel(
            name='bank102019_n',
        ),
        migrations.DeleteModel(
            name='bank102019_s',
        ),
        migrations.DeleteModel(
            name='bank112014_b',
        ),
        migrations.DeleteModel(
            name='bank112014_d',
        ),
        migrations.DeleteModel(
            name='bank112014_n',
        ),
        migrations.DeleteModel(
            name='bank112015_b',
        ),
        migrations.DeleteModel(
            name='bank112015_d',
        ),
        migrations.DeleteModel(
            name='bank112015_n',
        ),
        migrations.DeleteModel(
            name='bank112016_b',
        ),
        migrations.DeleteModel(
            name='bank112016_d',
        ),
        migrations.DeleteModel(
            name='bank112016_n',
        ),
        migrations.DeleteModel(
            name='bank112016_s',
        ),
        migrations.DeleteModel(
            name='bank112017_b',
        ),
        migrations.DeleteModel(
            name='bank112017_d',
        ),
        migrations.DeleteModel(
            name='bank112017_n',
        ),
        migrations.DeleteModel(
            name='bank112017_s',
        ),
        migrations.DeleteModel(
            name='bank112018_b',
        ),
        migrations.DeleteModel(
            name='bank112018_d',
        ),
        migrations.DeleteModel(
            name='bank112018_n',
        ),
        migrations.DeleteModel(
            name='bank112018_s',
        ),
        migrations.DeleteModel(
            name='bank112019_b',
        ),
        migrations.DeleteModel(
            name='bank112019_d',
        ),
        migrations.DeleteModel(
            name='bank112019_n',
        ),
        migrations.DeleteModel(
            name='bank112019_s',
        ),
        migrations.DeleteModel(
            name='bank122014_b',
        ),
        migrations.DeleteModel(
            name='bank122014_d',
        ),
        migrations.DeleteModel(
            name='bank122014_n',
        ),
        migrations.DeleteModel(
            name='bank122015_b',
        ),
        migrations.DeleteModel(
            name='bank122015_d',
        ),
        migrations.DeleteModel(
            name='bank122015_n',
        ),
        migrations.DeleteModel(
            name='bank122016_b',
        ),
        migrations.DeleteModel(
            name='bank122016_d',
        ),
        migrations.DeleteModel(
            name='bank122016_n',
        ),
        migrations.DeleteModel(
            name='bank122016_s',
        ),
        migrations.DeleteModel(
            name='bank122017_b',
        ),
        migrations.DeleteModel(
            name='bank122017_d',
        ),
        migrations.DeleteModel(
            name='bank122017_n',
        ),
        migrations.DeleteModel(
            name='bank122017_s',
        ),
        migrations.DeleteModel(
            name='bank122018_b',
        ),
        migrations.DeleteModel(
            name='bank122018_d',
        ),
        migrations.DeleteModel(
            name='bank122018_n',
        ),
        migrations.DeleteModel(
            name='bank122018_s',
        ),
        migrations.DeleteModel(
            name='bank122019_b',
        ),
        migrations.DeleteModel(
            name='bank122019_d',
        ),
        migrations.DeleteModel(
            name='bank122019_n',
        ),
        migrations.DeleteModel(
            name='bank122019_s',
        ),
        migrations.DeleteModel(
            name='bank_s',
        ),
        migrations.AlterField(
            model_name='banks',
            name='name',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='forms',
            name='data',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
    ]
