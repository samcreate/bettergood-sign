#!/usr/bin/env python

import time

import automationhat


if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

while True:
    automationhat.relay.one.toggle()

    time.sleep(0.9)
