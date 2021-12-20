# execbg

## Overview

execbg is a simple command that run the given command in background.

## Usage

```
# Below execute sleep 100 in background
$ execbg sleep 100
run: sleep 100, PID: 14444
$ ps | grep 14444
     11    11.83      11.92       0.08   14444   2 sleep
# PID 14444 will keep running when you exit from shell.
```

## Requirement
- python >= 3.9
- Windows 10

## Instration

With pip:
```
$ pip install git+https://github.com/watabe951/execbg
```

With pipx (recommended):
```
$ pipx install git+https://github.com/watabe951/execbg
```


