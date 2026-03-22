from flask import Flask, request, jsonify
from flask_cors import CORS
import pymssql
import os

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
    # إذا كان bytes، حوله إلى string
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

        cursor.execute("SELECT id, image, prix FROM chega_table")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()


        rows = clean_data(rows)  # ✅ الحل هنا
        return jsonify(rows)

    except Exception as e:
        if isinstance(e, bytes):
            return jsonify({"error": e.decode("utf-8", errors="replace")})
        return jsonify({"error": str(e)})
    
@app.route("/get_gaz_table", methods=["GET"])
def get_gaz_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("SELECT id, image, prix FROM gaz_table")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()


        rows = clean_data(rows)  # ✅ الحل هنا
        return jsonify(rows)

    except Exception as e:
        if isinstance(e, bytes):
            return jsonify({"error": e.decode("utf-8", errors="replace")})
        return jsonify({"error": str(e)})

@app.route("/add_chega_table", methods=["POST"])
def add_chega_table():
    try:
        data = request.json
        username = data.get("username")
        email = data.get("email")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Users (username, email) VALUES (%s, %s)",
            (username, email)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify_error(e)
@app.route("/test_db")
def test_db():
    try:
        conn = get_connection()
        return "Connected ✅"
    except Exception as e:
        return str(e)
