from docx import Document
from trucking.settings import MEDIA_ROOT
import os


def create_doc(instance):
    # document = Document(f'{MEDIA_ROOT}/Заявка_№5_Wuxi.docx')
    # path = f'Организации/{instance.user.unp}/Документы(Заявки)/Перевозка/{instance.user.email}/Заявка_{instance.created.strftime("%d.%m.%Y_%H:%M:%S")}.docx'
    # full_path = f'{MEDIA_ROOT}/{path}'
    # try:
    #     document.save(full_path)
    # except FileNotFoundError:
    #     os.makedirs('/'.join(full_path.split('/')[:-1]), mode=0o777, exist_ok=False)
    #     document.save(full_path)
    # finally:
    #     return path
    pass
