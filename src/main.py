from irrp import IRRP
import signal
import sys

def _sys_exit(signal, frame):
    print('abort')
    sys.exit()

sample = [3605, 1675, 499, 371, 499, 1235, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 1235, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 1235, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 371, 499, 1235, 499, 371, 499, 1235, 499, 1235, 499, 1235, 499, 1235, 499, 371, 499, 371, 499, 1235, 499, 371, 499, 1235, 499, 1235, 499, 1235, 499, 1235, 499, 371, 499, 1235, 600]

if __name__ == '__main__':
    import sys
    debug = 0
    
    ir = IRRP(no_confirm=True)
    if debug == 0:
        result = ir.Record(GPIO=18, post=130)
        ir.stop()
        print(result)
    elif debug == 1:
        ir.Playback(GPIO=17, data=sample)
        ir.stop()
    elif debug == 2:
        import pigpio, time
        pi = pigpio.pi()
        pi.set_mode(17, pigpio.OUTPUT)
        pi.write(17, pigpio.HIGH)
        time.sleep(2)
        pi.write(17, pigpio.LOW)
        pi.stop()
    