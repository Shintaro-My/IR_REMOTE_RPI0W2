from irrp import IRRP
import signal
import sys

def _sys_exit(signal, frame):
    print('abort')
    sys.exit()



if __name__ == '__main__':
    n = len(sys.argv)
    if n % 2 == 0 or n == 1:
        raise Exception('引数の数が不正です。[ssid1, pass1, ssid2, pass2, ...]のように入力してください。')
    networks = [create_pass(*sp, priority=i) for i, sp in enumerate(splitter(sys.argv[1:]))]
    context = WPA_HEADER + '\n\n' + '\n'.join(networks) + '\n'
    
    with open('_temp.txt', 'w') as f:
        f.write(context)
    
    print(context)

if __name__ == '__main__':
    import sys
    debug = 1
    n = len(sys.argv)
    if n:
        debug = int(sys.argv[0])
    else:
        debug = 0
    
    if debug == 0:
        ir = IRRP(file="ir.ircode", post=130, no_confirm=True)
        ir.Record(GPIO=18, ID="light:on")
        ir.stop()
    elif debug == 1:
        ir = IRRP(file="test", no_confirm=True)
        ir.Playback(GPIO=17, ID=sys.argv[1] if n > 1 else "light:on")
        ir.stop()
    elif debug == 2:
        import pigpio, time
        pi = pigpio.pi()
        pi.set_mode(17, pigpio.OUTPUT)
        pi.write(17, pigpio.HIGH)
        time.sleep(2)
        pi.write(17, pigpio.LOW)
        pi.stop()
    