flag = True
moves = 0
lifes = 3
direction = ""
correctCombination = "SSNWES"
while flag:
    prompt = "Which way do you want to go? (N, S , W, E )"
    election = input(prompt)
    if election != "N" or election!= "S" or election!= "W" or election!= "E":
        print("Invalid input, please type N, W, E or S")
        moves += 1
        break
    if election == "N" or election == "S" or election =="W" or election == "E":

        if(election.__contains__(correctCombination)):
            direction = direction + election
            print("Good choice, you are now one step closer!")
            moves +=1
            break
        else:
            print("Try again")
            moves+=1

    if moves%10==0:
        lifes -= 1
        if lifes ==0:
            ("Game Over, you lost all your lifes")
            flag = False
            continue
    if election == correctCombination:
        print ("GG")





