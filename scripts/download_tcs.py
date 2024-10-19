#!/usr/bin/python3

"""Download problems from Competitive Companion and generate testcase files

Usage:
  download_tcs.py
  download_tcs.py [options] 

Options:
  -h --help             Show this screen.
  -n, --number N        Number of problems.
  -s, --single          Download a single problem
  -t, --timeout TIME    Timeout for listening to problems. in seconds

"""

from docopt import docopt
import http.server
import json
from pathlib import Path
import os

def get_problem_name(data):
    return data['name'].split('.')[0].split()[0]

def get_single_problem(timeout=None):
    json_data = None
    class RequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            nonlocal json_data
            json_data = json.load(self.rfile)

    server = http.server.HTTPServer(('127.0.0.1',10043),RequestHandler)
    server.timeout = timeout
    server.handle_request()

    if json_data is not None:
        name = get_problem_name(json_data)
        print(f'Successfully downloaded problem {name}')
    else:
        print("ERROR: No data recieved")

    return json_data


def get_full_contest(timeout=15):
    print(timeout)
    data_set = [get_single_problem()]
    while True:
        problem_data = get_single_problem(timeout)
        if problem_data is None:
            break
        data_set.append(problem_data)

    return data_set


def get_n_problems(n):
    data_set = []
    for _ in range(n):
        problem_data = get_single_problem()
        if problem_data is not None:
            data_set.append(problem_data)

    return data_set


def gen_tc_files(data, tc_dir):
    name = get_problem_name(data)
    for i, d in enumerate(data['tests'], start=1):
        with open(tc_dir / f'{name}_in{i}.txt', 'w') as f:
            f.write(d['input'])

        with open(tc_dir / f'{name}_out{i}.txt', 'w') as f:
            f.write(d['output'])


def main():
    tc_dir = Path('.')/"testcases"
    if not os.path.exists(tc_dir):
        os.mkdir(tc_dir)

    args = docopt(__doc__)

    data_set = None
    if n := args['--number']:
        n = int(n)
        data_set = get_n_problems(n)
    elif args['--single']:
        data_set = [get_single_problem()]
    elif timeout := args['--timeout']:
        timeout = float(timeout)
        data_set = get_full_contest(timeout)
    else:
        data_set = get_full_contest()
    
    for data in data_set:
        gen_tc_files(data, tc_dir)

if __name__ == "__main__":
    main()

