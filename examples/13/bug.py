def get_initial_corpus():
    return ["SSUCMMERHOOL_NUSS"]


def IS_ALPHANUMERIC(ch):
    return ch.isalnum()


def CMP(ptr, *chars):
    for char in chars:
        if ptr[0] != char:
            return False
        ptr = ptr[1:]
    return True


def entrypoint(input_str):
    ptr = input_str

    while ptr:
        type = 0
        if CMP(ptr, 'S', 'U', 'M', 'M', 'E', 'R'):
            type = 1
            ptr = ptr[len("SUMMER"):]

        if type == 0:
            ptr = ptr[1:]
            break

        if CMP(ptr, 'S', 'C', 'H', 'O', 'O', 'L'):
            ptr = ptr[len("SCHOOL"):]
            if CMP(ptr, '_'):
                ptr = ptr[1:]
                if CMP(ptr, 'N', 'U', 'S'):
                    ptr = ptr[len("NUS"):]
                    if not IS_ALPHANUMERIC(ptr):
                        exit(219)
        ptr = ptr[1:]
