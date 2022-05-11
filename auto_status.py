import calendar
from datetime import date

import click
import requests
import urllib3
from requests.structures import CaseInsensitiveDict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = 'https://slack.com/api/users.profile.set?'


def set_status(status, emoji, token):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {token}"

    url_str = base_url + 'profile={'
    url_str += '"status_text":"' + status + '"'
    url_str += ', "status_emoji":":' + emoji + ':"'
    url_str += ', "status_text":"' + status + '"'
    url_str += '}'

    response = requests.get(url_str, headers=headers, verify=False)
    print(f"response: {response.text}")


@click.command()
@click.option('--token', type=click.STRING, default="", help="Slack App Token.")
def main(token):
    today = calendar.day_name[date.today().weekday()]
    status = ""
    emoji = ""

    print(f"today is {today}")
    if today.upper() in ['MONDAY', 'WEDNESDAY', 'FRIDAY']:
        status = "원격근무"
        emoji = "house_with_garden"
    elif today.upper() in ['TUESDAY', 'THURSDAY']:
        status = "사무실근무"
        emoji = "signal_strength"
    else:
        print(f"Sleep more~")

    if status:
        set_status(status, emoji, token)
