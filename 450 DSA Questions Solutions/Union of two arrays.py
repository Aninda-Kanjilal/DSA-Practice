class Solution:
    def doUnion(self,a,n,b,m):
        arr=[]
        for i in range(n):
            arr.append(a[i])
        for i in range(m):
            arr.append(b[i])
        hashset=set(arr)
        hashset=list(hashset)
        return len(hashset)
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n,m=[int(x) for x in input().strip().split()]
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
