# rasa_coffee_chatbot
# **Coffee Chatbot - README**

## **1. Project Domain and Motivation**
The Coffee Chatbot is a conversational AI assistant designed to help users order coffee, receive recommendations based on the weather, discover coffee recipes, and more. This project showcases a practical application of chatbot technologies combined with real-time data from external APIs to create a personalized and interactive user experience.


---

## **2. Implemented Scenarios**

1. **Order Coffee**: Ability to order coffee with customized options for coffee type and sugar quantity.  
2. **Cancel Order**: Cancel an order at any point during the conversation.  
3. **Suggest Popular Coffees**: Suggest a list of popular coffee types.  
4. **Payment Confirmation**: Built-in payment confirmation simulation.  
5. **Weather-Based Coffee Suggestions**: Use the OpenWeatherMap API to suggest hot or cold coffee based on the weather.  
6. **Coffee Recipe Recommendations**: Use a real API to provide coffee recipes.  
7. **Fallback Responses**: Handle unrecognized user inputs gracefully.

---

## **3. Integrated Data Sources**
1. **OpenWeatherMap API:** Fetches real-time weather data to suggest hot or cold coffee.
   - **Rationale:** Improves the user experience by making personalized recommendations based on external factors like weather.
2. **Spoonacular API:** Dynamically fetches creative coffee recipes.
   - **Rationale:** Adds a layer of engagement by suggesting various ways users can enjoy their coffee.

---

## **4. Challenges and Solutions**
- **Challenge:** Handling fallback responses effectively.  
  **Solution:** Integrated an `nlu_fallback` intent and configured the fallback policies.
  
- **Challenge:** Managing dynamic API interactions.  
  **Solution:** Implemented proper error handling in the `actions.py` to inform users if an API request fails.

- **Challenge:** Ensuring smooth conversation flow.  
  **Solution:** Optimized the `MemoizationPolicy` and `RulePolicy` for context-sensitive responses.

---
## **5. Setting Up Keys and Credentials**
1. **OpenWeatherMap API:**  
   - Register at [OpenWeatherMap](https://openweathermap.org/) and get an API key.  
   - Set it in `actions.py`:  
     ```python
     api_key_weather = "YOUR_OPENWEATHERMAP_API_KEY"
     ```

2. **Spoonacular API:**  
   - Register at [Spoonacular](https://spoonacular.com/) and get an API key.  
   - Set it in `actions.py`:  
     ```python
     api_key_recipes = "YOUR_SPOONACULAR_API_KEY"
     ```
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
```bash
rasa run actions
```

### **6. Start the Rasa Server**
In a different terminal:
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
