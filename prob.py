import scipy.stats as stats 

prob = 1 - stats.binom.cdf(6,10,0.5)

print("the probability of getting more than 6 in 10 coins is :", prob)