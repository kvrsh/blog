# That would be me
import matplotlib.pyplot as pp
x = np.linspace(-1,1,100)
for i in range(20):
    pp.plot(x, x**(i+1))
    
for i in range(20):
    pp.plot(x, -(i/10+1)**x+1)
pp.xlim(-1,1)
pp.ylim(-1,1)
pp.savefig('me.png')
