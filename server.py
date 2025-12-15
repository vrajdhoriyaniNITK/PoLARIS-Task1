from flask import Flask , request
import os
from datetime import datetime as dt
import sqlite3

webapp = Flask(__name__)
uploads = "evidence001"


if not os.path.exists(uploads):
    os.mkdir(uploads)


db_name = "audit_logs.db"


def startdb():
    connect1 = sqlite3.connect(db_name)
    cursor1 = connect1.cursor()


    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS events( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    timestamp TEXT,
    evidence_path TEXT,
    ip_address TEXT) """
    )

    connect1.commit()
    connect1.close()

startdb()

@webapp.route("/")
def home():
    return "Server running"

@webapp.route("/uploads", methods=["POST"])

def upload():
    device_id = request.form.get("device_id", "UNKNOWN")
    #get file
    img = request.files.get("img")

    if not img:
        return {"error": "No image sent"},400
    
    # creating a timestamped file
    timestamp = dt.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{timestamp}.jpg"


    save_path = os.path.join(uploads,file_name)
    img.save(save_path)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events(device_id,timestamp,evidence_path,ip_address) VALUES(?,?,?,?) """,
    (device_id,timestamp,save_path,request.remote_addr)



    )

    conn.commit()
    conn.close()

    return {"status": "received","filename": file_name}
    



if __name__ == "__main__":
    webapp.run(host="0.0.0.0",port=2000)


