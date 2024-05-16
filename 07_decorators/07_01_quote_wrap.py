# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def add_quotes(func):
    def quote(text):
        return f'"{func(text)}"'
    return quote

@add_quotes
def phrase(text):
    return text

print(phrase("Hello world!"))