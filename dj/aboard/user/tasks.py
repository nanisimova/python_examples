from celery import shared_task
import datetime

@shared_task
def send_email_registration():
    f = open("/root/www/python_examples/dj/aboard/report.txt", 'a')
    f.write(str(datetime.datetime.today()) + "\n")
    f.close()

