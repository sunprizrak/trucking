from docx import Document
from trucking.settings import MEDIA_ROOT
import os


def create_doc(object, instance):
    document = Document(f'{MEDIA_ROOT}/Заявка_№5_Wuxi.docx')
    path_save = f'Организации/{instance.user.unp}/Документы(Заявки)/Перевозка/{instance.user.email}/Заявка_{instance.created.strftime("%d.%m.%Y_%H:%M:%S")}.docx'
    try:
        document.save(f'{MEDIA_ROOT}/{path_save}')
    except FileNotFoundError:
        os.makedirs('/'.join(path_save.split('/')[:-1]), mode=0o777, exist_ok=False)
        document.save(f'{MEDIA_ROOT}/{path_save}')
    finally:
        object.objects.create(
            claim=instance,
            doc=path_save,
        )

