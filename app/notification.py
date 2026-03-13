from difflib import SequenceMatcher

def check_significant_change(old, new):

    similarity = SequenceMatcher(None, old, new).ratio()

    return similarity < 0.95


def send_notification(doc_id):

    print(f"Notification: Document {doc_id} significantly changed")