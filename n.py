l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20, 21,22]

remainder = len(l) % 10
limit = int((len(l)// 10) + remainder/remainder)
count = 1
start = 0
end = 1
while count <= limit:
    if count == limit:
        end += remainder
    else:
        end += 10
    print("start:", start)
    curr = l[start:end]
    print("end:", end)
    print(curr)
    start = end
    count += 1

