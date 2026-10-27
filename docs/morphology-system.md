# 🇮🇳 BHARTI Language Framework (BMC)
## 📂 Morphology System — Master Specification (Version 2.0)

> **Author:** Emperor AD  
> **System:** Morphology System / रूपविज्ञान प्रणाली  
> **Status:** Finalized & Locked  
> **Core Principle:** Non-Concatenative Isolation & Zero-Internal-Derivation  

---

## 1. रूपविज्ञान — परिभाषा (Definition)

BMC Morphology वह system है जो ROOT में approved Morphology Markers जोड़कर नए words या concepts का निर्माण करती है।

### मूलभूत नियम:
1. प्रत्येक ROOT स्वयं एक meaningful Concept है।
2. ROOT किसी एक grammatical category (Noun, Verb, Adjective) तक permanently limited नहीं होता।
3. Morphology Markers, ROOT या पहले से बने meaning में एक निर्धारित प्रकार का logical change करते हैं।
4. Gender, Number, Person, Tense, Aspect या Case के कारण ROOT के भीतर कोई mandatory internal change नहीं होता।
5. Tense और Aspect पूरी तरह separate Auxiliary System के अंतर्गत आते हैं।
6. Negation (`Na`) और Plural (`'s`) इस system से पूरी तरह बाहर हैं, क्योंकि वे independent systems के parts हैं।

---

## 2. ROOT — Nature & Usage

ROOT एक basic meaningful unit है, जो किसी Action, State, Object, Person, Quality, Idea या अन्य Concept को express कर सकता है।

1. ROOT किसी एक grammatical category तक permanently restricted नहीं होता।
2. Sentence में ROOT का grammatical function उसके usage और sentence structure पर depend करता है।
3. ROOT का use Subject, Object या Verb की तरह हो सकता है, यदि उसका meaning और sentence structure इसकी अनुमति देते हैं।
4. Verb Root कभी conjugate नहीं होता। इसके सभी Tense और Aspect अलग Auxiliary System द्वारा निर्धारित किए जाते हैं।

---

## 3. Morphology Markers — Iron-Clad Definitions

### 3.1. ta — STATE / QUALITY
* **Core Function:** ROOT या उससे बने meaning से ऐसा Concept बनाना जो किसी State, Condition या Quality को express करे।
* **Strict Boundary:** यह सीधे किसी Process (`an`), Manner (`vat`) या Person/Doer (`va`) को express नहीं करता।
* **Mutually Exclusive:** एक ही derived form में `ta` और `ik` का एक साथ use नहीं हो सकता।

### 3.2. va — PERSON / DOER
* **Core Function:** किसी ROOT, Action या Concept से associated Person या Doer को indicate करने वाला word बनाना।
* **Strict Boundary:** इसका meaning automatically Expert, Professional या Skilled Person नहीं होता।
* **Final Marker Position:** `va` हमेशा अंतिम Derivational Marker होगा। इसके बाद कोई दूसरा Derivational Marker नहीं आ सकता।

### 3.3. an — PROCESS / ACTION
* **Core Function:** ROOT या उससे बने meaning को किसी Dynamic Action, Process या Event के रूप में express करना।
* **Strict Boundary:** यह किसी Static State (`ta`), Characteristic (`ik`) या Manner (`vat`) को directly express नहीं करता। यह किसी Action, Process या Event का dynamic concept प्रस्तुत करता है।

### 3.4. ik — CHARACTERISTIC
* **Core Function:** ऐसा Characteristic या Property बनाने वाला Marker जिससे किसी दूसरे Noun या suitable Concept को modify या describe किया जा सके।
* **Strict Boundary:** यह स्वतंत्र State (`ta`) नहीं है।
* **Mutually Exclusive:** एक ही derived form में `ik` और `ta` का एक साथ use नहीं हो सकता।

### 3.5. vat — MANNER / METHOD
* **Core Function:** यह indicate करता है कि कोई Action या Process किस Method, Manner या Way से perform किया जाता है।
* **मुख्य प्रश्न:** "कैसे?" / "किस तरीके से?"
* **Strict Boundary:** यह Person/Doer (`va`), Process (`an`) या Capability (`abl`) को directly express नहीं करता।

### 3.6. abl — CAPABILITY / ABILITY
* **Core Function:** किसी Action को perform करने की Capability, Ability या Potential को express करना।
* **मुख्य अर्थ:** "कर सकने योग्य" / "करने की क्षमता"
* **Strict Boundary:** किसी Action को करने की Ability और वास्तव में उस Action का होना अलग-अलग concepts हैं। `abl` स्वयं Process (`an`) या Abundance (`ful`) को express नहीं करता।

### 3.7. ful — ABUNDANCE / FULL OF
* **Core Function:** किसी Quality, Element या Characteristic की Abundance, Fullness या भरपूर Presence को express करना।
* **Strict Boundary:** यह Capability (`abl`) या Process (`an`) को directly express नहीं करता।
* **Fixed Order:** जब `abl` और `ful` दोनों का use valid हो, तब `abl` हमेशा `ful` से पहले आएगा।

---

## 4. Fixed Derivational Order (निश्चित व्युत्पत्ति क्रम)

एक से अधिक Morphology Markers के जुड़ने का निर्धारित और अपरिवर्तनीय क्रम:

$$\text{[ROOT]} + \text{[ta / ik]} + \text{[vat]} + \text{[an]} + \text{[abl]} + \text{[ful]} + \text{[va]}$$

### मुख्य नियम:
1. Markers को मनमाने क्रम में नहीं लगाया जा सकता।
2. `ta` और `ik` एक ही derived form में mutually exclusive हैं।
3. `va` हमेशा अंतिम Derivational Marker होगा।
4. `va` के बाद कोई दूसरा Derivational Marker नहीं आ सकता।
5. Derivation के बाद Plural (`'s`) और Case Markers अपनी independent grammatical systems के rules के अनुसार आ सकते हैं।

---

## 5. Compound Concept (संयुक्त अवधारणा)

दो independent ROOTs को जोड़कर एक Compound Concept बनाया जा सकता है।

$$\text{[ROOT]} + \text{[ROOT]} \rightarrow \text{COMPOUND CONCEPT}$$

### Rules:
1. दो ROOTs के combination से एक नया Compound Concept बनाया जा सकता है।
2. Compound बनने के बाद पूरे Compound पर valid Morphology Markers लगाए जा सकते हैं।

---
* **Project:** BHARTI Modern Code (BMC)
* **Framework:** Universal AI-Friendly Language System
