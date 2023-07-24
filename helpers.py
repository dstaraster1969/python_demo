import argparse
import yaml
import requests
import json


def parse_args():
    parser = argparse.ArgumentParser(description='Fetch from API and filter')
    parser.add_argument('num_pages', help='The number of pages to retrieve')
    parser.add_argument('filter', help='The JSON string to filter on')

    args = parser.parse_args()
    return int(args.num_pages), args.filter


def get_data_from_api(num_pages):
    url = yaml.safe_load(open('./config.yml'))['url']
    results = []
    for i in range(1, num_pages):
        data = requests.get(f'{url}?page={i}').json()
        for d in data:
            results.append(d)

    return results
