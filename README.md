# MDP

A Markov decision process (MDP), by definition, is a sequential decision problem for a fully observable, stochastic environment with a Markovian transition model and additive rewards. It consists of a set of states, a set of actions, a transition model, and a reward function. 

A solution to a MDP is called a policy π(s). It specifies an action for each state s. In a MDP, we aim to find the optimal policy that gives the highest expected utility.

Markov decision process solver.
This project uses Markov decision process to model an optimal policy, creating Bellman equations and doing value iteration to achieve the optimal policy.

First of all, we create a file with the transitions, actions and probabilities of each transition, using the function createtxt which takes as inputs a list of states another of actions and creates the file.
In our implementation we had most of the states that had the same format regarding the relations between states, actions and probabilities, and then 3 of them which were "unique" and we had to write them by hand, but feel free to change that to match your specific problem.

Then we read that file with regular expressions looking for the lines that follow our desired pattern->"State1-Action-State2:Probability" If the line matches that expression we store it in a list and if not we just ignore it, after reading all the file, we use the function duplicates to eliminate any possible line that was repeated and we sort the list.
