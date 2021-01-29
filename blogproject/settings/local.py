from .common import *

SECRET_KEY = '5_e8db4i=f)bn+=u^=j2yah@sr8g(-gxv^b3z#s59g3j6ta1+8'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 搜索设置
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://elasticsearch_local:9200/'
