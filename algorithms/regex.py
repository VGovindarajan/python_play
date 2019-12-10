import re


def initial():
    content = "The kids were playing soccer in the yard."
    caret = re.search(r'^Th', content)
    dollar = re.search(r'rd\.$', content)
    kids = re.search(r'ki..', content)
    playStart = re.search(r'pl[\w]*', content)
    ingEnd = re.search(r'[\w]*ing', content)

    if caret:
        print(caret.group())
    else:
        print("caret not found.")

    if dollar:
        print(dollar.group())
    else:
        print("dollar not found.")

    if kids:
        print(kids.group())
    else:
        print("kids not found.")

    if playStart:
        print(playStart.group())
    else:
        print("playStart not found.")

    if ingEnd:
        print(ingEnd.group())
    else:
        print("ingEnd not found.")

def main():
    initial()

if __name__ == "__main__":
    main()