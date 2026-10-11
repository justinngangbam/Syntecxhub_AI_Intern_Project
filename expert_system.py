class RuleBasedExpertSystem:
    def __init__(self):
        # 1. Build a facts base and rule engine (if-then rules)
        self.rules = [
            {"if": ["fever", "cough"], "then": "possible_infection"},
            {"if": ["possible_infection", "body_ache"], "then": "flu"},
            {"if": ["possible_infection", "runny_nose"], "then": "common_cold"},
            {"if": ["sneeze", "itchy_eyes"], "then": "allergies"}
        ]
        self.facts = set()  # Stores known facts
        self.log = []       # Logs inference steps

    def ask_user_symptoms(self):
        # 2. Accept user facts (symptoms)
        print("Welcome to the Medical Expert System!")
        print("Available symptoms to choose from:")
        print(" -> fever, cough, body_ache, runny_nose, sneeze, itchy_eyes\n")
        
        user_input = input("Enter your symptoms (separated by commas): ").lower()
        
        # Clean up the input and add to our facts base
        symptoms = [s.strip() for s in user_input.split(",") if s.strip()]
        self.facts.update(symptoms)
        print(f"\n[Initial Facts Recorded]: {self.facts}\n")

    def forward_chaining(self):
        # 3. Infer conclusions using forward chaining
        new_fact_added = True
        
        print("--- Inference Steps ---")
        # Loop continues until no new rules can be triggered
        while new_fact_added:
            new_fact_added = False
            
            for rule in self.rules:
                conditions = rule["if"]
                conclusion = rule["then"]
                
                # Check if ALL conditions in the 'if' clause are present in our facts
                if all(condition in self.facts for condition in conditions):
                    
                    # If the conclusion is new, add it to facts and log it
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        
                        # 4. Log inference steps for the user
                        step_message = f"IF {conditions} THEN {conclusion}"
                        self.log.append(step_message)
                        print(f"Rule Triggered -> {step_message}")
                        
                        # Set to True so the engine checks the rules again (multi-step inference)
                        new_fact_added = True
                        
        print("-----------------------\n")

    def display_conclusions(self):
        # Filter the facts to only show final diagnoses
        diseases = ["flu", "common_cold", "allergies"]
        diagnoses = [fact for fact in self.facts if fact in diseases]
        
        print("--- Final Conclusion ---")
        if diagnoses:
            print(f"Based on your symptoms, you might have: {', '.join(diagnoses)}")
        else:
            print("Could not reach a specific diagnosis. You might just be healthy or need a real doctor!")
        
        print("\n--- Reasoning Path (How we got here) ---")
        if not self.log:
            print("No rules were triggered.")
        for step in self.log:
            print(step)

if __name__ == "__main__":
    system = RuleBasedExpertSystem()
    system.ask_user_symptoms()
    system.forward_chaining()
    system.display_conclusions()