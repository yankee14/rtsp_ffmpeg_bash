""" All-In-One RTSP Surveillance Recorder """
import json

import ffmpeg

#from surveillance import Surveillance
#import ipdb
#ipdb.set_trace()


def main():
    """ Program entry """
    print('hello')
    probe = ffmpeg.probe('rtsp://192.168.1.15:554/live/ch00_0')
    probe = json.dumps(probe, sort_keys=True, indent=4)
    print(probe)

    probe2 = ffmpeg.probe(
        "/home/yankee/Videos/FEDEVEL/Advanced PCB Layout Course/Lesson 01/lesson_01.mkv"
    )
    probe2 = json.dumps(probe2, sort_keys=True, indent=4)
    print(probe2)


if __name__ == "__main__":
    main()
