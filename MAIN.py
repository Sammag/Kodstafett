choice = 0
message = ""

while choice != 3:
    print("Välkomen till loggboken.")
    print("1. Läs loggar")
    print("2. Skriv en logg")
    print("3. Avsluta")
    choice = int(input())

    if choice == 1:
        f = open('log.txt', 'r')
        for line in f:
            print(line)
        f.close()

    elif choice == 2:
        f = open('log.txt', 'a+')
        message = input("Skriv din nya rad: ")
        f.write("\n" + message)
        f.close()

    else:
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