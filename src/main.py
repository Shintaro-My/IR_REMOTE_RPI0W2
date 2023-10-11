from irrp import IRRP
import signal
import sys

def _sys_exit(signal, frame):
    print('abort')
    sys.exit()

if __name__ == '__main__':
    debug = 2
    if debug == 0:
        ir = IRRP(file="ir.ircode", post=130, no_confirm=True)
        ir.Record(GPIO=18, ID="light:on")
        ir.stop()
    elif debug == 1:
        ir = IRRP(file="test", no_confirm=True)
        ir.Playback(GPIO=17, ID="1")
        ir.stop()
    elif debug == 2:
        import pigpio, time
        pi = pigpio.pi()
        pi.set_mode(15, pigpio.OUTPUT)
        pi.write(15, pigpio.HIGH)
        time.sleep(2)
        pi.stop()
    