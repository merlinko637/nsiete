

## Faster R-CNN

Faster R-CNN je vylepšená verzia jej predchodcu Fast R-CNN a tá je zase vylepšená verzia obyčajnej R-CNN. Všetky 3 typy týchto architektúr fungujú na princípe „regiónov“, na ktoré sa vstupný obrázok rozdelí. Pri prvých dvoch typoch sa na určenie regiónov používa takzvané „selektívne hľadanie“, pri ktorom sa určí cca 2000 regiónov, ktoré sa ďalej pošlú do konvolučnej neurónovej siete.

Faster R-CNN je vylepšená práve o určovnie regiónov, ktoré je pomocou „selektívneho hľadania“ veľmi pomalé. V tomto prípade regióny určí samostatná neurónová sieť, ktorá je naučená, ako obrázok rozdeliť na regióny. Následne je pomocou „RoI pooling“ vrstvy obrázok s regiónmi zmenšený a sú predikované objekty v jednotlivých regiónoch.

Architektúru Faster R-CNN môžme vidieť na obrázkoch nižšie.


<img src="img/fasterRCNN.PNG" alt="RCNN" width="500"/>
<img src="img/fasterrcnnModel.PNG" alt="RCNN1" width="700"/>



## YOLO

You Only Look Once architektúra pozerá na celý obrázok narozdiel od predchádzajúcich, ktoré hľadali objekty len vrámci určených regiónov. V tomto prípade, ako už z názvu vyplýva, sa na obrázok neurónová sieť pozrie len raz a pri tomto zároveň odhadne bounding boxy a aj jednotlivé objekty v týchto boxoch. Dosiahne to pomocou rozdelenia vstupného obrázku na mriežku SxS. Pre každý z bounding boxov potom vytvorí mapu pravdepodobností tried. Tie, ktoré majú pravdepodobnosť nad určitou hranicou sú v konečnom dôsledku vybrané za správne a je v nich detekovaný objekt.
Z tohto dôvodu má však tento algoritmus problém s detekciou malých objektov vrámci obrázku. Oproti predchádzajúcim algoritmom je však rádovo rýchlejší. 

To, ako pracuje YOLO spolu s jeho architektúrou môžme vidieť na obrázkoch nižšie.

<img src="img/yolo.PNG" alt="YOLO" width="500"/>
<img src="img/yoloModel.PNG" alt="YOLO1" width="700"/>


Porovnanie týchto dvoch architektúr (+ R-CNN a Fast R-CNN) môžme vidieť na grafe, ktorý nám ukazuje závislosť presnosti a rýchlosti detekcie objektu.

<img src="img/porovnanie.PNG" alt="YOLO1" width="700"/>


## Vlastná architektúra

V predchádzajúcom odovzdaní sme mali implementovanú prevzatú Faster R-CNN architektúru, ktorú sme natrénovali na našom datasete opísanom v Analýze dát. V tomto odovzdaní sme sa snažili implementovať vlastnú neurónovú sieť s Faster R-CNN architektúrou, ktorej kód je možné vidieť v súbore ```CustomNN.ipynb```. Pri implementácii tejto vlastnej neurónovej siete sme však narazili na veľa problémov, z ktorých sa nám viaceré odstrániť podarilo, no niektoré sme sami odstrániť nevedeli. Vzhľadom na to, že sa na našu tému na internete nedali nájsť žiadne custom neurónové siete a všetky tutoriály ku tejto téme využívali už niektoré z predprogramovaných architektúr a API, nevedeli sme sa so vzniknutými problémami popasovať. Najväčším problémom pre nás bolo vytvoriť vhodný formát vstupných dát (X, Y), ktorému by fit funkcia rozumela. Snažili sme sa obrázky reshape-ovat, meniť im rozmery, ale neúspešne. Z tohto dôvodu sme sa rozhodli použiť už predprogramované architektúry a spraviť ich porovnanie.


## Trénovanie Faster R-CNN

Pri trénovaní vlastného modelu pre architektúru Faster R-CNN sme vychádzali z nasledovného tutoriálu https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85. Na snímke obrazovky z Tensorboardu je možné vidieť priebeh trénovania, konkrétne metriku Loss. Tu je možné vidieť viacero grafov, z toho prvé 4 zobrazujú metriku Loss pre jednotlivé časti priebehu algoritmu (prvé dve pre klasifikáciu regiónov a druhé dve sú pre Region Proposal Network) a posledná zobrazuje celkovú Loss funkciu. 
Trénovanie prebiehalo približne 7 hodín a je možné vidieť, že približne druhá polovica trénovania bola už zbytočná lebo model sa už ďalej nevylepšoval. Môžeme pozorovať, že najnižšia dosiahnutá hodnota je približne 0,022. 

<img src="img/FasterRCNN-Tensorboard.PNG" alt="Faster R-CNN tensorboard"/>

## Trénovanie YOLO

Trénovanie vlastného modelu pre architektúru YOLO prebiehalo podľa návodu https://blog.insightdatascience.com/how-to-train-your-own-yolov3-detector-from-scratch-224d10e55de2. Bol použitý rovnaký vstupný dataset, teda približne 100 obrázkov. Trénovanie prebiehalo počas noci a zastavilo sa automaticky po 72 epochách, kedy model dosiahol Loss o výške 12.5799 a už sa nevylepšoval. Táto hodnota je výrazne odlišná od tej, dosiahnutej pri predošlej architektúre. Vydedukovali sme, že YOLO pravdepodobne potrebuje o niečo väčší dataset pre dosiahnutie lepšej úspešnosti než Faster R-CNN. Napriek tomu, dokázal natrénovaný model plniť svoju úlohu relatívne dobre. 

Výstup z trénovania je možné vidieť v súbore /training/YOLO_training_logs.txt

## Popis navrhnutýchých experimentov

V rámci nášho experimentu, sme chceli jednotlivé architektúry porovnať na zariadení Nvidia Jetson Nano, ktoré bolo spomínané v našom návrhu riešenia. Najprv sme sa pokúšali spojazdniť YOLO architektúru, nakoľko sfunkčniť ju na bežnom PC bolo oveľa jednoduchšie než Faster R-CNN, nakoľko nevyžadovala tak zdĺhavý proces inštalácie.

Snaha bola vytvoriť Docker image, ktorý by mal pripravené prostredie tak, aby bolo možné danú implementáciu YOLO na ňom spustiť. To sa nám aj podarilo, no žiaľ spojazdniť tento image na spomínanom zariadení z neznámych dôvodov opakovane zlyhávalo. To nám zmarilo nádej, akýmkoľvek spôsobom porovnať tieto architektúry na tomto zariadení a tak sme sa teda museli uspokojiť s porovnaním na PC s integrovanou grafickou kartou. 

## Vyhodnotenie experimentov

Faster R-CNN

```test_images\1.jpg Time spent: 5.649sec
test_images\10.jpg Time spent: 1.405sec
test_images\11.jpg Time spent: 1.584sec
test_images\2.jpg Time spent: 1.565sec
test_images\3.jpg Time spent: 1.541sec
test_images\4.jpg Time spent: 1.489sec
test_images\5.jpg Time spent: 1.551sec
test_images\7.jpg Time spent: 1.592sec
test_images\8.jpg Time spent: 1.552sec
test_images\9.jpg Time spent: 1.584sec
```

YOLO 

```
test_images\1.jpg Time spent: 2.105sec
test_images\10.jpg Time spent: 1.139sec
test_images\11.jpg Time spent: 1.136sec
test_images\2.jpg Time spent: 1.143sec
test_images\3.jpg Time spent: 1.130sec
test_images\4.jpg Time spent: 1.139sec
test_images\5.jpg Time spent: 1.135sec
test_images\7.jpg Time spent: 1.127sec
test_images\8.jpg Time spent: 1.157sec
test_images\9.jpg Time spent: 1.123sec
```

Porovnávali sme teda čas, potrebný pre vyhodnotenie jednotlivých snímkov a skóre, priradené jednotlivým predikciám. 

Výstup je možno vidieť v priečinku /evaluation/output_images

Vyhodnotenie experimentu
Z výsledkov experimentu je možné pozorovať, že tak, ako internetové zdroje tvrdili, architektúra YOLO je naozaj o niečo rýchlejšia. Skóre bolo však pri jednotlivých predikciách rádovo nižšie než pri architektúre Faster R-CNN. To však nie je nič prekvapivé vzhľadom na výslednú hodnotu Loss funkcie YOLO modelu. 

Vstupom bolo 10 snímkov automobilov, ktoré neurónová sieť pred tým nikdy nevidela. Výstupom sú tieto obrázky s označeným miestom, kde sa EČV nachádza. V prípade Faster R-CNN môžeme vidieť, že v prípade niektorých obrázkoch bola predikcia neúspešná, teda na obrázku nebola EČV identifikovaná napriek tomu, že sa tam nachádza. To mohlo byť spôsobené tým, že automobily boli v o niečo väčšej vzdialenosti než väčšina tých, v trénovacom datasete. 
