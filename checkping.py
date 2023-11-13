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
        TARGET_IP = getDefaultGateway()
        time.sleep(30)

def main():
    setIP()
    while True:
        res = subprocess.run(['ping', '-c', '1', TARGET_IP])
        code = res.returncode # 0: success, 1: failed
        if code:
            subprocess.run(['sudo', 'ifconfig', 'wlan0', 'up'])
            time.sleep(10)
            setIP()
        time.sleep(60)

if __name__ == '__main__':
    main()