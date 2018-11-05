#!/usr/bin/env python
#encoding: utf8
import rospy
from speak_tools.srv import *
import sys


def speak_client(text):
    rospy.wait_for_service("speak_text")
    try:
        speak_text = rospy.ServiceProxy("speak_text", SpeakedText)
        resp = speak_text(text)
        return resp.message
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def usage():
    return "%s <text>" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        #text = sys.argv[1]
        # print"Requesting %s" % text
        print "%s" % (speak_client("こんばんわに"))
    else:
        print usage()

"""
speak_server.pyのテスト用
"""
