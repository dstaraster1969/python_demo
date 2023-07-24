import asyncio
import aiohttp
import sys

from helpers import parse_args, get_data_from_api
from filter import filter_all, filter_data


def main():
    data = get_data_from_api(num_pages)
    filtered_data = filter_all(data, json_filter)
    print(filtered_data)


if __name__ == '__main__':
    num_pages, json_filter = parse_args()
    main()
