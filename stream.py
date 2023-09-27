import os
import gi
import argparse

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib

Gst.init(None)

class TestRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, src_file):
        GstRtspServer.RTSPMediaFactory.__init__(self)
        self.src_file = src_file

    def do_create_element(self, url):
        src_demux = "filesrc location={} ! qtdemux name=demux".format(self.src_file)
        h264_transcode = "demux.video_0"
        pipeline = "{0} {1} ! queue ! rtph264pay name=pay0 config-interval=1 pt=96".format(src_demux, h264_transcode)
        print("Element created: " + pipeline)
        return Gst.parse_launch(pipeline)

class GstreamerRtspServer():
    def __init__(self, port, dst_stream, mp4):
        self.rtspServer = GstRtspServer.RTSPServer()
        factory = TestRtspMediaFactory(mp4)
        factory.set_shared(True)
        mountPoints = self.rtspServer.get_mount_points()
        mountPoints.add_factory('/{}'.format(dst_stream), factory)
        self.rtspServer.set_service(str(port))
        self.rtspServer.attach(None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RTSP Server")
    parser.add_argument("--port", type=int, default=8558, help="Port for the RTSP server")
    parser.add_argument("--dst-stream", type=str, default="stream1", help="Destination stream name")
    parser.add_argument("--mp4", type=str, default="inventec_glove_08.mp4", help="Path to the MP4 video file")
    args = parser.parse_args()

    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    BASE = script_dir
    src_file = os.path.join(BASE, "videos", args.mp4)

    print("Video =", src_file)
    print("URL: rtsp://[IP]:{0}/{1}".format(args.port, args.dst_stream))

    s = GstreamerRtspServer(args.port, args.dst_stream, src_file)
    loop = GLib.MainLoop()
    loop.run()
