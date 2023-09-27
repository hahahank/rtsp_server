# rtsp_server

## Prerequisites
Before running the scripts, you need to install some required packages and Python libraries.
```bash
# Update package list
apt update
# Install required libraries
apt -y install libgirepository1.0-dev gir1.2-gst-rtsp-server-1.0
# Install Python packages
pip install pycairo PyGObject
```

## Usage
Webcam Streaming
To stream from a webcam, use the following command:

```bash

sudo python3 stream_by_webcam.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
```
## Video Streaming
To stream from a video file, use the following command:

```bash 
sudo python3 stream.py --port 8558 --dst-stream stream1 --mp4 [xxx]
```
