def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! I am Disease Checker. How can I help you?"

    # Small talk
    elif "how are you" in user_input or "how's life" in user_input:
        return "I am well. What about you? Any unusual symptoms bothering you?"

    # Disease info
    disease_info = {
        "cold": ["runny nose", "sore throat", "cough", "sneezing"],
        "flu": ["fever", "chills", "muscle aches", "cough", "congestion"],
        "malaria": ["fever", "chills", "sweats", "headaches", "nausea"],
        "dengue": ["high fever", "severe headaches", "pain behind the eyes", "joint and muscle pain", "rash"],
        "corona": ["fever", "dry cough", "tiredness", "loss of taste or smell", "difficulty breathing"],
        "typhoid": ["high fever", "weakness", "stomach pain", "loss of appetite", "diarrhea", "constipation"],
        "influenza": ["fever", "cough", "sore throat", "runny or stuffy nose", "muscle or body aches"],
        "chickenpox": ["itchy rash", "blisters", "fever", "tiredness", "loss of appetite"],
        "pneumonia": ["cough", "cough with phlegm", "fever", "chills", "difficulty breathing", "chest pain"],
        "diabetes": ["increased thirst", "frequent urination", "extreme hunger", "unexplained weight loss", "fatigue"],
        "heartattack": ["chest pain", "shortness of breath", "pain in arms, back, neck, jaw, or stomach", "nausea", "lightheadedness"],
        "hypertension": ["headaches", "shortness of breath", "nosebleeds", "flushing", "dizziness"],
        "asthma": ["shortness of breath", "chest tightness", "wheezing", "coughing"],
        "allergy": ["sneezing", "itchy eyes", "runny nose", "rash", "swelling"],
        "migraine": ["throbbing pain", "nausea", "sensitivity to light", "sensitivity to sound", "visual disturbances"],
        "arthritis": ["joint pain", "stiffness", "swelling", "reduced range of motion"],
        "depression": ["persistent sadness", "loss of interest", "fatigue", "changes in appetite", "difficulty concentrating"],
        "anxiety": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "irritability"],
        "eczema": ["dry skin", "itching", "redness", "inflammation", "crusting"],
        "psoriasis": ["red patches of skin", "silvery scales", "dry skin", "itching", "burning sensation"],
        "tuberculosis": ["persistent cough", "weight loss", "night sweats", "fever", "fatigue"],    
        "hepatitis": ["fatigue", "jaundice", "abdominal pain", "loss of appetite", "nausea"],
        "measles": ["high fever", "cough", "runny nose", "red eyes", "rash"],
        "mumps": ["swollen salivary glands", "fever", "headache", "muscle aches", "fatigue"],
        "rubella": ["mild fever", "rash", "swollen lymph nodes", "joint pain", "headache"],
        "whoopingcough": ["severe coughing fits", "whooping sound", "runny nose", "fever", "vomiting after coughing"],
        "cholera": ["severe diarrhea", "dehydration", "nausea", "vomiting", "muscle cramps"],
        "typhus": ["high fever", "headache", "rash", "muscle pain", "chills"],
        "cancer": ["unexplained weight loss", "fatigue", "pain", "skin changes", "lumps or swelling"],
        "alzheimers": ["memory loss", "confusion", "difficulty completing familiar tasks", "problems with language", "changes in mood or behavior"],
        "cancer": ["unexplained weight loss", "fatigue", "pain", "skin changes", "lumps or swelling"],
        "smallpox": ["high fever", "rash", "blisters", "fatigue", "headache"],
        "syphilis": ["sores", "rash", "fever", "swollen lymph nodes", "fatigue"],
        "gonorrhea": ["painful urination", "discharge", "pelvic pain", "swelling", "sore throat"],
        "chlamydia": ["painful urination", "discharge", "pelvic pain", "bleeding between periods"],
        "rabies": ["fever", "headache", "excessive salivation", "muscle spasms", "confusion"],
        "chikungunya": ["fever", "joint pain", "headache", "muscle pain", "rash"],
        "tetanus": ["muscle stiffness", "muscle spasms", "difficulty swallowing", "fever", "sweating"],
        "piles": ["painful bowel movements", "bleeding", "itching", "swelling", "discomfort"],
        "jaundice": ["yellowing of skin and eyes", "dark urine", "fatigue", "abdominal pain", "nausea"],
        "leprosy": ["skin lesions", "numbness", "muscle weakness", "eye problems", "enlarged nerves"],
        
    }

    # Case 1: Ask for symptoms of a disease
    if "symptoms of" in user_input:
        disease = user_input.split("symptoms of")[-1].strip()
        if disease in disease_info:
            symptoms = disease_info[disease]
            return f"The symptoms of {disease} are: {', '.join(symptoms)}"
        else:
            return "Sorry, I don't have information about that disease."

    # Case 2: Detect disease from symptoms user types
    for disease, symptoms in disease_info.items():
        if any(symptom in user_input for symptom in symptoms):
            return f"You might have {disease}. Please consult a healthcare professional for confirmation."

    # Case 3: Thank you
    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."

    # Case 4: Fallback
    return "I'm sorry, I couldn't identify that. Try 'symptoms of <disease>' or describe your symptoms."


# ---------------------------
# Chat loop
# ---------------------------
if __name__ == "__main__":
    print("🤖 Disease Checker: Hello! Know the symptoms of diseases or describe your symptoms.Type 'quit' to exit.\n")
    while True:
        user_inp = input("You: ")
        if user_inp.lower() in ["quit", "exit", "bye"]:
            print("🤖 Chatbot: Stay healthy! Goodbye 👋")
            break
        response = chatbot_response(user_inp)
        print(f"🤖 Chatbot: {response}\n")
