#!/bin/bash

ffmpeg -ar 8000 -f alsa -i plughw:1,0 -acodec mp2 -b:a 128k -f rtp rtp://********:**** &
