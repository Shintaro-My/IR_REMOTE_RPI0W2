
import sqlite3

DB_NAME = 'database.db'

class DB:
    def __init__(self, name=DB_NAME) -> None:
        self.db_name = name
        self.setup()
        
    def setup(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        
    def terminate(self):
        self.cur.close()
        self.conn.close()
        
    def run(self, queries):
        results = []
        try:
            self._setup()
            results = [[v for v in self.cur.execute(query.strip())] for query in queries]
            self.conn.commit()
        except Exception as e:
            print(e)
        return results
    
        
if __name__ == '__main__':
    db = DB()
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
    