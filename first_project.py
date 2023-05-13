import re 

class State:
    """This class contains information about the state
    """
    def __init__(self, name:str):
        self.name = name

class States:
    """_summary_

    Returns:
        _type_: _description_
    """
    def __init__(self):
        pass
    
    def __iadd__(self, next:State):
        
        return self
    
    def __len__(self):
        """_summary_
        """
    def __iter__(self):
        """Returns 
        """
    def __next__(self):
        """
        """

class Transition:
    """This class contains the information about actions between states
    """
    def __init__(self, from_state: State, probability:int, policy:str, to_state: State):
        """Any action is identified by a name which is a string. The probability of that action is used in the MDP computation 

        Args:
            name (str): identifier of the action
            prob (float): probability of the action """
        self.from_state = from_state
        self.policy = policy
        self.to_state = to_state
        self.probability = probability
    def __getstate1__(self):
        return self.from_state
    def __getstate2__(self):
        return self.to_state
    def __getprobability__(self):
        return self.probability
    def __getpolicy__(self):
        return self.policy


class Transitions:
    """Container of transitions
    """
    def __init__(self, size,head):
        self.head = head
        self
    
   
    
    def __len__(self):
        """_summary_
        """
    def __iter__(self):
        """Returns 
        """
    def __next__(self):
        """
        """

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
            if (min_sum -Vi[v])<0:
                cond = False
            Vi[v]=minimum(sum)
            sum = 0
           


    
def optimal_policy(state):
    """compute the optimal policy
    """
    for i in range():
        pass
   
def compute():
    """Compute the data
    """

def get(lines:list):    
    final = []

    for line in lines:
        split = line.replace(':','-')
        split = split.split('-')
        final.append(split)
    return final
    
def create_matrix(lines:list):
    counter = 0

    matrix = [[0]*(len(lines)+1) for _ in range(len(lines)+1)]
    lines_states = []
    for i in range(lines):
        lines_states.append(lines[i][0])
        lines_states.append(lines[i][2])
    list_states = duplicates(list_states)
    list_states = sorted(list_states)
    for i in range(len(lines)+1): 
        if list_states
        print(counter)
        matrix[0][1] = lines[0]
        matrix[1][0] = lines[0][1]
        matrix[1][1] = lines[0][1]
        counter += 1
 
    
    return matrix


        


            
            
            
    
lines =  parse("input.txt")
separated_lines = get(lines)
matrix = create_matrix(separated_lines)
print(matrix)
