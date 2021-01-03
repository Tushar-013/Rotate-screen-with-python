import rotatescreen as rs
import time


screen =rs.get_primary_display()
for i in range(13):
    time.sleep(2)
    screen.rotate_to(i*90%360)
