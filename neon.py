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
    buzz.play()
    time.sleep(0.2)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.3)
    automationhat.relay.one.toggle()
    time.sleep(0.2)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()

    # first buzz

    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.3)
    automationhat.relay.one.toggle()
    time.sleep(0.2)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()

    time.sleep(0.2)
    automationhat.relay.one.toggle()
    time.sleep(0.1)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    automationhat.relay.one.toggle()
    time.sleep(0.01)
    print("Light Buzz ends")


buzz_lights()