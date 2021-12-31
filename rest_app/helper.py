import json
from django.conf import settings
import platform


def PriceJson():
    try:
        if platform.system() == 'Linux':
            json_open = open(settings.BASE_DIR / 'static/json/price.json')
        else:
            json_open = open(settings.BASE_DIR/ 'static\\json\\price.json')
        data = json.load(json_open)
        json_open.close()
        return data
    except Exception as e:
        return []
