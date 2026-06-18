#given
p_s = 0.02
p_free_given_s = 0.80
p_free_given_not_s = 0.10

#total free
p_not_s = 1 - p_s
p_free = p_free_given_s * p_s + p_free_given_not_s * p_not_s

#applying bayes theorem

p_s_given_free = (p_free_given_s * p_s) / p_free


print(f"probability of spam if word free is present(p(S|f)) is {p_s_given_free: .4f}")