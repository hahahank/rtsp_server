# rtsp_server

## Video
sudo python3 stream_by_webcam.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
## Webcam 
sudo python3 stream.py --port 8558 --dst-stream stream1 --mp4 worker-zone-detection.mp4
