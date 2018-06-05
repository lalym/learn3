with open ('referat.txt', 'r', encoding='utf-8') as f:
    file=f.read()
    file=file.split()
    words=len(file)
    print(words)

