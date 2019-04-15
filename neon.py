#!/usr/bin/env python

from pygame import mixer

import time

import automationhat

mixer.init()

buzz = mixer.Sound('buzz.wav')

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

# while True:
#     automationhat.relay.one.toggle()
    
#     time.sleep(0.9)


def buzz_lights():
    print("Light Buzz begins")
    # play sound
    buzz.play()
    # wait for audio to get to where it's making sound
    time.sleep(0.098)

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
    automationhat.relay.one.toggle()
    time.sleep(0.23)

    # end of all 12 @ 0.036
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)
    automationhat.relay.one.toggle()
    time.sleep(0.036)

    print("Light Buzz ends")


buzz_lights()