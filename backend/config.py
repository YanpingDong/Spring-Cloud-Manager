import os
from app.utils.Properties import parseProperties
#Note:do not change this file's location, or you need to modify the  BASE_DIR
#something may help:os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
class GlobalVar:
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    PROPERTIES = parseProperties(BASE_DIR + '/config.properties')
