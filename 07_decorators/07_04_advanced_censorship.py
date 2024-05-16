# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor_the_words(*args):
    def censor(func):
        def censored_words(text):
            bad_words = {}
            for arg in args:
                low_arg = arg.lower()
                bad_words[low_arg] = low_arg[0] + ("*" * (len(low_arg) -1))
                cap_arg = arg.capitalize()
                bad_words[cap_arg] = cap_arg[0] + ("*" * (len(cap_arg) -1))
                upper_arg = arg.upper()
                bad_words[upper_arg] = upper_arg[0] + ("*" * (len(cap_arg) -1))
            sentence = ""
            word = ""
            for char in str(func(text)):
                if word in bad_words.keys():
                    word = bad_words[word]
                if char != " " and (char.isalpha() or char == "'"):
                    word += char
                    continue
                elif len(word) != 0:
                    sentence += word + char + ""
                    word = ""
                else:
                    sentence += char
            return sentence
        return censored_words
    return censor

@censor_the_words("shoot", "Crab")
def repeat(text):
    return text

print(repeat("I bumped my toe! SHOOT! let's get some crab."))
