import asyncio
import aiohttp
import sys
import json

from helpers import parse_args, get_data_from_api
from filter import filter_all


def main():
    data = get_data_from_api(num_pages)
    filtered_data = filter_all(data, json.loads(json_filter))
    formatted = json.dumps(filtered_data, indent=2)
    print(formatted)


if __name__ == '__main__':
    num_pages, json_filter = parse_args()
    main()
