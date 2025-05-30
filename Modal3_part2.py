#!/usr/bin/env python3

timeNow = int(input('Please enter current time in 24-hour format\n'))
alarmWait = int(input('Please enter the number of hours to wait for alarm\n'))

def alarmNewTime(time,wait):
    return (time + wait)% 24

alarmTime = alarmNewTime(timeNow,alarmWait)
    
print('\nIf the current time is {} o`clock'.format(timeNow))
print('You want your alarm to be in {} hours'.format(alarmWait))
print('Your Alarm is now set for {} o`clock'.format(alarmTime))


