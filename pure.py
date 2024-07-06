


should_send_notification = False
def send_email_to_devs(msg):
    global should_send_notification
    # for some reason, this gets called twice
    # so ignore every alternate invocation
    if should_send_notification:
        print(msg)
    should_send_notification = not should_send_notification

def call_api(url):
    return -1

def get_scores(id):
    scores = call_api(f'https://myapi.com/{id}')
    if scores < 0:
        send_email_to_devs("Negative score. Resetting to zero")
        return 0
    return scores

if get_scores(id) < 10:
    print("Game over. Total score = ", get_scores(id))


