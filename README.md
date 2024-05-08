# Fast Response Image Loader (FRIL)
Kods un citas daļas priekš FRIL

<h4 align="center">FRIL - metode digitālo mākslas darbu attēlošanai.</h4>

<p align="center">
  <a href="#kas-tas-ir">Key Kas tas ir?</a> •
  <a href="#pielietotās-tehnoloģijas">Pielietotās tehnoloģijas</a> •
  <a href="#lietošanas-inkstrukcijas">Lietošanas instrukcijas</a> •
  <a href="#programmas-funkcionalitāte">Programmas funkcionalitāte</a> •
  <a href="#risinājuma-ierobežojumi">Risinājuma ierobežojumi</a> •
  <a href="#atsauces">Atsauces</a>
</p>

## Kas tas ir
FRIL ir ātrs attēlu lādētājs, kas izmanto 128X64 bitu oled ekrānu lai attēlotu pbm formāta attēlus. Signāls tiek padots no Rādiofrekvences Identifikātora (RFID) sensora kad tam tuvumā tiek pielikta kartiņa kam ir piesaistīts Near Field Communication (NFC) dati. Katrs attēls tiek saglabātas uz paša raspberry pi pico.

## Pielietotās tehnoloģijas
Priekš darbības ir nepieciešamas sekojošās detaļas:
* Raspberry Pi pico
* I2C oled displejs
* MFRC522 RFID lasītājs

![screenshot](https://cdn.discordapp.com/attachments/835944990122573836/1233465100292198501/image.png?ex=663c5aa4&is=663b0924&hm=02a7c345a92161eaac2df1abc1a6c77ad48d819323205c47a0c3d37907e48729&)

(Attēls 1)

## Lietošanas inkstrukcijas

### Koda instalēšana un palaišana

* Lejupieldādēt kodu.
* Savienot Raspberry pi pico pie datora un augšipielādēt failus 
* Pirms koda palaišanas, vajag saslēgt ierīces pēc dotās shēmas (skat. att.1)
* Kodu ir vēlams palaist caur Thonny programmu.

### Savas kertes iestatīšana

* Programma konsolē dod ziņu kāda karte tika noskenēta (arī gadījumos, kad karte nav atpazīta)
* Pieliekot programmai nezināmu karti, konsolē rodas tas ID, ko var nokopēt un pielietot kodā, kur var tai piešķirt savu attēlu/animāciju

## Programmas funkcionalitāte

* Spēj lasīt NFC ID  un uzrādīt to konmsolē.
* Oled ekrānā uzrāda atticīgo attēlu atkarībā no piesaistītās kartes NFC.
* Spēj uzrādīt animācijas kamēr tiek uzturēts attiecīgais NFC signāls.

## Risinājuma ierobežojumi

* Koda palaišanai ir nepieciešams dators
* Risinājumā nav implementāts akumulators
* Nepieciešamība manuāli mainīt kodu priekš saviem attēliem vai kartes ID
* Ierobežota krātuve, kas var uzturēt dažus mazas izsķirtspējas attēlus.
* 1 bita displejs (binārs signāls)
  
## Atsauces
* Pielietotā biblioteka - MFRC522 ( https://github.com/mdxs/MFRC522 )
* Thonny mājaslapa - https://thonny.org/
