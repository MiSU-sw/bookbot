def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = 0
        for w in file_contents.split():
            num_words += 1

        print(f"Found {num_words} total words")

def sort_on(items):
    return items["num"]

def get_num_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_chars = dict()
        file = list(file_contents)
        for c in file:
            if (c.isalpha()):
                try:
                    num_chars[c.lower()] += 1
                except KeyError:
                    num_chars[c.lower()] = 1

        L = list()
        for k in num_chars:
            d = dict()
            d["char"] = k
            d["num"] = num_chars[k]
            L.append(d)

        L.sort(reverse=True, key=sort_on)
        for d in L:
            print(f"{d['char']}: {d['num']}")
