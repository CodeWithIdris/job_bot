import imaplib
import email

def check_positive_responses():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("yourgmail@gmail.com", "app_password")
    mail.select("inbox")

    result, data = mail.search(None, "UNSEEN")
    ids = data[0].split()

    for num in ids:
        result, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        subject = msg["subject"].lower()

        positive_keywords = ["interview", "schedule", "next step", "shortlisted"]
        negative_keywords = ["unfortunately", "regret", "not selected"]

        if any(word in subject for word in positive_keywords):
            print("🎉 Interview detected:", subject)

            