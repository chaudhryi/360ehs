# Generated by Django 3.0.3 on 2020-02-25 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_doctor_rate_ar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='hire_date',
            new_name='hire_date',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='home_phone',
            new_name='home_phone',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='mobile_phone',
            new_name='mobile_phone',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='rate_ad',
            new_name='rate_ad',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='rate_ex',
            new_name='rate_ex',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='rate_ime',
            new_name='rate_ime',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='rate_ns',
            new_name='rate_ns',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='rate_pr',
            new_name='rate_pr',
        ),
        migrations.RenameField(
            model_name='agentbill',
            old_name='BillDate',
            new_name='bill_date',
        ),
        migrations.RenameField(
            model_name='agentbill',
            old_name='BillPaid',
            new_name='bill_paid',
        ),
        migrations.RenameField(
            model_name='agentbill',
            old_name='BillTotal',
            new_name='bill_total',
        ),
        migrations.RenameField(
            model_name='agentbill',
            old_name='DatePaid',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='applypayment',
            old_name='amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='applypayment',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='Agent',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='assessment_date',
            new_name='assessment_date',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='assessment_time',
            new_name='assessment_time',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='claim_number',
            new_name='claim_number',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='claimant_name',
            new_name='claimant_name',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='Clinic',
            new_name='clinic',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='Doctor',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_date',
            new_name='invoice_date',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_number',
            new_name='invoice_number',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_paid',
            new_name='invoice_paid',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_subtotal',
            new_name='invoice_subtotal',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_tax',
            new_name='invoice_tax',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='invoice_total',
            new_name='invoice_total',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='report_type',
            new_name='report_type',
        ),
        migrations.RenameField(
            model_name='assessment',
            old_name='Source',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='claim_number',
            new_name='claim_number',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='date_of_accident',
            new_name='date_of_accident',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='date_of_birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='full_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='claimant',
            old_name='title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='main_contact',
            new_name='main_contact',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='office_phone',
            new_name='office_phone',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='rate_ime',
            new_name='rate_ime',
        ),
        migrations.RenameField(
            model_name='clinic',
            old_name='rate_ns',
            new_name='rate_ns',
        ),
        migrations.RenameField(
            model_name='clinicbill',
            old_name='BillDate',
            new_name='bill_date',
        ),
        migrations.RenameField(
            model_name='clinicbill',
            old_name='BillPaid',
            new_name='bill_paid',
        ),
        migrations.RenameField(
            model_name='clinicbill',
            old_name='BillTotal',
            new_name='bill_total',
        ),
        migrations.RenameField(
            model_name='clinicbill',
            old_name='DatePaid',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='cmpa',
            new_name='cmpa',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='cpso',
            new_name='cpso',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='home_phone',
            new_name='home_phone',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='mobile_phone',
            new_name='mobile_phone',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rate_ad',
            new_name='rate_ad',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Rate_AR',
            new_name='rate_ar',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rate_ex',
            new_name='rate_ex',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rate_ime',
            new_name='rate_ime',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rate_ns',
            new_name='rate_ns',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='rate_pr',
            new_name='rate_pr',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='BillDate',
            new_name='bill_date',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='BillPaid',
            new_name='bill_paid',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='BillSubtotal',
            new_name='bill_subtotal',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='BillTax',
            new_name='bill_tax',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='BillTotal',
            new_name='bill_total',
        ),
        migrations.RenameField(
            model_name='doctorbill',
            old_name='DatePaid',
            new_name='date_paid',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Applied',
            new_name='applied',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='applied_balance',
            new_name='applied_balance',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='check_number',
            new_name='check_number',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='Source',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='report_type',
            new_name='report_type',
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='Source',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='reporttype',
            old_name='Abbreviation',
            new_name='abbreviation',
        ),
        migrations.RenameField(
            model_name='reporttype',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='Billing_Contact',
            new_name='billing_contact',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='Billing_email',
            new_name='billing_email',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='Billing_Phone',
            new_name='billing_phone',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='Contact_email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='contact_phone',
            new_name='contact_phone',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='main_contact',
            new_name='main_contact',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='notes',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='office_phone',
            new_name='office_phone',
        ),
    ]
