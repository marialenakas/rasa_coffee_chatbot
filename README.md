# my_rasa_chatbot
# **Coffee Chatbot - README**

## **Project Overview**

Αυτός είναι ένας διαλογικός πράκτορας βασισμένος στο **Rasa**, ο οποίος βοηθά τους χρήστες να παραγγείλουν καφέ, να ακυρώσουν την παραγγελία τους, να λάβουν συστάσεις καφέ με βάση τον καιρό, και να δουν συνταγές καφέ από ένα πραγματικό API.

---

## **Project Features**

1. **Order Coffee**: Δυνατότητα παραγγελίας καφέ με προσαρμοσμένες επιλογές για τύπο καφέ και ποσότητα ζάχαρης.
2. **Cancel Order**: Ακύρωση παραγγελίας σε οποιαδήποτε στιγμή της συνομιλίας.
3. **Weather-Based Coffee Suggestions**: Χρήση του OpenWeatherMap API για συστάσεις ζεστού ή κρύου καφέ.
4. **Coffee Recipe Recommendations**: Χρήση ενός πραγματικού API για συνταγές καφέ.
5. **Payment Confirmation**: Ενσωματωμένη προσομοίωση πληρωμής.
6. **Fallback Responses**: Χειρισμός μη αναγνωρισμένων εισόδων.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### **2. Create and Activate the Virtual Environment using Anaconda**
```bash
conda activate rasa_env
```
> **Σημείωση**: Έχεις ήδη δημιουργήσει και εγκαταστήσει το περιβάλλον μέσω της Anaconda, οπότε παραλείπεις το `conda create` βήμα.

---

### **3. Install Required Dependencies**
```bash
pip install rasa
pip install rasa-sdk
pip install requests
```

### **4. Train the Model**
```bash
rasa train
```

### **5. Run the Action Server**
Ανοίγεις ένα νέο τερματικό, πηγαίνεις στον κατάλογο του project, και εκτελείς:
```bash
rasa run actions
```

### **6. Start the Rasa Server**
Σε άλλο τερματικό:
```bash
rasa shell
```

---

## **Project Structure**
```
/my_rasa_project
├── actions/                     # Custom actions using APIs and business logic
│   └── actions.py               # Περιέχει το API για καιρό και συνταγές
├── config.yml                   # Ρυθμίσεις pipeline και πολιτικών
├── data/
│   ├── nlu.yml                  # Παραδείγματα για intents
│   ├── stories.yml              # Ροές συνομιλίας
│   ├── rules.yml                # Κανόνες για fallback και ειδικές περιπτώσεις
├── domain.yml                   # Intents, entities, slots, actions
├── endpoints.yml                # Ρύθμιση endpoint για τα custom actions
├── models/                      # Εκπαιδευμένα μοντέλα
└── README.md                    # Τεκμηρίωση
```

---

## **Core Intents και Δράσεις**

| **Intent**            | **Παραδείγματα**                                       | **Bot Response / Action**                         |
|----------------------|--------------------------------------------------------|--------------------------------------------------|
| `order_coffee`        | "I want to order coffee"                              | Ζητάει τύπο καφέ και προτίμηση ζάχαρης            |
| `cancel_order`        | "Cancel my order"                                     | Ακυρώνει την παραγγελία                           |
| `confirm_payment`     | "I want to pay now"                                   | Επιβεβαιώνει την πληρωμή                          |
| `ask_popular_coffees` | "What are some popular coffee types?"                 | Παρουσιάζει δημοφιλείς καφέδες                    |
| `ask_coffee_weather`  | "Recommend a coffee based on weather"                 | Προτείνει καφέ με βάση τον καιρό                  |
| `ask_coffee_recipes`  | "Can you suggest me some coffee recipes?"             | Παρουσιάζει συνταγές καφέ από το API              |
| `nlu_fallback`        | "τυχαίο κείμενο"                                      | Ενεργοποιεί fallback                              |

---

## **Real-world APIs**
1. **OpenWeatherMap API**: Προσφέρει δυναμικές συστάσεις για ζεστά ή κρύα ροφήματα με βάση τον καιρό.
2. **Coffee Recipes API**: Παρέχει συνταγές καφέ.

---

## **APIs Configuration**
Βεβαιώσου ότι το αρχείο **actions.py** περιέχει σωστά τα API keys:
```python
api_key_weather = "YOUR_OPENWEATHERMAP_API_KEY"
api_key_recipes = "YOUR_RECIPES_API_KEY"
```

---

## **Fallback Handling**
Η πτώση στην προεπιλεγμένη απάντηση γίνεται μέσω των παρακάτω:
- Ορισμός intent `nlu_fallback`.
- Ρύθμιση κανόνα fallback στο `rules.yml`.

---

## **Testing**
### **Interactive Mode**
Χρησιμοποίησε:
```bash
rasa interactive
```

### **Manual Testing**
Μπορείς να δοκιμάσεις παραγγελίες καφέ, ακυρώσεις, και API συστάσεις με το:
```bash
rasa shell
```

---

## **Future Enhancements**
- Προσθήκη voice input με speech recognition.
- Διαχείριση ιστορικού παραγγελιών μέσω βάσης δεδομένων.

---
