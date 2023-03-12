#!/usr/bin/env python
import argparse
import os
import subprocess
import traceback

import requests


def run_file(file_path, args_list):
    # execute the specified file
    try:
        f = open(file_path, "r")
        txt = f.read()
        cmd_args = ["python", file_path] + args_list
        try:
            subprocess.check_output(cmd_args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            # print(e.output.decode())
            exception_log = e.output.decode()
            print("-" * 50)
            print("[GPTPy] Your code has an error!")
            # print(exception_log)
            r = requests.post(
                "https://api.gptpy.net/api/gptpy/free",
                json={"python_interpreter_error": exception_log, "user_code": txt},
            )
            print("[GPTPy] Error Reason: ")
            print(r.json()["explanation"])
            print("[GPTPy] Here's fixed code:")
            print(r.json()["suggested_code"])
            print("-" * 50)
    except Exception as e:
        exception_log = traceback.format_exc()
        print("-" * 50)
        print("[GPTPy] May be Input has error..?")
        print(exception_log)
        r = requests.post(
            "https://api.gptpy.net/api/gptpy/free",
            json={"python_interpreter_error": exception_log},
        )
        print("[GPTPy] Error Reason: ")
        print(r.json()["explanation"])
        print("[GPTPy] Here's solution:")
        print(r.json()["suggested_code"])
        print("-" * 50)


def main():
    # define command-line arguments
    parser = argparse.ArgumentParser(
        description="Run a Python file with a custom wrapper"
    )
    parser.add_argument("file", type=str, help="Path to the Python file to run")
    parser.add_argument(
        "args", nargs=argparse.REMAINDER, help="Arguments to pass to the Python script"
    )

    # parse the arguments
    args = parser.parse_args()

    # if args.file path does not exist, print error message and exit
    if not os.path.exists(args.file):
        print("[GPTPy] File not found: {}".format(args.file))
        exit(1)

    # run the file with the wrapper
    run_file(args.file, args.args)


if __name__ == "__main__":
    main()
