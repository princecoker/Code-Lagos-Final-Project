'''
NAME:  COKER OMOBOLA MICHAEL
PHONE: 07082710055, 07030746641
EMAIL: princecoker@gmail.com
TRACK: PYTHON
'''


def variance():
    # import collection to compute frequency in list
    import collections
    
    #create lists
    initial_list = []
    fx = []
    fxsquare = []
    cc = 1

    #accept input for number of distribution
    print()
    max = input('How many values do you wish to analyse?--->')

    #loop to collect data for initial_list
    while cc <= int(max):
        initial_list.append(input('The No '+str(cc)+' value for x is:---> '))
        cc = cc + 1
    print ('Initial_list is ---> ',initial_list)    #to print initial_list
    print()

    #to extract frequency of element in list initial_list
    freq_dict = collections.Counter(initial_list)
       
    #to extract frequency as a list
    f = freq_dict.values()
    f = list(f)
    print ('list(f) --->',f)                        #to display frequency
    print()

    #to extract distribution as a list
    x = freq_dict.keys()
    x = [int(j) for j in x]                         #to convert distribution to integer
    print ('list(x)---> ',x)                        #to display distribution
    print()

    #compute fx and fxsquare for each distribution
    z = 0
    while z < len(x):
        fx.append(x[z] * f[z])
        fxsquare.append(fx[z]**2)
        z = z + 1
        
    a = sum(fxsquare)

    right_value = a/int(max)

    b = sum(fx)/int(max)

    left_value = ((sum(fx))/int(max))**2

    mean = sum(fx)/int(max)

    var = (right_value)-(left_value)
    
    print ('sample is ', max)
    print ('mean is', mean)
    print ('The variance of the distribution is ',round(var))
    return


def standard_deviation():
    from math import sqrt

    #import collection to compute frequency in list
    import collections
    
    #create lists
    initial_list = []
    fx = []
    fxsquare = []
    cc = 1

    #accept input for number of distribution
    print()
    max = input('How many values do you wish to analyse?--->')

    #loop to collect data for initial_list
    while cc <= int(max):
        initial_list.append(input('The No '+str(cc)+' value for x is:---> '))
        cc = cc + 1
    print ('Initial_list is ---> ',initial_list)    #to print initial_list
    print()

    #to extract frequency of element in list initial_list
    freq_dict = collections.Counter(initial_list)
       
    #to extract frequency as a list
    f = freq_dict.values()
    f = list(f)
    print ('list(f) --->',f)                        #to display frequency
    print()

    #to extract distribution as a list
    x = freq_dict.keys()
    x = [int(j) for j in x]                         #to convert distribution to integer
    print ('list(x)---> ',x)                        #to display distribution
    print()

    #compute fx and fxsquare for each distribution
    z = 0
    while z < len(x):
        fx.append(x[z] * f[z])
        fxsquare.append(fx[z]**2)
        z = z + 1
        
    a = sum(fxsquare)

    right_value = a/int(max)

    b = sum(fx)/int(max)

    left_value = ((sum(fx))/int(max))**2

    mean = sum(fx)/int(max)

    var = (right_value)-(left_value)

    stdv = sqrt(var)
    
    print ('sample is ',max)
    print ('mean is ',mean)
    print ('The standard deviation is of the distribution is ',round(stdv,2))
    return




#used to call both variance and standard deviation in a loop
import time

print ('''
Welcome to Timeless Statistical Calculator (TSC) 2018.
The Calculator is designed to compute only sample variance and standard deviation.
Have Fun.
'''
)

commence = 0
while commence == 0:
    status = str(input('Do you wish to continue yes or no? ----> '))
    print()

    if status == 'no':
          commence = commence + 1

    elif status == 'yes':
        entry = input('To calculate variance enter 1, to calculate standard deviation enter 2 ===> ')
        if entry == '1':
            variance()
            print()
            time.sleep(5)
            
        elif entry == '2':
            standard_deviation()
            print()
            time.sleep(5)

print ('Good Bye')
