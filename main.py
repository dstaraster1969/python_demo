import asyncio
import aiohttp
import argparse
import sys
from filter import filter_all, filter_data


def main():
    num_pages, json_filter = parse_args()
    data = 

def parse_args():
    parser = argparse.ArgumentParser(description='Fetch from API and filter')
    parser.add_argument('num_pages', help='The number of pages to retrieve')
    parser.add_argument('filter', help='The JSON string to filter on')

    args = parser.parse_args()
    return args.num_pages, args.filter


if __name__ == '__main__':
    main()