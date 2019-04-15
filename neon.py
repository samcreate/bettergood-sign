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
    
    print("Light Buzz ends")


buzz_lights()