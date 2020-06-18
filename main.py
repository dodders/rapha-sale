import aws
from bs4 import BeautifulSoup
import requests


def check_sale(event, context):
    print('starting with event:', event, ' context:', context)

    page = requests.get('https://www.rapha.cc')
    soup = BeautifulSoup(page.text, 'html.parser')
    sale_finds = soup.find_all(string=['Sale', 'sale'])
    msg = 'sale not found'
    if len(sale_finds) > 0:
        msg = 'sale found'
    aws.send_status(msg)
    print(msg, ' done.')


if __name__ == "__main__":
    check_sale(None, None)
