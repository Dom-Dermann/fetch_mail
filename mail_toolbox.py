import imaplib, email
import os

class FetchMail():
    con = None
    error = None

    def __init__(self, mail_server, username, password):
        self.con = imaplib.IMAP4_SSL(mail_server)
        self.con.login(username, password)
        self.con.select(readonly=False)

    def close_connection(self):
        """
        close connection to imap mail server
        """
        self.con.close()
    
    def save_attachment(self, msg, download_folder='/home/domdom/Desktop/downloads'):
        """
        Save attachments form given message to specified folder

        return: file path to attachment
        """
        att_path = "No attachment found."
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(download_folder, filename)

            if not os.path.isfile(att_path):
                print(" ---- writing file ---- ")
                with open(att_path, 'wb') as f:
                    f.write(part.get_payload(decode=True))
        return att_path

    def fetch_unread_messages(self):
        """
        retrieve unread messages
        """
        emails=[]
        result, messages = self.con.search(None, 'Unseen')
        if result == 'OK':
            for message in messages[0].split():
                try:
                    ret, data = self.con.fetch(message, '(RFC822)')
                except:
                    print("No new email to read.")
                    self.close_connection()
                    exit()

                msg = email.message_from_bytes(data[0][1])
                if isinstance(msg, str) == False:
                    emails.append(msg)
                response, data = self.con.store(message, '+FLAGS', '\\Seen')
            return emails

        self.error = "Failed to retrieve emails."
        return emails

    def parse_email_address(self, email_address):
        """
        Helper function to parse email address from the message

        return: tuple (name, address)
        """

        return email.utils.parseaddr(email_address)

    def show_senders(self):
        """
        Shows all the senders of current emails
        """
        senders = []
        result, data = self.con.uid('search', None, "ALL")
        if result == 'OK':
            for num in data[0].split():
                result, data = self.con.uid('fetch', num, '(RFC822)')
                if result == 'OK':
                    email_message = email.message_from_bytes(data[0][1])
                    senders.append(email_message['From'])
        return senders
