# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def add_seperator(symbol):
    def add_quotes(func):
        def quote(text):
            print(f"{(symbol) * (len(text *6))}")
            func(text)
            print(f"{(symbol) * (len(text *6))}")
        return quote
    return add_quotes

@add_seperator("*")
def greeting(text):
    print(text)

greeting("Hello")