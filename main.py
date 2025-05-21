import os
import base64
import mimetypes
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

def create_service(client_secret_file, api_name, api_version, scopes):
    """
    Creates a Google API service.

    Parameters:
        client_secret_file (str): Path to the client secret JSON file.
        api_name (str): Name of the Google API.
        api_version (str): Version of the API.
        scopes (list): List of scopes for the API.

    Returns:
        service: Authorized Google API service instance.
    """
    cred = None
    pickle_file = f'token_{api_name}_{api_version}.pickle'

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            cred = flow.run_local_server(port=8080)

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    service = build(api_name, api_version, credentials=cred)
    return service

def send_email_with_attachments(service, sender, to, subject, body_text, attachments):
    """
    Sends an email with attachments using the Gmail API.

    Parameters:
        service: Authorized Gmail API service instance.
        sender (str): Email address of the sender.
        to (list): List of recipient email addresses.
        subject (str): Subject of the email.
        body_text (str): Body text of the email.
        attachments (list): List of file paths to attach.
    """
    message = MIMEMultipart()
    message['to'] = ', '.join(to)
    message['from'] = sender
    message['subject'] = subject

    message.attach(MIMEText(body_text, 'plain'))

    for file_path in attachments:
        content_type, encoding = mimetypes.guess_type(file_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)

        with open(file_path, 'rb') as f:
            file_data = f.read()

        file_name = os.path.basename(file_path)
        part = MIMEBase(main_type, sub_type)
        part.set_payload(file_data)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=file_name)
        message.attach(part)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    send_message = {'raw': raw_message}

    try:
        sent_message = service.users().messages().send(userId='me', body=send_message).execute()
        print(f'Email sent successfully! Message ID: {sent_message["id"]}')
    except Exception as e:
        print(f'An error occurred: {e}')




#just ignore the calendar part for now becoz it just prints the next 10 events in the google calendar



# def get_upcoming_events(service, max_results=10):
#     """
#     Retrieves the next upcoming events from the user's primary calendar.

#     Parameters:
#         service: Authorized Calendar API service instance.
#         max_results (int): Maximum number of events to retrieve.
#     """
#     now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

#     try:
#         events_result = service.events().list(
#             calendarId='primary',
#             timeMin=now,
#             maxResults=max_results,
#             singleEvents=True,
#             orderBy='startTime'
#         ).execute()
#         events = events_result.get('items', [])

#         if not events:
#             print('No upcoming events found.')
#             return

#         print('Upcoming events:')
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(f"{start} - {event.get('summary', 'No Title')}")
#     except Exception as e:S
#         print(f'An error occurred: {e}')

if __name__ == '__main__':
    CREDENTIALS = 'credentials.json'

    # Create Gmail service
    gmail_scopes = ['https://mail.google.com/']
    gmail_service = create_service(CREDENTIALS, 'gmail', 'v1', gmail_scopes)

    # # Create Calendar service
    # calendar_scopes = ['https://www.googleapis.com/auth/calendar.readonly']
    # calendar_service = create_service(CREDENTIALS, 'calendar', 'v3', calendar_scopes)

    # Send email with attachments
    sender_email = 'example@gmail.com'
    recipient_emails = ['exampleforsender@gmail.com']
    email_subject = 'yen anbu maganeyyyy.......'
    email_body = 'appavidam irundhu.....I am sending to through the gmail automation program ..If you have any doubt regarding this please visit my github account for calendar and gmail automation program..  and One Important update today evening 3:00pm we are gonna meet Prasina sathish mam to show our architecture of our project so be prepared'
    attachment_files = ['your/path/to/attachment.pdf']

    send_email_with_attachments(
        service=gmail_service,
        sender=sender_email,
        to=recipient_emails,
        subject=email_subject,
        body_text=email_body,
        attachments=attachment_files
    )

    # # Retrieve upcoming calendar events
    # get_upcoming_events(service=calendar_service, max_results=10)
