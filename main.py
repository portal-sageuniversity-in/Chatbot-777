import random

arr = [" " for _ in range(9)]
    
def print_box(arr):
    print(f"{arr[0]} | {arr[1]} | {arr[2]} ")
    print(f"--|---|--")
    print(f"{arr[3]} | {arr[4]} | {arr[5]} ")
    print(f"--|---|--")
    print(f"{arr[6]} | {arr[7]} | {arr[8]} ")
    
def check_winner(player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if arr[win[0]] == arr[win[1]] == arr[win[2]] == player:
            print(f"{player}, is win Congrulation!")
            return True
    return False
            
print_box(arr) 
chance = 0 
for i in range(5):
    print("X,s Turn")
    try:
        pos = int(input("Enter a Number between (0 to 8) :- "))
        if arr[pos] == " ":
            arr[pos] = "X"
            chance+=1
            print_box(arr)
            if check_winner("X"):
                break
    except:
        print("Invalid Input")
    
    print("O,s Turn")
    pos = int(random.randint(0,8))
    if arr[pos] == " ":
        arr[pos] = "O"
        chance+=1
        print_box(arr)
        if check_winner("O"):
            break
    
if chance == 9:
    print("Game Draw!")


    