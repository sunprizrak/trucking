from django.contrib.auth import get_user_model
from django.db import models
from .utils import create_doc


def path_static_dec(instance, filename):
    return 'Организации/{user_unp}/Документы(Заявки)/Статическая_декларация/{user_email}/{filename}'.format(user_unp=instance.user.unp, user_email=instance.user.email, filename=filename)


def path_import_dec(instance, filename):
    return 'Организации/{user_unp}/Документы(Заявки)/Импортная_декларация/{user_email}/{filename}'.format(user_unp=instance.user.unp, user_email=instance.user.email, filename=filename)


class Claim(models.Model):
    shipping_name = models.CharField(verbose_name='Наименование груза', max_length=100)
    gross_weight = models.DecimalField(verbose_name='Вес брутто', max_digits=10, decimal_places=1)
    count_seats = models.IntegerField(verbose_name='Колличество мест')
    TYPESEATS = (
        (None, 'Выбрать'),
        ('1', 'Паллеты'),
        ('2', 'Ящики'),
        ('3', 'Рулоны'),
        ('4', 'Навал'),
        ('6', 'Коробки'),
        ('6', 'Другое'),
    )
    length_seats = models.DecimalField(verbose_name='Длина', max_digits=10, decimal_places=1)
    width_seats = models.DecimalField(verbose_name='Ширина', max_digits=10, decimal_places=1)
    height_seats = models.DecimalField(verbose_name='Высота', max_digits=10, decimal_places=1)
    type_seats = models.CharField(verbose_name='Вид мест', max_length=1, choices=TYPESEATS)
    point_departure = models.CharField(verbose_name='Пункт отправления', max_length=100)
    destination = models.CharField(verbose_name='Пункт назначения', max_length=100)
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)


class PreliminaryClaim(Claim):
    start_date = models.DateField(verbose_name='с')
    end_date = models.DateField(verbose_name='по')
    fly = models.BooleanField(verbose_name='Авиа', default=False)
    train = models.BooleanField(verbose_name='Ж/д', default=False)
    ship = models.BooleanField(verbose_name='Море', default=False)
    auto = models.BooleanField(verbose_name='Авто', default=False)
    contact_person = models.CharField(verbose_name='Контактное лицо', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=30)
    MESENGERS = (
        (None, 'Выбрать'),
        ('WTA', 'WhatsApp'),
        ('VB', 'Viber'),
        ('TG', 'Telegram'),
        ('SKP', 'Skype')
    )
    messenger = models.CharField(verbose_name='Messenger', max_length=3, choices=MESENGERS, blank=True)
    messenger_number = models.CharField(verbose_name='Номер мессенджера', max_length=30, blank=True)

    def __str__(self):
        return f'Запрос ставки на перевозку {self.shipping_name}'

    class Meta:
        verbose_name = 'Запрашиваемая ставка'
        verbose_name_plural = 'Запрашиваемые ставки'


class ShippingClaim(Claim):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Код ТН ВЭД', max_length=10)
    FEATURES = (
        ('D', 'Опасный'),
        ('ND', 'Не опасный'),
    )
    cargo_features = models.CharField(verbose_name='Особеннонсти груза', max_length=2, default='ND', choices=FEATURES)
    INSURANCE = (
        ('YES', 'Требуется'),
        ('NO', 'Не требуется'),
    )
    cargo_insurance = models.CharField(verbose_name='Страхование граза', max_length=3, default='NO', choices=INSURANCE)
    date_loading = models.DateField(verbose_name='Дата Загрузки')
    TRANSPORT = (
        (None, 'Выбрать'),
        ('FLY', 'Авиа'),
        ('TRAIN', 'Ж/д'),
        ('SHIP', 'Море'),
        ('AUTO', 'Авто'),
    )
    transport = models.CharField(verbose_name='Вид транспорта', max_length=5, choices=TRANSPORT)
    person_loading = models.CharField(verbose_name='Контактное лицо на загрузке', max_length=100)
    per_load_number = models.CharField(verbose_name='Номер телефона', max_length=30)
    MESENGERS = (
        (None, 'Выбрать'),
        ('WTA', 'WhatsApp'),
        ('VB', 'Viber'),
        ('TG', 'Telegram'),
        ('SKP', 'Skype'),
    )
    per_load_msg = models.CharField(verbose_name='Messenger', max_length=3, choices=MESENGERS, blank=True)
    per_load_msg_number = models.CharField(verbose_name='Номер мессенджера', max_length=30, blank=True)
    person_unloading = models.CharField(verbose_name='Контактное лицо на выгрузке', max_length=100)
    per_unload_number = models.CharField(verbose_name='Номер телефона', max_length=30)
    per_unload_msg = models.CharField(verbose_name='Messenger', max_length=3, choices=MESENGERS, blank=True)
    per_unload_msg_number = models.CharField(verbose_name='Номер мессенджера', max_length=30, blank=True)
    doc = models.FileField(verbose_name='Документ(Заявка)', max_length=255, blank=True)
    STATUSES = (
        ('F', 'Обрабатывается'),
        ('S', 'В пути'),
        ('E', 'Доставлена'),
    )
    status = models.CharField(verbose_name='Статус', max_length=1, default='F', choices=STATUSES, blank=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        self.doc = create_doc(self)
        super().save()

    def __str__(self):
        return f'Заявка на перевозку {self.shipping_name}'

    class Meta:
        verbose_name = 'Заявка на перевозку'
        verbose_name_plural = 'Заявки на перевозку'


class StaticDeclaration(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doc = models.FileField(verbose_name='Статическая декларация', max_length=255, upload_to=path_static_dec)
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Статическая декларация {self.user}'

    class Meta:
        verbose_name = 'Статическая декларация'
        verbose_name_plural = 'Статические декларации'


class ImportDeclaration(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    doc = models.FileField(verbose_name='Импортная декларация', max_length=255, upload_to=path_import_dec)
    created = models.DateTimeField(verbose_name='Создана', auto_now_add=True)

    def __str__(self):
        return f'Импортная декларация {self.user}'

    class Meta:
        verbose_name = 'Импортная декларация'
        verbose_name_plural = 'Импортные декларации'