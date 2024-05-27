# Competition Participant Fuzzer
Template repository for the Fuzzing Competition

### Competition Leaderboard and Scoring:
https://nus-fuzzing-hackathon-2024.github.io/

## CI Job

Please make sure to enable the CI job to check that your fuzzer is working properly:

1. On the forked repo Github web interface, navigate to:
 ```Settings → Actions → General → Workflow Permissions```
2. Select “Read and write permissions”, then click “Save”
3. Verify CI job is enabled by making a small commit (such as changing the team name in the README.md file)


## Dependencies

We are using Python 3.10 in the evaluation environment.

Install all Python package dependencies needed by the Fuzzing Book baseline fuzzer with:

```
pip install -r requirements.txt
```

You may want to do this in a Python [virtual environment](https://docs.python.org/3/library/venv.html) to avoid global dependency conflicts.

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

## Competition Compatability Summary
1. Fork this template repo (keep it [private](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274) to avoid integrity disputes)
2. Give `dylanjwolff` access to your Github repository
3. Fill out the [Google Form](https://docs.google.com/forms/d/1WoiEGgFWDUs9WLSmpt-36C0HzQNYACoJds4QrDm8yDA/viewform)
4. Make changes to your fuzzer (include *all* new files/dependencies in the Dockerfile) -- **DO NOT** change the name of `fuzzer.py`
5. Check that the CI job passes for your changes
6. Cut a `tar.gz` [release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) on Github to have it included in the next [benchmarking run](https://nus-fuzzing-hackathon-2024.github.io/)

## Implementation Ideas
Below are some sample ideas for fuzzer implementations (not exhaustive!).
Entries marked with a '&dagger;' are options we believe will be more straightforward to implement.


**Coverage Feedback**

- [Be Sensitive and Collaborative: Analyzing Impact of Coverage Metrics in Greybox Fuzzing](https://www.usenix.org/system/files/raid2019-wang-jinghan.pdf)
(Many good options in this paper!) &dagger;

**Mutation Strategy**

- [MOPT: Optimize Mutation Scheduling for Fuzzers](https://www.usenix.org/system/files/sec19-lyu.pdf) &dagger;
- [FairFuzz: A Targeted Mutation Strategy for Increasing Greybox Fuzz Testing Coverage](https://dl.acm.org/doi/pdf/10.1145/3238147.3238176)

**Comparison Instrumentation and Branch Distance**

<!--- - [Harvey: A Greybox Fuzzer for Smart Contracts](https://mariachris.github.io/Pubs/FSE-2020-Harvey.pdf) &dagger;
(Sections 4.2 and 4.3) -->

- [REDQUEEN: Fuzzing with Input-to-State Correspondence](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04A-2_Aschermann_paper.pdf) &dagger;
- [Laf-Intel: Circumventing Fuzzing Roadblocks with Compiler Transformations](https://lafintel.wordpress.com/) &dagger;

**Gradient Descent Fuzzing**

- [Angora: Efficient Fuzzing by Principled Search](https://web.cs.ucdavis.edu/~hchen/paper/chen2018angora.pdf) (Section 3.4)
<!--- - [JIGSAW: Efficient and Scalable Path Constraints Fuzzing](https://www.cs.ucr.edu/~csong/oakland22-jigsaw.pdf) (Section 4.D) -->

**Taint Analysis or Dataflow Guided Fuzzing**

*Inference-Based:*

- [GREYONE: Data Flow Sensitive Fuzzing](https://www.usenix.org/conference/usenixsecurity20/presentation/gan)
<!--- - [PATA: Fuzzing with Path Aware Taint Analysis (S\&P 2022)](http://www.wingtecher.com/themes/WingTecherResearch/assets/papers/sp22.pdf) (more complex) -->

*Propagation-Based:*

The Fuzzing Book [gives an intro and some scaffolding code](https://www.fuzzingbook.org/html/InformationFlow.html) for dataflow analysis, but we are not interested in command injection specifically for the competition micro-benchmarks.
You would instead need to find a way to leverage dataflow analysis to cover additional conditional branches within the benchmark programs.

- [DatAFLow: Toward a Data-Flow-Guided Fuzzer](https://dl.acm.org/doi/pdf/10.1145/3587156)

**Concolic Execution (White Box Fuzzing / Dynamic Symbolic Execution)**

Improve the Fuzzing Book white box fuzzer!

**Hybrid Fuzzing**

Combine the fuzzing book implementations of Concolic and Greybox fuzzers!
