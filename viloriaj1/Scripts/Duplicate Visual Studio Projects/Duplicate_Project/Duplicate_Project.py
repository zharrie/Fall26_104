import os
import shutil

def clone_complete_solution(source_dir, dest_dir, old_name, new_name):
    print("🚀 Starting complete solution duplication...")
    
    if os.path.exists(dest_dir):
        print(f"❌ Error: Destination '{dest_dir}' already exists. Please delete it first.")
        return

    # 1. Copy everything safely to the new clean directory
    print(f"📁 Copying all files to:\n  {dest_dir}...")
    shutil.copytree(source_dir, dest_dir)
    print("✅ Files copied successfully.")

    # 2. Rename files (.vbproj, .user, .sln, .pfx, .resx) inside the new folder
    print("\n✏️ Renaming all project components...")
    for root, dirs, files in os.walk(dest_dir):
        for filename in files:
            if any(filename.lower().endswith(ext) for ext in ['.vbproj', '.vbproj.user', '.sln', '.pfx', '.resx']):
                old_file_path = os.path.join(root, filename)
                new_filename = filename.replace(old_name, new_name)
                
                if new_filename == filename:
                    new_filename = filename.replace("RMA Soft", new_name).replace("RMA soft", new_name)
                    
                if new_filename == filename:
                    base, ext = os.path.splitext(filename)
                    if filename.lower().endswith('.user'): 
                        new_filename = f"{new_name}.vbproj.user"
                    elif filename.lower().endswith('.vbproj') or filename.lower().endswith('.sln') or filename.lower().endswith('.pfx'):
                        new_filename = f"{new_name}{ext}"
                    
                new_file_path = os.path.join(root, new_filename)
                if old_file_path != new_file_path:
                    os.rename(old_file_path, new_file_path)
                    print(f"  Renamed file: {filename} -> {new_filename}")

    # 3. Update the text contents of configuration AND resource (.resx) files
    print("\n🔗 Updating internal paths inside project files and .resx resources...")
    for root, dirs, files in os.walk(dest_dir):
        for filename in files:
            # Added .resx to the file content update process
            if any(filename.lower().endswith(ext) for ext in ['.sln', '.vbproj', '.resx']):
                file_path = os.path.join(root, filename)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Replace old path names with the new folder name
                updated_content = content.replace("RMA Soft", new_name)
                updated_content = updated_content.replace("RMA soft", new_name)
                updated_content = updated_content.replace(old_name, new_name)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"  Fixed paths inside: {filename}")

    print(f"\n🎉 Success! The entire solution and all .resx resource paths are fully updated to: {new_name}")

# --- FIXED CONFIGURATION ---
SOURCE_FOLDER = r"C:\Users\Jviloria\VBA Projects\RMA Soft\RMA Soft"
DEST_FOLDER   = r"C:\Users\Jviloria\VBA Projects\RMA Soft\Project Duplicates\RMA_app 20261022"

OLD_PROJECT_NAME = "RMA soft"
NEW_PROJECT_NAME = "RMA_app"

clone_complete_solution(SOURCE_FOLDER, DEST_FOLDER, OLD_PROJECT_NAME, NEW_PROJECT_NAME)

