import configparser
import os
import os.path

class Config(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance
    
    def __init__(self):
        if (self.__initialized): return
        self.__initialized = True
        
        self.config_path = './config/config.ini'
        self.config = configparser.ConfigParser()

        if (os.path.isfile(self.config_path) == False):
            f = open(self.config_path, 'w')
            f.close()

        self.config.read(self.config_path)

        self.__attempt_add_section('APP_CONFIG')
        self.__attempt_add_section('BLOB_CONFIG')

        self.__write_to_file()

    def get_option(self, section, option):
        return self.config[section][option]
    
    def set_option(self, section, option, value):
        self.__attempt_add_section(section)
        self.config.set(section, option, value)
        self.__write_to_file()

    # will only set value if an option does not already exist
    def attempt_set_option(self, section, option, value):
        self.__attempt_add_section(section)
        if (self.config.has_option(section, option) == False):
            self.set_option(section, option, value)


    def __attempt_add_section(self, section):
        if (self.config.has_section(section) == False):
            self.config.add_section(section)
            self.__write_to_file()

    def __write_to_file(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
