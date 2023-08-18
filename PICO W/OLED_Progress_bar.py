from machine import Pin, I2C
import sh1106
import utime

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

## note that we can only draw from 0 to 62
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
display.sleep(False)

display.fill(0) # clear to black
display.text('Amoolya Garg', 0, 0, 1) # at x=0, y=0, white on black
# line under title
display.hline(0, 9, 127, 1)
# bottom of display
display.hline(0, 30, 127, 1)
# left edge
display.vline(0, 10, 32, 1)
# right edge
display.vline(127, 10, 32, 1)

for i in range(0, 118):
    # box x0, y0, width, height, on
    display.fill_rect(i,10, 10, 10, 1)
    # draw black behind number
    display.fill_rect(10, 21, 30, 8, 0)
    num = round(i*100/117,1)
    display.text(str(num), 10, 21, 1)
    display.show() # update display
    utime.sleep(1)

print('done')
