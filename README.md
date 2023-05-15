# MDP

A Markov decision process (MDP), by definition, is a sequential decision problem for a fully observable, stochastic environment with a Markovian transition model and additive rewards. It consists of a set of states, a set of actions, a transition model, and a reward function. 

A solution to a MDP is called a policy π(s). It specifies an action for each state s. In a MDP, we aim to find the optimal policy that gives the highest expected utility.

Markov decision process solver.
This project uses Markov decision process to model an optimal policy, creating Bellman equations and doing value iteration to achieve the optimal policy.

First of all, we create a file with the transitions, actions and probabilities of each transition, using the function createtxt which takes as inputs a list of states another of actions and creates the file.
In our implementation we had most of the states that had the same format regarding the relations between states, actions and probabilities, and then 3 of them which were "unique" and we had to write them by hand, but feel free to change that to match your specific problem.

Then we read that file with regular expressions looking for the lines that follow our desired pattern->"State1-Action-State2:Probability" If the line matches that expression we store it in a list and if not we just ignore it, after reading all the file, we use the function duplicates to eliminate any possible line that was repeated and we sort the list. After that, we separate the lines with the function "get" meaning that we have a list with the following format-> [init_state, action, end_state, prob, init_state2, action2, end_state2, prob2 .....] 

Following that step, we use the "create_matrix" function that creates the CPT's for the actions of the MDP. The function works the following way, the traversal from any state to another considers an action which has a determined probability. Each line is converted to a position inside of a probability matrix. Probability matrices are organized based on the action. For example; a line, state0-1-state1:70 would be interpreted as going from state0 to state1 with action 1, probability of 0.7. This would then be introduced into the matrix which contains the probabilities of states with action 1 and would take the position 0,1. This is given that state0 is the first of the states and state 1 is the second. Therefore, each probability matrix contains a list of each individual state which contains the probability of going from that state to any other. An example could be the probabilities of state0: [0,0.7,0.2,0.1]. Therefore through this method we can utilize minimum resources by creating structures. 

After that, we use the CPT's as inputs for the function "Bellman_Equation" which creates the Bellmans equations and does value iteration, we have set the function to keep iterating until the difference between the previously computed value and the actual value is less than 0.5 The equations have the following format 

![image](https://github.com/snakedata/MDP/assets/115793176/4bcb91a9-6c81-48fe-bbfa-b6b99fc82388)


To finish it up, we print on screen the optimal policy. Which is defined by:

![image](https://github.com/snakedata/MDP/assets/115793176/ddd99308-5458-493c-9f04-1a148f7da6bc)


Reference

Stuart Russell and Peter Norvig. Artificial Intelligence: A Modern Approach (3rd ed.).
