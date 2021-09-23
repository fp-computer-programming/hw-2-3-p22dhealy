# author: 9/23/21

pop = 332774992

gain = 25 

year= 60 * 60 * 24 * 365
day = 60 * 60 * 24 

future_pop = pop + ((year + day) // gain)
print(future_pop)
