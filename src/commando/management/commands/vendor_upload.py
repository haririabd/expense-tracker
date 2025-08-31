import os
from helpers import uploader
from django.core.management.base import BaseCommand
from django.conf import settings
from decouple import config

class Command(BaseCommand):
    """
    A management command to upload vendor static files to Dropbox.
    """
    help = "Uploads vendor static files to Dropbox to a user-specified folder."
    
    def add_arguments(self, parser):
        """
        Adds command-line arguments to the management command.
        """
        parser.add_argument(
            'project_name',
            type=str,
            help="The project name to use for the Dropbox destination folder."
        )
        
    def handle(self, *args: any, **options: any):
        self.stdout.write("Uploading vendor static files...")
        
        DROPBOX_TOKEN = config('DROPBOX_TOKEN')
        LOCAL_FOLDER = settings.STATICFILES_VENDOR_DIR
        
        # Access the user-provided project name from the options dictionary.
        project_name = options['project_name']
        
        if not project_name:
            self.stdout.write(self.style.ERROR("No project name entered. Exiting.."))
            return
        
        # Construct the full Dropbox destination path by combining a base path
        # with the user's input. The path must start with a '/'.
        DROPBOX_DEST = os.path.join('/', project_name, 'vendors').replace("\\", "/")
        self.stdout.write(f"Uploading vendor static files to folder {DROPBOX_DEST}.")
        try:
            # Perform the upload once, without an infinite loop
            uploader.upload_folder_to_dropbox(LOCAL_FOLDER, DROPBOX_DEST, DROPBOX_TOKEN)
            self.stdout.write(self.style.SUCCESS("Successfully uploaded vendor files to Dropbox."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Process interrupted by user. Exiting..'))