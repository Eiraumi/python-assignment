def acronym(phrase):
    result = ""
    for word in phrase.split():
        result += word[0].upper()
    return result

# TEST
print(acronym("unidentified foreign object"))
