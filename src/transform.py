import pandas as pd 

def transform_data(df_Policy, df_txns, df_actuarial):
    premium = df_txns[df_txns["txn_type"].str.lower() == "premium"]
    claims = df_txns[df_txns["txn_type"].str.lower() == "claim"]

    total_premium = premium.groupby("policy_id")["amount"].sum().reset_index()
    total_premium.columns = ["policy_id", "total_premiums"]

    total_claims = claims.groupby("policy_id")["amount"].sum().reset_index()
    total_claims.columns = ["policy_id", "total_claims"]


    policy_summary = pd.DataFrame({"policy_id":df_Policy["policy_id"].unique()})
    policy_summary = policy_summary.merge(total_premium, on="policy_id", how="left")
    policy_summary = policy_summary.merge(total_claims, on="policy_id", how="left")

    policy_summary = policy_summary.fillna(0)

    policy_summary["net_cashflow"] = policy_summary["total_premiums"] + policy_summary["total_claims"]
  
    final_reporting = policy_summary.merge(df_Policy, on="policy_id", how="inner")
    final_reporting = final_reporting.merge(df_actuarial, on="policy_id", how="inner")
    
    

    if final_reporting["policy_id"].isnull().any():
        raise ValueError(" Quality Check Failed: Found NULL policy_id values in final table!")
        
    if len(final_reporting) == 0:
        raise ValueError(" Quality Check Failed: The final output table is completely empty!")
    
    return final_reporting


 