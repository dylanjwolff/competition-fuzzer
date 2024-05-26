# Participant Fuzzer
Template repository for the Fuzzing Competition

## CI Job

Please make sure to enable the CI job to check that your fuzzer is working properly:

1. On the forked repo Github web interface, navigate to:
 ```Settings → Actions → General → Workflow Permissions```
2. Select “Read and write permissions”, then click “Save”
3. Verify CI job is enabled by making a small commit (such as changing the team name in the README.md file)


## Setup
Install all dependencies needed by the Fuzzing Book baseline fuzzer with:

```
pip install -r requirements.txt
```

You may want to do this in a Python **virtual environment** to avoid global dependency conflicts.

## Usage

The fuzzer expects a file named `bug.py` to be *in the same directory as the fuzzer file* (`fuzzer.py`).
**DO NOT RENAME THE FUZZER FILE** -- the competition infrastructure will run `python fuzzer.py` to start your fuzzer.
The `bug.py` file will have two functions: an `entrypoint` that is fuzzed by the fuzzer and `get_initial_corpus` function which returns a list of initial inputs for the fuzzer.
Several example bugs are included in the `examples` directory.
To run the fuzzer on an example bug, copy e.g. `examples/0/bug.py` to the base directory of this repository before running the fuzzer with the command above.
I.e.:

```
cp examples/0/bug.py .
python fuzzer.py
```

Whether or not the bug has been triggered will be detected by the competition infrastructure; no need to implement a special exception handler or detection mechanism yourself.
In these examples, finding the bug is indicated by the fuzzer exiting with a particular exit code (219).
The detection method *will* be different in the competition, so don't search the program for a particular exit code etc. to find the bug location.
