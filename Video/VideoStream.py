#!/usr/bin/python
# This file is used to set up video streaming between the Drone and the BaseStation.

import os
import subprocess

class streamer:
    def __init__(self):
        self.StreamProcess = subprocess

    def start(self, w='640', h='360', fps='60'):
        try:
            self.StreamProcess = subprocess.Popen(['sudo', 'raspivid', '-o', '-', '-t', '0', '-w', w, '-h', h, '-vf', '-hf', '-fps', fps, '-n', '|', 'cvlc', '-vvv', 'stream:///dev/stdin', '--sout', "'#rtp{sdp=rtsp://:8554/}'", ':demux=h264'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("Failed to start streamer. Error: ", e)
            exit()

    def stop(self):
        self.StreamProcess

class watcher:
    def __init__(self):