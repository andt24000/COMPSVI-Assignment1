"""
Student Support Chatbot
Unit 6 Final Project

This chatbot demonstrates:
- Variables
- User input
- Conditional statements (if/elif/else)
- Modular functions
- Loops
- Dictionaries and lists
- Input validation and robustness
"""

# ---------------------------
# Dictionary storing chatbot responses
# ---------------------------

study_tips = [
    "Break study sessions into 25-minute intervals (Pomodoro technique).",
    "Review your notes within 24 hours of class.",
    "Teach the material to someone else to reinforce learning.",
    "Eliminate distractions by silencing your phone.",
    "Use active recall instead of rereading notes."
]

fun_facts = [
    "Did you know? The brain uses about 20% of your body's energy.",
    "Octopuses have three hearts!",
    "Honey never spoils.",
    "Bananas are berries, but strawberries are not.",
    "Sharks existed before trees."
]

time_management_advice = {
    "procrastinating": "Start with the smallest task first to build momentum.",
    "overwhelmed": "Write everything down and prioritize the top 3 tasks.",
    "distracted": "Try studying in a new environment like a library.",
    "tired": "Make sure you're sleeping at least 7-8 hours per night."
}


# ---------------------------
# Function to greet user
# ---------------------------

def greet_user():
    """
    Asks for the user's name and returns it.
    Ensures the name is not empty.
    """
    while True:
        name = input("Hi! What's your name? ").strip()
        if name:
            print(f"\nNice to meet you, {name}! I'm your Student Support Chatbot.")
            return name
        else:
            print("Please enter a valid name.")


# ---------------------------
# Display menu options
# ---------------------------

def display_menu(name):
    """
    Displays chatbot options.
    """
    print(f"\nWhat would you like help with today, {name}?")
    print("1. Study Tips")
    print("2. Time Management Advice")
    print("3. Motivation")
    print("4. Fun Fact")
    print("5. Exit")


# ---------------------------
# Study tips function
# ---------------------------

def give_study_tip():
    """
    Gives a random study tip from the list.
    """
    import random
    tip = random.choice(study_tips)
    print("\n📚 Study Tip:")
    print(tip)


# ---------------------------
# Time management function
# ---------------------------

def give_time_management_advice():
    """
    Asks user about their struggle and gives advice.
    """
    print("\nWhat best describes your situation?")
    print("Options: procrastinating, overwhelmed, distracted, tired")

    issue = input("Enter your situation: ").lower().strip()

    if issue in time_management_advice:
        print("\n⏳ Advice:")
        print(time_management_advice[issue])
    else:
        print("Sorry, I don't recognize that issue. Try one of the listed options.")


# ---------------------------
# Motivation function
# ---------------------------

def give_motivation(name):
    """
    Gives personalized motivation.
    """
    print(f"\n💪 You’ve got this, {name}!")
    print("Progress is better than perfection.")
    print("Every small step forward counts.")


# ---------------------------
# Fun fact function
# ---------------------------

def give_fun_fact():
    """
    Displays a random fun fact.
    """
    import random
    fact = random.choice(fun_facts)
    print("\n🎉 Fun Fact:")
    print(fact)


# ---------------------------
# Main chatbot loop
# ---------------------------

def run_chatbot():
    """
    Main function that runs the chatbot loop.
    """
    name = greet_user()  # Store user's name

    while True:
        display_menu(name)

        choice = input("\nEnter the number of your choice: ").strip()

        # Conditional logic handling user choices
        if choice == "1":
            give_study_tip()

        elif choice == "2":
            give_time_management_advice()

        elif choice == "3":
            give_motivation(name)

        elif choice == "4":
            give_fun_fact()

        elif choice == "5":
            print(f"\nGoodbye, {name}! Keep working hard and stay positive!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# ---------------------------
# Program entry point
# ---------------------------

if __name__ == "__main__":
    run_chatbot()