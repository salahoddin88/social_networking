import re

def is_valid_email(string):
    """ Check provided string is email or not """
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if re.match(email_pattern, string):
        return True
    else:
        return False