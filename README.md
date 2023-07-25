This demonstration of python skills calls into a public REST API. `config.yaml` points to an API for television shows, but it could be modified to run against any REST API that doesn't require authentication. It then filters those results on the filter list that's passed in.

This code demonstrates consuming a REST API, manipulating JSON, recursion, and concurrency.


To run from the command line:

`davin@my_laptop MINGW64 /c/python-demo (filter)
pip install -r requirements.txt`

`davin@my_laptop MINGW64 /c/python-demo (filter)
$ python main.py 3 '[{"language": "English"}, {"name": "Downton Abbey"}]'`