""" Manage and monitor surveillance configuration """
import configparser


class SurveillanceConfiguration:
    """ Manage and monitor surveillance configuration """
    def __init__(self):
        self.CONFIGURATION_FILEPATH = './surveillance_configuration.ini'

        self.latest_configuration = None
        self.spawn_configuration_monitor()

    def spawn_configuration_monitor(self):
        pass

    def write_default_configuration(self):
        pass

    def read_configuration_from_disk(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIGURATION_FILEPATH)
