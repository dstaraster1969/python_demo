import asyncio
import json

from helpers import parse_args, get_data_from_api
from filter import filter_all


async def main():
    # first grab the data from the API. Getting all pages on one thread takes
    # forever, so made the call asynchronous, but getting all pages still takes
    # too long.
    data = await get_data_from_api(num_pages)

    # filter that data on all filters passed in
    filtered_data = filter_all(data, json.loads(json_filter))

    # make it pretty
    formatted = json.dumps(filtered_data, indent=2)
    print(formatted)

if __name__ == '__main__':
    num_pages, json_filter = parse_args()
    asyncio.run(main())
