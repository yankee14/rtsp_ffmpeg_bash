""" All-In-One RTSP Surveillance Recorder """
import json
import sys
import ffmpeg
import configparser

#from surveillance import Surveillance
#import ipdb
#ipdb.set_trace()

# CONSTANTS
output_dir: str = '/dev/shm'
configuration_file = './surveillance_configuration.py'

camera_list: tuple = []
camera_streams_list = []


def enumerate_cameras():
    """ Add camera links to list """

    print("Enumerating cameras...")
    camera_list.append(
        ('test_camera', 'rtsp://192.168.1.15:554/live/ch00_0', False))
    print("Enumerated: ", camera_list)


def probe_cameras():
    """ Check which cameras in list are up """

    for camera_index, camera in enumerate(camera_list):
        print('Checking if', camera[0], 'at', camera[1], 'is up')
        try:
            ffmpeg.probe(camera[1])
        except ffmpeg.Error:
            print('Could not probe', camera[0], 'at', camera[1])
            continue

        print(camera[0], 'at', camera[1], 'is up')
        camera_list[camera_index] = (camera[0], camera[1], True)
        print(camera_list)


def prepare_streams():
    """ Generate ffmpeg calls, but don't run yet """

    for camera_index, camera in enumerate(camera_list):
        stream = ffmpeg
        stream = ffmpeg.input(camera[1])
        stream = ffmpeg.output(stream,
                               output_dir + '/' + camera[0] +
                               '_%Y-%m-%d_%H-%M-%S.mp4',
                               f='segment',
                               segment_time='10',
                               segment_atclocktime='1',
                               strftime='1',
                               reset_timestamps='1',
                               vcodec='copy',
                               acodec='n')
        stream = ffmpeg.overwrite_output(stream)
        camera_streams_list.append(stream)
        print(stream.compile())


def record_cameras():
    """ Record camera streams """

    for camera_index, camera in enumerate(camera_list):
        if not camera[2]:
            continue

        print('Recording from', camera[0], 'at', camera[1])
        try:
            ffmpeg.run(camera_streams_list[camera_index])
        except ffmpeg.Error:
            print('had error')


def main():
    """ Program entry """

    print('hello')

    enumerate_cameras()
    probe_cameras()
    prepare_streams()
    #record_cameras()
    sys.exit()

    probe = ffmpeg.probe('rtsp://192.168.1.15:554/live/ch00_0')
    probe = json.dumps(probe, sort_keys=True, indent=4)
    print(probe)


if __name__ == "__main__":
    main()
