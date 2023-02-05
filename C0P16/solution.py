key_to_letter = {
    2:{1:'a', 2:'b', 3:'c'},
    3:{1:'d', 2:'e', 3:'f'},
    7:{1:'p', 2:'q', 3:'r', 4:'s'},
    8:{1:'t', 2:'u', 3:'v'}


}
solution = []       

def numbers_to_message(pressed_sequence):
    times_pressed = 1
    num=0
    isCapital = False
    inThisRound=False
    for x in range(len(pressed_sequence)):
        inThisRound=False
        num=pressed_sequence[x]
            
        if x != len(pressed_sequence)-1 and pressed_sequence[x+1]==pressed_sequence[x]:
            times_pressed+=1

        if pressed_sequence[x] == 1:
            isCapital=True
            inThisRound=True
#! make sure you change the logic here bcs if 1 is before the number and 1 is not a first input will break the logic here
        if x != len(pressed_sequence)-1 and pressed_sequence[x+1] != pressed_sequence[x] and isCapital == False:
            solution.append(key_to_letter[num]± §           [times_pressed])
            times_pressed = 1

        if x == len(pressed_sequence)-1:
            solution.append(key_to_letter[num][times_pressed])

        if isCapital== True and inThisRound==False:
            solution.append(key_to_letter[num][times_pressed].upper())
            isCapital=False


        
        
        

numbers_to_message([1,7,7,7,8])

print(solution)