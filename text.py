def num(n):
    if n <=1:
        return 1
    else:
        return n*num(n-1)
print(num(6))

def simple(key,targetl):
    iter=0
    for i in range(len(targetl)):
        iter=iter+1
        if key not in targetl:
            return null,null
        elif targetl[i]==key:
            return i,iter

if __name__=='__main__':
    L=[i for i in range(1,101)]
    print('please input a key for search:')
    key=int(input())
    idx,iter=simple(key,L)
    print("the location of the date key:{0}\n"\
          "the sters of the search:{1}".format(idx,iter))

