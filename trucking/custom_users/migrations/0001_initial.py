# Generated by Django 4.2.1 on 2023-05-12 20:33

import custom_users.managers
import custom_users.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Наименование организации')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Юридический адрес')),
                ('bank_account', models.CharField(blank=True, max_length=40, verbose_name='Банковский счёт')),
                ('unp', models.CharField(blank=True, max_length=9, validators=[django.core.validators.MinLengthValidator(9)], verbose_name='УНП')),
                ('contract_1', models.FileField(blank=True, max_length=255, upload_to=custom_users.models.path_contract_1, verbose_name='Договор на грузоперевозки')),
                ('contract_2', models.FileField(blank=True, max_length=255, upload_to=custom_users.models.path_contract_2, verbose_name='Договор на оказание услуг таможенного представителя')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-created'],
            },
            managers=[
                ('objects', custom_users.managers.CustomUserManager()),
            ],
        ),
    ]
