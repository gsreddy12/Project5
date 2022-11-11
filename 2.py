#Printing Multiple variables

#Method1
name='Sateesh'
age=36
country='India'
print("Printing Normally.......")
print(name,age,country)

print("Printing with commas")
print(name,age,country,sep=',')

#Method2
name='Sateesh'
age=36
country='India'
print("{}{}{}".format(name,age,country))
print("Name:{},Age:{},Country:{}".format(name,age,country))

#Method3
name='Sateesh'
age=36
country='India'
print("{0}{1}{2}".format(name,age,country))
print("Name:{0},Age:{1},Country:{2}".format(name,age,country))
print("Country:{2},Name:{0},Age:{1}".format(name,age,country))
print("{0}{0}{1}{1}{2}{2}".format(name,age,country))

#Method4
name='Sateesh'
age=36
country='India'
print("{n}{a}{c}".format(n=name,a=age,c=country))
print("Name:{n},Age:{a},Country:{c}".format(n=name,a=age,c=country))
print("Country:{c},Name:{n},Age:{a}".format(n=name,a=age,c=country))
print("{n}{n}{a}{a}{c}{c}".format(n=name,a=age,c=country))

#Method5
print("Without Separator......")
print(name+str(age)+country)
print("Separator with commas.....")
print(name+","+str(age)+","+country)
print("Printing with messages......")
print("Name:"+name+" Age:"+str(age)+" Country:"+country)

