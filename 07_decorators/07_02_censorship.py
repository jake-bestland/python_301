# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"



def censor(func):
    def censored_words(text):
        bad_words = {"Shoot":"S****"}
        sentence = ""
        word = ""
        for char in str(func(text)):
            if word in bad_words.keys():
                word = bad_words[word]
            if char != " " and (char.isalpha() or char == "'"):
                word += char
                continue
            elif len(word) != 0:
                sentence += word + char
                word = ""
            else:
                sentence += char
        return sentence
    return censored_words

@censor
def repeat(text):
    return text

print(repeat("I bumped my toe! Shoot!"))