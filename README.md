# rtsp_server
apt update
pip install pycairo
apt -y install libgirepository1.0-dev
pip install PyGObject
apt -y install gir1.2-gst-rtsp-server-1.0
pip install pycairo

## Webcam
sudo python3 stream_by_webcam.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
## Video 
sudo python3 stream.py --port 8558 --dst-stream stream1 --mp4 worker-zone-detection.mp4
