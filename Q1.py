import time
list = [" "]
state = 1
pointer = 0
step = 0
start_time = time.time()
while(state != "accept"):
    if(state == 1):
        if(list[pointer] == " "):
            list[pointer] = "1"
            if(pointer == 0):
                list.insert(0," ")
            else:
                pointer-=1
            state = 2
        elif(list[pointer] == "1"):
            list[pointer] = "1"
            if(pointer == len(list)-1):
                list.append(" ")
            pointer+=1
            state = 3
    elif(state == 2):
        if(list[pointer] == " "):
            list[pointer] = "1"
            if(pointer == 0):
                list.insert(0," ")
            else:
                pointer-=1
            state = 3
        elif(list[pointer] == "1"):
            list[pointer] = "1"
            if(pointer == 0):
                list.insert(0," ")
            else:
                pointer-=1
            state = 2
    elif(state == 3):
        if(list[pointer] == " "):
            list[pointer] = "1"
            if(pointer == 0):
                list.insert(0," ")
            else:
                pointer-=1
            state = 4
        elif(list[pointer] == "1"):
            list[pointer] = " "
            if(pointer == len(list)-1):
                list.append(" ")
            pointer+=1
            state = 5
    elif(state == 4):
        if(list[pointer] == " "):
            list[pointer] = "1"
            if(pointer == len(list)-1):
                list.append(" ")
            pointer+=1
            state = 1
        elif(list[pointer] == "1"):
            list[pointer] = "1"
            if(pointer == len(list)-1):
                list.append(" ")
            pointer+=1
            state = 4
    elif(state == 5):
        if(list[pointer] == " "):
            state = "accept"
        elif(list[pointer] == "1"):
            list[pointer] = " "
            if(pointer == len(list)-1):
                list.insert(len(list)," ")
            pointer+=1
            state = 1
    else:
        break
    step+=1
print("--- %s seconds ---" % (time.time() - start_time))
print("guess u didn't expect that I STOPED at ",step,"th step 😈 !!!!")
