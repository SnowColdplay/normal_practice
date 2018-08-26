"题目描述：将数组按照某组，倒叙输出，例如"
"输入两行 8 3, 1 2 3 4 5 6 7 8."
"8代表人数，3代表汽车数，1 2 3 4 5 6 7 8代表每个人的编号，输入是 7 8 4 5 6 1 2 3"
"解释：一共8个人，3个车，所以3个人一组，倒叙上车，但是每组顺序不变，只是组顺序变，第一个车两个人，其他车3个人。"
import sys
work_re=[]
n=2
while n:
    ss=sys.stdin.readline()
    if ss.strip():
        line=ss.strip().split()
        work_re.append([int(x) for x in line])
        n=n-1
m=work_re[0][0]
n=work_re[0][1]
yuangong=work_re[1]
print(work_re)
res=[]

if m%n>0:
    each=m/n+1
else:
    each=m/n

if m%n>0:
    res.extend(yuangong[len(yuangong)-m%n:])
    print(res)
    for i in range(n-1,0,-1):
        res.extend(yuangong[(m//n+1)*(i-1):(m//n+1)*i])
else:
    for i in range(n,0,-1):
        res.append(yuangong[(m//n)*(i-1):(m//n)*i])
print(res)