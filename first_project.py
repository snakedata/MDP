import re 
    
def parse(file: str)-> str:

    """Given a file it returns any strings that match the format given
    """
    lines  = []
    i = 0
    with open(file) as stream:
        for line in stream:
            m=re.match(r'^\w+-\w+-\w+:[0-9]+$',line)
            if m!=None:
                print("There is a match\n")
                print(line)
                lines.append(line)
                i += 1
                
            else:
                print("This line does not follow the pattern")   
    return lines                 

def minimum(l:list):
    return l.index(min(l))

def duplicates(l:list):
    return list(set(l))

def Bellman_Equation(costs:list,probabilities:list):
    """Computing the bellman equations for each state

    Vi+1(StateX) = min(cost(policy1)+P1(StateX|StateX)Vi(StateX)+P1(StateY|StateX)Vi(StateY)+P1(StateZ|StateX)Vi(StateZ),
                       cost(policy2)+P2(StateX|StateX)Vi(StateX)+P2(StateY|StateX)Vi(StateY)+P2(StateZ|StateX)Vi(StateZ))
    """
    #The organization of the lists costs and probabilities has to be very specific
    #                   State 1        State2          State3        State 1        State2          State3       State 1        State2          State3   
    #Probabilies:   [[[0.5,0.2,0.3],[0.1,0.0,0.3],[0.2,0.2,0.4]],[[0.3,0.1,0.2],[0.2,0.0,0.1],[0.4,0.3,0.2]],[[0.1,0.3,0.3],[0.1,0.0,0.3],[0.3,0.2,0.5]]]
    #                               Policy 1                                        Policy 2                                Policy 3
    #Costs:         [1,1,1]
    # Policy1,Policy2,Policy3
    Vi = [1]*len(probabilities)         
    #create a list of lenght of policies
    sum = [0]*len(costs)
    min_sum = 0
    cond = True
    while cond:
        #length of costs tells us the amount of policies
        for v in range(len(Vi)):
            for i in range(len(costs)):
                sum[i]  += costs(i)
                for policy in range(len(probabilities[i])):
                    for state in range(len(probabilities[i][policy])):
                        sum[i] += probabilities[i][policy][state]*Vi(state)
            min_sum = minimum(sum)
            if (min_sum -Vi[v])<0.5:
                cond = False
            Vi[v]=minimum(sum)
            sum = 0
    return Vi       


    
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
    f.write("State16-0-State16:90\n")                ##State16=16ºC State17=24.5ºC State18=25ºC
    f.write("State16-0-State0:10\n")
    f.write("State17-0-State17:20\n")
    f.write("State17-0-State15:70\n")
    f.write("State17-0-State18:10\n")
    f.write("State18-0-State18:30\n")
    f.write("State18-0-State17:70\n")
    for i in states:     ##For loop to write the operations involving the thermostat on
        for p in range(0,4):
            f.write("state"+str(states[i])+"-1-"+"state"+str(states[i]-state2[p])+":"+str(probon[p]))
            f.write("\n")
    f.write("State15-1-State15:30\n")
    f.write("State15-1-State0:50\n")
    f.write("State15-1-State1:20\n")
    f.write("State17-1-State17:20\n")
    f.write("State17-1-State18:70\n")
    f.write("State17-1-State15:10\n")
    f.write("State18-1-State18:90\n")
    f.write("State18-1-State17:10\n")

def create_matrix(lines:list):
    counter = 0
    
    matrix = [[0]*(len(lines)+1) for _ in range(len(lines)+1)]
    
    policies = []
    states = []
    for policy in range(lines):
        policies.append(lines[policy][1])
    policies = duplicates(policies)
    policies = sorted(policies)    
    for i in range(lines):
        states.append(lines[i][0])
        states.append(lines[i][2])
    states = duplicates(states)
    states = sorted(states)
    for i in range(lines):
        position_policy = policies.index(lines[i][1])
        position_state1 = states.index(lines[i][0])
        position_state2 = states.index(lines[i][2])
        matrix[position_policy][position_state1][position_state2] = lines[i][3]
    return matrix


lines =  parse("input.txt")
separated_lines = get(lines)
matrix = create_matrix(separated_lines)
Bellman_Equation(matrix)
