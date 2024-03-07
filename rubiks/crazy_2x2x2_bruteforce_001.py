
def algorithm2substitutionlist(algorithm:str) -> list(int):
    '''
    passes "list(range(0,24))" through the permutation of an algorithm <TODO: and all its symetricaly applicable copys> and returns the index list
    '''
    pass

algorithms = [] #list of algorithms as string representation.



'''
ADD A WAY TO INPUT ALGORITHMS
'''
slist = [] #"Substitution-List" contining lists that where run through an algorithm, so that the fields where moved. this movement is recorded for each algorithm in "slists"
for algorithm in algorithms:
    slist.append(algorithm2substitutionlist(algorithm))
