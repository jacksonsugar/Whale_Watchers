#!/bin/sh

arecord -D plughw:1,0 -f dat | sshpass -p '*****' ssh -C whale-srv@***** aplay -f dat &
