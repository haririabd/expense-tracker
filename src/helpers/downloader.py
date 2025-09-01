import os
import dropbox
import requests
from pathlib import Path

def download_to_local(url:str, out_path:Path, parent_mkdir:bool=True):
    # check if out_path is an instance of python pathlib
    # and if valid, makesure it is exist / create the path
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib.Path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any newline conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False

def download_folder_from_dropbox(dbx_source_path, local_dest_path, dbx_token):
    """
    Recursively downloads all files from a Dropbox folder to a local path.

    Args:
        dbx_source_path (str): The full path to the source folder in Dropbox.
        local_dest_path (str): The local path where the folder will be downloaded.
        dbx_token (str): The Dropbox API access token.
    """
    dbx = dropbox.Dropbox(dbx_token)

    try:
        # List all files and folders in the source path.
        # This is a recursive process to get all nested files.
        for entry in dbx.files_list_folder(dbx_source_path, recursive=True).entries:
            # Construct the relative path from the source folder
            relative_path = os.path.relpath(entry.path_lower, dbx_source_path.lower())
            
            # Construct the full local destination path
            local_path = os.path.join(local_dest_path, relative_path)
            
            # If the entry is a file, download it. If it's a folder, create it.
            if isinstance(entry, dropbox.files.FileMetadata):
                # Ensure the local directory exists before downloading
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                
                print(f"Downloading: {entry.path_lower} --> {local_path}")
                dbx.files_download_to_file(local_path, entry.path_lower)
            elif isinstance(entry, dropbox.files.FolderMetadata):
                # Create the local directory if it doesn't exist
                os.makedirs(local_path, exist_ok=True)
                print(f"Creating local folder: {local_path}")
                
    except dropbox.exceptions.ApiError as err:
        if isinstance(err.error, dropbox.files.DownloadError) and err.error.is_path:
            print(f"Path does not exist in Dropbox: {dbx_source_path}")
        else:
            raise err