import aiohttp
import sys
import asyncio
import json

from helpers import parse_args, get_data_from_api
from filter import filter_all


async def main():
    # first grab the data from the API. Number of pages is required because
    # getting all pages from the API takes 15 mins
    data = await get_data_from_api(num_pages)

    # filter that data on all filters passed in
    filtered_data = filter_all(data, json.loads(json_filter))

    # make it pretty
    formatted = json.dumps(filtered_data, indent=2)
    print(formatted)

if __name__ == '__main__':
    num_pages, json_filter = parse_args()
    asyncio.run(main())
