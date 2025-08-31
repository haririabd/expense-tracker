import os
import dropbox

def upload_folder_to_dropbox(local_folder, dbx_base_path, dbx_token):
    dbx = dropbox.Dropbox(dbx_token)
    
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_folder)
            dropbox_path = os.path.join(dbx_base_path, relative_path).replace("\\", "/")
            
            print(f"Uploading: {relative_path} --> {dropbox_path}")
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)