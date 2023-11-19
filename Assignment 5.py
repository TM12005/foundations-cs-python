#The only change i did was to convert the list to lower() in the if statement

def selectionSort(list1): #O(n^2)
  border=0
  while border < len(list1)-1: #O(n), n being the length of the list
    minIndex=border # contain the index of the minimum element
    for i in range(border+1, len(list1)): # to find the index of the minimum element, O(n)
      if list1[i].lower() < list1[minIndex].lower(): #O(1), is the line that specifies the order
        minIndex=i
    #swap the two elements
    temp=list1[border] #O(1)
    list1[border]=list1[minIndex]
    list1[minIndex]=temp

    # list1[border],list1[minIndex]=list1[minIndex],list1[border]

    border=border+1
    # border+=1
  print(list1)

list1 = ["aA", "b", "BD", "Bc","D"]

selectionSort(list1)

#-----------------------------------------------------------------------

# only thing that I changed was the "<" to ">" in line 44

def mergeSort(list1,start,end): #O(n log n)
  # base case
  if start==end: #I have a list of length 1
    return
  mid=(start+end)//2 #binary search
  mergeSort(list1,start,mid) # dividing the list further
  mergeSort(list1,mid+1,end)
  merge(list1,start,mid,end) # I am passing the division of the list

def merge(list1,start,mid,end): # to merge the two sublists into a sorted one, O(n), n being the length of the list
  new_list=[]
  ind1=start # this points to the start of the first sub-list
  ind2=mid+1 # this points to the start of the second sub-list

  while ind1<=mid and ind2<=end: # I have elements in both sublists
    if list1[ind1]>list1[ind2]: 
      new_list.append(list1[ind1])
      ind1+=1
    else: # the element in my second sublist is smaller
      new_list.append(list1[ind2])
      ind2+=1
  # this means that the elements of sublist 1 OR sublist 2 are complete

  while ind1<=mid:
    new_list.append(list1[ind1])
    ind1+=1
    
  while ind2<=end: 
    new_list.append(list1[ind2])
    ind2+=1

  # I finished copying all the elements
  #new_list contains the same elements as list1 but in an ordered way
  list1[start:end+1]=new_list


list2 = [3,5,1,8,-10]
mergeSort(list2,0,len(list2)-1)
print(list2)