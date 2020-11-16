""" RTSP Surveillance Camera Manager """

from typing import List
import time
from camera import Camera

cameras: List[Camera] = []

def enumerate_cameras():
    """ Generate set of test cameras """
    cameras.extend([
            Camera(name="trash", stream_url="rtsp://192.168.1.10:554/live/ch00_0"),
            Camera(name="back patio", stream_url="rtsp://192.168.1.12:554/live/ch00_0"),
            Camera(name="breaker", stream_url="rtsp://192.168.1.13:554/live/ch00_0"),
            Camera(name="driveway", stream_url="rtsp://192.168.1.14:554/live/ch00_0")])

    for camera in cameras:
        print(camera)

    cameras[0].probe()

    time.sleep(10)

    for camera in cameras:
        print(camera)

def main():
    """ Program entry point """
    enumerate_cameras()

if __name__ == "__main__":
    main()
