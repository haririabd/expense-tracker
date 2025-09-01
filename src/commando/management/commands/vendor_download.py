import os
from django.core.management.base import BaseCommand
from django.conf import settings
from decouple import config
from helpers import downloader

class Command(BaseCommand):
    """
    A management command to download vendor static files from Dropbox.
    """
    help = "Downloads vendor static files from a Dropbox source folder."

    def add_arguments(self, parser):
        """
        Adds command-line arguments to the management command.
        """
        parser.add_argument(
            'dbx_source_folder',
            type=str,
            help="The full path to the source folder in Dropbox (e.g., /Apps/my-app/vendors)."
        )

        # parser.add_argument(
        #     'local_dest_path',
        #     type=str,
        #     default=settings.STATICFILES_BASE_DIR,
        #     help="The local path where the files will be downloaded to."
        # )

    def handle(self, *args, **options):
        self.stdout.write("Starting Dropbox download...")

        DROPBOX_ACCESS_TOKEN = config('DROPBOX_ACCESS_TOKEN')

        # Access the user-provided arguments from the options dictionary.
        dbx_source_folder = options['dbx_source_folder']
        local_dest_path = settings.STATICFILES_BASE_DIR

        # Ensure the Dropbox path starts with a forward slash.
        if not dbx_source_folder.startswith('/'):
            dbx_source_folder = '/' + dbx_source_folder

        self.stdout.write(f"Downloading from Dropbox folder: {dbx_source_folder} to local path: {local_dest_path}")

        try:
            downloader.download_folder_from_dropbox(dbx_source_folder, local_dest_path, DROPBOX_ACCESS_TOKEN)
            self.stdout.write(self.style.SUCCESS("Successfully downloaded vendor files from Dropbox."))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Process interrupted by user. Exiting..'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))