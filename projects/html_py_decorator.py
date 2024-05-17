# Write a decorator function that wraps text passed to it in a specified HTML tag.
# The user should be able to decide which tag to use.

def tagify(tag):
    def add_tag(func):
        def content(*text):
            return f"<{tag}>{func(*text)}</{tag}>"
        return content
    return add_tag


@tagify("p")
def greet(name):
    return f"Hello, {name}"


@tagify("div")
def lorem():
    return "Lorem ipsum dolor sit amet, ..."

print(lorem())
print(greet("Bessy"))