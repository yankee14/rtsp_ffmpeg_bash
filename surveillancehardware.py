""" Benchmarking tools for surveillance """
import multiprocessing

import psutil


class SurveillanceHardware:
    HARDWARE_INFO_FILENAME: str = 'hardware_info.ini'

    available_cores: int = -1

    def __init__(self):
        self.load_previous_hardware_configuration()
        self.load_current_hardware_configuration()
        self.read_available_cores()
        self.save_current_hardware_configuration()
        self.benchmark()

    def load_previous_hardware_configuration(self):
        print('Loading previous hardware configuration')

    def load_current_hardware_configuration(self):
        print('Loading current hardware configuration')

    def save_current_hardware_configuration(self):
        print('Saving current hardare configuration')

    def read_available_cores(self):
        print('Reading current usable core count')
        self.core_count = psutil.cpu_count(logical=True)
        print(f'Found {self.core_count} available cores')

    def benchmark(self):
        print('Benchmarking')
