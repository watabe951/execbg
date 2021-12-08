import subprocess
import sys
import argparse

def main():
    # parse
    parser = argparse.ArgumentParser(description='run command in background')
    parser.add_argument('command', type=str, nargs=1, help='command to execute')
    parser.add_argument('arg', type=str, nargs='*', help='arguments to pass to the command')
    args = parser.parse_args()

    executable = args.command + args.arg
    # run
    po = subprocess.Popen(executable, creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)

    # send some message
    print(f"run: {' '.join(executable)}, PID: {po.pid}")
if __name__ == "__main__":
    main()
