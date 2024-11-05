with open('test.txt', 'r') as reader: #it closes automatically after process finishes. Also you can spesify for r or w mode.
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)