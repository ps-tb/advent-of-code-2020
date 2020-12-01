def read_lines(filename):
    with open(filename, "rt") as f:
        for line in f:
            yield line