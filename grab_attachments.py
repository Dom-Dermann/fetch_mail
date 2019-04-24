import mail_toolbox
import argparse
import graph_converter as gc

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Please provide the password.")
    parser.add_argument('--password', '-p', help="provide password to gmail.")
    args = parser.parse_args()

    gmail = mail_toolbox.FetchMail('imap.gmail.com', 'fileinputs@gmail.com', args.password)
    messages = gmail.fetch_unread_messages()

    paths = []
    for i, msg in enumerate(messages):
        path = gmail.save_attachment(msg)
        paths.append(path)
        print(f'File {i+1} written in {path}')

    for path in paths:
        dataset = gc.data_model(path)
        se = dataset.find_max_money()
        print(se)

   