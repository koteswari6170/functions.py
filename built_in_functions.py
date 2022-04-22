'''   Pre-Defined Functions  '''

'''     soted()      '''
# a=[1,6,3,8,2]
# a.sort()
# print(a)               #[1,2,3,6,8]
# print(sorted([3,76,23,45,2]))   #[2, 3, 23, 45, 76]
# a.sort(reverse=True)
# print(a)        #[8, 6, 3, 2, 1]

'''   all()   '''
# print(all([True,1,2]))                   #True
# print(all([True,'',1,2]))                #False
# print(all([True,' ',1,2]))               #True
# print(all([True,False,1,2]))             #False
# print(all([True,True,1,2,0]))            #False
# print(all([True,True,1,2,None]))         #False

'''     Any()    '''
# print(any([True,False,False,23]))        #True
# print(any([False,False,0]))              #False
# print(any([True,False,False,23,None]))   #True

# print(bool(False))         #False
# print(bool(1))             #True
# print(bool(0))             #False
# print(bool(None))          #False
# print(bool('bool'))        #True

'''    eval()    '''
# print('eval=',eval('5+8-1'))          #eval= 12
# a=eval('5+6*1')
# b=eval('5.8-1.5')
# print(a,type(a))   #11 int
# print(b,type(b))     #4.3 float

'''   sum()   '''
# print('sum=',sum([2,4,6,7]))             #sum= 19
# print('sum=',sum([10.5,20,30]))          #sum= 60.5

'''       reversed()- list     '''
# for i in reversed([10,25,34,65]):
    # print(i)

'''            reversed()-tuple        '''
# for i in reversed((10,20,30,40)):
    # print(i)

'''      enumerate      '''
# a=['bread','sugar','milk']
# b=enumerate(a)
# print(type(b))         #enumerate
# print(dict(b))           #{0: 'bread', 1: 'sugar', 2: 'milk'}
# print(list(b))           #[(0, 'bread'), (1, 'sugar'), (2, 'milk')]
# print(tuple(b))            #((0, 'bread'), (1, 'sugar'), (2, 'milk'))

# a=['bread','sugar','milk']
# c=enumerate(a,5)
# print(list(c))       #[(5, 'bread'), (6, 'sugar'), (7, 'milk')]
