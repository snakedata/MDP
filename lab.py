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
class Action:
    """This class contains the information about actions between states
    """
    def __init__(self, name:str, prob: float):
        """Any action is identified by a name which is a string. The probability of that action is used in the MDP computation 

        Args:
            name (str): identifier of the action
            prob (float): probability of the action """
        self.name = name
        self.prob =prob
        
class Transition:
    """This class contains the information about actions between states
    """
    def __init__(self, from_state: State, action: Action, to_state: State):
        """Any action is identified by a name which is a string. The probability of that action is used in the MDP computation 

        Args:
            name (str): identifier of the action
            prob (float): probability of the action """
        self.from_state = from_state
        self.action = action
        self.to_state = to_state

class Transitions:
    """Container of transitions
    """
    def __init__(self):
        pass
    
    def __iadd__(self, other:Action):
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
    

   
def compute():
    """Compute the data
    """

def get(lines:list):    
    for line in lines:
        split_line1 = line.split('-')
        split_line2 = line.split(':')
        split_line1[2] = split_line2[1] 
        print(split_line1)
        
            
            
            
    
lines =  parse("input.txt")
separated_lines = get(lines)