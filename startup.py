#!/usr/bin/python
from pushbullet import Pushbullet
import time, sys
pb = Pushbullet(sys.argv[1])
push = pb.push_note('Kali StartUP Complate', time.ctime())
