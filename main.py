import os 
from src.extract import read_json_schema, validate_extract 
from src.transform import transform_data
from src.load import save_output, archive_raw_files


def run_pipeline():
    raw_dir = "data/raw"
    policy_file = os.path.join(raw_dir,"policy_data.csv")
    transactions_file = os.path.join(raw_dir,"transactions.csv")
    actuarial_file = os.path.join(raw_dir,"actuarial_output.csv")


    try:
        schema = read_json_schema()

        # Extract 
        df_policy = validate_extract(policy_file, "policy_data",schema)
        df_txns = validate_extract(transactions_file,"transactions",schema)
        df_actuarial= validate_extract(actuarial_file, "actuarial_output",schema)
        print(df_policy.head(2))
        print(df_actuarial.head(2))
        print(df_txns.head(2))

        # 2. Transform 
        print("Starting Transformation Phase...")
        df_final = transform_data(df_policy, df_txns, df_actuarial)
        print(" Transformations Successful ")
        print(df_final[['policy_id', 'total_premium', 'total_claims', 'net_cashflow', 'csm', 'expected_cashflow']].head(2))

        # 3. Load
        save_output(df_final)
        
        # Files kept in raw folder for future use
        # archive_raw_files([policy_file, transactions_file, actuarial_file])


    except Exception as e :
        print(f"error Details : {str(e)}")
        


if __name__ == "__main__":
    run_pipeline()




