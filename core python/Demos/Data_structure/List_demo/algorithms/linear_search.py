def linearsearch(li, searchEle):
    for ind in range(0, len(li)):
        if(searchEle == li[ind]):
            return ind
    else:
        return -1
li = [45, 67, 23, 89, 56, 13, 10, 90]
ele = int(input('Enter element to find:'))
res = linearsearch(li, ele)

if(res != -1):
    print(f'{ele} is present at index:{res}')
else:
    print(f'{ele} is not present at list:')


