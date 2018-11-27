choice = 0
message = ""

while choice != 3: # en while loop som går tills choice 3
    print("Välkomen till loggboken.")
    print("1. Läs loggar")
    print("2. Skriv en logg")
    print("3. Avsluta")
    choice = int(input())

    if choice == 1: # om choice 1 så öppnas så gör detta 
        f = open('log.txt', 'r') # öppnar log.txt i read only
        for line in f: # printar alla rader 
            print(line)
        f.close()

    elif choice == 2: # om choice 2 
        f = open('log.txt', 'a+') # öppnar log.txt i append + läge 
        message = input("Skriv din nya rad: ") # skriv din kommentar 
        f.write("\n" + message)
        f.close()

    else: # lades till för kosmetisk effekt 
        print("          | ") 
        print("　　　　　| ")
        print("　　　　　| ")
        print("　　　　　| ")
        print("　　　　　| ")
        print("　　　　　| ") 
        print("　　　　　| ")
        print("　／￣￣＼| ")
        print("＜ ´･ 　　|＼ ")
        print("　|　３　 | 丶＼ - ")
        print("＜ 、･　　|　　＼ ")
        print("　＼＿＿／∪ _ ∪) ")
        print("　　　　　 Ｕ Ｕ")