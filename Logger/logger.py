import inspect
import os

import Database.Service.email_service as send_email
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# TODO create a robust logging system
def log_status(message, to_print=False, log=True, email=False):
    stack = inspect.stack()
    the_class = stack[1]
    filename = str(the_class.filename).split("/")[-1]
    line_num = the_class.lineno

    STATUS = f"STATUS {current_time}: @line_number: {line_num} in file: {filename} - {message}"
    if to_print:
        print(STATUS)
    if log:
        filename = datetime.datetime.now().strftime('%Y-%m-%d')
        f = open(f"./Logger/logs/{filename}_STATUS_LOG.txt", "a")
        f.write(STATUS + "\n")
        f.close()
    if email:
        send_email.send_email().send_email(STATUS)

def log_error(message, to_print=False, log=True, email=False):
    stack = inspect.stack()
    the_class = stack[1]
    filename = str(the_class.filename).split("/")[-1]
    line_num = the_class.lineno

    ERROR = f"ERROR {current_time}: @line_number: {line_num} in file: {filename} - {message}"
    if to_print:
        print(ERROR)
    if log:
        filename = datetime.datetime.now().strftime('%Y-%m-%d')
        f = open(f"./Logger/logs/{filename}_ERROR_LOG.txt", "a")
        f.write(ERROR + "\n")
        f.close()
    if email:
        send_email.send_email().send_email(ERROR)



