import os
import shutil

def save_output(df, output_path="data/processed/ifrs17_reporting.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    
    df.to_csv(output_path, index=False)
    print(f" File shipped successfully! Target output saved at: {output_path}")

def archive_raw_files(file_list, archive_dir="data/archive/"):
    """Moves the processed day's files out of our inbox and into the cabinet."""
    # Ensure the archive directory exists
    os.makedirs(archive_dir, exist_ok=True)
    
    for file_path in file_list:
        if os.path.exists(file_path):
            # Extract just the filename (e.g., 'transactions.csv') from the path
            file_name = os.path.basename(file_path)
            
            # Physically move the file from data/raw to data/archive
            shutil.move(file_path, os.path.join(archive_dir, file_name))
            print(f"Filed away safely: Moved {file_name} to the archive folder.")