# GPTPy: Your kind Python guide, powered by AI to fix errors and explain code

[![asciicast](https://asciinema.org/a/momJh0P8YiZRY5IW0ZwTTynhA.svg)](https://asciinema.org/a/momJh0P8YiZRY5IW0ZwTTynhA)

## Installation

```bash
pip install -U gptpy
```

## Usage

```bash
gptpy runnable_python_code.py
```

## Example

Here's a simple Python code, which has a syntax error.

```python
# test.py
def add(a, b):
    print("a + b)
```

If you run `test.py`, you will get an error.

```
$ python test.py 
  File "~/test.py", line 1
    print("a + b)
                 ^
SyntaxError: EOL while scanning string literal
```

Now, let's use `gptpy` to fix the error.

```
$ gptpy test.py 
--------------------------------------------------
[GPTPy] Your code has an error!
[GPTPy] Error Reason: 

# The user forgot to close the string with a single quote.
SyntaxError: EOL while scanning string literal

[GPTPy] Here's fixed code:

print("a + b")
--------------------------------------------------
```

## Limitations

- GPT-3 is not perfect. It may not be able to fix all errors.
- It may take a while to get the result.

