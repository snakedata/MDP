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
           
