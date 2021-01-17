import time
x = [7, 2, 3, 5, 9, 1]
def insertion(list):
for index in range(1,len(list)):
value = list[index]
i = index - 1
while i>=0 and (value < list[i]):
list[i+1] = list[i] # shift number in slot i right to slot i+1
list[i] = value # shift value left into slot i
i = i – 1
def bubble(unsorted_list):
length = len(unsorted_list) - 1
sorted = False
while not sorted:
sorted = True
for i in range(length):
if unsorted_list[i] > unsorted_list[i+1]:
sorted = False
unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
def mergesort4(x):
result = []
if len(x) < 20:
return sorted(x)
mid = int(len(x) / 2)
y = msort4(x[:mid])
z = msort4(x[mid:])
i = 0
j = 0
while i < len(y) and j < len(z):
if y[i] > z[j]:
result.append(z[j])
j += 1
else:
result.append(y[i])
i += 1
result += y[i:]
result += z[j:]
def selectionsort( aList ):
for i in range( len( aList ) ):
least = i
for k in range( i + 1 , len( aList ) ):
if aList[k] < aList[least]:
least = k
temp = aList[least]
aList[least] = aList[i]
aList[i] = temp
def shellsort(array):
gap = len(array) // 2 # loop over the gap
while gap > 0:
for i in range(gap, len(array)):
val = array[i]
j = i
while j >= gap and array[j - gap] > val:
array[j] = array[j - gap]
j -= gap
array[j] = val
gap //= 2
def quicksort(myList, start, end):
if start < end:
# partition the list
pivot = partition(myList, start, end) # sort both halves
quicksort(myList, start, pivot-1)
quicksort(myList, pivot+1, end)
def partition(myList, start, end):
pivot = myList[start]
left = start+1
right = end
done = False
while not done:
while left <= right and myList[left] <= pivot:
left = left + 1
while myList[right] >= pivot and right >=left:
right = right -1
if right < left:
done= True
else:
temp=myList[left] # swap places
myList[left]=myList[right]
myList[right]=temp # swap start with myList[right]
temp=myList[start]
myList[start]=myList[right]
myList[right]=temp
return right
def test():
start = time.clock()
bubble(y)
elapsed = (time.clock() - start)
print( "Time taken for bubble = ", elapsed)
start = time.clock() #setting time for start
insertion(x)
elapsed = (time.clock() - start)
print ("Time taken for Insertion = ", elapsed)
start = time.clock()
mergesort4(x)
elapsed = (time.clock() - start) # calculating time taken
print ("Time taken for Mergesort = ", elapsed)
selectionsort(x)
elapsed = (time.clock() - start)
print ("Time taken for Selectionsort = ", elapsed)
shellsort(x)
elapsed = (time.clock() - start)
print ("Time taken for ShellSort = ", elapsed)
quicksort(x, 0, 5)
elapsed = (time.clock() - start)
print ("Time taken for QuickSort = ", elapsed)
test() # method for time complexity
