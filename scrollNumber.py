a = 100
b = 500
noScroll = True
for i in range(a,b+1):
    c = str(i)
    chrs = set(c)
    if '0' in chrs:
        continue
    if len(chrs)<len(c):
        continue
    n = len(c)
    j = int(c[0])%n
    while c[j] in chrs:
        chrs.remove(c[j])
        j = (int(c[j])+j)%n#
    if len(chrs)==0:
        print(i)
        noScroll = False
if noScroll:
    print(-1)