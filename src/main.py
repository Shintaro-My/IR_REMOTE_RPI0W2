from irrp import IRRP
import signal
import sys

def _sys_exit(signal, frame):
    print('abort')
    sys.exit()

if __name__ == '__main__':
    """
    ir = IRRP(file="ir.ircode", post=130, no_confirm=True)
    ir.Record(GPIO=18, ID="light:on")
    ir.stop()
    """
    ir = IRRP(file="test", no_confirm=True)
    ir.Playback(GPIO=17, ID="1")
    ir.stop()
    