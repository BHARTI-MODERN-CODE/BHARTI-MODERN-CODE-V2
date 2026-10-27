"""
============================================================
 BHARTI Modern Language Framework - Core Grammar Engine
 Author: Emperor AD
============================================================
 Description:
 Yeh core engine script BHARTI bhasha ke mukhya niyamo 
 ko programmatically validate aur process karne ke liye hai.
 
 Key Principles Implemented:
 - 1 Sound = 1 Symbol & No Pronunciation Exceptions
 - No Schwa (/ə/) Sound
 - Regular Grammar (No verb changes by person/number)
 - Separate Tense & Aspect markers (ha, tha, ga)
 - Universal Question Structure ('Ki' at start)
 - Direct Negation Rule ('Na' attached to verb)
 - Subject + Object + Verb (SOV) Structure
============================================================
"""

class BhartiLanguageEngine:
    def __init__(self):
        self.version = "2.0"
        self.language_name = "BHARTI"
        self.author = "Emperor AD"
        self.core_principles = [
            "1 Sound = 1 Symbol (No Schwa /ə/ sound)",
            "Regular Grammar (No verb conjugation)",
            "Universal Question via 'Ki' at the start",
            "Direct Negation via 'Na' prefix on verbs",
            "Strict SOV (Subject + Object + Verb) Structure"
        ]

    def display_project_info(self):
        """
        Project ki mukhya jankari aur siddhant print karta hai.
        """
        print("=" * 60)
        print(f" 🇮🇳 Language Name : {self.language_name} (Version {self.version})")
        print(f" 👑 Created By    : {self.author}")
        print("-" * 60)
        print(" Core Principles & Rules Loaded:")
        for idx, principle in enumerate(self.core_principles, 1):
            print(f"  {idx}. {principle}")
        print("=" * 60)

    def process_sentence(self, subject: str, obj: str, verb: str, tense: str = "ha", is_question: bool = False, is_neg: bool = False):
        """
        Bharti Grammar Rule ke mutabiq sentence format karta hai.
        Structure: [Ki?] Subject + Object + [Na-?] Verb + Tense
        """
        # Negation rule: 'Na' ko seedhe verb ke sath joda jata hai
        v_form = f"Na-{verb}" if is_neg else verb
        
        # Tense markers: ha (Present), tha (Past), ga (Future)
        sentence_core = f"{subject} {obj} {v_form} {tense}"
        
        # Universal question structure: वाक्य की शुरुआत में 'Ki' ka prayog
        if is_question:
            final_sentence = f"Ki {sentence_core}?"
        else:
            final_sentence = f"{sentence_core}."
            
        return final_sentence


if __name__ == "__main__":
    # Engine ko initialize karein
    engine = BhartiLanguageEngine()
    engine.display_project_info()
    
    print("\n--- BHARTI Grammar Validation Tests ---\n")
    
    # 1. Normal Statement Test (SOV + Tense)
    # Ram (Subject) kitab (Object) padh (Verb) ha (Present Tense)
    print("[Test 1] Normal Sentence (SOV + Tense):")
    print("Output:", engine.process_sentence("Ram", "kitab", "padh", tense="ha"))
    
    # 2. Universal Question Test (Starts with 'Ki')
    print("\n[Test 2] Question Structure (Starts with 'Ki'):")
    print("Output:", engine.process_sentence("Mi", "pani", "pi", tense="tha", is_question=True))
    
    # 3. Direct Negation Test ('Na' attached directly to verb)
    print("\n[Test 3] Negation Rule ('Na' attached to verb):")
    print("Output:", engine.process_sentence("Vo", "khaana", "kha", tense="ga", is_neg=True))
  
