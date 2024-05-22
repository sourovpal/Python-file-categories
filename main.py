import os
import shutil
import datetime
def organize_files(source_dir, dest_dir):
    for folder in ['Images', 'Documents', 'Videos', 'Others']:
        folder_path = os.path.join(dest_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            
            file_ext = filename.split('.')[-1].lower()

            if file_ext in ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg"]:
                dest_folder = 'Images'
            elif file_ext in ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "rtf"]:
                dest_folder = 'Documents'
            elif file_ext in ["mp4", "avi", "mov", "mkv", "wmv", "flv", "webm", "mpeg", "mpg", "3gp"]:
                dest_folder = 'Videos'
            else:
                # continue
                dest_folder = 'Others'

            # Move the file to the appropriate folder
            dest_path = os.path.join(dest_dir, dest_folder, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {dest_folder}")

def main():
    source_dir = "C:\\Users\\User\\Downloads\\"
    dest_dir = './directory'
    organize_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
