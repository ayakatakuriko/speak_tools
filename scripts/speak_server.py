#!/usr/bin/env python
#encoding: utf8
import subprocess
import rospy
from speak_tools.srv import *
<<<<<<< HEAD
import jtalk
=======
from jtalk import jtalk
>>>>>>> 718399a62aba15f615b86d898be4fc33d5b5c184


def speaker(req):
    jtalk(req.text)
<<<<<<< HEAD
=======
    resp = SpeakedTextResponse()
>>>>>>> 718399a62aba15f615b86d898be4fc33d5b5c184
    resp.success = True
    resp.message = "Success to speak " + req.text
    return resp


def speaker_server():
    rospy.init_node('speaker_server')
    srv = rospy.Service("speak_text", SpeakedText, speaker)
    print "Ready to speak text."
    rospy.spin()


if __name__ == '__main__':
    speaker_server()

"""
クライアントからSpeakedTextというサービスをうけとって発話させるROSノード
"""
