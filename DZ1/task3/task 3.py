with open('input.txt', 'r') as f:
    text = f.read()
    chars_left = 20
    result = ''
    for word in text.split():
        if len(word) > chars_left:
            result += '\n' + word + ' '
            chars_left = 20 - len(word) - 1
        else:
            result += word + ' '
            chars_left -= len(word) + 1
with open('output.txt', 'w') as out:
        out.write(result)