# 🇮🇳 BHARTI Language Framework (BMC)
## 📂 Numeral System — Revised Master Copy (Version 2.0)

> **Author:** Emperor AD  
> **System:** Numeral System / संख्या प्रणाली  
> **Status:** Finalized & Locked  
> **Language:** Bharti Modern Code (BMC)  

---

## 1. Numeral System का उद्देश्य

BMC Numeral System का उद्देश्य:
1. भारतीय Numerical System की मूल संरचना को बनाए रखना।
2. BMC की Roman/Latin writing system के अनुसार spelling रखना।
3. संख्या को पढ़ने और बोलने में सरल रखना।
4. प्रत्येक numerical component को स्पष्ट रखना।
5. AI/Computer के लिए संख्या को आसानी से parse करने योग्य बनाना।
6. अनावश्यक रूप से जुड़े हुए लंबे numeral words से बचना।
7. एक ही numerical structure के लिए नियमित नियम रखना।
8. अनावश्यक exceptions से बचना।

---

## 2. Basic Digits — Final

* `0` = Jero
* `1` = Ek
* `2` = Do
* `3` = Tii
* `4` = Caa
* `5` = Pac
* `6` = Cha
* `7` = Sat
* `8` = Aat
* `9` = Nau

---

## 3. Tens — Final

* `10` = Das
* `20` = Biis
* `30` = Tiis
* `40` = Calis
* `50` = Pcas
* `60` = Sath
* `70` = Sttar
* `80` = Assi
* `90` = Nave

### Compound Numbers
दहाई और इकाई को अलग-अलग components के रूप में लिखा जाएगा।

* **उदाहरण:**
  * `21` = `Biis Ek`
  * `35` = `Tiis Pac`
  * `48` = `Calis Aat`
  * `99` = `Nave Nau`

---

## 4. Large Numerical Units

* `100` = Sao
* `1,000` = Wjar
* `1,00,000` = Lakh
* `1,00,00,000` = Karorq
* `10⁹` = Arab
* `10¹¹` = Kharab
* `10¹³` = Niil
* `10¹⁵` = Padam
* `10¹⁷` = Sankh
* `10¹⁹` = MahaSankh

> वर्तमान विस्तारित मानक सूची MahaSankh तक है। इससे आगे के ऐतिहासिक या नए मात्रकों को अलग से परिभाषित किया जा सकता है।

---

## 5. Space Separation Rule

प्रत्येक स्वतंत्र numeral component को अलग शब्द के रूप में लिखा जाएगा। हर component के बीच एक `SPACE` होगा।

* **गलत:** `Dasek`, `Daspac`, `Biistii`, `Naveaat`
* **सही:** `Das Ek`, `Das Pac`, `Biis Tii`, `Nave Aat`

---

## 6. Numeral Composition Rule

संख्या के components को उनके place-value के अनुसार बड़े से छोटे क्रम में लिखा जाएगा।

* **उदाहरण:**
  * `11` = `Das Ek`
  * `15` = `Das Pac`
  * `21` = `Biis Ek`
  * `35` = `Tiis Pac`
  * `123` = `Ek Sao Biis Tii`
  * `352` = `Tii Sao Pcas Do`

यहाँ प्रत्येक component अपनी निर्धारित numerical value बनाए रखेगा।

---

## 7. Implicit Ek Rule

यदि कोई large numerical unit स्वयं पूरी संख्या है और उसका multiplier `1` है, तो उसके पहले `Ek` नहीं लिखा जाएगा।

* **उदाहरण:**
  * `Sao` = 100
  * `Wjar` = 1,000
  * `Lakh` = 1,00,000
  * `Karorq` = 1,00,00,000

लेकिन compound number में `Ek` स्पष्ट रूप से लिखा जाएगा, जब वह किसी component का आवश्यक हिस्सा हो।
* **उदाहरण:** `Ek Sao Ek` = 101

---

## 8. Zero Rule

* `0` = Jero

`Jero` का उपयोग स्वतंत्र संख्या या गणितीय संदर्भ में किया जाएगा।

सामान्य cardinal numbers में ऐसे zero place-values को अलग से नहीं लिखा जाएगा जिनका कोई non-zero component नहीं है। शेष components का स्थान-मूल्य सुरक्षित रहना चाहिए।

* **उदाहरण:**
  * `100` = Sao
  * `1,005` = Ek Wjar Pac
  * `1,020` = Ek Wjar Biis
  * `1,200` = Ek Wjar Do Sao

---

## 9. Multiplier Rule

किसी बड़ी numerical unit से पहले आने वाला संख्या-component उस unit का multiplier होगा।

$$\text{Structure:} \quad \text{Multiplier} + \text{Large Numerical Unit}$$

* **उदाहरण:**
  * `Wjar` = 1,000
  * `Do Wjar` = 2,000
  * `Das Wjar` = 10,000
  * `Do Lakh` = 2,00,000
  * `Tii Karorq` = 3,00,00,000
  * `Pac Arab` = $5 \times 10^9$

यदि multiplier `1` है, तो Implicit Ek Rule लागू होगा (जैसे `Wjar`, न कि `Ek Wjar` — जब संख्या ठीक 1,000 हो)।

मिश्रित बड़ी संख्याओं में प्रत्येक component को उसके सही place-value के अनुसार लिखा जाएगा (जैसे 2,05,000 की रचना में 2 Lakh और 5 Thousand के components शामिल होंगे)।

---

## 10. Complex Numbers & Extended Format

अत्यंत बड़ी संख्याओं के लिए Kharab या उससे आगे के निर्धारित मात्रकों का उपयोग किया जा सकता है। 

सभी components के बीच `SPACE` रखा जाएगा। Multiplier Rule, Implicit Ek Rule और Numeral Composition Rule लागू होंगे।

---

## 11. Machine / AI Readability

Space-separated numeral components को अलग-अलग tokens के रूप में पहचाना जा सकेगा।

* **उदाहरण:** `Ek Sao Biis Tii`
* **Tokens:** `Ek` | `Sao` | `Biis` | `Tii`

हर token का अर्थ उसके निर्धारित numerical value और composition rules के अनुसार समझा जाएगा।

---
* **Project:** BHARTI Modern Code (BMC)
* **Framework:** Universal AI-Friendly Language System
