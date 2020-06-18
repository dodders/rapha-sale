import boto3
from datetime import date


# initialize aws connection.
print('aws starting...')
# session = boto3.Session(profile_name='dep')
session = boto3.Session()
sns = session.client('sns')


def send_status(sale_status):
    today = str(date.today())
    msg = 'Rapha sale ' + sale_status + ' ' + today
    resp = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:397678393215:george',
        Subject=msg,
        Message=msg
    )
    print('email sent', resp)
