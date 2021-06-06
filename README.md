# DAT0x02SignalSpaning
This repository is from our bachelor thesis, "Detection and localization of illicit wireless communication in an exam room through passive signal reconnaissance"


## System Requirements (Currently)

* Python 3.9.5
* 4 computer devices
* Spyder - Anaconda (Recommended editor)
* Wi-Fi 2.4 router
* Ethernet cable 
* Wireshark (latest version)
* Airmon-ng

## Compile & Run the system

För att köra systemet placeras tre bärbara datorer ut i rummet som en triangel, dessa bärbara datorer refereras som ankare hädanefter. En fjärde dator som används som server, som har linux som operativ system krävs även. Ett lokalt nätverk måste kopplas upp, i projektet användes mobil nät för att skapa ett lokalt nätverk tillsammans med en router. Det spelar ingen roll hur ett lokalt nätverk skapas, men det måste finnas en router med åtminstone fyra lan-portar. Ankarna och servern behöver sedan kopplas med ethernet kablar till lan-portarna hos routern. Därefter placeras de bärbara datorerna i monitorläge med hjälp av airmon. Med airmon går det även att bestämma vilka wifi-kanaler man vill lyssna på, alternativt om man vill lyssna på alla wifi-kanaler. Därefter uppskattas koordinater för ankarna med valfria mätinstrument i rummet. Dessa koordinater behöver skrivas in i variablerna point1, point2, point3 i server filen. Vilken punkt som är vilken är inte viktigt, däremot i funktionen iptopoint i server filen behöver man skriva i den lokala ip-adressen som respektive ankare har för respektive punkt. Klienten behöver också konfigureras genom att variabeln host i filen wiresharkhandler.py som finns i projektets github repo i system mappen behöver sättas lika med serverns lokala ip-adress. Sedan startas server.py som finns i samma map som tidigare på server datorn. Därefter startas wiresharkhandler.py på varje ankare och när alla tre ankare har startat kommer resultatet att visas i det grafiska gränssnittet på server datorn. 

To set up the system you'll need to:

1. Set up monitor mode on each computer device
2. Connect the ethernet cables from each computer to the router
3. The selected computer which will act as the server must firstly run the server.py file. (Server computer)
4. The other 3 computers runs the wiresharkHandler.py file. (Anchor computer)

If instructions are followed correctly, data will start to collect.


