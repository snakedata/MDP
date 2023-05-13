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

def Bellman_Equation():
    """Computing the bellman equations 
    """
    
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

        line.replace('-',':')
        split = line.split('-')
        print(split)
        final.append(split)
    return final
    
def create_matrix(lines:list):
    counter = 0

    matrix = [[0]*len(lines) for _ in range(len(lines))]
    print(matrix)

    for i in lines:
        matrix[counter] = lines[0]
        matrix[0][counter] = lines[1]
        matrix[counter][counter] = lines[2]
    return matrix


        


            
            
            
    
lines =  parse("input.txt")
separated_lines = get(lines)
matrix = create_matrix(separated_lines)
print(matrix)
