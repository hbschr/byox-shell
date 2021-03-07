import os
import shlex
import subprocess
import sys


state = {
    'cwd': os.getcwd(),
}


def execute(*args):
    if len(args) == 0:
        return

    if args[0] == 'exit':
        raise EOFError()
    elif args[0] == "cd":
        if len(args) == 1:
            state['cwd'] = os.getcwd()
        else:
            state['cwd'] = os.path.abspath(os.path.join(state['cwd'], args[1]))
        print(f"cwd: {state['cwd']}")
        return

    subprocess.run(args, cwd=state['cwd'])


def main():
    try:
        while True:
            x = input("> ")
            execute(*shlex.split(x))
    except EOFError:
        print("exit")
        sys.exit(0)
