import zipfile
import os
import shutil
import ipdb
import os
import ipdb

def sanitize_path(path):
    return path.rstrip(' ').replace(' ', '_')

def log_to_file(file_path, msg):
    print(msg)       
    with open(file_path, 'a') as f:
        f.write(msg + '\n')

def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:

            for member in zip_ref.namelist():
                sanitized_name = sanitize_path(member)
                full_extract_path = os.path.join(extract_to, sanitized_name)

                if member.endswith('/'):
                    if not os.path.exists(full_extract_path):
                        os.makedirs(full_extract_path)
                    log_to_file('log_sucessfull_folders.txt', f"Successfully created directory: {full_extract_path}")
                else:
                    os.makedirs(os.path.dirname(full_extract_path), exist_ok=True)
                    with zip_ref.open(member) as source, open(full_extract_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                    log_to_file("log_sucess_extract.txt", f"Successfully extracted file: {full_extract_path}")

    except zipfile.BadZipFile:
        ipdb.set_trace()
        log_to_file('log_failed_extraction.txt', f"Failed to extract {zip_path}: {e}")

zip_files = [_ for _ in os.listdir() if _.endswith('.zip')]
if __name__ == "__main__":
    extract_to = './extracted_files'
    for zip_file in zip_files:
        zip_file_number = int(zip_file.split('-')[2].split('.')[0])
        print(zip_file_number)  
        if zip_file_number >= 31:
            log_to_file('log_zips_extracting.txt', f'Extracting {zip_file} to {extract_to}')
            extract_zip(zip_file, extract_to)
            log_to_file('log_zips_extracting.txt', f'Finished extracting {zip_file} to {extract_to}')
        


