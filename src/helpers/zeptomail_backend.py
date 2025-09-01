# my_app/zeptomail_backend.py
import requests
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMultiAlternatives

class ZeptoMailBackend(BaseEmailBackend):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Fetch the API URL and token from Django settings
        self.api_url = getattr(settings, 'ZEPTOMAIL_API_URL', None)
        self.api_token = getattr(settings, 'ZEPTOMAIL_API_TOKEN', None)
        self.headers = {
            'Authorization': f'Zoho-enczapikey {self.api_token}',
            'Content-Type': 'application/json',
        }

    def send_messages(self, email_messages):
        if not self.api_url or not self.api_token:
            # Handle cases where settings are not configured
            if not self.fail_silently:
                raise ValueError("ZeptoMail API URL or token is not configured.")
            return 0

        sent_count = 0
        for message in email_messages:
            try:
                # Construct the JSON payload from the Django EmailMessage object
                payload = {
                    "from": {"address": message.from_email},
                    "to": [{"email_address": {"address": addr}} for addr in message.to],
                    "subject": message.subject,
                }

                # Handle plain text and HTML bodies
                if message.body:
                    payload['textbody'] = message.body
                if isinstance(message, EmailMultiAlternatives) and message.alternatives:
                    for content, mimetype in message.alternatives:
                        if mimetype == 'text/html':
                            payload['htmlbody'] = content
                            break

                # Make the POST request to the ZeptoMail API
                response = requests.post(self.api_url, json=payload, headers=self.headers)
                response.raise_for_status() 
                sent_count += 1

            except requests.exceptions.RequestException as e:
                if not self.fail_silently:
                    raise e
        return sent_count