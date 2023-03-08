#!/usr/bin/env python

import argparse
import subprocess
import traceback

import requests


def run_file(file_path, *args):
    # execute the specified file
    try:
        f = open(file_path, "r")
        txt = f.read()
        # exec(txt)
        subprocess.check_call(["python", file_path] + list(args))
    except Exception as e:
        exception_log = traceback.format_exc()
        r = requests.post(
            "https://api.gptpy.net/api/gptpy/free",
            json={"python_interpreter_error": exception_log, "user_code": txt},
        )
        print("-" * 50)
        print("[GPTPy] Your code has an error!")
        print("[GPTPy] Error Reason: ")
        print(r.json()["explanation"])
        print("[GPTPy] Here's fixed code:")
        print(r.json()["suggested_code"])
        print("-" * 50)
        # you can also log or handle the exception here


def main():  # define command-line arguments
    parser = argparse.ArgumentParser(
        description="Run a Python file with a custom wrapper"
    )
    parser.add_argument("file", type=str, help="Path to the Python file to run")
    parser.add_argument(
        "args", nargs="*", help="Arguments to pass to the Python script"
    )

    # parse the arguments
    args = parser.parse_args()

    # run the file with the wrapper
    run_file(args.file, *args.args)


if __name__ == "__main__":
    main()
