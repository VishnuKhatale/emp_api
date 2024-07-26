# Generated by Django 5.0.7 on 2024-07-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_buisness_email_enquiry_business_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='service_request',
            field=models.CharField(choices=[('Cloud Services', 'Cloud Services'), ('Managed Services', 'Managed Services'), ('Managed Security Services', 'Managed Security Services'), ('Colocation Services', 'Colocation Services'), ('Software as a Service', 'Software as a Service'), ('Platform as a Service', 'Platform as a Service'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
