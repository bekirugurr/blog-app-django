from datetime import datetime, timedelta
import random
import string

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

#! Bu fonksiyonu kullanmadım. Bunun yerine DTL timesince filter ile hallettim
def elapsed_time(start):
    now = datetime.now() - timedelta(hours=3)
    if now.year - start.year:
        if now.year - start.year > 1:
           return f'{now.year - start.year} years'            
        else:
           return '1 year'
    elif now.month - start.month:
        if now.month - start.month > 1:
            return f'{now.month - start.month} months'
        else:
            return '1 month'
    elif now.day - start.day:
        if now.day - start.day > 7:
            return f'{now.day - start.day // 7} weeks'
        elif now.day - start.day == 7:
            return '1 week'
        elif now.day - start.day > 1:
            return f'{now.day - start.day} days'
        else:
            return '1 day'
    elif now.hour - start.hour:
        if now.hour - start.hour > 1:
            return f'{now.hour - start.hour} hours'
        else:
            return '1 hour'
    else:
        if now.minute - start.minute > 1:
            return f'{now.minute - start.minute} minutes'
        else:
            return '1 minute'



