# Théorie

Limite de 1/n :

Quand on est en temps court, on observe que l’effet des branches portant 2 feuilles ou plus est négligeable devant celui des branches portant 1 feuille. On a donc une seule équation, ce qui limite le nombre d’inconnues qu’on peut chercher. La limite de 1/n correspond à la limite où les branches à plus d’1 feuille ne sont plus négligeables

On a la même quantité d’informations en regardant 10 fois plus loin avec 10 fois moins d’échantillons dans un cadre théorique parfait sans bruit avec scénario parfaitement adapté. La limite est d’ordre 1/n

Il faut avoir un theta de l’ordre du nombre de sites qu’on veut (du genre $10^6$ pas mal d’un point de vue biologique, on prend en gros $10$ fois la taille efficace)

La méthode d’Abdel est plus complète que stairway plot car elle explore toutes les possibilités au lieu de faire l’euristique, et elle utilise une résolution analytique sur les espérances des tailles de branche étage par étage au lieu d’une espérance sur tous les étages

Tester avec des tailles de génome plus faible (actuellement $10^9$, essayer des ordres de grandeur inférieurs)

![[Présentation_SFS.pdf]]

# Plan d’expérience

Scénarios à tester : tous les croisements entre $n=\{10,100,1000\}$ et les scénarios 1 changement $t=\{0.001,0.01,0.1\}$ avec croissance ou décroissance d’ordre 2 et même chose avec un bottleneck inversé, temps ancien à $t=0.5$.
# Commandes réalisées

## Génération des SFS avec past

#### Deux blocs, décroissance

##### $t=10^{-1}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,2 -o SFS_generated/decrease_2/sfs_n10_cst_e_1_dec.txt

##### $t=10^{-1}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,2 -o SFS_generated/decrease_2/sfs_n100_cst_e_1_dec.txt

##### $t=10^{-1}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,2 -o SFS_generated/decrease_2/sfs_n1000_cst_e_1_dec.txt

##### $t=10^{-2}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,2 -o SFS_generated/decrease_2/sfs_n10_cst_e_2_dec.txt

##### $t=10^{-2}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,2 -o SFS_generated/decrease_2/sfs_n100_cst_e_2_dec.txt

##### $t=10^{-2}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,2 -o SFS_generated/decrease_2/sfs_n1000_cst_e_2_dec.txt

##### $t=10^{-3}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,2 -o SFS_generated/decrease_2/sfs_n10_cst_e_3_dec.txt

##### $t=10^{-3}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,2 -o SFS_generated/decrease_2/sfs_n100_cst_e_3_dec.txt

##### $t=10^{-3}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,2 -o SFS_generated/decrease_2/sfs_n1000_cst_e_3_dec.txt

#### Deux blocs, croissance

##### $t=10^{-1}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5 -o SFS_generated/increase_2/sfs_n10_cst_e_1_croiss.txt

##### $t=10^{-1}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5 -o SFS_generated/increase_2/sfs_n100_cst_e_1_croiss.txt

##### $t=10^{-1}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5 -o SFS_generated/increase_2/sfs_n1000_cst_e_1_croiss.txt

##### $t=10^{-2}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5 -o SFS_generated/increase_2/sfs_n10_cst_e_2_croiss.txt

##### $t=10^{-2}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5 -o SFS_generated/increase_2/sfs_n100_cst_e_2_croiss.txt

##### $t=10^{-2}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5 -o SFS_generated/increase_2/sfs_n1000_cst_e_2_croiss.txt

##### $t=10^{-3}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5 -o SFS_generated/increase_2/sfs_n10_cst_e_3_croiss.txt

##### $t=10^{-3}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5 -o SFS_generated/increase_2/sfs_n100_cst_e_3_croiss.txt

##### $t=10^{-3}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5 -o SFS_generated/increase_2/sfs_n1000_cst_e_3_croiss.txt

#### Trois blocs, bottleneck inversé

##### $t=10^{-1}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_1_inv_bot.txt

##### $t=10^{-1}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_1_inv_bot.txt

##### $t=10^{-1}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_1_inv_bot.txt

##### $t=10^{-2}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_2_inv_bot.txt

##### $t=10^{-2}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_2_inv_bot.txt

##### $t=10^{-2}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_2_inv_bot.txt

##### $t=10^{-3}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_3_inv_bot.txt

##### $t=10^{-3}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_3_inv_bot.txt

##### $t=10^{-3}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,2,1 -o SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_3_inv_bot.txt

#### Trois blocs, bottleneck

##### $t=10^{-1}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n10_cst_e_1_bot.txt

##### $t=10^{-1}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5, -o SFS_generated/bottleneck_2/sfs_n100_cst_e_1_bot.txt

##### $t=10^{-1}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.1,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n1000_cst_e_1_bot.txt

##### $t=10^{-2}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n10_cst_e_2_bot.txt

##### $t=10^{-2}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n100_cst_e_2_bot.txt

##### $t=10^{-2}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.01,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n1000_cst_e_2_bot.txt

##### $t=10^{-3}$, $n=10$

./bin/simulation -n 10 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n10_cst_e_3_bot.txt

##### $t=10^{-3}$, $n=100$

./bin/simulation -n 100 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n100_cst_e_3_bot.txt

##### $t=10^{-3}$, $n=1000$

./bin/simulation -n 1000 -l 1000000000 -t 0.001 -f 0 -m constant_piecewise -p 0.001,0.5,0.5,1 -o SFS_generated/bottleneck_2/sfs_n1000_cst_e_3_bot.txt

## Inférence des scénarios avec PASTII

#### Deux blocs, décroissance

##### $t=10^{-1}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n10_cst_e_1_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n10_cst_e_1_dec/ -o 0 -c 3

##### $t=10^{-1}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n100_cst_e_1_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n100_cst_e_1_dec/ -o 0 -c 3

##### $t=10^{-1}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n1000_cst_e_1_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n1000_cst_e_1_dec/ -o 0 -c 3

##### $t=10^{-2}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n10_cst_e_2_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n10_cst_e_2_dec/ -o 0 -c 3

##### $t=10^{-2}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n100_cst_e_2_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n100_cst_e_2_dec/ -o 0 -c 3

##### $t=10^{-2}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n1000_cst_e_2_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n1000_cst_e_2_dec/ -o 0 -c 3

##### $t=10^{-3}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n10_cst_e_3_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n10_cst_e_3_dec/ -o 0 -c 3

##### $t=10^{-3}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n100_cst_e_3_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n100_cst_e_3_dec/ -o 0 -c 3

##### $t=10^{-3}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/decrease_2/sfs_n1000_cst_e_3_dec.txt -p ../inf/SFS_generated/decrease_2/sfs_n1000_cst_e_3_dec/ -o 0 -c 3

#### Deux blocs, croissance

##### $t=10^{-1}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n10_cst_e_1_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n10_cst_e_1_croiss/ -o 0 -c 3

##### $t=10^{-1}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n100_cst_e_1_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n100_cst_e_1_croiss/ -o 0 -c 3

##### $t=10^{-1}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n1000_cst_e_1_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n1000_cst_e_1_croiss/ -o 0 -c 3

##### $t=10^{-2}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n10_cst_e_2_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n10_cst_e_2_croiss/ -o 0 -c 3

##### $t=10^{-2}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n100_cst_e_2_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n100_cst_e_2_croiss/ -o 0 -c 3

##### $t=10^{-2}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n1000_cst_e_2_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n1000_cst_e_2_croiss/ -o 0 -c 3

##### $t=10^{-3}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n10_cst_e_3_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n10_cst_e_3_croiss/ -o 0 -c 3

##### $t=10^{-3}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n100_cst_e_3_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n100_cst_e_3_croiss/ -o 0 -c 3

##### $t=10^{-3}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/increase_2/sfs_n1000_cst_e_3_croiss.txt -p ../inf/SFS_generated/increase_2/sfs_n1000_cst_e_3_croiss/ -o 0 -c 3

#### Trois blocs, bottleneck inversé

##### $t=10^{-1}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_1_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_1_inv_bot/ -o 0 -c 3

##### $t=10^{-1}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_1_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_1_inv_bot/ -o 0 -c 3

##### $t=10^{-1}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_1_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_1_inv_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_2_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_2_inv_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_2_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_2_inv_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_2_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_2_inv_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_3_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n10_cst_e_3_inv_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_3_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n100_cst_e_3_inv_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_3_inv_bot.txt -p ../inf/SFS_generated/inv_bottleneck_2/sfs_n1000_cst_e_3_inv_bot/ -o 0 -c 3

#### Trois blocs, bottleneck

##### $t=10^{-1}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n10_cst_e_1_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n10_cst_e_1_bot/ -o 0 -c 3

##### $t=10^{-1}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n100_cst_e_1_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n100_cst_e_1_bot/ -o 0 -c 3

##### $t=10^{-1}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n1000_cst_e_1_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n1000_cst_e_1_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n10_cst_e_2_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n10_cst_e_2_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n100_cst_e_2_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n100_cst_e_2_bot/ -o 0 -c 3

##### $t=10^{-2}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n1000_cst_e_2_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n1000_cst_e_2_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=10$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n10_cst_e_3_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n10_cst_e_3_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=100$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n100_cst_e_3_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n100_cst_e_3_bot/ -o 0 -c 3

##### $t=10^{-3}$, $n=1000$

bash past.sh --sfs ../past/SFS_generated/bottleneck_2/sfs_n1000_cst_e_3_bot.txt -p ../inf/SFS_generated/bottleneck_2/sfs_n1000_cst_e_3_bot/ -o 0 -c 3

## Comparaison graphique des scénarios inférés et théoriques avec PASTII


# Résultats
