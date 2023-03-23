import configparser
import os
import os.path

class Config(object):
    def __init__(self):
        
        config_path = './config/config.ini'

        self.config = configparser.ConfigParser()

        if (os.path.isfile(config_path) == False):
            f = open(config_path, 'w')
            f.close()

        self.__attempt_add_section('APP_CONFIG')
        self.__attempt_add_section('BLOB_CONFIG')

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def get_section(self, section, value):
        return self.config[section][value]
    
    def __attempt_add_section(self, section):
        if (self.config.has_section(section) == False):
            self.config.add_section(section)
