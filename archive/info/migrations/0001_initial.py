# Generated by Django 4.2.4 on 2023-08-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matric', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=50)),
                ('DoB', models.DateField(help_text='Date of Birth')),
                ('department', models.CharField(max_length=50)),
                ('graduating_year', models.CharField(choices=[('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=50)),
                ('gce', models.ImageField(blank=True, upload_to='gce/')),
                ('waec', models.ImageField(blank=True, upload_to='waec/')),
                ('jamb', models.ImageField(blank=True, upload_to='jamb/')),
                ('birth_cert', models.ImageField(blank=True, upload_to='birth/')),
                ('passport', models.ImageField(blank=True, upload_to='passport/')),
                ('date_reg', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'ordering': ['surname'],
            },
        ),
    ]
