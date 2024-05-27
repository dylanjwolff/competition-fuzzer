def get_initial_corpus():
    return ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]

def entrypoint(s):
    if s == "areallyreallyreallyreallyreallyreallylongstring":
        print("Found the bug!")
        exit(219)

