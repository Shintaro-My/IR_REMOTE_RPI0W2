from irrp import IRRP
from sqlite import DB
import ir_string as irstr

import signal
import sys

def _sys_exit(signal, frame):
    print('abort')
    sys.exit()


sample = [3604, 1613, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 1178, 569, 74322, 3604, 1613, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 1178, 569, 74322, 3604, 1613, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 305, 569, 1178, 569, 305, 569, 1178, 569, 1178, 569, 1178, 569, 1178, 569, 305, 569, 1178, 569]


def init_irdb(db: DB):
    db.run([
    """
    CREATE TABLE IF NOT EXISTS IRTable(
        Key   TEXT PRIMARY KEY,
        Value TEXT
    )
    """
    ])

def get_all_ir(db: DB):
    results, = db.run(["SELECT * FROM IRTable"])
    print(results)
    
def set_ir(db: DB, name: str, value: str):
    db.run([
    f"""
    INSERT INTO Test (Key, Value)
    VALUES (\"{name}\", \"{value}\")
    ON CONFLICT(Key)
    DO UPDATE SET Value=\"{value}\"
    """
    ])

if __name__ == '__main__':
    import sys
    print(sys.argv)
    
    debug = 1
    
    db = DB()
    irrp = IRRP(no_confirm=True)
    
    if debug == 0:
        result = irrp.Record(GPIO=18, post=130)
        irrp.stop()
        print(result)
        set_ir( db, 'test', irstr.encode(result) )
        get_all_ir(db)
    elif debug == 1:
        irrp.Playback(GPIO=17, data=sample)
        irrp.stop()
    elif debug == 2:
        import pigpio, time
        pi = pigpio.pi()
        pi.set_mode(17, pigpio.OUTPUT)
        pi.write(17, pigpio.HIGH)
        time.sleep(2)
        pi.write(17, pigpio.LOW)
        pi.stop()
    
    db.terminate()