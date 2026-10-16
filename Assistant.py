from datetime import datetime
import random
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests



# ---------------- VOICE OUTPUT ----------------

engine = pyttsx3.init()


import subprocess

def speak(text):
    print(text)
    safe_text = text.replace("'", "''")
    subprocess.run([
        "powershell",
        "-NoProfile",
        "-Command",
        f"$s = New-Object -ComObject SAPI.SpVoice; $s.Speak('{safe_text}')"
    ])
# ---------------- VOICE INPUT ----------------

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Speech service is not available.")
        return ""


# ---------------- PERCEPTION ----------------

def perception(x1, x2):
    if x1 == 1 and x2 == 1:
        return 1
    elif x1 == 0 and x2 == 0:
        return 0
    else:
        return -1


# ---------------- MAIN ASSISTANT ----------------

while True:

    command = listen()

    if command == "":
        continue

    # TIME
    if "time" in command:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak("Current time is " + current_time)

    # DATE
    elif "date" in command:
        today = datetime.now().strftime("%B-%d-%Y")
        speak("Today's date is " + today)

    # CALCULATE / ADD
    elif "calculate" in command:
        speak("Enter first number")
        num1 = float(input())
        speak("Enter second number")
        num2 = float(input())
        result = num1 + num2
        speak("The answer is " + str(result))

    # SUBTRACT
    elif "subtract" in command:
        speak("Enter first number")
        num1 = float(input())
        speak("Enter second number")
        num2 = float(input())
        result = num1 - num2
        speak("The answer is " + str(result))

    # MULTIPLY
    elif "multiply" in command:
        speak("Enter first number")
        num1 = float(input())

        speak("Enter second number")
        num2 = float(input())
        result = num1 * num2
        speak("The answer is " + str(result))

    # DIVIDE
    elif "divide" in command:
        speak("Enter first number")
        num1 = float(input())
        speak("Enter second number")
        num2 = float(input())

        if num2 == 0:
            speak("Cannot divide by zero.")
        else:
            result = num1 / num2
            speak("The answer is " + str(result))

    # MODULUS
    elif "modulus" in command:
        speak("Enter first number")
        num1 = int(input())
        speak("Enter second number")
        num2 = int(input())

        if num2 == 0:
            speak("Cannot find modulus with zero.")
        else:
            result = num1 % num2
            speak("The modulus is " + str(result))

    # SQUARE
    elif "square" in command:
        speak("Enter a number")
        num = float(input())
        result = num ** 2
        speak("The square is " + str(result))

    # GUESSING GAME
    elif "guess" in command:
        secret_number = random.randint(1, 10)

        speak("Guess a number between 1 and 10:")
        guess = int(input())

        if guess == secret_number:
            speak("Correct! You guessed it!")

        elif guess < secret_number:
            speak("Too low!")

        else:
            speak("Too high!")

        print("The correct number was:", secret_number)
    
    # GREETING
    elif "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

    # QUOTES
    elif "quote" in command:
        quotes = [
            "The best way to predict the future is to invent it.",
            "Life is 10% what happens to us and 90% how we react to it.",
            "The only limit to our realization of tomorrow is our doubts of today."
        ]
        speak(random.choice(quotes))

        # FACTS
    elif "fact" in command:
            facts = [
                "Python is a programming language.",
                "AI stands for Artificial Intelligence.",
                "Machine Learning is a part of AI."
            ]
            speak(random.choice(facts))

    # HELP
    elif "help" in command:
        speak(
            "I can tell you the time and date, perform calculations, "
            "open websites, tell jokes, motivate you, and explain "
            "Artificial Intelligence, Machine Learning, and Deep Learning."
        )

    # RECOMMENDATION
    elif "recommend" in command:
        speak("What do you need a recommendation for?")
        choice = input().lower()

        if choice == "study":
            speak(
                "I recommend studying for 30 minutes "
                "and taking a short break."
            )

        elif choice == "fitness":
            speak(
                "I recommend doing a short workout "
                "and staying active."
            )

        elif choice == "food":
            speak(
                "I recommend choosing a balanced meal "
                "with protein and vegetables."
            )

        else:
            speak("Sorry, I don't have a recommendation for that.")
    
    # GOOGLE 
    elif "google" in command:
        speak("opening Google ")
        webbrowser.open("https://www.google.com")

    # YOUTUBE
    elif "youtube" in command:
        speak("opening YouTube ")
        webbrowser.open("https://www.youtube.com")
    
    # WHATSAPP
    elif "whatsapp" in command:
        speak("opening WhatsApp ")
        webbrowser.open("https://web.whatsapp.com")

    # CHROME
    elif "chrome" in command:
        speak("opening Google Chrome ")
        webbrowser.open("https://www.google.com/chrome/")

    # GMAIL
    elif "gmail" in command:
        speak("opening Gmail ")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    
    # SPOTIFY
    elif "spotify" in command:
        speak("opening Spotify ")
        webbrowser.open("https://open.spotify.com/")


    # MUSIC
    elif "music" in command:
        speak(
            "I recommend listening to some relaxing music "
            "or your favorite playlist."
        )

    # JOKE
    elif "joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]

        speak(random.choice(jokes))

    # MOTIVATION
    elif "motivate" in command:
        motivational_quotes = [
            "You can do it!",
            "Keep going!",
            "Believe in yourself!"
        ]

        speak(random.choice(motivational_quotes))

    # WEATHER
    elif "weather" in command:
        speak(
            "I recommend checking a weather app "
            "for the latest weather information."
        )

    # NAME
    elif "name" in command:
        speak("What is your name?")
        name = input()
        speak("Hello " + name + "! Nice to meet you.")


    # PERCEPTION
    elif "perception" in command:
        speak("Enter first value, 0 or 1:")
        x1 = int(input())
        speak("Enter second value, 0 or 1:")
        x2 = int(input())
        speak("Calculating perception...")


        result = perception(x1, x2)
        speak("The perception result is: " + str(result))
        if result == 1:
            speak("Both values are 1.")

        elif result == 0:
            speak("Both values are 0.")

        else:
            speak("The values are different.")


     # ABOUT ASSISTANT
    elif "who are you" in command or "what can you do" in command:
        speak(
        "I am your Virtual AI Assistant, also called Mini Alexa. "
        "I can tell you the time and date, perform calculations, "
        "open websites, tell jokes, motivate you, and explain "
        "Artificial Intelligence, Machine Learning, and Deep Learning."
    )
         

    # ARTIFICIAL INTELLIGENCE
    elif "ai" in command or "artificial intelligence" in command:
        speak(
            "I am an AI assistant designed to help you "
            "with different tasks."
        )

    # MACHINE LEARNING
    elif "ml" in command or "machine learning" in command:
        speak(
            "Machine Learning is a part of artificial intelligence "
            "that learns patterns from data."
        )

    # DEEP LEARNING
    elif "dl" in command or "deep learning" in command:
        speak(
            "Deep Learning is a part of Machine Learning "
            "that uses neural networks with multiple layers."
        )

    # EXIT
    elif "exit" in command:
        speak("Goodbye!")
        break

    # UNKNOWN COMMAND
    else:
        speak("Sorry, I don't know that command.")