import textwrap

def wrap(string, max_width):
    wraps = textwrap.wrap(string, max_width)
    modified_string = ''
    for wrap in wraps:
        modified_string+=wrap+'\n'
    return modified_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)