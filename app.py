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
def get_chega_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM chega_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = "data:image/png;base64," + base64.b64encode(row["image"]).decode("utf-8")
               # row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})
 

@app.route("/get_gaz_table", methods=["GET"])
def get_gaz_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM gaz_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})



@app.route("/get_mouf_table", methods=["GET"])
def get_mouf_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM mouf_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/get_shose_table", methods=["GET"])
def get_shose_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM shose_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})



@app.route("/get_dress_table", methods=["GET"])
def get_dress_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM dress_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/get_womth_table", methods=["GET"])
def get_womth_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM womth_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/get_child_table", methods=["GET"])
def get_child_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM child_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route("/get_divers_table", methods=["GET"])
def get_divers_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM divers_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/get_back_table", methods=["GET"])
def get_back_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM back_table")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/get_imagebtn", methods=["GET"])
def get_imagebtn():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT * FROM imagebtn")
        rows = cursor.fetchall()

        for row in rows:
            if row.get("image") and isinstance(row["image"], bytes):
                row["image"] = base64.b64encode(row["image"]).decode("utf-8")

        cursor.close()
        conn.close()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)})
 
@app.route("/test_db")
def test_db():
    try:
        conn = get_connection()
        return "Connected ✅"
    except Exception as e:
        return str(e)
