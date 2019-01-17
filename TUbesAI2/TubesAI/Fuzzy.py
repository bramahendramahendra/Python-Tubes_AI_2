EmosiList = [97,36,63,82,71,79,55,57,40,57,77,68,60,82,40,80,60,50,100,11,58,68,64,57,77,98,91,50,95,27]
ProvokasiList = [74,85,43,90,25,81,62,45,65,45,70,75,70,90,85,68,72,95,18,99,63,70,66,77,55,64,59,95,55,79]

def Berita(E,P):
	TabelEmosi = RumusTabelEmosi(E)
	TabelProvokasi = RumusTabelProvokasi(P)
	return RumusInference(TabelEmosi,TabelProvokasi)

def RumusTabelEmosi(E):
	if(E<20):
		HasilTabelEmosi = ['Sangat Rendah',0,'Sangat Rendah',1]
	elif(20<= E < 40):
		HasilTabelEmosi = ['Sangat Rendah',((40-E)/(40-20)),'Rendah',((E-20)/(40-20))]
	elif(40<= E < 60):
		HasilTabelEmosi = ['Rendah',((62-E)/(62-40)),'Tinggi',((E-40)/(62-40))]
	elif(60<= E < 80):
		HasilTabelEmosi = ['Tinggi',((80-E)/(80-62)),'Sangat Tinggi',((E-62)/(80-62))]
	else:
		HasilTabelEmosi = ['Sangat Tinggi',0,'Sangat Tinggi',1]
	return  HasilTabelEmosi

def RumusTabelProvokasi(P):
	if(P<20):
		HasilTabelProvokasi = ['Sangat Rendah',0,'Sangat Rendah' , 1]
	elif(20<= P < 40):
		HasilTabelProvokasi = ['Sangat Rendah',((40-P)/(40-20)) ,'Rendah',((P-20)/(40-20))]
	elif(40<= P < 60):
		HasilTabelProvokasi = ['Rendah',((62-P)/(62-40)),'Tinggi' ,((P-40)/(62-40))]
	elif(60<= P < 80):
		HasilTabelProvokasi = ['Tinggi',((80-P)/(80-62)),'Sangat Tinggi',((P-62)/(80-62))]
	else:
		HasilTabelProvokasi = ['Sangat Tinggi',0,'Sangat Tinggi',1]
	return  HasilTabelProvokasi

def RumusInference(TE,TP):
	boolInference = [RumusBoolInference(TE[0],TP[0]),RumusBoolInference(TE[0],TP[2]),RumusBoolInference(TE[2],TP[0]),RumusBoolInference(TE[2],TP[2])]
	doubleInference = [RumusDoubleInference(TE[1],TP[1]),RumusDoubleInference(TE[1],TP[3]),RumusDoubleInference(TE[3],TP[1]),RumusDoubleInference(TE[3],TP[3])]
	true = 0
	false = 0
	loop = 0
	print(boolInference[loop])
	while(loop < 4):
		if boolInference[loop]=='True':
			if true==0:
				true = doubleInference[loop]
			else:
				if doubleInference[loop] > true:
					true = doubleInference[loop]
		else:
			if false == 0:
				false = doubleInference[loop]
			else:
				if doubleInference[loop] > false:
					false = doubleInference[loop]
		loop = loop + 1
	return RumusHoax(RumusNilaiHoax(true,false))


def RumusBoolInference(StatusEmosi,StatusProvokasi):
	if(StatusEmosi == 'Sangat Rendah' and StatusProvokasi == 'Sangat Rendah'):
		return 'False'
	elif(StatusEmosi == 'Rendah' and StatusProvokasi == 'Sangat Rendah'):
		return 'False'
	elif(StatusEmosi == 'Tinggi' and StatusProvokasi == 'Sangat Rendah'):
		return 'False'
	elif(StatusEmosi == 'Sangat Tinggi'  and StatusProvokasi == 'Sangat Rendah'):
		return 'False'
	elif(StatusEmosi == 'Sangat Rendah'and StatusProvokasi == 'Rendah'):
		return 'False'
	elif(StatusEmosi == 'Rendah' and StatusProvokasi == 'Rendah'):
		return 'False'
	elif(StatusEmosi == 'Tinggi' and StatusProvokasi == 'Rendah'):
		return 'False'
	elif(StatusEmosi == 'Sangat Tinggi' and StatusProvokasi == 'Rendah'):
		return 'True'
	elif(StatusEmosi == 'Sangat Rendah' and StatusProvokasi == 'Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Rendah' and StatusProvokasi == 'Tinggi'):
		return 'False'
	elif(StatusEmosi == 'Tinggi' and StatusProvokasi == 'Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Sangat Tinggi' and StatusProvokasi == 'Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Sangat Rendah' and StatusProvokasi == 'Sangat Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Rendah' and StatusProvokasi == 'Sangat Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Tinggi' and StatusProvokasi == 'Sangat Tinggi'):
		return 'True'
	elif(StatusEmosi == 'Sangat Tinggi' and StatusProvokasi == 'Sangat Tinggi'):
		return 'True'


def RumusDoubleInference(NilaiEmosi,NilaiProvokasi):
	if (NilaiEmosi < NilaiProvokasi):
		return NilaiEmosi
	else:
		return NilaiProvokasi

def RumusNilaiHoax(T,F):
	return ((T*25)+(F*60)/(T+F))

def RumusHoax(Hoax):
	if(Hoax < 30):
		return 'ya'
	else:
		return 'tidak'


LoopBerita = 0

while (LoopBerita < 30):
	print(EmosiList[LoopBerita])
	print(ProvokasiList[LoopBerita])
	BeritaList =  Berita(EmosiList[LoopBerita],ProvokasiList[LoopBerita])
	print(BeritaList[LoopBerita])
	LoopBerita = LoopBerita+1
