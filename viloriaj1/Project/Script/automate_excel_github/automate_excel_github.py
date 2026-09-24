import os
import subprocess
import time
import pandas as pd

try:
    # 1. Configure file paths
    file_path = r"C:\Users\Jviloria\OneDrive - Konica Minolta\ドキュメント\MCU Python Course\Final_Project_Plan.xlsm"
    sheet_name = "Main"
    md_file_path = r"C:\Users\Jviloria\OneDrive - Konica Minolta\ドキュメント\MCU Python Course\Fall26_104\viloriaj1\Project\Final_Project_Plan.md"
    
    # Identify the Git repository folder dynamically based on where the .md file is saved
    repo_dir = os.path.dirname(md_file_path)

    # 2. Read and convert Excel data
    print("Reading Excel file...")
    project_data = pd.read_excel(file_path, sheet_name=sheet_name)

    print("Converting to Markdown table...")
    convert_to_table = project_data.to_markdown(index=False)

    # 3. Save the Markdown table into a text file
    print(f"Saving Markdown file to: {md_file_path}")
    with open(md_file_path, "w", encoding="utf-8") as f:
        f.write("# Final Project Plan\n\n")  # Adds a header to your file
        f.write(convert_to_table)
        
    print("Successfully created Markdown file locally.")

    # 4. Git Upload Sequence (Runs only if the file save succeeded)
    print(f"Staging changes in Git repository: {repo_dir}")
    # Run 'git add' targeting the specific folder
    subprocess.run(["git", "add", md_file_path], cwd=repo_dir, check=True)
    
    # Create a timestamped commit message
    commit_msg = f"Auto-update project plan: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    print(f"Committing changes: {commit_msg}")
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, check=True)
    
    print("Pushing updates to GitHub...")
    subprocess.run(["git", "push"], cwd=repo_dir, check=True)
    
    print("--- Process Complete! Markdown updated and pushed to GitHub successfully. ---")

except Exception as e:
    print(f"Error encountered: {e}")

