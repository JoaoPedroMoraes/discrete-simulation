#Aula 13/06
import scipy.stats as st
import matplotlib.pyplot as plt
import math as m

l = st.uniform.rvs(size=2000, loc=75)

k = round(3.3 * m.log10(2000))

plt.hist(l,bins=k)
plt.show()
