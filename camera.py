""" Surveillance Cameras """
import pprint
import urllib.parse
import sys
import arrow
#import json
#import platform
#import subprocess

import ffmpeg


class Camera:
    """ Surveillance Cameras """

    count: int = 0

    def __init__(self,
                 name: str = "default",
                 stream_url: str = "rtsp://169.254.0.0:554/live/ch00_0"):
        Camera.count += 1
        self.name: str = name
        self.stream_url = urllib.parse.urlparse(stream_url)

        self.is_up: bool = False
        self.datetime_last_up: arrow = None
        self._probe: str = None
        self.datetime_last_probe: arrow = None

    def __del__(self):
        Camera.count -= 1

    def __str__(self) -> str:
        output: str = "Camera '" + self.name + "' at '" + str(self.stream_url.geturl()) + " was "

        if not self.datetime_last_probe:
            output += "never probed"
            return output

        output+= "last probed " + self.datetime_last_probe.humanize(arrow.utcnow()) + \
        " at " + str(self.datetime_last_probe)

        return output


#    def check_if_up(self):
#        """ ICMP ping to check if camera is up """
#        ping_params = ('-n'
#                       if platform.system().lower() == 'windows' else '-c')
#        ping_command = ['ping', ping_params, '1', self.stream_url.netloc]
#        self.is_up = (0 == subprocess.run(ping_command, check=False))
#        self.datetime_last_up = datetime.datetime.now(tz=pytz.UTC)

    def probe(self):
        """ Probe camera with FFmpeg, store results in probe """
        print("Probing camera '" + self.name + "' at " +
              str(self.stream_url.geturl()))

        self.datetime_last_probe = arrow.utcnow()
        try:
            self._probe = ffmpeg.probe(str(self.stream_url.geturl()))
        except ffmpeg.Error:
            print("fatal error", file=sys.stderr)
            self.is_up = False
            return

        self.is_up = True
        self.datetime_last_up = self.datetime_last_probe
        pprint.pprint(self._probe)

if __name__ == "__main__":
    # camera count before creation
    print("Camera.count = " + str(Camera.count))

    # create a default camera and show count
    cam1 = Camera()
    print("Camera.count = " + str(Camera.count))

    # create a named camera w/ url and show count
    cam2 = Camera(name="hello",
                  stream_url="rtsp://169.254.0.0:554/live/ch00_0")
    print("Camera.count = " + str(Camera.count))

    # destroy a camera and show count
    del cam2
    print("Camera.count = " + str(Camera.count))

    # create a named camera w/ url and show all
    cam2 = Camera(name="test",
                  stream_url="rtsp://192.168.1.10:554/live/ch00_0")
    print("Camera.count = " + str(Camera.count))

    print("cam2.name = " + cam2.name)
    print("cam2.ip_address = " + str(cam2.stream_url.geturl()))
    print("cam2.is_up = " + str(cam2.is_up))
    print("cam2.datetime_last_up = " + str(cam2.datetime_last_up))
    print("cam2.datetime_last_probe: " + str(cam2.datetime_last_probe))

    #print(cam2.stream_url)
    cam2.probe()
    print("cam2.name = " + cam2.name)
    print("cam2.ip_address = " + str(cam2.stream_url.geturl()))
    print("cam2.is_up = " + str(cam2.is_up))
    print("cam2.datetime_last_up = " + str(cam2.datetime_last_up))
    print("cam2.datetime_last_probe: " + str(cam2.datetime_last_probe))

    cam1.probe()
    print("cam1.name = " + cam1.name)
    print("cam1.ip_address = " + str(cam1.stream_url.geturl()))
    print("cam1.is_up = " + str(cam1.is_up))
    print("cam1.datetime_last_up = " + str(cam1.datetime_last_up))
    print("cam1.datetime_last_probe: " + str(cam1.datetime_last_probe))
