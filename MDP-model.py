import re 
import file_reader


def parse(file: str)-> list:
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

def equate_lists(li:list)->list:
    """returns an object that contains every position of the list introduced
    """
    obj = create_list_of(1,len(li))
    for i in range(len(li)):
        obj[i] = li[i]
    return obj

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


def Bellman_Equation(costs:list,probabilities:list)-> list:
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
    #create a list which contains a list in each position of length states
    Vi = [create_list_of(1,len(probabilities[0][0])) for _ in range(2)] 
    #intial termometer at state 22 degrees is 0
    Vi[0][11] = 0
    #costs of each action is equivalent for now to the inital costs
    sum = create_list_of(1,len(probabilities))
    sum = equate_lists(costs)
    iter = 50
    
    min_sum = 0 
    cond = True
    
    for v in range(iter):
        #iterate through he number of states
        for state in range(len(probabilities[0])):    
            #iterate through the number of actions
            for action in range(len(probabilities)):
                #iterate through the number of probabilities from going from state: state to any other state
                for probability in range(len(probabilities[action][state])):
                    #for state find the optimal action each iteration which will be the mimunm of that the sum of the cost of each action of each state
                    sum[action] += probabilities[action][state][probability]*Vi[0][probability]
                min_sum = min(sum)
            #replace Vi+1 with min_sum
            Vi[1][state]=min_sum
            Vi[0] = equate_lists(Vi[1])
            #ensure that position 11 of state 22 degrees is 0
            Vi[1][11] = 0  
            Vi[0][11] = 0
            sum = equate_lists(costs)
    return Vi[1]       

def optimal_policy(Vi:list,probabilities:list,costs:list)->str:
    optimal_policy= create_list_of(0,len(Vi))      
    """for action in range(len(probabilities[0])):
        for i in range (len(costs)):
            for probability in range(len(probabilities[action][state])):
                sum[i]= costs[i]+probabilities[action][state][probability]*Vi[1][probability]"""
    sum = equate_lists(costs)
    for state in range(len(probabilities[0])):    
            #iterate through the number of actions
        for action in range(len(probabilities)):
                #iterate through the number of probabilities from going from state: state to any other state
            for probability in range(len(probabilities[action][state])):
                    sum[action] += probabilities[action][state][probability]*Vi[probability]
                    print(sum)
        print("State:",state)

        if sum[0]<sum[1]:
            optimal_policy[state]="OFF"
        else:
            optimal_policy[state]="ON"
        sum = create_list_of(1,2)
    print(optimal_policy)
    return Vi, optimal_policy    
    


def create_matrix(lines:list)-> list:
    """
    Creates a matrix of the following format:
                        State 1        State2          State3        State 1        State2          State3       State 1        State2          State3   
    Probabilies:   [[[0.5,0.2,0.3],[0.1,0.0,0.3],[0.2,0.2,0.4]],[[0.3,0.1,0.2],[0.2,0.0,0.1],[0.4,0.3,0.2]],[[0.1,0.3,0.3],[0.1,0.0,0.3],[0.3,0.2,0.5]]]
                                   action 1                                        action 2                                action 3
    
    Actions, states and probabilities are read from the split lines introduced.
    To go from state1 to state2 with action 1 would be matrix[action1][state1][state2]
    """
    actions = []
    states = []
   #Take each split line and append froma and to states to list states and action to list actions
    for i in range(len(lines)):
        actions.append(lines[i][1])
        states.append(lines[i][0])
        states.append(lines[i][2])
    #Remove duplicates and sort lexicographically   
    states = duplicates(states)
    states = sorted(states) 
    actions = duplicates(actions)
    actions = sorted(actions)  
    
    
    #Create the probability matrix of dimensions len(actions)*len(states)*len(states):
    #We create a list of 0's of size len(states) iterated over size len(states) positions and over the number of actions
    tmatrix = [[[0]*(len(states)) for _ in range(len(states))] for _ in range(len(actions))]


    
    for i in range(len(lines)):
        #Since actions and states have been sorted we can obtain the position we want in the matrix using indices
        position_action = actions.index(lines[i][1])
        position_state1 = states.index(lines[i][0])
        position_state2 = states.index(lines[i][2])
        

        #Move probability to corresponding position State1 - Action -> State2 
        probability = int(lines[i][3])/100
        tmatrix[position_action][position_state1][position_state2] = probability
       
    
    return tmatrix
state_input = []

for i in range(16):
    state_input.append(i)
   
file_reader.createtxt(state_input,[0,1])
lines =  parse("newfile.txt")
separated_lines = get(lines)

matrix = create_matrix(separated_lines)
v = Bellman_Equation([1,2],matrix)

#Mapping function:
print("INITIAL STATE:16ºC\t\t GOAL STATE:22ºC\n")
print("Value function after doing the Bellman equations:")
i=16
n=0
while n<=18:
    print("State" +str(i)+" : "+str(v[0][n]))
    i=i+0.5
    n=n+1
i=16
n=0
print("\nOptimal policy for each state is:")
while n<=18:
    print("State" +str(i)+" : "+str(v[1][n]))
    i=i+0.5
    n=n+1
