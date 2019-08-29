* Bayes Theroem
    - P(X|Y) = [P(Y|X) P(X)] / [[P(Y|X)P(X)] + [P(Y|!X)P(!X)]]

* Strength of Bayes Theorem:

    - can use simplisitic probabilities to calculate non simplistic probs.
    If I want to know the prob that P(S | V) where
        S = email is spam
        V = email contains word Viagra
    Then you really only need collections of spam and not spam data to do your
    calculate (or draw stats needed to perform said calculation)

* Big Assumption of NAIVE Bayes

    - P(X_i | Y), each X_i is independant of each other. Rigoursly,
    P(X_1=x_1, ... X_n=x_n | Y) = P(X_1=x_1 | Y) * ... * P(X_n=x_n | Y)

* Big Assumption of NAIVE Bayes let's us

    - for each P(X_i|Y), we can calculate the equivalent right hand side of Bayes theorem independently and just multiply

* Underflow

    - refers to the idea that computers have a tough time working with floating point numbers very close to zero (they lose accuracy).

* working with large products of probs but avoiding underflow:

    - exp(log(P_1) + log(P_2) + log(P_3) + ... log(P_n))

* Smoothing constant K for Naive Bayes

    - handles case where having zero instances in your bayes training data causes you to multiply a zero and screw up ur model

    P(X_i | S) = (k + data meeting X_i in S) / (2k + number of data meeting S)

<!-- ON PAGE 239 -->
