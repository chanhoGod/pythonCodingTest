while True:
    try:
        s = input()
        
        if s == "" or s[-1] == "\n":
            break
        print(s)
    except EOFError:
        break