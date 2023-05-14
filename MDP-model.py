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


def Bellman_Equation(costs:list,probabilities:list):
    """Computing the bellman equations for each state
    Vi+1(StateX) = min(cost(action1)+P1(StateX|StateX)Vi(StateX)+P1(StateY|StateX)Vi(StateY)+P1(StateZ|StateX)Vi(StateZ),
                       cost(action2)+P2(StateX|StateX)Vi(StateX)+P2(StateY|StateX)Vi(StateY)+P2(StateZ|StateX)Vi(StateZ))
    The organization of the lists costs and probabilities has to be very specific
                       State 1        State2          State3        State 1        State2          State3       State 1        State2          State3   
    Probabilies:   [[[0.5,0.2,0.3],[0.1,0.0,0.3],[0.2,0.2,0.4]],[[0.3,0.1,0.2],[0.2,0.0,0.1],[0.4,0.3,0.2]],[[0.1,0.3,0.3],[0.1,0.0,0.3],[0.3,0.2,0.5]]]
                                   action 1                                        action 2                                action 3
    Costs:         [1,1,1]
    action1,action2,action3

           
    Create a list of lenght of actions of sums and actions
    """
    
    Vi = create_list_of(1,len(probabilities[0][0])) 
    Vi[2] = 0
    #costs of each action is equivalent for now to the inital costs
    sum = costs
    iter = 10
    
    min_sum = 0
    cond = True
    
    for v in range(iter):
        #iterate through he number of states
        for state in range(len(probabilities[0])):    
            #iterate through the number of actions
            for action in range(len(probabilities)):
                print(probabilities[action][state])
                #iterate through the number of probabilities from going from state: state to any other state
                for probability in range(len(probabilities[action][state])):
                    #for state find the optimal action each iteration which will be the mimunm of that the sum of the cost of each action of each state
                    sum[action] += probabilities[action][state][probability]*Vi[probability]
                    print(sum)

                
            print(Vi)
            print(sum)
            min_sum = min(sum)
            Vi[state]=min_sum
            sum =create_list_of(1,2)
            if (min_sum -Vi[action])<0.1:
                cond = False 
    return Vi       


    


def create_matrix(lines:list):
    
    actions = []
    states = []
   
    for action in range(len(lines)):
        actions.append(lines[action][1])
    actions = duplicates(actions)
    actions = sorted(actions)  
     
    for i in range(len(lines)):
        states.append(lines[i][0])
        states.append(lines[i][2])
    states = duplicates(states)
    states = sorted(states) 
    
    
    smatrix1 = [[0]*(len(states)) for _ in range(len(states))]
    smatrix2 = [[0]*(len(states)) for _ in range(len(states))]
    tmatrix = create_list_of(1,2)
     
    
    for i in range(len(lines)):
        position_action = actions.index(lines[i][1])
        position_state1 = states.index(lines[i][0])
        position_state2 = states.index(lines[i][2])
        

        
        probability = int(lines[i][3])/100
        if position_action == 0:
            smatrix1[position_state1][position_state2] = probability
        elif position_action == 1:
            smatrix2[position_state1][position_state2] = probability
    
    tmatrix[0] = smatrix1
    tmatrix[1] = smatrix2
        

    return tmatrix

state_input = []
for i in range(15):
    state_input.append(i)

file_reader.createtxt(state_input,[0,1])
lines =  parse("newfile.txt")
separated_lines = file_reader.get(lines)

matrix = create_matrix(separated_lines)
v = Bellman_Equation([1,1],matrix)

print(matrix)
