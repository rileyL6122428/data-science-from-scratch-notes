with two events E and F, 

if knowing something about E implies certain outcomes for F
    then F depends on E
else
    F is independant of E

Mathemtically, independence is written as

P(E, F) = P(E)P(F)
    probability E and F occur equals product of probs that either event occurs

Conditional probability
    P(E | F) = P(E, F) / P(F) OR
    P(E, F) = P(E | F) P(F)

If E independent of F, show that P(E | F) = P(E)
    P(E, F) = P(E | F) P(F)
    P(E)P(F) = P(E | F) P(F)
    P(E) = P(E | F)

Problem: For E, F, 
    prove if P(E | F) != 0 and P(E | !F) = 0, 
        then E is a subset of F
    assume P(E | F) != 0, P(E | !F) = 0, E is not a subset of F. 
        if E is not a subset of F, then some prob  of E lies outside of F, OR
        P(E | !F) != 0, which is a contradiction

Problem: Show If E is a subset of F, then P(E, F) = P(E)
    P(E, F) = P(E) Intersection P(F)
            = P(E), since P(E) is a subset of P(F) (by set theory thereoms)

Problem: Family has two kids unknown gender, equal prob of boy or girl
E = both kids girls
F = older kid is girl = 0.5
what is P(E | F)?

    P(F) = 0.5
    P(E, F) = 0.25 (from examination of venn diagram intersection)
    P(E | F) = P(E, F) / P(F)
             = 0.25 / 0.5
             = 0.5
    
Problem: Family has two kids unknown gender, equal prob of boy or girl
E = both kids girls
L = at least one is a girl
what is P(E | L)?
    P(E) = 0.25
    P(L) = 0.75
    P(E | L) = P(E,L) / P(L)
             = P(E) / P(L)
             = (1/4) / (3/4)
             = 1/3

 Bayes Theorem derivation:
    
    P(E|F) = P(E, F) / P(F)
           = P(F|E) P(E)/ P(F)
           = P(F|E) P(E) / [P(F|E)P(E) + P(F|!E)P(!E)]

Usefulness of Bayes Theorem:
    can calculate the probability that E Occurs Given F with knowledge of
    F|E, F|!E, E, 

A Random Variable -> A variable whose possible values have an associated prob
distribution.

Expected Value of a random variable -> average of prob weights * quantified outcomes

* Continuous prob distributions modeled with

    - pdf -> Probability Density Function

* CDF
    - cumulative distribution function, prob that and random variable is
        less than or equal to a certain value

formula for normal distribution:
    s = sigma = standard dev
    f(x|µ,s) = [1/((2pi)^(.5)s)][exp(-(x-µ)^2/(2(s^2)))]

when µ is 0 and s = 1, then we have the "standard normal distribution"

Turns out that if Z is a standard normal random variable, then
X = sZ + µ is also normal random variable with mean µ and std_dev s.

* Central Limit Theorem

    - in essence, a random variable defined as the average of independant and
      identically distributed random variables is itself approximately normally
      distributed.
      Also, if x_1, x_2, ... x_n are random vars with mean µ and std_dev 
      sigma / root(n), then
      ((x_1 + ... + x_n) - µn) / (sigma * root(n)) is approximately normally distributed with mean 0 and std_dev 1
      
