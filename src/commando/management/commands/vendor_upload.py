from helpers import uploader
from django.core.management.base import BaseCommand
from django.conf import settings
from decouple import config

class Command(BaseCommand):
    """
    A management command to upload vendor static files to Dropbox.
    """
    help = "Uploads vendor static files to Dropbox."
    
    def handle(self, *args: any, **options: any):
        self.stdout.write("Uploading vendor static files. Ctrl + C to stop the process..")
        
        DROPBOX_TOKEN = config('DROPBOX_TOKEN')
        LOCAL_FOLDER = settings.STATICFILES_VENDOR_DIR
        DROPBOX_DEST = '/vendors'
        
        try:
            while True:
                uploader.upload_folder_to_dropbox(LOCAL_FOLDER, DROPBOX_DEST, DROPBOX_TOKEN)
                self.stdout.write(self.style.SUCCESS("Successfully uploaded vendor files to Dropbox."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Process interrupted by user. Exiting..'))