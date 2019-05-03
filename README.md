# Climed
Weather Station

                      Projet CLIMED : Station Météo


 


		
 Réalisé par : Sofiene Chaouch































Introduction générale 
Dans le cadre de ce projet, nous avons choisi de travailler sur une station météo. Ce projet a pour but de nous amener à travailler en équipe et en autonomie sur une réalisation d’une station météo intelligente. 
En effet, notre station devra effectuer des relevés d'humidité, de température, de luminosité et de vitesse du vent, pour ensuite les afficher sur une page web et un en utilisant un service cloud . 
Ce projet consiste à : 
• étudier et identifier les différents composants, 
• programmer les capteurs, 



Chapitre 1 : Etude bibliographique 
1.	Introduction 

Notre projet consiste à réaliser un dossier technique joint d’une conception d’une station météo. Une station météo est un appareil qui collecte des données liées à la météo et à l'environnement en utilisant de nombreux capteurs différents. Nous pouvons mesurer des différents indicateurs comme : Température, Humidité, vitesse du Vent, Pression barométrique, quantités du Pluie … 

2. Elaboration du cahier des charges 
Il s'agit d'une station météo automatique réalisant des acquisitions temps réel de mesures météorologiques et en capacité de les sauvegarder et/ou publier ou transmettre immédiatement vers un serveur dédié. 
La station météo doit, dans sa version la plus basique, réaliser des mesures de : 
 pression atmosphérique en Pascals ou hecto pascals (hPa) (précision <0.5hPa) 
 température en °C (précision < 0.2°C) 
 humidité relative en % de la saturation (précision <1%) 
 vitesse de vent en m/s (précision <0.1m/s) 
 direction du vent en degrés par rapport au Nord géographique (précision < 2 degrés) 
 Qualité d’air : PM10 ,  PM25

Les données de pluviométrie, de rayonnement, si elles sont disponibles, peuvent également être acquises. 

3. Etude du projet 
La station météo est un ensemble de capteurs qui enregistrent et fournissent des mesures physiques et des paramètres météorologiques liés aux variations du climat. 
3.1. Analyse fonctionnelle 
Il est nécessaire de faire son analyse fonctionnelle. Celle-ci est une démarche indispensable permettant de définir les besoins auxquels devra répondre le projet, et donc les solutions techniques à envisager en conséquence. Elle permet d'établir une base solide sur laquelle tout le projet reposera. L’analyse fonctionnelle se décompose en deux parties, qui ont chacune des fonctions bien distinctes et complémentaires : 
3.1.1. Analyse fonctionnelle externe 
C’est l’analyse du point de vue client ou utilisateur du produit, qui s’intéresse uniquement aux besoins auxquels répondre : ce sont les fonctions de service

3.2. Choix des composants 

Carte de développement : Raspberry pi 3 B+ :

                                    

DHT22 Capteur de Température et d'Humidité : 
Pour obtenir la température et l’humidité, nous avons utilisé Le DHT22, c’ est un capteur de très apprécié pour sa simplicité de mise en oeuvre et son coût peu élevé. Il ne requiert qu'une résistance de tirage et une alimentation 3V ou 5V pour fonctionner. 
Caractéristiques 
 Alimentation 3 à 5 V et E / S 2.5mA max utilisation actuelle lors de la conversion (lors de la demande de données) 
 Bon pour des lectures d'humidité de 0-100% avec une précision de 2-5% 
 Bon pour des lectures de température de -40 à 80 ° C Précision de ± 0,5 ° C 
 Pas plus de 0,5 Hz de fréquence d'échantillonnage (une fois toutes les 2 secondes) 
 Taille du corps 15.1mm x 25mm x 7.7mm 
 4 broches avec espacement de 0,1 " 
                                                                                                                                       

BMP180 capteur de la pression atmosphérique et de la température 
Les capteurs de pression barométriques mesurent la pression absolue de l'air autour d'eux. Cette pression varie avec le temps et l'altitude. Selon la façon dont vous interprétez les données, vous pouvez surveiller les changements de temps, mesurer l'altitude ou toute autre tâche nécessitant une lecture précise de la pression. 
Caractéristiques 
 Dimension du PCB : 10 x 12 x 2 mm (11mm de hauteur avec le connecteur droit soudé) Alimentation : de 3 à 5 Volts 
 Faible consommation : 5 μA pour 1 mesure par seconde 
 Plage de mesure de la pression atmosphérique : de 300-1100 hPa (jusqu’à 9000m au-dessus de niveau de la mer) 
 Précision de mesure : 0,03hPa – 0,25m d’altitude 
 Fonctionnement : de -40°C à +85°C 
                                                                                                                               
Pluviomètre 
Un pluviomètre est un instrument météorologique destiné à mesurer la pluie tombée pendant un intervalle de temps donné
                                                                                                                                           
WindSonic 
WindSonic mesure les temps pris pour qu'une impulsion ultrasonique du son circule du transducteur nord vers le transducteur sud, et le compare avec le temps nécessaire au déplacement d'une impulsion.
                                                                                            
                                                                                             


Capteur NOVA PM SDS 011 

Le capteur SDS 011 Le capteur SDS 011 est un capteur de qualité de l’air très récent mis au point par inovafit, une entreprise dérivée de l’université de Jinan (Shandong). Avec sa taille, il est probablement l'un des meilleurs capteurs en termes de précision: alors que d'autres capteurs ont tendance à vouloir réduire la taille du capteur, le SDS 011 a opté pour un compromis de taille lui permettant d'utiliser un ventilateur plus grand. Et plus le ventilateur est grand, meilleure est la qualité. 

                                                                                                                            






Specifications


Ceci est la spécification du SDS011. Il ne faut pas considérer toutes ces valeurs comme allant de soi, car il existe souvent une grande différence entre ce qui est dit possible et ce qui est réellement possible (et c’est pourquoi nous organisons toutes nos expériences).
Sortie: PM2,5, PM10
Gamme de mesure: 0.0-999.9μg / m3
Tension d'entrée: 5V
Courant maximum: 100mA
Courant de sommeil: 2mA
Temps de réponse1 seconde
Fréquence de sortie des données série: 1 fois / seconde
Résolution du diamètre des particules: ≤0.3μm
Erreur relative: 10%
Gamme de température: -20 ~ 50 ° C
Taille physique: 71mm * 70mm * 23mm

 



Site Web et Hébergement :
Domaine : lien
https://climed-aabbf.firebaseapp.com/

 
 

Hébergement : firebase Hosting
 

En local sur NGINX server 


 



Stocage et visualisation des donnée : 
Ubidots cloud service                                                                              
                                                                                             
	
