def add_zeros(elem:str)->str:
    """Adds zeroes to the name of the states so instead of being state0 it is state00 state1 is state01 and so on  
    """""
    return str(elem).rjust(2, '0')
def createtxt(states:list, actions:list)->None:
    """"Creates a text file with the format State1-Action-State2:Probability
    """""
    proboff=[70,20,10]
    probon=[10,20,50,20]
    state2=[-1,0,1,2]
    f = open("newfile.txt", "w+")
    for i in range(1,len(states)):     ##For loop to write the operations involving the thermostat off
        for p in range(0,3):
            f.write("state"+add_zeros(str(states[i]))+"-"+str(actions[0])+"-"+"state"+add_zeros(str(int(states[i])+int(state2[p])))+":"+str(proboff[p]))
            f.write("\n")
    f.write("state00-0-state00:90\n")                
    f.write("state00-0-state01:10\n")                   ##state00=16ºC state16= 24ºC state17=24.5ºC state18=25ºC
    f.write("state17-0-state17:20\n")
    f.write("state17-0-state16:70\n")               ##Manually writing the operations that are exceptions
    f.write("state17-0-state18:10\n")
    f.write("state18-0-state18:30\n")
    f.write("state18-0-state17:70\n")
    for i in range(1,len(states)):    ##For loop to write the operations involving the thermostat on
        for p in range(0,4):
            f.write("state"+add_zeros(str(states[i]))+"-"+str(actions[1])+"-"+"state"+add_zeros(str(int(states[i])+int(state2[p])))+":"+str(probon[p]))
            f.write("\n")
    f.write("state00-1-state00:30\n")
    f.write("state00-1-state01:50\n")
    f.write("state00-1-state02:20\n")
    f.write("state17-1-state17:20\n")
    f.write("state17-1-state18:70\n")           ##Manually writing the operations that are exceptions
    f.write("state17-1-state16:10\n")
    f.write("state18-1-state18:90\n")
    f.write("state18-1-state17:10\n")
 
