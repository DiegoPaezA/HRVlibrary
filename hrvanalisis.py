# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:37:50 2015
Updated on Thu March 17 2022
@author: Diego Ricardo Páez
@reference: https://repositorio.ufsc.br/handle/123456789/160626
@site: https://www.mrdpaez.com
@github:https://github.com/DiegoPaezA

"""


from hrvclassA import hrvclass
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


rr1 = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusS1.txt',dtype ='int')

rr=(rr1)
hrvAnalisis = hrvclass() # inicializa la clase
rr_new = hrvAnalisis.filtrohrv(rr) # filter and resample the signal

# analisis de tiempo
print("Media HRV:", hrvAnalisis.mediahrv(), "ms")
print("Bpm: ", hrvAnalisis.Bpm())
print("SDNN: ",  hrvAnalisis.SDNN() , "ms")
print("RMSSD: ", hrvAnalisis.RMSSD(), "ms")
print("NN50: ",  hrvAnalisis.NN50())
print("pNN50: ", hrvAnalisis.pNN50() , "%")
print("Tempo Total: ", hrvAnalisis.tempoTotal(), "s")
 
Vt = hrvAnalisis.vectorTempo()

#analisis en frequencia
Pxx,Fxx,aVLF,aLF,aHF,pVLF,pLF,pHF,lfhf,aTotal  = hrvAnalisis.freqDomainHRV(rr_new,fs = 4.0)

print("VLF:", aVLF, "ms^2")
print("LF:", aLF, "ms^2")
print("HF:", aHF, "ms^2")
print("LF/HF:", "%.4f" % lfhf)


#--------------------------------------------VFC
#fig, ax = plt.subplots()
fig, (ax,ax1) = plt.subplots(2,1)
ax.plot(Vt,rr_new,color='black', linewidth = 2,linestyle = '--',marker='o',markersize=6,markerfacecolor=(1, 0, 0, 1))
ax.set_xlabel("Tempo[S]")
ax.set_ylabel("RR [ms]")
ax.grid(True)
ax1.grid(True)
#--------------------------------------------Freq
#fig, ax1 = plt.subplots()
ax1.plot(Fxx,Pxx,color='black',linewidth = "2")
ax1.set_xlim(0,0.4)
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("PSD (ms^2/Hz)")
p3 = Rectangle((0, 0), 1, 1, fc=(0.49,1.0,1.0)) #fc = facecolor
p2 = Rectangle((0, 0), 1, 1, fc=(0.69,0.49,1.0))
p1 = Rectangle((0, 0), 1, 1, fc=(0.49,0.49,1.0))
ax1.legend([p1, p2,p3], ["VLF","LF", "HF"])
#
ax1.fill_between(Fxx,Pxx,0,where=Fxx>=0.14, facecolor=(0.49,1.0,1.0), alpha=1)
ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.15, facecolor=(0.69,0.49,1.0), alpha=1)
ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.04, facecolor=(0.49,0.49,1.0), alpha=1)
ax1.axvline(x=0.039,linewidth=4, color='r')
ax1.axvline(x=0.1487,linewidth=4, color='r')




