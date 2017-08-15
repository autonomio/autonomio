from string import ascii_lowercase
import itertools

def col_name_generator(data):

    limit = data.shape[1]
    out = []
    counter = 0

    def iter_all_strings():
        size = 1
        while True:
            for s in itertools.product(ascii_lowercase, repeat=size):
                yield "".join(s)
            size +=1

    for s in iter_all_strings():
        out += s
        counter += 1
        if counter == limit :
            data.columns = out
            return data
            break