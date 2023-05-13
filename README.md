# MDP
Markov decision process solver.
This project uses Markov decision process to model an optimal policy, creating Bellman equations to do so.

First of all, we create a file with the transitions, actions and probabilities of each transition, using the function createtxt which takes as inputs a list of states another of actions and creates the file.
In our implementation we had most of the states that had the same format regarding the relations between states, actions and probabilities, and then 3 of them which were "unique" and we had to write them by hand, but feel free to change that to match your specific problem.

Then we read that file with regular expressions looking for the lines that follow our desired pattern->"State1-Action-State2:Probability" If the line matches that expression we store it in a list and if not we just ignore it, after reading all the file, we use the function duplicates to eliminate any possible line that was repeated and we sort the list.
