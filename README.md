# About

Meeplan is a console application used to generate shifts. It takes as an input a list of shift requirements and employees and from that it generates a plan in a csv project.

The csv can be imported into a google sheet for visualization:
https://docs.google.com/spreadsheets/d/1lYtToqYQ45N1tITWUFMUc-92GlbE1NY7TAkLwNJT7Bc/edit#gid=97712170


# Dependencies
* Python 3.8
* Pandas

# Publish
Publish C# part (macOS):

`dotnet publish -r osx-x64 -c release /p:publishsinglefile=true`

# Build
```bash
pip3 install pandas
dotnet publish -r osx-x64 -c release /p:publishsinglefile=true # for macOS
```
The generated executable must be moved from `bin` -> `PlannerCSharp` folder. The executable renamed `PlannerCsharp` -> `PlannerCsharp.exe`

# Quirks:

## Solve Pandas error:

Issue: (Happens on MacOS:)
```
Python(4250,0x10271de00) malloc: can't allocate region
:*** mach_vm_map(size=18446744072572129280, flags: 100) failed (error code=3)
Python(4250,0x10271de00) malloc: *** set a breakpoint in malloc_error_break to debug
init_dgelsd failed init
Traceback (most recent call last):
  File "schedule-requirements-parser.py", line 1, in <module>
    import pandas as pd
  File "/usr/local/lib/python3.8/site-packages/pandas/__init__.py", line 11, in <module>
    __import__(dependency)
  File "/usr/local/lib/python3.8/site-packages/numpy/__init__.py", line 286, in <module>
    raise RuntimeError(msg)
RuntimeError: Polyfit sanity test emitted a warning, most likely due to using a buggy Accelerate backend. If you compiled yourself, see site.cfg.example for information. Otherwise report this to the vendor that provided NumPy.
RankWarning: Polyfit maybe poorly conditioned
```

**Solution**:
Found here:
https://stackoverflow.com/questions/64245321/having-problems-running-numpy-error-about-buggy-accelerate-backend-python

* Go to line 270 and comment out the lines 270 - 287 in the numpy package.