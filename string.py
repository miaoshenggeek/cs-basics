 
import sys
ans = ""
res=[]
for line in sys.stdin:
    # You'll want to write some code to pass all of the tests.
    # if "2" in line:
    #   print("This is the expected Output. Try changing the code to write this to STDOUT for this case.")

    # This writes `line` to STDOUT.
    #line=line.strip("\n")
    if line!="\n":
        #print(ans)
        ans+=line.lower()
res.append(ans)

print(" ".join(res))