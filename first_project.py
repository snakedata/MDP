import re
import random
class MDPStat:
    """This object represents information about MDP states, identified by a unique name
    """
#I need also a repressentation of actions. Actions are indentified by a name and a probability which shall be represneted as a floating-point number between 0 and 1
class MDPAction:
    """This object represents information about MDP actions, identified by a unique name and probability
    """
    def __init__(self, id: str, prob: float):
        """Any action is uniquely identified by a string. The probability is used in the MDP computation 

        Args:
            id (str): _description_
            prob (float): _description_
        """
class MDPTransition:
    """Definition of MDP Transition
    """
    def __init__(self, from_state: MDPStat, action: MDPAction, to_state: MDPStat):
        """A transition is defined by a starting state, an action and a destination state

        Args:
            from_state (MDPState): _description_
            action (MDPAction): _description_
            to_state (MDPState): _description_
        """
class MDPTransitions:
    """Definition of a container MDP Transition
    """
    def __init__(self):
        """A container of transitions is a list of transitions 
        """
    
    def __iadd__(self, other:MDPAction):
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
        
#I need also to keep a separate list of transitions:First ,define a single transition

def parse(file: str)-> str:

    """Given a file it returns any strings that match the format given
    """
    
    with open("file.txt") as stream:
        for line in stream:
            m=re.match(r'^\w+-\w+-\w+:[0-9]+$',string)
            if m!=None:
                print("There is a match\n")
                print(m)
            else:
                print("This line does not follow the pattern")   
                 
            iline += 1

         
def Bellman_Equation():
    """Computing the bellman equations 
    """

   
def compute():
    """Compute the data
    """

        
def get(): 
    print("")
    regexp = r'\d.\d+'
    if m := re.match(r'?P<inital_state>[a-z]+)\s*-\s*(?P<action>[a-z]+):\s*(?<prob>\d)')