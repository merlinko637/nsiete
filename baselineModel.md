# Riešenie 

Na základe rôznych zdrojov a návodov sme si určili, že pred implementáciou našej neurónovej siete, využijeme nejaké z existujúcich riešení, aby sme si odskúšali a nasimulovali, ako by mal náš program fungovať. 
Chceli sme teda, aby bolo možné na snímke identifikovať pozíciu EČV a nakresliť okolo nej tzv. bounding box. 

Identifikovali sme, že pre tento scenár bude vhodné použiť Tensorflow object detection API. Tu sme si zvolil architektúru Faster RCNN Inception v2. Pre natrénovanie vlastného modelu bolo potrebné zmeniť pôvodný 
konfiguračný súbor a nastaviť mu cesty k našim vygenerovaným TFRecordom, k našej label mape a nastaviť počet testovacích snímkov, ktoré máme v testovacom datasete. Následne sme mohli pomocou Object detection API začať tento model trénovať. 

Trénovanie bolo uskutočnené na CPU. Napriek tomu, že sme zo zvedavosti nechali model trénovať celú noc, veľmi dobré výsledky dával už po pomerne krátkom čase. Priebeh trénovania sme sledovali pomocou tensorboardu. 
Po trénovaní sme vyexportovali inferenčný graf z posledného vygenerovaného modelu. 

Na záver sme prevzali skript, ktorý bol upravený tak, aby používal náš natrénovaný model a na ňom sme si mohli ručne odskúšať funkčnosť nášho modelu. Skript sa nachádza v priečinku license_plate_detection ako license_plate_detection.py. Tento skript prejde všetky snímky v priečinku test_images a obrázky s detekovanou EČV vloží do test_output priečinka.

Do finálneho odovzdania plánujeme navrhnúť našu neurónovú sieť, ktorej architektúru si sami navrhneme a celý vyššie spomínaný postup bude realizovaný nad ňou.