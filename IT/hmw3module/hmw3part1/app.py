import os
import shutil
import concurrent.futures

def copy_file(file_path, destination_folder):
    try:
        shutil.copy(file_path, destination_folder)
        print(f"Copied {file_path} to {destination_folder}")
    except Exception as e:
        print(f"Error copying {file_path}: {e}")

def process_directory(source_directory, destination_directory):
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_extension = file.split('.')[-1]
            dest_folder = os.path.join(destination_directory, file_extension)
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            source_file_path = os.path.join(root, file)
            copy_file(source_file_path, dest_folder)

def main(source_dir, dest_dir):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(process_directory, source_dir, dest_dir)

if __name__ == "__main__":
    source_directory = r"F:\PROJECTS\IT\hmw3module\hmw3part1\Trash"
    destination_directory = r"F:\PROJECTS\IT\hmw3module\hmw3part1\Sorted"
    main(source_directory, destination_directory)
