def get_initial_corpus():
    return ["testtest"]

def transform(s):
    new = [chr(ord(c) - 1) for c in s]
    print(new)
    return "".join(new)

  
def entrypoint(input):
    if len(input) < 8:
        return False

    if(input[0:4] == transform(input[4:8])):
        exit(219)

     
