# rasa_coffee_chatbot
# **Coffee Chatbot - README**

## **1. Project Domain and Motivation**
The Coffee Chatbot is a conversational AI assistant designed to help users order coffee, receive recommendations based on the weather, discover coffee recipes, and more. 
This project showcases a practical application of chatbot technologies combined with real-time data from external APIs to create a personalized and interactive user experience.

---

## **2. Implemented Scenarios**
There were 4 requirements, every task has a parenthesis of the requirement that it belongs to.

1. **Order Coffee**: Ability to order coffee with customized options for coffee type and sugar quantity.  (requirement 1)
2. **Cancel Order**: Cancel an order at any point during the conversation.  (requirement 1)
3. **Suggest Popular Coffees**: Suggest a list of popular coffee types.  (requirement 1)
4. **Payment Confirmation**: Built-in payment confirmation simulation.  (requirement 2)
5. **Weather-Based Coffee Suggestions**: Use the OpenWeatherMap API to suggest hot or cold coffee based on the weather.  (requirement 3)
6. **Coffee Recipe Recommendations**: Use a real API to provide coffee recipes.  (requirement 3)
7. **Fallback Responses**: Handle unrecognized user inputs gracefully. (requirement 4)

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
## **5.1 Setting Up Keys and Credentials**
1. **OpenWeatherMap API:**  
   - Register at [OpenWeatherMap](https://openweathermap.org/) and get an API key.  
   - Set it in `actions.py`:  
     ```python
     api_key_weather = "YOUR_OPENWEATHERMAP_API_KEY"
     ```
    It may take an hour or two for your key to be activated
   
3. **Spoonacular API:**  
   - Register at [Spoonacular](https://spoonacular.com/) and get an API key.  
   - Set it in `actions.py`:  
     ```python
     api_key_recipes = "YOUR_SPOONACULAR_API_KEY"
     ```
---     
## **5.2 Installation**

### **1. Clone the Repository**
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### **2. Create and Activate the Virtual Environment using Anaconda**
I activate my rasa enviroment through anacoda.
You can activate your enviroment with this command 

```bash
conda activate rasa_env
```
If you have anacoda to your computer, open it, on the left side it has "enviroments"
---
click on it 
---
Then click on "create" button
---
name your enviroment rasa_env 
---
run the enviroment
---
click open in terminal
---
you made it to rasa env!

In every case make sure you are on the right folder, else type 
```bash
cd <your-rasa_file-directory>
```
---

### **3. Install Required Dependencies**
if  you already have rasa on your computer skip this step, else go to rasa's site for directions 
https://rasa.com/

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

## **6. Example Conversation: Full Interaction**
```
Scenario 1: Ordering and Canceling Coffee

User: hi  
Bot: Hello! How can I help you today?  

User: order coffee  
Bot: What type of coffee would you like to order? (e.g., Espresso, Latte, Cappuccino)  

User: espresso  
Bot: How much sugar would you like in your coffee? (e.g., No sugar, One spoon, Two spoons)  

User: no sugar  
Bot: Your Espresso coffee with No sugar is on the way!  

Scenario 2 : Cancel Order
User: Cancel order  
Bot: Your coffee order has been canceled.

Scenario 3: Suggesting Popular Coffees
User: suggest coffee  
Bot: Some popular coffee types are: Espresso, Cappuccino, Latte, Americano, Macchiato.

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
