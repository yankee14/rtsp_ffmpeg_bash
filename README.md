# rtsp_ffmpeg_bash
Manage multiple simultaneous RTSP video streams (e.g. surveilance footage) using FFmpeg and BASH.

The approach to managing the footage is to first acquire the footage raw, then gradually apply encoding and processing as CPU processing power permits.

# USAGE

1. Edit `user_settings.sh` to insert your RTSP URLs, storage directories, etc.
2. Run rtsp_ffmpeg_bash.sh
3. *optionally* create system service

# UNDER THE HOOD

#### 1. TRIAGE
 - Acquire footage raw directly from stream
 - Save to volatile memory
 - No processing yet
 - Split file every N<sub>1</sub> seconds or N<sub>2</sub> mebibytes
 - Time sensitive action, such as scan for motion, neural network object classification, text message of still frame, etc.
 
#### 2. BASIC COMPRESSION, CONCATENATION
 - Concatenate video streams for long term storage
 - Duration? Filesize?
 - Compression level?
 - Save to non-volatile memory
 
#### 3. PANELIZE VIEW
 - Live stream to monitor
 - e.g.:
![]( https://upload.wikimedia.org/wikipedia/commons/e/e6/Nigloland_-_Manoir_Hant%C3%A9_-_Cam%C3%A9ras.jpg "Panelized Video")
