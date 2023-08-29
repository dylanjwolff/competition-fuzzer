def get_initial_corpus():
    return ["fuzz"]

i = 0
def entrypoint(s):
    global i
    i += 1
    if i > 100:
        exit(219)

if __name__ == "__main__":
  for p in range(0, 110):
      entrypoint(get_initial_corpus()[0])
