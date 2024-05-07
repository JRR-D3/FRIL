# FRIL
Kods un citas daļas priekš FRIL (Fast-Responce Image Loader)

<h4 align="center">FRIL (Fast-Response Image Loader) - metode digitālo mākslas darbu attēlošanai.</h4>

<p align="center">
  <a href="#kas-tas-ir">Key Kas tas ir?</a> •
  <a href="#Pielietotās-tehnoloģijas">Pielietotās tehnoloģijas</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## Kas tas ir
FRIL ir ātrs attēlu lādētājs, kas izmanto 128X64 bitu oled ekrānu lai attēlotu pbm formāta attēlus. Signāls tiek padots no RFID sensora kad tam tuvumā tiek pielikta kartiņa kam ir piesaistīts NFC dati. Katrs attēls tiek saglabātas uz paša raspberry pi pico.

## Pielietotās tehnoloģijas
Priekš darbības ir nepieciešamas sekojošās detaļas:
* Raspberry Pi pico
* I2C oled displejs
* MFRC522 RFID lasītājs

![screenshot](https://cdn.discordapp.com/attachments/835944990122573836/1233465100292198501/image.png?ex=663b0924&is=6639b7a4&hm=ee73f2001a1c7d2ce5663615d5ece159c108fadb1afe91fe27709f4ec3912d2a&)
(Attēls 1)

## Lietošanas inkstruktāža

### Koda instalēšana un palaišana

*Lejupieldādēt kodu.
*Lavienot raspberry pi pico ar datoru un ievietoto kodu uz tā. 
*Tad pēc koda ievietošanas pēc dotajiem piniem kodā ir jāsaliek shēma ko var redzēt attēlā 1.
*Kodu ir vēlams palaist caur thonny programmu.

### Savas kertes iestatīšana

* Programma konsolē dod ziņu kāda karte tika noskenēta (arī gadījumos, kad karte nav atpazīta)
* Pieliekot programmai nezināmu karti, konsolē rodas tas ID, ko var nokopēt un pielietot kodā, kur var tai piešķirt savu attēlu/animāciju

### Programmas funkcionalitāte

*Spēj lasīt NFC ID  un uzrādīt to konmsolē.
*Oled ekrānā uzrāda atticīgo attēlo atkarībā no piesaistītās kartes NFC ID.
*Spēj uzrādīt animācijas kamēr tiek uzturēts attiecīgais NFC signāls.

## Risinājuma ierobežojumi

* Koda palaišanai ir nepieciešams dators
* Risinājumā nav implementāts akumulators
* Nepieciešamība manuāli mainīt kodu priekš saviem attēliem vai kartes ID
* Ierobežota krātuve kas var uzturēt dažus mazas izsķirt spējas attēlus.
* 1 bita displejs (binārs signāls)
  
## Atsauces
* Pielietotā biblioteka - MFRC522 ( https://github.com/mdxs/MFRC522 )
