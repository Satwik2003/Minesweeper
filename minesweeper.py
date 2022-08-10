import random as rand

def GenMineMap():
    arr= list([0 for row in range(5)] for column in range(5))

    
    "Placing Bomb"

    for num in range(3):
        x = rand.randint(0,4)
        y = rand.randint(0,4)
        arr[y][x] = 'X'

        if (x >= 1 and x <= 3):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1

        if (x==0):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1

        if (x==4):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1

        if (x > 0 and x <= 4) and (y >= 1 and y <= 4):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1

        if (x >= 0 and x <= 3) and (y >= 1 and y <= 4):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1

        if (x >= 0 and x <= 4) and (y >= 1 and y <= 4):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1

        if (x >= 0 and x <= 3) and (y >= 0 and y <= 3):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1

        if (x >= 1 and x <= 4) and (y >= 0 and y <= 3):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1

        if (x >= 0 and x <= 4) and (y >= 0 and y <= 3):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1

    return arr

def GenPlayMap():
    arr = [['-' for row in range(5)] for column in range(5)]
    return arr

def CheckWon(map):
    count = 0
    for row in map:
        for cell in row:
            if cell == '-':
                count += 1
    
    if (count == 3):
        return True
    else:
        return False

def End(score):
    print("Your score: ", score)
    cont = input("Play again (y/n): ")

    if (cont == 'n'):
        print("Congratulations!")
        return False
    return True

def Display(map):
    for row in map:
        print('\t'.join(str(cell) for cell in row))
        print("")

def Game():
    GameStatus = True 

    
    while (GameStatus):
        minemap = GenMineMap()
        playmap = GenPlayMap()
        score = 0

        while True:
            if (CheckWon(playmap) == False):
                print("----Player Map----")
                Display(playmap)
                print("Enter Cell: ")
                x = int(input("Enter X co-ordinate: "))
                x -= 1
                y = int(input("Enter Y co-ordinate: "))
                y -= 1

                if (playmap[y][x] == 0 or playmap[y][x] == 1 or playmap[y][x] == 2 or playmap[y][x] == 3):
                    print("Choose another cell")
                    continue

                else:
                    if (minemap[y][x] == 'X'):
                        print("Game Over!")
                        Display(minemap)
                
                        GameStatus = End(score)
                        break
                
                    else:
                        playmap[y][x] = minemap[y][x]
                
                        score += 1
            else:
                print("Game Won")

                Display(minemap)

                GameStatus = End(score)
                break
            
if __name__ == "__main__":
    Game()
    