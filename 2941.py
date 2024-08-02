N = input()

length_N = len(N)

N = N[::-1]

for i in range(0, len(N)):
    # try:
        if N[i] == "=":
            if N[i+1] == "z":
                i += 1
                length_N -= 1
                if N[i+2] == "d":
                    i += 1
                    length_N -= 1
            elif N[i+1] == "s" or N[i+1] == "c":
                i += 1
                length_N -= 1
                        
            
        elif N[i] == "j":
            if N[i+1] == "l" or N[i+1] == "n":
                i += 1
                length_N -= 1
                
        elif N[i] == "-":
            i += 1
            length_N -= 1
    # except:
    #     continue
    

print(length_N)