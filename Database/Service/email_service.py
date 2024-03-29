import smtplib, ssl
import Data.config_read as configuration
import Database.clean as clean
import datetime


class send_email:
    def __init__(self):
        config = configuration.config()
        self.username = config.email_username
        self.password = config.email_password

    def weekly_update_email(self):
        port = 465  # For SSL

        context = ssl.create_default_context()
        sender_email = self.username
        receiver_email = "pjk1413@gmail.com"

        warnings = ""

        list_of_stock_status = ""

        for stock in clean.clean().get_stock_table_status_behind():
            list_of_stock_status += stock + "\n"

        message = f"""
                Subject: Database Status {datetime.datetime.now()}
                Database Status as of {datetime.datetime.now()}

                {warnings}

                List of all stock tables that are currently behind or not up to date:
                {list_of_stock_status}
                """

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(sender_email, receiver_email, message)

    def daily_update_email(self):
        port = 465  # For SSL

        context = ssl.create_default_context()
        sender_email = self.username
        receiver_email = "pjk1413@gmail.com"

        warnings = ""

        list_of_stock_status = ""

        for stock in clean.clean().get_stock_table_status_behind():
            list_of_stock_status += stock + "\n"

        message = f"""
        Subject: Database Status {datetime.datetime.now()}
        Database Status as of {datetime.datetime.now()}

        {warnings}

        List of all stock tables that are currently behind or not up to date:
        {list_of_stock_status}
        """

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.username, self.password)
            server.sendmail(sender_email, receiver_email, message)

def warning_email(self, message):
    port = 465
    username = configuration.config().email_username
    password = configuration.config().email_password
    sender_email = username
    receiver_email = configuration.config().email_receive

    context = ssl.create_default_context()
    message = f"""
            Subject: Database Status {datetime.datetime.now()}
            Database Status as of {datetime.datetime.now()}
            
            ERROR: {message}
            """

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message)