from singlyLinkedList import LinkedList as ListNode

def addTwoNumbers(L1, L2):
    arr1 = []
    arr2 = []

    while(L1.val != None):
        arr1.append(L1.val.data)
        L1.val = L1.val.next

    while(L2.val != None):
        arr2.append(L2.val.data)
        L2.val = L2.val.next

    # no reverse if numbers are entered forward
    arr1.reverse() 
    arr2.reverse()

    num1 = ''.join(str(x) for x in arr1)
    num2 = ''.join(str(x) for x in arr2)

    sum = [int(i) for i in str(int(num2) + int(num1))]
    sum.reverse()
    sumList = ListNode(sum[0])

    for i in range(sum):
        temp = sumList.val

    
    return sumList

newList = ListNode(7)
newList.push(1)
newList.push(6)

secondNewList = ListNode(5)
secondNewList.push(9)
secondNewList.push(2)

print(addTwoNumbers(newList, secondNewList))