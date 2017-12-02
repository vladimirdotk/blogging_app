#!/usr/bin/env python3

import os
import time
from dotenv import load_dotenv
from pymailcloud.PyMailCloud import PyMailCloud

load_dotenv('.env')

cloud = PyMailCloud(os.getenv('MAIL_RU_LOGIN'), os.getenv('MAIL_RU_PASSWORD'))
cloud.upload_files(
    [
        {
        'filename': os.path.abspath('./run/' + os.getenv('DB_FILE_NAME')),
        'path': 'blog_db/' + str(round(time.time())) + '/'
        }
    ]
)