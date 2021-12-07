import subprocess
import sys

def main():
    executable = sys.argv
    del executable[0]
    print("run:", executable)
    subprocess.Popen(executable, creationflags=subprocess.CREATE_NO_WINDOW, close_fds=True)
if __name__ == "__main__":
    main()
