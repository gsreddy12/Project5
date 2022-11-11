print(complex(False))
print(complex(1,-0))

#String formatting in Python

# %
# {}

print("%s is having %s Years Experience in IT"%("Sateesh","15+"))
print("%s is having %d Years Experience in IT"%("Sateesh",10))

name="Sateesh"
print("Hello %s"%name)

name='python'
print('Hello {}'.format(name))

name='sateesh'
print('{} is Author of Pyhton'.format(name))
year=1989
print('{} is Author of Pyhton and developed year is {}'.format(name,year))
exp=40
print('{} is Author of Pyhton and developed year is {}, Total experience is {}'.format(name,year,exp))

print('{0} is Author of Pyhton and developed year is {1}, Total experience is {2}'.format(name,year,exp))
