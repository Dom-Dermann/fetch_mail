import mail_toolbox
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Please provide the password.")
    parser.add_argument('--password', '-p', help="provide password to gmail.")
    args = parser.parse_args()

    gmail = mail_toolbox.FetchMail('imap.gmail.com', 'fileinputs@gmail.com', args.password)
    messages = gmail.fetch_unread_messages()
    for i, msg in enumerate(messages):
        path = gmail.save_attachment(msg)
        print(f'File {i+1} written in {path}')

