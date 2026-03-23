from flask import Flask, request, jsonify
from flask_cors import CORS
import pymssql
import os
import base64
app = Flask(__name__)
CORS(app)

# Get DB connection info from environment
DB_SERVER = os.environ.get("DB_SERVER")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

def get_connection():
    return pymssql.connect(
        server=DB_SERVER,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=1433,
        timeout=5,
        login_timeout=5
    )

def clean_data(data):
    if isinstance(data, list):
        return [clean_data(row) for row in data]
    elif isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, bytes):
        return data.decode("utf-8", errors="replace")
    else:
        return data


def jsonify_error(e):
    
    if isinstance(e, bytes):
        msg = e.decode('utf-8', errors='replace')
    else:
        msg = str(e)
    return jsonify({"error": msg})

@app.route("/get_chega_table", methods=["GET"])




@app.route("/all_data", methods=["GET"])
def get_all_data():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        # Chega
        cursor.execute("SELECT * FROM chega_table")
        chega = cursor.fetchall()
        for row in chega:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        # Gaz
        cursor.execute("SELECT * FROM gaz_table")
        gaz = cursor.fetchall()
        for row in gaz:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        # Mouf
        cursor.execute("SELECT * FROM mouf_table")
        mouf = cursor.fetchall()
        for row in mouf:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")


        cursor.execute("SELECT id, image, prix FROM shose_table")
        shose = cursor.fetchall()

        for row in shose:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.execute("SELECT id, image, prix FROM back_table")
        back = cursor.fetchall()




        for row in back:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")


        cursor.execute("SELECT id, image, prix FROM womth_table")
        womth = cursor.fetchall()

        for row in womth:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")



        cursor.execute("SELECT id, image, prix FROM dress_table")
        dress = cursor.fetchall()



        for row in dress:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.execute("SELECT id, image, prix FROM divers_table")
        divers = cursor.fetchall()





        for row in divers:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        
        cursor.execute("SELECT id, image, prix FROM child_table")
        child = cursor.fetchall()

        for row in child:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")



        cursor.execute("SELECT id, image, prix FROM imagebtn")
        imagebtn = cursor.fetchall()




        for row in imagebtn:
            if isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        conn.close()

        return jsonify({
            "chega": chega,
            "gaz": gaz,
            "mouf": mouf,
            "shose": shose,
            "back": back,
            "womth": womth,
            "dress": dress,
            "child": child,
            "divers": divers,
            "imagebtn": imagebtn
            
        })

    except Exception as e:
        return jsonify({"error": str(e)})
 
 
 
 


 
@app.route("/test_db")
def test_db():
    try:
        conn = get_connection()
        return "Connected ✅"
    except Exception as e:
        return str(e)
