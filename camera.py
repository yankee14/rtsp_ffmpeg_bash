""" Surveillance Cameras """
import datetime
import pytz
import ipaddress


class Camera:
    """ Surveillance Cameras """
    def __init__(self,
                 name: str = "default",
                 ip: ipaddress = ipaddress.IPv4Address("169.254.0.0")):
        self.name: str = name
        self.ip: ipaddress = ip
        self.up: bool = False
        self.last_up_check: datetime = datetime.datetime(0,
                                                         0,
                                                         0,
                                                         0,
                                                         0,
                                                         0,
                                                         tz=pytz.UTC)
