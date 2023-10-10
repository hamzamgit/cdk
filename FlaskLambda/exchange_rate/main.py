import requests
import xml.etree.ElementTree as ET
import json

from datetime import datetime, timedelta


def get_currency_data(root):
    currency_data = {}

    currency_name_elements = root.getchildren()[2].getchildren()
    for element in list(currency_name_elements):
        date = element.attrib.get("time")
        currencies = element.getchildren()
        currency_data[date] = {}
        for cube in list(currencies):
            currency = cube.attrib.get("currency")
            rate = cube.attrib.get("rate")
            currency_data[date][currency] = rate
    return currency_data


def get_weekdays(start_date):
    if start_date:
        week_no = start_date.weekday()
    else:
        week_no = datetime.today().weekday()
    if week_no == 0:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    elif week_no == 6:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    elif week_no == 5:
        present_day = start_date
        current_date = present_day.strftime("%Y-%m-%d")
        last_day = present_day - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")
    else:
        current_date = start_date.strftime('%Y-%m-%d')
        last_day = start_date - timedelta(days=1)
        last_date = last_day.strftime("%Y-%m-%d")

    return current_date, last_date


def extract_currencies():
    request_url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml?ccff4b91d2713471dadc8ccca7e8490f"
    print("REQUEST URL", request_url)
    response = requests.get(request_url)
    root = ET.fromstring(response.text)
    currency_data = get_currency_data(root=root)
    return currency_data


def get_currency_rates():
    start_date = datetime(day=17, month=1, year=2023)
    current_date, last_date = get_weekdays(start_date=start_date)

    return {
            x: {
                "today": float(CURRENCY_DATA[current_date][x]),
                "difference": round(float(CURRENCY_DATA[current_date][x]) - float(CURRENCY_DATA[last_date][x]), 3)
            }
            for x, y in CURRENCY_DATA[last_date].items()
    }


if __name__ == '__main__':
    CURRENCY_DATA = extract_currencies()
    print(json.dumps(get_currency_rates(), indent=4))
