#!/usr/bin/env python
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

from pygame import mixer

import time

import automationhat


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="v7GX18dRgLVtjClDmFdKjUyCZ"
consumer_secret="OcSrqC2pDGfeuEqSx47vTmtzKuhcxGNudw1caZeVof8G6WAhyK"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="19003041-amWGCdU217o0YRptsMcfGohphU2Cet0VxxeButUAo"
access_token_secret="b8wEYmm6ppHXsAY9NKCpHmIB0DvVKNcZRYW6JQKcKEKHK"



mixer.init()

buzz = mixer.Sound('/home/pi/bettergood/buzz.wav')

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)



def buzz_lights():
    # print("Light Buzz begins")
    # play sound
    buzz.play()
    # wait for audio to get to where it's making sound
    time.sleep(0.4)

    # 12 toggles @ 0.0239
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    automationhat.relay.one.toggle()
    time.sleep(0.0239)
    
    # 5 big toggles @ 0.23
    automationhat.relay.one.toggle()
    time.sleep(0.23)
    automationhat.relay.one.toggle()
    time.sleep(0.23)
    
    # 5 quickies at 0.046
    automationhat.relay.one.toggle()
    time.sleep(0.046)
    automationhat.relay.one.toggle()
    time.sleep(0.046)
    automationhat.relay.one.toggle()
    time.sleep(0.046)
    automationhat.relay.one.toggle()
    time.sleep(0.046)
    automationhat.relay.one.toggle()
    time.sleep(0.046)
    # finish last of the mid sequence
    automationhat.relay.one.toggle()
    time.sleep(0.23)

buzz_lights()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        buzz_lights()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['bettergood'])