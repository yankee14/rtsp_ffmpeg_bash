""" FFMPEG-based Surveillance Camera Transcoding and Storage Tool """

from surveillanceconfiguration import SurveillanceConfiguration
from surveillancehardware import SurveillanceHardware


class Surveillance:
    """ Monitor, record, and backup surveillance footage """

    surveillance_configuration = SurveillanceConfiguration()
    surveillance_hardware = SurveillanceHardware()

    def __init__(self):
        self.load_surveillance_configuration()
        self.load_hardware_info()
        self.spawn_video_capture()
        self.spawn_short_term_transcoding()
        self.spawn_long_term_transcoding()
        self.spawn_post_processing()
        self.spawn_alerts()

    def load_surveillance_configuration(self):
        print('Loading configuration')

    def load_hardware_info(self):
        print('Loading hardware info')

    def spawn_video_capture(self):
        print('Spawning immediate storage')

    def spawn_short_term_transcoding(self):
        print('Spawning short-term storage')

    def spawn_long_term_transcoding(self):
        print('Spawning long-term storage')

    def spawn_post_processing(self):
        print('Spawning post processing')

    def spawn_alerts(self):
        print('Spawning alerts')
