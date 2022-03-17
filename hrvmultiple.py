#!/usr/bin/env python
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
import matplotlib.font_manager as font_manager
from matplotlib.patches import Rectangle
import time as t

rrbasal = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusBasal1.txt',dtype ='int')
rr1 = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusS1.txt',dtype ='int')
rr2 = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusS2.txt',dtype ='int')
rr3 = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusS3.txt',dtype ='int')
rr4 = np.loadtxt('C:/Users/diego/Documents/Proyectos/Github/Heart Rate Variabilty App/rrmarcusS4.txt',dtype ='int')



rrgeral = [rrbasal, rr1,rr2,rr3,rr4]

def analisisVFC(rr,sesion,tresmin = 0):
    hrvAnalisis = hrvclass() # inicializa la clase
    rr_new = hrvAnalisis.filtrohrv(rr,tresmin) # filter and resample the signal
    
    resultado = []
    
    #analisis en frequencia
    #analisis en frequencia
    Pxx,Fxx,aVLF,aLF,aHF,pVLF,pLF,pHF,lfhf,aTotal  = hrvAnalisis.freqDomainHRV(rr_new,fs = 4.0)
    
    resultado.append(hrvAnalisis.mediahrv())
    resultado.append(hrvAnalisis.Bpm())
    resultado.append(hrvAnalisis.SDNN())
    resultado.append(hrvAnalisis.RMSSD())
    resultado.append(hrvAnalisis.NN50())
    resultado.append(hrvAnalisis.pNN50())
    resultado.append(aVLF)
    resultado.append(aLF)
    resultado.append(aHF)
    resultado.append(pVLF)
    resultado.append(pLF)
    resultado.append(pHF)
    resultado.append(lfhf)
    resultado.append(aTotal)
    
    Vt = hrvAnalisis.vectorTempo()
    
    Vt = hrvAnalisis.vectorTempo()
    print(len(Vt), len(rr_new) , hrvAnalisis.tempoTotal())
    #--------------------------------------------VFC
    # Set the font dictionaries (for plot title and axis titles)
    axis_font = {'size':'15'}
    
    #fig, ax = plt.subplots()
    fig, (ax,ax1) = plt.subplots(2,1)
    ax.plot(Vt,rr_new,color='black', linewidth = 1, linestyle = '--' , marker='o', markersize=4, markerfacecolor=(1, 0, 0, 1))
    ax.set_xlabel("Tempo[s]",**axis_font)
    ax.set_ylabel("RR [ms]",**axis_font)
    ax.tick_params(labelsize=12) # letras ejes x y size 
    ax.grid(True)
    ax1.grid(True)
    
    #--------------------------------------------Freq
    #fig, ax1 = plt.subplots()
    ax1.plot(Fxx,Pxx,color='black',linewidth = "2")
    ax1.set_xlim(0,0.4)
    ax1.set_xlabel("Frequency (Hz)",**axis_font)
    ax1.set_ylabel("PSD (ms^2/Hz)",**axis_font)
    ax1.tick_params(labelsize=12)
    p3 = Rectangle((0, 0), 1, 1, fc=(0.49,1.0,1.0)) #fc = facecolor
    p2 = Rectangle((0, 0), 1, 1, fc=(0.69,0.49,1.0))
    p1 = Rectangle((0, 0), 1, 1, fc=(0.49,0.49,1.0))
    ax1.legend([p1, p2,p3], ["VLF","LF", "HF"],prop={'size':15})

    #
    ax1.fill_between(Fxx,Pxx,0,where=Fxx>=0.14, facecolor=(0.49,1.0,1.0), alpha=1)
    ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.15, facecolor=(0.69,0.49,1.0), alpha=1)
    ax1.fill_between(Fxx,Pxx,0,where=Fxx<=0.04, facecolor=(0.49,0.49,1.0), alpha=1)
    ax1.axvline(x=0.039,linewidth=4, color='r')
    ax1.axvline(x=0.1487,linewidth=4, color='r')

    return resultado

if __name__ == '__main__':
    
    print("---------------------")

    a = np.zeros((14, len(rrgeral)))
    sesion = 0    
    tresmin = 0 #tresminFlag: 1 = Ajustar rr a tres minutos , 0 = Analisis normal
    for i in range(0,len(rrgeral)): 
        result = analisisVFC(rrgeral[i],sesion,tresmin)
        a[:,i] = result
        sesion += 1        
        print("---------------")
    if tresmin == 0:     
        np.savetxt('resultado.txt', a, fmt = '%10.1f')  
    elif tresmin == 1: 
        np.savetxt('resultado3min.txt', a, fmt = '%10.1f')  