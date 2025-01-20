# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:59:27 2025

@author: Pol
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})

points_lin=np.linspace(0,2,1000)
points_log=np.geomspace(1e-10,2,1000)

breakpoints=[0.000100,0.000133,0.000178,0.000237,0.000316,0.000421,0.000562,0.000749\
,0.000999,0.001332,0.001776,0.002368,0.003157,0.004209,0.005612,0.007483,0.009977\
,0.013303,0.017738,0.023650,0.031534,0.042045,0.056060,0.074747,0.099662,0.132883\
,0.177177,0.236236,0.314981,0.419975,0.559967,0.746622,0.995496,1.327328,2.000000]

# Décroissance

temps_sim=np.array([[[breakpoints[25]],[breakpoints[15]]\
,[breakpoints[34]]],[[breakpoints[25]]\
,[breakpoints[17]],[breakpoints[13]]],[[breakpoints[25]]\
,[breakpoints[17]],[breakpoints[9]]]])
tailles_sim=np.array([[[999714.941752,2001208.462727],[365894.822621,1998658.292037]\
,[1992934.027952,2017766.611594]],[[1001869.577041,2000154.821740]\
,[1005892.441799,1997674.514247],[1657577.279732,2000150.681410]]\
,[[999998.034151,1998290.581587],[998109.474562,1998618.708338]\
,[1002359.371515,1999312.139087]]])/2e5
temps_reel=np.array([[0.1],[0.01],[0.001]])
tailles_reel=np.array([5,10])
RMSD_lin=np.zeros([3,3])
RMSD_log=np.zeros([3,3])
RMSD_chg=np.zeros([3,3])
for i in range(3):
    for j in range(3):
        #Linéaire
        for k in points_lin:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            else: res+=tailles_sim[j,i,1]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            else: res-=tailles_reel[1]
            RMSD_lin[j,i]+=res**2
        RMSD_lin[j,i]=(RMSD_lin[j,i]/len(points_lin))**0.5
        #Log
        for k in points_log:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            else: res+=tailles_sim[j,i,1]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            else: res-=tailles_reel[1]
            RMSD_log[j,i]+=res**2
        RMSD_log[j,i]=(RMSD_log[j,i]/len(points_log))**0.5
        #Changements de taille
        chg_taille=np.sort(np.append(np.append(temps_sim[j,i],temps_reel[i]),[2]))-1e-5
        for k in chg_taille:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            else: res+=tailles_sim[j,i,1]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            else: res-=tailles_reel[1]
            RMSD_chg[j,i]+=res**2
        RMSD_chg[j,i]=(RMSD_chg[j,i]/len(chg_taille))**0.5
print("Décroissance :")
print("RMSD linéaire :")
print(RMSD_lin)
print("RMSD log :")
print(RMSD_log)
print("RMSD changements de taille :")
print(RMSD_chg)

# Affichage RMSD=f(n,t)

n=np.array([3,2,1])
t=np.array([-3,-2,-1])

# Create a meshgrid for plotting
n_grid, t_grid = np.meshgrid(n, t)

# Plotting the 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(n_grid, t_grid, RMSD_log, edgecolor='k', alpha=0.8)
droite = ax.plot(n, t, [RMSD_log[0,0],RMSD_log[1,1],RMSD_log[2,2]], color="red")


# Bottleneck

temps_sim=np.array([[[breakpoints[26],breakpoints[29]],[breakpoints[24],breakpoints[28]]\
,[breakpoints[25],breakpoints[29]]],[[breakpoints[1],breakpoints[25]],\
[breakpoints[17],breakpoints[32]],[breakpoints[13],breakpoints[32]]]\
,[[breakpoints[25],breakpoints[34]],[breakpoints[17],breakpoints[32]]\
,[breakpoints[9],breakpoints[33]]]])
tailles_sim=np.array([[[973689.316905,227726.111353,816165.339926],[716280.224858,215990.127610,771438.996537]\
,[540229.554603,360624.156343,781788.987475]],[[998598.088022,998598.088022,500348.632125]\
,[1004731.904821,497942.380401,891881.217726],[687329.061571,497720.145056,891447.463206]]\
,[[999873.366651,506110.552563,1247676.812971],[1000405.263226,498677.724367,891819.293643]\
,[998732.097046,500514.545070,996559.169108]]])/2e5
temps_reel=np.array([[0.1,0.5],[0.01,0.5],[0.001,0.5]])
tailles_reel=np.array([10,5,10])
RMSD_lin=np.zeros([3,3])
RMSD_log=np.zeros([3,3])
RMSD_chg=np.zeros([3,3])
for i in range(3):
    for j in range(3):
        #Linéaire
        for k in points_lin:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            elif k<temps_sim[j,i,1]:
                res+=tailles_sim[j,i,1]
            else: res+=tailles_sim[j,i,2]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            elif k<temps_reel[i,1]:
                res-=tailles_reel[1]
            else: res-=tailles_reel[2]
            RMSD_lin[j,i]+=res**2
        RMSD_lin[j,i]=(RMSD_lin[j,i]/len(points_lin))**0.5
        #Log
        for k in points_log:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            elif k<temps_sim[j,i,1]:
                res+=tailles_sim[j,i,1]
            else: res+=tailles_sim[j,i,2]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            elif k<temps_reel[i,1]:
                res-=tailles_reel[1]
            else: res-=tailles_reel[2]
            RMSD_log[j,i]+=res**2
        RMSD_log[j,i]=(RMSD_log[j,i]/len(points_log))**0.5
        #Changements de taille
        chg_taille=np.sort(np.append(np.append(temps_sim[j,i],temps_reel[i]),[2]))-1e-5
        for k in chg_taille:
            res=0
            if k<temps_sim[j,i,0]:
                res+=tailles_sim[j,i,0]
            elif k<temps_sim[j,i,1]:
                res+=tailles_sim[j,i,1]
            else: res+=tailles_sim[j,i,2]
            
            if k<temps_reel[i,0]:
                res-=tailles_reel[0]
            elif k<temps_reel[i,1]:
                res-=tailles_reel[1]
            else: res-=tailles_reel[2]
            RMSD_chg[j,i]+=res**2
        RMSD_chg[j,i]=(RMSD_chg[j,i]/len(chg_taille))**0.5
print("Bottleneck :")
print("RMSD linéaire :")
print(RMSD_lin)
print("RMSD log :")
print(RMSD_log)
print("RMSD changements de taille :")
print(RMSD_chg)

# Affichage RMSD=f(n,t)

n=np.array([3,2,1])
t=np.array([-3,-2,-1])

# Create a meshgrid for plotting
n_grid, t_grid = np.meshgrid(n, t)

# Plotting the 3D surface
fig2 = plt.figure(figsize=(10, 7))
ax = fig2.add_subplot(111, projection='3d')
surf = ax.plot_surface(n_grid, t_grid, RMSD_log, edgecolor='k', alpha=0.8)
droite = ax.plot(n, t, [RMSD_log[0,0],RMSD_log[1,1],RMSD_log[2,2]], color="red")



