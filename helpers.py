
import random
import string
import time

def get_existed_user_data():
    return 'ivan1100@gmail.ru', '123123'

def generate_unique_email():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"ui_test_{int(time.time())}_{suffix}@example.com"

def generate_unique_pass():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"pass_{int(time.time())}_{suffix}"

def generate_unique_email_invalid():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"ui_test_{int(time.time())}_{suffix}@matroshka"

def generate_unique_pass_invalid():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"pass_{int(time.time())}_{suffix}"