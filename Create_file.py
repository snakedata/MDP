def createtxt(states:list, actions:list):
    """"Creates a text file with the format State1-Action-State2:Probability
    """""
    proboff=[70,20,10]
    probon=[10,20,50,20]
    state2=[-1,0,1,2]
    f = open("newfile.txt", "w+")
    for i in states:     ##For loop to write the operations involving the thermostat off
        for p in range(0,3):
            f.write("state"+str(states[i])+"-"+str(actions[0])+"-"+"state"+str(states[i]+state2[p])+":"+str(proboff[p]))
            f.write("\n")
    f.write("state15-0-state15:90\n")                ##state15=16ºC state16=24.5ºC state17=25ºC
    f.write("state15-0-state0:10\n")
    f.write("state16-0-state16:20\n")
    f.write("state16-0-state14:70\n")
    f.write("state16-0-state17:10\n")
    f.write("state17-0-state17:30\n")
    f.write("state17-0-state16:70\n")
    f.write("state0-0-state15:70\n")
    for i in states:     ##For loop to write the operations involving the thermostat on
        for p in range(0,4):
            f.write("state"+str(states[i])+"-"+str(actions[1])+"-"+"state"+str(states[i]+state2[p])+":"+str(probon[p]))
            f.write("\n")
    f.write("state15-1-state15:30\n")
    f.write("state15-1-state0:50\n")
    f.write("state15-1-state1:20\n")
    f.write("state16-1-state16:20\n")
    f.write("state16-1-state17:70\n")
    f.write("state16-1-state14:10\n")
    f.write("state17-1-state17:90\n")
    f.write("state17-1-state16:10\n")
    f.write("state0-1-state15:10\n")
