
import sqlite3

DB_NAME = 'database.db'

class DB:
    def __init__(self, name=DB_NAME) -> None:
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()
        
    def run(self, queries):
        results = [[v for v in self.cur.execute(query.strip())] for query in queries]
        self.conn.commit()
        return results
    
    def terminate(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    db = DB()
    try:
        db.run([
        """
        CREATE TABLE IF NOT EXISTS Test(
            Key   TEXT PRIMARY KEY,
            Value INTEGER
        )
        """,
        """
        INSERT INTO Test (Key, Value)
        VALUES (\"test\", 100)
        ON CONFLICT(Key)
        DO UPDATE SET Value=100
        """
        ])
        results, = db.run(["SELECT * FROM Test"])
        print(results)
    
    except Exception as e:
        print(e)
        
    finally:
        db.terminate()