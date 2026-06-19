import numpy as np
import matplotlib.pyplot as plt


# generate highly skewed population(exponential distribution)
population = np.random.exponential(scale= 2, size = 100000)

#take 1000 samples of size 30 and their means
sample_mean = [np.mean(np.random.choice(population, size = 30)) for _ in range(1000)]


#plot histogram
plt.hist(sample_mean, bins=30, edgecolor= 'black')
plt.title('Distribution of sample mean of size 30 from skewed population', loc='center')
plt.axvline(np.mean(population), color = 'red', label = 'population mean')
plt.legend()
plt.show()