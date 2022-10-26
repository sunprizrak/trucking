from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


def path_contract_1(instance, filename):
    return 'Договоры/{user_name}/грузоперевозки/{user_email}/{filename}'.format(user_name=instance.name,user_email=instance.email, filename=filename)


def path_contract_2(instance, filename):
    return 'Договоры/{user_name}/таможенный_представитель/{user_email}/{filename}'.format(user_name=instance.name, user_email=instance.email, filename=filename)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(verbose_name='Наименование организации', max_length=255, blank=True)
    address = models.CharField(verbose_name='Юридический адрес', max_length=255, blank=True)
    bank_account = models.CharField(verbose_name='Банковский счёт', max_length=40, blank=True)
    unp = models.CharField(verbose_name='УНП', max_length=30, blank=True)
    contract_1 = models.FileField(verbose_name='Договор на грузоперевозки', upload_to=path_contract_1, blank=True)
    contract_2 = models.FileField(verbose_name='Договор на оказание услуг таможенного представителя', upload_to=path_contract_2, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email