def trap(x,a,b,c,d):
    if(x <= a or x >= d):
        return 0
    elif(x>=b and x<=c):
        return 1
    elif(x>a and x<b):
        return(x-a)/(b-a)
    else:
        return (-x+d)/(d-c)

def emosi_mf(x):
    E1= trap(x,-1,0,10,25)
    E2= trap(x,10,25,60,80)
    E3 =trap(x,60,80,100,101)
    return [E1,E2,E3]

def provokasi(x):
    P1 = trap(x, -1, 0, 20, 35)
    P2 = trap(x, 20, 35, 60, 80)
    P3 = trap(x, 60, 80, 100, 101)
    return [P1, P2, P3]

def inferensi_tidak(E,P):
    T1 = min(E[0], P[0])
    T2 = min(E[0], P[1])
    T3 = min(E[1], P[0])
    T4 = min(E[1], P[1])
    T5 = min(E[2], P[0])
    return max([T1,T2,T3,T4,T5])

def inferensi_ya(E,P):
    Y1 = min(E[0], P[2])
    Y2 = min(E[1], P[2])
    Y3 = min(E[2], P[1])
    Y4 = min(E[2], P[2])
    return max([Y1,Y2,Y3,Y4])

def sugeno(ya,tidak):
    return ((tidak*75)+(ya*25))/(tidak+ya)

def yesno(x):
    if x>=45:
        return 'tidak'
    else:
        return 'ya'

def Berita(E,P):
    hasilemosi = emosi_mf(E)
    hasilprovokasi = provokasi(P)
    print(hasilemosi)
    print(hasilprovokasi)
    print(inferensi_tidak(hasilemosi,hasilprovokasi))
    print(inferensi_ya(hasilemosi,hasilprovokasi))
    no = inferensi_tidak(hasilemosi,hasilprovokasi)
    yes = inferensi_ya(hasilemosi,hasilprovokasi)
    #print(sugeno(yes,no))
    uhu = sugeno(yes,no)
    return yesno(uhu)

B = ['B01','B02','B03','B04','B05','B06','B07','B08','B09','B10','B11','B12','B13','B14','B15','B16','B17','B18','B19','B20']
EmosiList = [97,36,63,82,71,79,55,57,40,57,77,68,60,82,40,80,60,50,100,11]
#,58,68,64,57,77,98,91,50,95,27]
ProvokasiList = [74,85,43,90,25,81,62,45,65,45,70,75,70,90,85,68,72,95,18,99]
#,63,70,66,77,55,64,59,95,55,79]
Asli = ['Y','Y','T','Y','T','Y','T','T','T','T','Y','Y','T','Y','T','Y','T','Y','T','Y']

LoopBerita = 0
while (LoopBerita < 20):
    E1=EmosiList[LoopBerita]
    P1=ProvokasiList[LoopBerita]
    BeritaList =  Berita(E1,P1)
    print(B[LoopBerita],EmosiList[LoopBerita],ProvokasiList[LoopBerita],Asli[LoopBerita],BeritaList)
    print()
    LoopBerita = LoopBerita+1
