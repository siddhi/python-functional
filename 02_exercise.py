# Fix the code below so that it becomes pure

from datetime import datetime

def is_month_start():
    today = datetime.now()
    return today.day == 1


def calculate_remaining_credits(credits, spent):
    # If it's the start of the month, reset credits to 500
    if is_month_start():
        credits = 500
    return credits - spent


