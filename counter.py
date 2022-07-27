def counter(file, word):
    count = 0
    text = ""

    for i in file:
        text = i
        count = count + text.lower().count(word)

    return count


def openFile(file_name):
    file = open(file_name, "r")
    return file
