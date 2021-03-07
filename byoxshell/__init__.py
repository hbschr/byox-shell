import os
import shlex
import subprocess
import sys

__version__ = '0.1.0'

state = {
    'cwd': os.getcwd(),
}


def execute(*args):
    if not len(args):
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
    if len(sys.argv) > 1 and sys.argv[1] in ['-v', '--version']:
        print(__version__)
        sys.exit(0)

    try:
        while True:
            x = input("> ")
            execute(*shlex.split(x))
    except EOFError:
        print("exit")
        sys.exit(0)
