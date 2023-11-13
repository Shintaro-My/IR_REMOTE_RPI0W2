import subprocess
import re
import time

TARGET_IP = None

def getDefaultGateway():
    res = subprocess.run(['route'], stdout=subprocess.PIPE)
    txt = res.stdout.decode()
    sch = re.search(r'default\s*(\S+)', txt)
    if not sch: return None
    ip = sch.groups()[0]
    return ip

def setIP():
    global TARGET_IP
    TARGET_IP = None
    while not TARGET_IP:
        try:
            TARGET_IP = getDefaultGateway()
            print(f'SET IP: {TARGET_IP}')
        except Exception as e:
            print(e)
        time.sleep(30)

def main():
    setIP()
    while True:
        res = subprocess.run(['ping', '-c', '1', TARGET_IP], stdout=subprocess.DEVNULL)
        print(f'PING: {TARGET_IP}')
        code = res.returncode # 0: success, 1: failed
        if code:
            subprocess.run(['sudo', 'ifconfig', 'wlan0', 'up'])
            time.sleep(10)
            setIP()
        time.sleep(60)

if __name__ == '__main__':
    main()