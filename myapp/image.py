from datetime import datetime
from random import random

import oss2


def upload_image(image):
    now = datetime.now()
    random_name = now.strftime("%Y%m%d%H%M%S") + str(int(random() * 1000)) + '.' + str(image).split('.')[-1]

    auth = oss2.Auth('LTAI5tHC5dvXL48NLigurbg1', 's4dLXbaSPG4GvlHqArkpmiqeHWcR4b')
    bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'petcharm')

    result = bucket.put_object(random_name, image)
    if result.status == 200:
        url = 'http://pic.petcharm.mcatk.com/' + random_name
        return url
    return None
