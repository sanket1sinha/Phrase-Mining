
# coding: utf-8

# In[ ]:

import copy
import itertools
min_sup=int(input())
ln=[]
while True:
    try:
        matrix=input()
        ln.append(matrix)
    except EOFError:
         break  
ln=[[i] for i in ln]
q=[]
for i in ln:
    a=[j.lower() for j in i]
    q.append(a)
j=[]
for i in q:
    b=" ".join(str(x) for x in i)
    g= ["*".join(x.strip() for x in b.split(" and "))]
    j.append(g)
j1=[]
for i in j:
    b=" ".join(str(x) for x in i)
    g= ["*".join(x.strip() for x in b.split(", "))]
    j1.append(g)
j2=[]
for i in j1:
    b=" ".join(str(x) for x in i)
    g= ["*".join(x.strip() for x in b.split(","))]
    j2.append(g)
o=[]
for i in j2:
    b=" ".join(str(x) for x in i)
    g= ["".join(x.strip() for x in b.split("."))]
    o.append(g)
l=[]
for i in o:
    a=[words for segments in i for words in segments.split()]
    l.append(a)
rmv=['a','an','are','as','at','by','be','for','from','has','he','in','is','it','its','of','on','that','the' ,'to','was','were','will','with']
uj=[]
for i in l:
    l3 = [x for x in i if x not in rmv]
    uj.append(l3)
p=[]
for i in uj:
    a=[[j] for j in i]
    p.append(a)
yu=[]
for j in p:
    
    gh=[]
    for i in j:
        the_new_list = [x.split('*') for x in i]
        gh.append(the_new_list[0])
    yu.append(gh)
    
#Recursive

def recursive(main, sub, s=0):
    if (not sub):
        return True
    fe = set(sub.pop(0))
    for i in range(s, len(main)):
        if (set(main[i]).issuperset(fe)):
            return recursive(main, sub, i + 1)
    return False
full=[]
item=[]
for i in yu:
    for j in i:
        for k in j:
            item.append(k)
item=sorted(set(item))
seq = [[[i]] for i in item]
single_candidate=[]
single_candidate_count=[]
for i in seq:
    c=0
    for j in yu:
        subseq=list(i)
        if recursive(j, subseq):
            c=c+1
    if c>=min_sup:
        single_candidate.append(i)
        single_candidate_count.append(c)
single_cand=tuple(zip(single_candidate, single_candidate_count))
full.append(single_cand)
dk=1
while True:
    cand_gen=[]
    if not full[dk-1]:
        break
    cand = [x[0] for x in full[dk - 1]]
    length=sum(len(i) for i in cand[0])
    length=length+1
    flt_cand=[]
    if length==2:
        for i in cand:
            for j in i:
                for k in j:
                    flt_cand.append(k)
        r=[[[i, j]] for i in flt_cand for j in flt_cand if j > i]
        r.extend([[[i], [j]] for i in flt_cand for j in flt_cand])
        cand_gen=r
    else:
        cd=[]
        length_of_cands=len(cand)
        for i in range(0,length_of_cands):
            for j in range(0,length_of_cands):
                new_cd=[]
                c1=cand[i]
                c2=cand[j]
                c1_temp= copy.deepcopy(c1)
                c2_temp=copy.deepcopy(c2)
                if(len(c1[0])==1):
                    c1_temp.pop(0)
                else:
                    c1_temp[0]=c1_temp[0][1:]
                if(len(c2[-1])==1):
                    c2_temp.pop(-1)
                else:
                    c2_temp[-1] = c2_temp[-1][:-1]
                if not c1_temp == c2_temp:
                    new_cd=[]
                    
                else:
                    new_cand=copy.deepcopy(c1)
                    if(len(c2[-1])==1):
                        new_cand.append(c2[-1])
                    else:
                        new_cand[-1].extend(c2[-1][-1])
                    new_cd=new_cand
                if(not new_cd==[]):
                    cd.append(new_cd)
        cd.sort()
        cand_gen=cd
    hh=[]
    for i in cand_gen:
         if i not in hh:
            hh.append(i)
    cand_prun=[]
    for c in hh:
        r=[]
        for i,item in enumerate(c):
            if(len(item)==1):
                sc=copy.deepcopy(c)
                sc.pop(i)
                r.append(sc)
            else:
                for j in range(len(item)):
                    sc=copy.deepcopy(c)
                    sc[i].pop(j)
                    r.append(sc)
        sequence=r
        for i in sequence:
            if i in cand:
                cand_prun.append(c)
    hg=[]
    for i in cand_prun:
         if i not in hg:
            hg.append(i)            
    sd=[]
    sdc=[]
    for i in hg:
        c=0
        for j in yu:
            subseq=list(i)
            if recursive(j, subseq):
                c=c+1 
        sd.append(i)
        sdc.append(c)
    s=tuple(zip(sd, sdc))
    final_elements = [(value, count) for (value, count) in s if (count >= min_sup)]
    full.append(final_elements)
    dk = dk + 1
full = full [:-1]
final_cands=[]
for i in full:
    for j in i:
        final_cands.append(j)
lo = []
if final_cands ==[]:
    print(final_cands)
else:
    
    for i in final_cands:
        if i not in lo:
            lo.append(i)
    count_elem=[]
    for i in lo:
        cl=str(i[0]).count(" ")+1
        count_elem.append(cl)
    m=max(count_elem)
    ql=[]
    for i in lo:
        cl=str(i[0]).count(" ")+1
        if cl>=m:
            ql.append(i)
    zt=[]
    f=[]
    for i in ql:
        v=[]
        for j in i[0]:
            if len(j)>1:
                j.sort()
                v.append(j)
            else:
                v.append(j)
        f.append(v)
        zt.append(i[1])
        sz=tuple(zip(f, zt))  
    cy=[]
    v=[]
    for i in sz:
        vr=[]
        for j in i[0]:
            if len(j)>1:
                b=" ".join(j)
                b1 =''.join(('(',b,')'))
                vr.append(b1)
            else:
                a="".join(str(x) for x in j)
                vr.append(a)
        vr=' '.join(vr)
        v.append(vr)
        cy.append(i[1])
        s2=tuple(zip(v, cy))
    final_list=sorted(s2, key=lambda element: (element[1], element[0]))
    for i in final_list:
        print(i[1],"["+i[0]+"]")

