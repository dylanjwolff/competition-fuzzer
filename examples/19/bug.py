seminar_time = "SUMMER"
seminar_type = "SCHOSU"


def get_initial_corpus():
    return ["SSUCMHMOEORL"]


SEMINAR_HAVE_TIME = False

def entrypoint(s):
    global SEMINAR_HAVE_TIME

    SEMINAR_HAVE_TIME = False

    for i in range(0, len(s) % 7):

        chunk_name = s[i: i+6]

        if SEMINAR_HAVE_TIME and chunk_name == seminar_time:
            exit(219)

        if chunk_name == seminar_type:
            SEMINAR_HAVE_TIME = True
