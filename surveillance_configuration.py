""" Manage and monitor surveillance configuration """
import configparser


class SurveillanceConfiguration:
    """ Manage and monitor surveillance configuration """

    CONFIGURATION_FILEPATH: str = './surveillance_configuration.ini'

    @classmethod
    def __init__(cls):
        cls.latest_configuration = None
        cls.spawn_configuration_monitor()

    @classmethod
    def spawn_configuration_monitor(cls):
        pass

    @classmethod
    def write_default_configuration(cls):
        pass

    @classmethod
    def read_configuration_from_disk(cls):
        config = configparser.ConfigParser()
        config.read(cls.CONFIGURATION_FILEPATH)

    @classmethod
    def __repr__(cls):
        pass
