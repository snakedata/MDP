import re 
import file_reader
    
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
def create_list_of(n:int,l:int):
    return [n]*l

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

           
    #create a list of lenght of policies of sums and policies
    
    Vi = create_list_of(1,len(probabilities[0])) 
    sum = create_list_of(0,len(probabilities)) 
    
  
    min_sum = 0
    cond = True

    while cond:
        #length of costs tells us the amount of policies
        for policy in range(len(probabilities)):
            sum[policy] = sum[policy]+ costs[policy]
            for state in range(len(probabilities[policy])):
                for probability in range(len(probabilities[policy][state])):
                    print("policy",policy)
                    print("state",state)
                    print("probability",probability)
                    sum[policy] += probabilities[policy][state][probability]*Vi[state]
                    print(sum)
            min_sum = minimum(sum)
            if (min_sum -Vi[policy])<0.5:
                cond = False
            
            Vi[policy]=minimum(sum)
            
    return Vi       


    


def create_matrix(lines:list):
    counter = 0
    policies = []
    states = []
   
    for policy in range(len(lines)):
        policies.append(lines[policy][1])
    policies = duplicates(policies)
    policies = sorted(policies)  
     
    for i in range(len(lines)):
        states.append(lines[i][0])
        states.append(lines[i][2])
    states = duplicates(states)
    states = sorted(states) 
    
    tmatrix = [0]*(len(policies))
    smatrix = [[0]*(len(states)) for _ in range(len(states))]
    for i in range(len(policies)):
        tmatrix[i] = smatrix

   
    for i in range(len(lines)):
        position_policy = policies.index(lines[i][1])
        position_state1 = states.index(lines[i][0])
        position_state2 = states.index(lines[i][2])
        tmatrix[position_policy][position_state1][position_state2] = int(lines[i][3])/100
    
    return tmatrix

state_input = []
for i in range(15):
    state_input.append(i)
file_reader.createtxt(state_input)
lines =  parse("newfile.txt")
separated_lines = file_reader.get(lines)
matrix = create_matrix(separated_lines)

v = Bellman_Equation(create_list_of(10,len(matrix[0])),matrix)
print(v)
