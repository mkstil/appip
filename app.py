from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc
import os

app = Flask(__name__)
CORS(app)  # للسماح للـ APK أو المتصفح بالوصول

# الاتصال بقاعدة البيانات من environment variable
conn_str = os.environ.get("DB_CONN")

def get_connection():
    return pyodbc.connect(conn_str)

@app.route("/get_users", methods=["GET"])
def get_users():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email FROM Users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        result = [{"id": r.id, "username": r.username, "email": r.email} for r in rows]
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.json
        username = data.get("username")
        email = data.get("email")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email) VALUES (?, ?)",
            (username, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)})

# لا تضع app.run() هنا عند استخدام Render
