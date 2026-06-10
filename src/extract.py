import os 
import json
import pandas as pd 

def read_json_schema(schema_path = "config\schema_validation.json"):

    with open(schema_path, "r") as f:
        return json.load(f)
    
def validate_extract(file_path, file_type,schema):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"missing expected file: {file_path}")
    
    df = pd.read_csv(file_path)
    expected_cols = schema[file_type]["columns"]

    actual_cols = list(df.columns)

    if actual_cols != expected_cols:
        raise ValueError (f"Expected columns: {expected_cols}\n"
            f"But got columns:  {actual_cols}")
    
    print(f"success! {file_type}")
    return df 