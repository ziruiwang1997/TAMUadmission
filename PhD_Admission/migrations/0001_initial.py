# Generated by Django 3.1.3 on 2020-11-12 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('App_Seq_No', models.AutoField(primary_key=True, serialize=False)),
                ('Application_ID', models.CharField(max_length=10)),
                ('Average_Review_Score', models.FloatField()),
                ('Applied_Degree', models.CharField(max_length=50)),
                ('Nationality', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Research_Interest', models.CharField(max_length=500)),
                ('Potential_Faculty', models.CharField(max_length=500)),
                ('BS_University_and_GPA', models.CharField(max_length=500)),
                ('MS_University_and_GPA', models.CharField(max_length=500)),
                ('GRE_Score', models.IntegerField()),
                ('TOEFL_Score', models.IntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Ethnicity', models.CharField(max_length=50)),
                ('Residency', models.CharField(max_length=50)),
                ('Citizenship', models.CharField(max_length=50)),
                ('Faculty_Contact', models.CharField(max_length=50)),
                ('Faculty_giving_GANT_GAT', models.CharField(max_length=50)),
                ('Faculty_giving_GAR', models.CharField(max_length=50)),
            ],
        ),
    ]