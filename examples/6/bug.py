def get_initial_corpus():
    return ["pssw"]

def entrypoint(s):
    i = ord(s[0])
    while i > 0:
        i -= 1
    if bar(s):
        if bar(s[5 : len(s)]):
            exit(219)

def bar(s):
    if len(s) > 0 and s[0] == 'p':
        if len(s) > 1 and s[1] == 's':
            if len(s) > 2 and s[2] == 's':
                if len(s) > 3 and s[3] == 'w':
                    if len(s) > 4 and s[4] == 'd':
                        return True
    return False
