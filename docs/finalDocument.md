

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