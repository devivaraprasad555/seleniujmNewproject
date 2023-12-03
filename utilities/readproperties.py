import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configrations\\config.ini")


class ReadConfig:

    @classmethod
    def get_url(cls):
        url = config.get("commonInfo","baseURL")
        return url
