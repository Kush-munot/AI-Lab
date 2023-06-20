cap_a = int(input())
cap_b = int(input())
target = int(input())
first, second = 0, 0
states = [first, second]
if(cap_a < target and cap_b < target):
        print("solution not possible")
else:
    for i in range(1):
        while first != target and second != target:
            states = [first, second]
            print (states)
            if second < cap_b:
                if first != 0:
                    if second+first <= cap_b:
                        second += first
                        first = 0
                        print("Transferring Water")
                    else:
                        n = first+second-cap_b
                        second = cap_b
                        first = n
                        print("Transferring Water")
                else:
                    first = cap_a
                    print("Filling Water")
            else:
                second = 0
                print("Emptying Water")
            
        print([first, second], "Solution Found")
