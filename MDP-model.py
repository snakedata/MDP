import re 
import file_reader
    
def parse(file: str)-> str:
    """Given a file it returns any strings that match the format given
    """
    lines  = []
    with open(file) as stream:
        for line in stream:
            m=re.match(r'^\w+-\w+-\w+:[0-9]+$',line)     ##If the line follows this format "string-string-string:any two digit number" is appended to the list
            if m!=None:
                lines.append(line)
            else:
                print("This line does not follow the desired format")   
    return lines                 
def get(lines:list)->list: 
    """Given a list it separates each element of the list if 
    """
    final = []
    for line in lines:
        split = line.replace(':','-')
        split = split.split('-')
        final.append(split)
    return final    
def minimum(l:list)->int:
    """returns the minimum element of the list
    """
    return l.index(min(l))

def duplicates(l:list)->list:
    """returns the list without any duplicates
    """
    return list(set(l))
def create_list_of(n:int,l:int)->list:
    """creates a list size l with every value equal to n
    """
    return [n]*l

def Bellman_Equation(costs:list,probabilities:list)->list:
    """Computing the bellman equations for each state
    Vi+1(StateX) = min(cost(policy1)+P1(StateX|StateX)Vi(StateX)+P1(StateY|StateX)Vi(StateY)+P1(StateZ|StateX)Vi(StateZ),
                       cost(policy2)+P2(StateX|StateX)Vi(StateX)+P2(StateY|StateX)Vi(StateY)+P2(StateZ|StateX)Vi(StateZ))
    The organization of the lists costs and probabilities has to be very specific
                       State 1        State2          State3        State 1        State2          State3       State 1        State2          State3   
    Probabilies:   [[[0.5,0.2,0.3],[0.1,0.0,0.3],[0.2,0.2,0.4]],[[0.3,0.1,0.2],[0.2,0.0,0.1],[0.4,0.3,0.2]],[[0.1,0.3,0.3],[0.1,0.0,0.3],[0.3,0.2,0.5]]]
                                   Policy 1                                        Policy 2                                Policy 3
    Costs:         [1,1,1]
    Policy1,Policy2,Policy3

           
    Create a list of lenght of policies of sums and policies
    """
    Vi = create_list_of(1,2)
    Vi = create_list_of(1,len(probabilities[0])) 
    #costs of each policy is equivalent for now to the inital costs
    sum = costs
    
    
    min_sum = 0
    cond = True

    while cond:
        #iterate through the number of policies
        for policy in range(len(probabilities)):
            #iterate through he number of states
            for state in range(len(probabilities[policy])):
                #iterate through the number of probabilities from going from state: state to any other state
                for probability in range(len(probabilities[policy][state])):
                    #for state find the optimal policy each iteration which will be the mimunm of that the sum of the cost of each policy of each state
                    sum[policy] += probabilities[policy][state][probability]*Vi[probability]
                
                min_sum = min(sum)
                
                Vi[state]=min_sum
                sum =costs
            if (min_sum -Vi[policy])<0.1:
                cond = False 
    return Vi          


    


def create_matrix(lines:list)->list:
    
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
        if position_state1 == 0:
            print("Policy:",lines[i][1],position_policy)
            print("State1:",lines[i][0],position_state1)
            print("State2:",lines[i][2],position_state2)
            print("Probability",int(lines[i][3])/100)
            print(tmatrix[0][0])
            print(tmatrix[0][0])
        tmatrix[position_policy][position_state1][position_state2] = int(lines[i][3])/100
  
    
    return tmatrix


state_input = []
for i in range(16):
    state_input.append(i)

file_reader.createtxt(state_input,[0,1])
lines =  parse("newfile.txt")
separated_lines = file_reader.get(lines)

matrix = create_matrix(separated_lines)
v = Bellman_Equation(create_list_of(1,len(matrix)),matrix)
print(v)

