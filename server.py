from flask import Flask , request
import os
from datetime import datetime as dt

webapp = Flask(__name__)
uploads = "evidence001"


if not os.path.exists(uploads):
    os.mkdir(uploads)


@webapp.route("/")
def home():
    return "Server running"

@webapp.route("/uploads", methods=["POST"])
def upload():
    #get file
    img = request.files.get("img")

    if not img:
        return {"error": "No image sent"},400
    
    # creating a timestamped file
    timestamp = dt.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{timestamp}.jpg"


    img.save(os.path.join(uploads,file_name))

    return {"status": "recieved","filename": file_name}


if __name__ == "__main__":
    webapp.run(host="0.0.0.0",port=2000)


