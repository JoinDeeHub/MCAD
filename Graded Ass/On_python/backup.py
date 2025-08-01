import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    # List all files in the source directory
    for file_name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, file_name)

        # Only handle files (ignore subdirectories)
        if os.path.isfile(source_path):
            dest_path = os.path.join(dest_dir, file_name)

            # If file already exists in destination, add timestamp
            if os.path.exists(dest_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(file_name)
                new_file_name = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_file_name)

            try:
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {file_name} -> {os.path.basename(dest_path)}")
            except Exception as e:
                print(f"Failed to copy {file_name}: {e}")

if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        src_dir = sys.argv[1]
        dst_dir = sys.argv[2]
        backup_files(src_dir, dst_dir)