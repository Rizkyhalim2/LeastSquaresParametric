#Rizky Syamsudin Halim - 15117095

import numpy as np 
import math
from numpy.linalg import inv


#input
koordinatawal = np.genfromtxt('kelas2.csv', delimiter=',')
BM = np.genfromtxt('BM panel.csv', delimiter = ',')
jumlahbm = len(BM)



#penyusunan matriks awal
index = np.zeros((len(koordinatawal),1))
for i in range(len(koordinatawal)) :
    index[i,0] = i+1

indexmin = np.zeros((len(koordinatawal) - 1,1))
for i in range(len(koordinatawal) - 1) :
    indexmin[i,0] = i+1




index1 = indexmin + 1

index1[len(index1)- 1] = index1[len(index1) - 1] - len(index1) 

index3 = indexmin - 1 
index3[0] = index3[0] + len(index3) 


koordinatinde = ((index[:,0], koordinatawal[:,0],koordinatawal[:,1]))
koordinatindex = np.transpose(koordinatinde)


jarak3 = np.zeros((len(koordinatawal) - 1,1))
for i in range(len(koordinatawal)-1) :
    jarak3[i,0] = math.sqrt(math.pow(koordinatawal[i,0]-koordinatawal[i+1,0], 2) + math.pow(koordinatawal[i,1]-koordinatawal[i+1,1], 2)) 

jarakT = np.array((indexmin[:,0], index1[:,0], jarak3[:,0]))
jarak = np.transpose(jarakT)

sudutbesar = np.zeros((len(koordinatawal)+1,3))
sudutbesar[0] = koordinatawal[len(koordinatawal)-2]
for i in range(len(koordinatawal)) :
    sudutbesar[i+1] = koordinatawal[i]

z = 0
sudut4 = np.zeros((len(koordinatawal) - 1,1))
for i in range(len(koordinatawal) - 1) :
    atas = (((sudutbesar[i+2,0]-sudutbesar[i+1,0])*(sudutbesar[i,0]-sudutbesar[i+1,0]))+((sudutbesar[i+2,1]-sudutbesar[i+1,1])*(sudutbesar[i,1]-sudutbesar[i+1,1])))
    bawah = math.sqrt(math.pow(sudutbesar[i+2,0]-sudutbesar[i+1,0],2)+math.pow(sudutbesar[i+2,1]-sudutbesar[i+1,1],2))*math.sqrt(math.pow(sudutbesar[i+1,1]-sudutbesar[i,1],2)+math.pow(sudutbesar[i+1,0]-sudutbesar[i,0],2))
    if koordinatawal[z,2] == 1 :
        sudut4[i] = 360 - np.degrees(np.arccos(atas/bawah)) 
        z = z + 1
    else :
        sudut4[i] = np.degrees(np.arccos(atas/bawah))
        z = z + 1

        
    
sudutT = np.array ((index1[:,0],indexmin[:,0],index3[:,0],sudut4[:,0]))
sudut = np.transpose(sudutT)


koordinatawalrev = np.zeros ((len(koordinatawal)-1,3))
for i in range(len(koordinatawalrev)) :
    koordinatawalrev[i] = koordinatindex[i]
print(koordinatawalrev)
print(koordinatawalrev)


pdkt=np.zeros((len(koordinatawalrev),3))
for i in range(len(BM)) :
    pdkt[i] = BM[i]

f = 0

for i in range(len(koordinatawalrev)-jumlahbm+2) :
    if koordinatawalrev[i,0] == pdkt[0,0] or koordinatawalrev[i,0] == pdkt[1,0] :
        continue
    else :
        pdkt[f+jumlahbm] = koordinatawalrev[i]
        f = f+1

np.savetxt('pdkt.csv', pdkt, delimiter=',', fmt=[ '%i' ,'%f' , '%f'], header='Titik,X,Y', comments='')
np.savetxt('jarak.csv', jarak, delimiter=',', fmt=[ '%i' ,'%i' , '%f'], header='dari,ke,jarak', comments='')
np.savetxt('sudut.csv', sudut, delimiter=',', fmt=[ '%i' ,'%i','%i','%f'], header='kiri,tengah,kanan,sudutbesar', comments='')


#input toleransi dan iterasi maksimum
iter_max = 1000
darike = np.array((jarak), dtype=object) 
bjarak = jarak[:,2]
kirikanan = np.array((sudut), dtype=object)
bsudut = np.deg2rad((sudut[:,3]))



idttk = np.array((pdkt), dtype=object)
idstation = np.array((pdkt[:,0]), dtype=object)

xypdkt = np.array([pdkt[:,1],pdkt[:,2]])
xypdktn= np.transpose(xypdkt)

jumlahtitik = np.size(xypdktn,0) - jumlahbm

jumlahT = jumlahtitik*2
jumlahjarak = np.size(jarak,0)

jumlahsudut = np.size(sudut,0)

jacobi1 = jumlahjarak+jumlahsudut
jacobi2 = jumlahtitik*2
jacobi = np.zeros((jacobi1,jacobi2))






#MatriksB/K
bukuran = np.concatenate(([bjarak, bsudut]))
bukuranbaru = np.reshape(bukuran,(-1,1))
idxy = np.zeros((jumlahT,2), dtype=object)
n=-1
for i in range (0, jumlahT, 2):
	n = n+1
	idxy[i,0] = pdkt[n,0]
	idxy[i,1] = 'x'
	
n = -1
for j in range (1, jumlahT, 2) :
    n = n+1
    idxy[j,0] = pdkt[n,0]
    idxy[j,1] = 'y'
    



#iterasi
x = np.zeros((jumlahT,1))
iterasi = 0 
bpdkt = np.zeros((jumlahjarak+jumlahbm+jumlahtitik,1))

for iterasi in range(0,iter_max) :
    if iterasi == iter_max :
        break
    else :
        pass
    

    for i in range (0, jumlahjarak) :
    	for j in range (0, jumlahbm + jumlahtitik) :
    		if darike[i,0] == idstation[j]:
    		    break
    		else:
    		    pass
    	    
    	for k in range(0, jumlahbm + jumlahtitik): 
    	    if darike[i,1] == idstation[k]:
    	        break
    	    else:
    	        pass
    	bpdkt[i,0] = math.sqrt(math.pow(xypdktn[k,0]-xypdktn[j, 0], 2) + math.pow(xypdktn[k,1]-xypdktn[j, 1],2))
    
    	
    	
   
    for i in range (0,jumlahsudut) :
    	for kiri in range (0,jumlahsudut) :
    		if kirikanan[i,0] == idstation[kiri]:
    			break
    		else:
    		    pass
    
    	for tengah in range (0,jumlahsudut) :
    		if kirikanan[i,1] == idstation[tengah]:
    			break
    		else:
    			pass
    
    	for kanan in range (0,jumlahsudut) :
    		if kirikanan[i,2] == idstation[kanan]:
    			break
    		else:
    			pass
    
    	deltaxkanan = xypdktn[kanan,0] - xypdktn[tengah,0]
    	deltaykanan = xypdktn[kanan,1] - xypdktn[tengah,1]
    	deltaxkiri = xypdktn[kiri, 0] - xypdktn[tengah,0]
    	deltaykiri = xypdktn[kiri, 1] - xypdktn[tengah,1]
    	if (deltaxkanan >= 0) and (deltaykanan > 0):
    		azkanan = np.degrees(math.atan(deltaxkanan/deltaykanan))
    	elif (deltaxkanan >= 0) and (deltaykanan < 0):
    		azkanan = np.degrees(math.atan(deltaxkanan/deltaykanan)) + 180
    	elif (deltaxkanan < 0) and (deltaykanan < 0):
    		azkanan = np.degrees(math.atan(deltaxkanan/deltaykanan)) + 180
    	elif (deltaxkanan <= 0) and (deltaykanan > 0):
    		azkanan = np.degrees(math.atan(deltaxkanan/deltaykanan)) + 360
    	elif (deltaxkanan > 0) and (deltaykanan == 0): #cek
    		azkanan = 90
    	elif (deltaxkanan < 0) and (deltaykanan == 0):
    		azkanan = 270
    
    	if (deltaxkiri >= 0) and (deltaykiri > 0):
    		azkiri = np.degrees(math.atan(deltaxkiri / deltaykiri))
    	elif (deltaxkiri >= 0) and (deltaykiri < 0):
    		azkiri = np.degrees(math.atan(deltaxkiri / deltaykiri)) + 180
    	elif (deltaxkiri < 0) and (deltaykiri < 0):
    		azkiri = np.degrees(math.atan(deltaxkiri / deltaykiri)) + 180
    	elif (deltaxkiri <= 0) and (deltaykiri > 0):
    		azkiri = np.degrees(math.atan(deltaxkiri / deltaykiri)) + 360
    	elif (deltaxkiri > 0) and (deltaykiri == 0): #cek
    	    azkiri = 90
    	elif (deltaxkiri < 0) and (deltaykiri == 0):
    	    azkiri = 270

    	bpdkt[jumlahjarak+i,0] = (azkanan - azkiri)
    	
    	
    	
    	if bpdkt[jumlahjarak + i,0] < 0:
    	    bpdkt[jumlahjarak + i, 0] = np.deg2rad(bpdkt[jumlahjarak + i, 0] + 360)
    	else:
    	    bpdkt[jumlahjarak + i, 0] = np.deg2rad(bpdkt[jumlahjarak + i, 0])
    	
    
    	    
    #pembentukanMatriksB
    b = bukuranbaru - bpdkt
    b1d = b.flatten()
    
    


    
    #pengisianMatriksJacobi
    
    #ukuran jarakf
    for i in range (0,jumlahjarak) :
        for dari in range (0, jumlahbm+jumlahtitik):
            if darike[i,0] == idstation[dari]:
                break
            else:
                pass
        
        for ke in range (0, jumlahbm+jumlahtitik):
            if darike[i,1] == idstation[ke]:
                break
            else:
                pass
    
    
        if (dari <= jumlahbm-1) and (ke > jumlahbm-1):
            jacobi[i, (ke+1 - jumlahbm) * 2 - 2] = jacobi[i, (ke + 1 - jumlahbm) * 2 - 2] + ((xypdktn[ke, 0] - xypdktn[dari, 0]) / bpdkt[i, 0])
            jacobi[i, (ke+1 - jumlahbm) * 2 - 1]  = jacobi[i, (ke + 1 - jumlahbm) * 2 - 1] + ((xypdktn[ke, 1] - xypdktn[dari, 1]) / bpdkt[i, 0])

        elif (ke <= jumlahbm-1) and (dari > jumlahbm-1) :
            jacobi[i, (dari+1 - jumlahbm) * 2 - 2]  = jacobi[i, (dari + 1 - jumlahbm) * 2 - 2] + ((xypdktn[dari, 0] - xypdktn[ke, 0]) / bpdkt[i, 0])
            jacobi[i, (dari+1 - jumlahbm) * 2 - 1] = jacobi[i, (dari + 1 - jumlahbm) * 2 - 1] + ((xypdktn[dari, 1] - xypdktn[ke, 1]) / bpdkt[i, 0])
        elif (dari > jumlahbm-1) and (ke > jumlahbm-1):
            jacobi[i, (ke+1 - jumlahbm) * 2 - 2] = jacobi[i, (ke + 1 - jumlahbm) * 2 - 2] + ((xypdktn[ke, 0] - xypdktn[dari, 0]) / bpdkt[i, 0])
            jacobi[i, (ke+1 - jumlahbm) * 2 - 1]  = jacobi[i, (ke + 1 - jumlahbm) * 2 - 1] + ((xypdktn[ke, 1] - xypdktn[dari, 1]) / bpdkt[i, 0])
            jacobi[i, (dari+1 - jumlahbm) * 2 - 2]  = jacobi[i, (dari + 1 - jumlahbm) * 2 - 2] + ((xypdktn[dari, 0] - xypdktn[ke, 0]) / bpdkt[i, 0])
            jacobi[i, (dari+1 - jumlahbm) * 2 - 1] = jacobi[i, (dari + 1 - jumlahbm) * 2 - 1] + ((xypdktn[dari, 1] - xypdktn[ke, 1]) / bpdkt[i, 0])
        

         

    	
    
    		        
    
    for i in range (0,jumlahsudut) : 
    	for kiri in range (0,jumlahtitik+jumlahbm) :
    		if kirikanan[i,0] == idstation [kiri]:
    			break
    		else :
    		    pass
    		
    
    	for tengah in range (0,jumlahtitik+jumlahbm) :
    		if kirikanan[i,1] == idstation [tengah]:
    			break
    		else : 
    		    pass
    		
    		
    	
    	for kanan in range (0,jumlahtitik+jumlahbm) :
    		if kirikanan[i,2] == idstation [kanan]:
    			break
    		else : 
    		    pass
    	
    	dtengahkiri = math.sqrt(math.pow(xypdktn[tengah, 0] - xypdktn[kiri, 0], 2) + math.pow(xypdktn[tengah, 1] - xypdktn[kiri, 1], 2))
    	dtengahkanan = math.sqrt(math.pow(xypdktn[tengah, 0] - xypdktn[kanan, 0], 2) + math.pow(xypdktn[tengah, 1] - xypdktn[kanan, 1], 2))
    	
    	if kiri <= jumlahbm-1 and tengah > jumlahbm-1 and kanan > jumlahbm-1:
    	    #Az tengah - kanan
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] + (xypdktn[tengah, 1] - xypdktn[kanan, 1]) / dtengahkanan**2
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] + (xypdktn[kanan, 0] - xypdktn[tengah, 0]) / dtengahkanan ** 2
    	    jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] + (xypdktn[kanan, 1] - xypdktn[tengah, 1]) / dtengahkanan ** 2
    	    jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] + (xypdktn[tengah, 0] - xypdktn[kanan, 0]) / dtengahkanan ** 2
    	    #Az tengah - kiri
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] - (xypdktn[tengah, 1] - xypdktn[kiri, 1]) / dtengahkiri ** 2
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1]  = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] - (xypdktn[kiri, 0] - xypdktn[tengah, 0]) / dtengahkiri ** 2
    	    
    	elif kiri > jumlahbm-1 and tengah > jumlahbm-1 and kanan <= jumlahbm-1: 
    	    #Az tengah - kanan
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] + (xypdktn[tengah, 1] - xypdktn[kanan, 1]) / dtengahkanan**2
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] + (xypdktn[kanan, 0] - xypdktn[tengah, 0]) / dtengahkanan ** 2 	
    	    #Az tengah - kiri
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] - (xypdktn[tengah, 1] - xypdktn[kiri, 1]) / dtengahkiri ** 2
    	    jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1]  = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] - (xypdktn[kiri, 0] - xypdktn[tengah, 0]) / dtengahkiri ** 2
    	    jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2]- (xypdktn[kiri, 1] - xypdktn[tengah, 1]) / dtengahkiri ** 2
    	    jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] - (xypdktn[tengah,0] - xypdktn[kiri, 0]) / dtengahkiri ** 2
    		    
    	elif kiri > jumlahbm-1 and tengah <= jumlahbm-1 and kanan > jumlahbm-1:
    	    #Az Tengah - Kanan%
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] + (xypdktn[kanan, 1] - xypdktn[tengah, 1]) / dtengahkanan ** 2
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] + (xypdktn[tengah, 0] - xypdktn[kanan, 0]) / dtengahkanan ** 2
    		        #Az Tengah - Kiri%
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2]- (xypdktn[kiri, 1] - xypdktn[tengah, 1]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] - (xypdktn[tengah,0] - xypdktn[kiri, 0]) / dtengahkiri ** 2
    		        
    	elif kiri <= jumlahbm-1 and tengah <= jumlahbm-1 and kanan > jumlahbm-1:
    		        #Az Tengah - Kanan%
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] + (xypdktn[kanan, 1] - xypdktn[tengah, 1]) / dtengahkanan ** 2
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] + (xypdktn[tengah, 0] - xypdktn[kanan, 0]) / dtengahkanan ** 2
    		        
    		        #Az Tengah - Kiri%
    		    
    	elif kiri > jumlahbm-1 and tengah <= jumlahbm-1 and kanan <= jumlahbm-1:
    		        #Az Tengah - Kanan%
    
    		        #Az Tengah - Kiri%
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2]- (xypdktn[kiri, 1] - xypdktn[tengah, 1]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] - (xypdktn[tengah,0] - xypdktn[kiri, 0]) / dtengahkiri ** 2
    		        
    	elif kiri <= jumlahbm-1 and tengah > jumlahbm-1 and kanan <= jumlahbm-1:
    		        #Az tengah - kanan
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] + (xypdktn[tengah, 1] - xypdktn[kanan, 1]) / dtengahkanan**2
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] + (xypdktn[kanan, 0] - xypdktn[tengah, 0]) / dtengahkanan ** 2
    
    		        #Az tengah - kiri
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] - (xypdktn[tengah, 1] - xypdktn[kiri, 1]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1]  = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] - (xypdktn[kiri, 0] - xypdktn[tengah, 0]) / dtengahkiri ** 2
    		        
    	else:
    		        #Az tengah - kanan
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] + (xypdktn[tengah, 1] - xypdktn[kanan, 1]) / dtengahkanan**2
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] + (xypdktn[kanan, 0] - xypdktn[tengah, 0]) / dtengahkanan ** 2
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 2] + (xypdktn[kanan, 1] - xypdktn[tengah, 1]) / dtengahkanan ** 2
    		  jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kanan+1 - jumlahbm) * 2 - 1] + (xypdktn[tengah, 0] - xypdktn[kanan, 0]) / dtengahkanan ** 2
    		        #Az tengah - kiri
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 2] - (xypdktn[tengah, 1] - xypdktn[kiri, 1]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1]  = jacobi[i + jumlahjarak, (tengah+1 - jumlahbm) * 2 - 1] - (xypdktn[kiri, 0] - xypdktn[tengah, 0]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 2]- (xypdktn[kiri, 1] - xypdktn[tengah, 1]) / dtengahkiri ** 2
    		  jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] = jacobi[i + jumlahjarak, (kiri+1 - jumlahbm) * 2 - 1] - (xypdktn[tengah,0] - xypdktn[kiri, 0]) / dtengahkiri ** 2
    

    #pembentukanmatriksW
    W = np.zeros((len(b),len(b)))
    for i in range(0,jumlahjarak) : 
        d1 = math.sqrt(math.pow(koordinatawal[i,0]-BM[0,1], 2) + math.pow(koordinatawal[i,1]-BM[0,2], 2)) 
        d2 = math.sqrt(math.pow(koordinatawal[i,0]-BM[1,1], 2) + math.pow(koordinatawal[i,1]-BM[1,2], 2)) 
        if d1 == 0 or d2 == 0 :
            W[i,i] = 1
        elif d1 <= d2 :
            W[i,i] = 1/d2/d2
        elif d1 > d2 :
            W[i,i] = 1/d1/d1

    for i in range(0,jumlahjarak) : 
        d1 = math.sqrt(math.pow(koordinatawal[i,0]-BM[0,1], 2) + math.pow(koordinatawal[i,1]-BM[0,2], 2)) 
        d2 = math.sqrt(math.pow(koordinatawal[i,0]-BM[1,1], 2) + math.pow(koordinatawal[i,1]-BM[1,2], 2)) 
        if d1 == 0 or d2 == 0 :
            W[i+jumlahjarak,i+jumlahjarak] = 1
        elif d1 <= d2 :
            W[i+jumlahjarak,i+jumlahjarak] = 1/d2/d2
        elif d1 > d2 :
            W[i+jumlahjarak,i+jumlahjarak] = 1/d1/d1

  

    

    x1= np.matmul(np.transpose(jacobi),W)
    x1w = inv(np.matmul(x1,jacobi))
    x2= np.matmul(np.transpose(jacobi),W)
    x2w = np.matmul(x2,b)
    x = np.matmul(x1w,x2w)
    print(x)

    xbaru = np.reshape(x,(-1,1))
    for i in range (0,jumlahtitik):
        xypdktn[jumlahbm+i,0]= xypdktn[jumlahbm+i,0]+x[(i+1)*2-2]
        xypdktn[jumlahbm+i,1]= xypdktn[jumlahbm+i,1]+x[(i+1)*2-1]


  
    iterasi = iterasi+1



v = np.subtract(np.matmul(jacobi,xbaru),b)
vt = np.transpose(v)
vtv = np.matmul(vt,v)
 

    
vaco = vtv/(jumlahjarak+jumlahsudut-jumlahtitik*2)
apriori = inv(np.matmul(np.transpose(jacobi),jacobi))

    
vacov = vaco[0,0]*apriori
standev = vtv/4
    
stdev = np.zeros((jumlahtitik*2, 1))
hasil = np.zeros((jumlahtitik,5))
    
for i in range(0,jumlahtitik*2):
    stdev[i,0] = math.sqrt(vacov[i, i])

for i in range(0,jumlahtitik):
    hasil[i, 0] = idttk[i + jumlahbm, 0]
    hasil[i, 1] = xypdktn[i + jumlahbm, 0]  
    hasil[i, 2] = stdev[((i+1) * 2) - 2, 0]
    hasil[i, 3] = xypdktn[i + jumlahbm, 1]
    hasil[i, 4] = stdev[((i+1) * 2) - 1, 0]

print(hasil)

plot = np.zeros((jumlahtitik+jumlahbm,3))
for i in range(0,jumlahtitik):
    plot[i, 0] = idttk[i + jumlahbm, 0]
    plot[i, 1] = xypdktn[i + jumlahbm, 0]  
    plot[i, 2] = xypdktn[i + jumlahbm, 1]

for i in range(0,jumlahbm) :
    plot[i+jumlahtitik] = BM[i]





np.savetxt('Hasiladjust.csv', hasil, delimiter=',', fmt=[ '%i' ,'%f' , '%f', '%f', '%f'], header='ID,X,StdDevX,Y,StdDevY', comments='')
np.savetxt('Plot.csv', plot, delimiter=',', fmt=[ '%i' ,'%f' , '%f'], header='ID,X,Y', comments='')
np.savetxt('jacobi.csv', jacobi, delimiter=',')

