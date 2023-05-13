def get(lines:list):    
    final = []

    for line in lines:
        split = line.replace(':','-')
        split = split.split('-')
        final.append(split)
    return final

def createtxt(states:list):
    actions=[0,1]   ###ELIMInate athe  end if neccesary
    proboff=[70,10,20]
    probon=[50,20,20,10]
    state2=[-1,0,1,2]
    f = open("newfile.txt", "w+")
    for i in states:     ##For loop to write the operations involving the thermostat off
        for p in range(0,3):
            f.write("state"+str(states[i])+"-0-"+"state"+str(states[i]-state2[p])+":"+str(proboff[p]))
            f.write("\n")
    f.write("state16-0-state16:90\n")                ##state16=16ºC state17=24.5ºC state18=25ºC
    f.write("state16-0-state0:10\n")
    f.write("state17-0-state17:20\n")
    f.write("state17-0-state15:70\n")
    f.write("state17-0-state18:10\n")
    f.write("state18-0-state18:30\n")
    f.write("state18-0-state17:70\n")
    for i in states:     ##For loop to write the operations involving the thermostat on
        for p in range(0,4):
            f.write("state"+str(states[i])+"-1-"+"state"+str(states[i]-state2[p])+":"+str(probon[p]))
            f.write("\n")
    f.write("state15-1-state15:30\n")
    f.write("state15-1-state0:50\n")
    f.write("state15-1-state1:20\n")
    f.write("state17-1-state17:20\n")
    f.write("state17-1-state18:70\n")
    f.write("state17-1-state15:10\n")
    f.write("state18-1-state18:90\n")
    f.write("state18-1-state17:10\n")