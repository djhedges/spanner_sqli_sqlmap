from google.cloud import spanner
import os

os.environ["SPANNER_EMULATOR_HOST"] = "localhost:9010"
client = spanner.Client(project="test-project")

def setup():
    instance = client.instance("test-instance")
    instance.create().result()
    
    database = instance.database("test-db", ddl_statements=[
        "CREATE TABLE Cars (id INT64 NOT NULL, name STRING(100), year INT64) PRIMARY KEY (id)",
        "CREATE TABLE EngineSpecs (id INT64 NOT NULL, model STRING(100), engine STRING(100), hp INT64, torque INT64) PRIMARY KEY (id)"
    ])
    database.create().result()

    with database.batch() as batch:
        batch.insert(table='Cars', columns=['id', 'name', 'year'], values=[
            (1, 'r32', 2004),
            (2, 'phaeton', 2004),
            (3, 'beetle_tdi', 2002),
            (4, 'rabbit', 1984),
        ])
        batch.insert(table='EngineSpecs', columns=['id', 'model', 'engine', 'hp', 'torque'], values=[
            (1, 'r32', '3.2L VR6', 240, 236),
            (2, 'phaeton', '4.2L V8', 335, 317),
            (3, 'beetle_tdi', '1.9L ALH TDI', 90, 155),
            (4, 'rabbit', '1.8L I4', 90, 105),
        ])
    print("Lab Data Loaded.")

if __name__ == "__main__":
    setup()
