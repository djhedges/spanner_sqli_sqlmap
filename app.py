from flask import Flask, request, jsonify
from google.cloud import spanner
import os

app = Flask(__name__)

os.environ["SPANNER_EMULATOR_HOST"] = "localhost:9010"
client = spanner.Client(project="test-project")
instance = client.instance("test-instance")
database = instance.database("test-db")

@app.route('/')
def get_car():
    model_name = request.args.get('model')
    query = f"SELECT name, year FROM Cars WHERE name = '{model_name}'"
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(query)
        cars = [{"name": row[0], "year": row[1]} for row in results]
        return jsonify(cars)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
