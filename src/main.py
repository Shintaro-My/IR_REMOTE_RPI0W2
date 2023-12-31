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
        Value TEXT,
        Desc  Text
    )
    """
    ])

def get_all_ir(db: DB):
    results, = db.run(["SELECT * FROM IRTable"])
    print(results)
    
def set_ir(db: DB, name: str, value: str, desc: str):
    db.run([
    f"""
    INSERT INTO IRTable (Key, Value, Desc)
    VALUES (\"{name}\", \"{value}\", \"{desc}\")
    ON CONFLICT(Key)
    DO UPDATE SET Value=\"{value}\", Desc=\"{desc}\"
    """
    ])

if __name__ == '__main__':
    import sys
    print(sys.argv)
    
    debug = 0
    
    db = DB()
    irrp = IRRP(no_confirm=True)
    try:
        init_irdb(db)
        
        if debug == 0:
            result = irrp.Record(GPIO=18, post=130)
            irrp.stop()
            print(result)
            set_ir( db, 'test', irstr.encode(result), 'abc' )
            get_all_ir(db)
        elif debug == 1:
            irrp.Playback(GPIO=17, data=sample)
            irrp.stop()
    except KeyboardInterrupt:
        print('abort.')
    except Exception as e:
        print(e)
    finally:
        db.terminate()