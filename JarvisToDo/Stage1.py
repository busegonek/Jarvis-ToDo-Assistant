import speech_recognition as sr
import pyttsx3

# Speech recognition setup
recognizer = sr.Recognizer()

# Text to speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('volume', 1.0)  # Speech volume

# Selecting an appropriate voice
voices = engine.getProperty('voices')
for voice in voices:
    if "en-us" in voice.id.lower():  # Selecting US English voice
        engine.setProperty('voice', voice.id)
        break

# Task list
tasks = [
    {"task": "Do exercise", "completed": False},
    {"task": "Study English", "completed": False},
    {"task": "Read a book", "completed": False},
    {"task": "Check emails", "completed": False}
]


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    with sr.Microphone() as source:
        print("I'm ready for Jarvis, waiting for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Speech input detected, processing...")
        command = recognizer.recognize_google(audio, language='en-US')
        print("Recognized command: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, speech could not be understood.")
        return ""
    except sr.RequestError:
        print("Google Speech API could not be reached. Using offline speech recognition...")
        return recognize_sphinx()  # Fallback to offline speech recognition


def recognize_sphinx():
    with sr.Microphone() as source:
        print("Using offline speech recognition. Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Speech input detected, processing...")
        command = recognizer.recognize_sphinx(audio)
        print("Recognized command: " + command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, speech could not be understood.")
        return ""


def show_to_do_list():
    speak("Here is your to-do list:")
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "completed"
        else:
            status = "not completed"
        speak(f"{index}. {task['task']}. Status: {status}")
        speak("Is it Done Zeus?")
        response = recognize_speech()
        while True:
            if "yes" in response:
                tasks[index - 1]["completed"] = True
                speak("Task checked. YOU ARE PERFECT ZEUS")
                break
            elif "no" in response:
                speak("Task not checked. Don't worry my darling. You have still plenty of time")
                break
            else:
                speak("Can you repeat it? I didn't understand correctly.")
                response = recognize_speech()


def inform_task_status():
    completed_count = sum(1 for task in tasks if task["completed"])
    not_completed_count = sum(1 for task in tasks if not task["completed"])
    speak(f"You have {completed_count} completed tasks and {not_completed_count} tasks not completed.")


if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you?")

    while True:
        command = recognize_speech()

        if "hello jarvis" in command:
            speak("Hi Zeus! How can I help you today?")
        elif "how are you" in command:
            speak("I'm doing great, thank you for asking! Just let me know what you need.")
        elif "what can you do" in command:
            speak("I can assist you with tasks like reminding your daily schedule. Just let me know what you need.")
        elif "show my to do list" in command:
            show_to_do_list()
        elif "inform me" in command:
            inform_task_status()
        elif "exit" in command:
            speak("Goodbye!")
            break
        elif "goodbye" in command:
            speak("Goodbye! Zeus")
            break
        elif "take care of yourself" in command:
            speak("Take care of yourself too! Zeus")
            break
        else:
            speak("Sorry, I didn't catch that. Could you please repeat?")
