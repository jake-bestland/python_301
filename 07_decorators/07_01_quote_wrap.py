# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def add_quotes(func):
    def quote(text):
        initial_result = func(text)
        new_result = f'"{initial_result}"'
        return new_result
    return quote

@add_quotes
def phrase(text):
    return text

print(phrase("Hello world!"))