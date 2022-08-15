min_guk=list(map(int,input().split()))
man_sae=list(map(int,input().split()))

min_guk=sum(min_guk)
man_sae=sum(man_sae)

if min_guk == man_sae:
    print(min_guk)
else:
    print(max(min_guk,man_sae))