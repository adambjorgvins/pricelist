"""þú biður um input sem eru jákvæðar heiltölur og þú átt að prenta út hve margar tölur eru prímtölur"""

n = input("Enter spaced numbers").strip().split(" ")
counter = 0
for number in n:
    if int(number) % 2 != 0:
         counter += 1
print(counter)


