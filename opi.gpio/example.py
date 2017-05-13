# -*- coding: utf-8 -*-
import time
from pizypwm import *
# Set GPIO pin #11 as PWM output with a frequency of 100 Hz
pwm = PiZyPwm(100,'PA11') #сдесь 100 - частота, PA11 - ножка на гребенке
# Start PWM output with a duty cycle of 20%. The pulse (HIGH state) will have a duration of
# (1 / 100) * (20 / 100) = 0.002 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 20) / 100) = 0.008 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity.
pwm.start(20) # запуск ШИМ с заполнение 20
time.sleep(10)
# Change duty cycle to 6%. The pulse (HIGH state) will now have a duration of
# (1 / 100) * (6 / 100) = 0.0006 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 6) / 100) = 0.0094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity.
pwm.changeDutyCycle(6) # изменение значения заполнения на 50
time.sleep(10)
# Change the frequency of the PWM pattern. The pulse (HIGH state) will now have a duration of
# (1 / 10) * (6 / 100) = 0.006 seconds, followed by a low state with a duration of
# (1 / 10) * ((100 - 6) / 100) = 0.094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity, but you may
# notice flickering.
pwm.changeFrequency(10)
time.sleep(10)
# Stop PWM output
print 'стоп'
pwm.stop()
