import re

with open("social-comments.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("social-comments-no-username.txt", "w", encoding="utf-8") as f:
    for line in lines:
        # Remove all instances of '@' followed by any characters up until a colon ':'
        line = re.sub(r'@[^:]*:', '', line)
        f.write(line)