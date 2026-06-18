p_d = 0.01
p_pos_given_d = 0.95
p_pos_given_not_d = 0.05

#probability of not death
p_not_d = 1 - p_d

#total probability of positive 
p_pos = p_pos_given_d * p_d + p_pos_given_not_d * p_not_d


# using bayes theorem to find probability desease given diagnos positive

p_d_given_pos = (p_pos_given_d * p_d)/ p_pos

print(f"p(D|+) = {p_d_given_pos:.3f}")