# zip function

name = ['Utsab', 'Shuvo', 'Shikto']
varsity = ['DIU', 'TUC', 'NS']

zipped1 = list(zip(name, varsity))
print(zipped1)

zipped2 = tuple(zip(name, varsity))
print(zipped2)

zipped3 = dict(zip(name, varsity))
print(zipped3)

# unzip function

name1, varsity1 = zip(*zipped1)
print(list(name1))
print(varsity1)
