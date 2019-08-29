# For our coin, let's say we assume a prior distribution on p.
# Maybe we don't want to take a stand on whether the coin is fair
#   We choose alpha and beta to both equal 50
# Maybe we have a strong belief that it lands head 55% of the time
#   We choose alpha to equal 55 and beta equals 45

# Then we flip our coin a bunch of times and see h heads and t tails
# Bayes Theorem tells us that the posterior distribution for p is again
# a beta distribution but with parameters alpha + h and beta + t.

# Bayesian inference lets us make statements about hypothesis

# Using Bayesian inference to test hypothesis is considered somewhat 
# controversial, in part because of subj nature of choosing a prior
# and because of its complicated derivation.
