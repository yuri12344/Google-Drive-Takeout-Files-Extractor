import zipfile
import os


def log_to_file(file_path, msg):
    print(msg)       
    with open(file_path, 'a') as f:
        f.write(msg + '\n')


def check_zip_integrity(zip_path):
    try:
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                print(f'Checking integrity of {zip_path}')
                bad_file = zip_ref.testzip()
                if bad_file:
                    log_to_file('log_failed_integrity.txt', f"Corrupted file found in {zip_path}: {bad_file}")
                    return False
                else:
                    log_to_file('log_successful_integrity.txt', f"{zip_path} passed integrity check.")
                    return True
        else:
            log_to_file('log_failed_integrity.txt', f"{zip_path} is not recognized as a ZIP file.")
            return False
    except Exception as e:
        log_to_file('log_failed_integrity.txt', f"Failed to check {zip_path}: {e}")
        return False


zip_files = [_ for _ in os.listdir() if _.endswith('.zip')]
if __name__ == "__main__":
    extract_to = './extracted_files'
    for zip_file in zip_files:
        zip_file_number = int(zip_file.split('-')[2].split('.')[0])
        if zip_file_number > 19:
            check_zip_integrity(zip_file)
        


