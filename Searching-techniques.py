import timeit
def Sequential_Search(dlist, item):
start = timeit.default_timer()
pos = 0
found = False
while pos < len(dlist) and not found:
if dlist[pos] == item:
found = True
else:
pos = pos + 1
stop = timeit.default_timer()
print (stop - start)
return found, pos
print(Sequential_Search([11,23,58,31,5,3],11))
def binary_search(item_list,item):
first = 0
start = timeit.default_timer()
last = len(item_list)-1
found = False
while( first<=last and not found):
mid = (first + last)//2
if item_list[mid] == item :
found = True
else:
if item < item_list[mid]:
last = mid - 1
else:
first = mid + 1
stop = timeit.default_timer()
print (stop - start)
return found
print(binary_search([1,2,3,5,8], 5))
