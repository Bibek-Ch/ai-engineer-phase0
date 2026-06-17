#given
p_s = 0.01
p_free_given_s = 0.8
p_free_given_not_s = 0.2

#probability of not spam
p_not_s = 1 - p_s

#calculate the probability of word free
p_free = p_free_given_s * p_s + p_free_given_not_s * p_not_s

#applying bayes theorem

p_s_given_free = (p_free_given_s * p_s)/p_free


print(f"probability of spam if word free is present(p(S|f)) is {p_s_given_free: .3f}")