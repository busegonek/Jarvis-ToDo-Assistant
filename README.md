# Jarvis ToDo Assistant

Jarvis ToDo Assistant is a Python application that helps you manage your tasks using voice commands. It utilizes speech recognition and text-to-speech capabilities to interact with the user.

## Features

- **Voice Commands:** Interact with Jarvis using voice commands like "hello jarvis", "show my to do list", "inform me", etc.
- **Task Management:** Manage your tasks with commands like marking tasks as completed or checking their status.
- **Offline Support:** Uses both online (Google Speech API) and offline (Sphinx) speech recognition.

### Speech Recognition and Text-to-Speech Setup

- Configured speech recognition using `speech_recognition` library.
- Initialized text-to-speech functionality using `pyttsx3`.
- Customized speech rate and volume for a personalized experience.

### Task Management

- Maintains a list (`tasks`) of tasks with their completion status.
- Each task is represented as a dictionary with keys for task name and completion status (`completed`).

### Functions

- **speak(text):** Utilizes text-to-speech to read out provided text aloud.
- **recognize_speech():** Listens via microphone, recognizes speech using Google Speech API or Sphinx, and converts it to text.
- **recognize_sphinx():** Provides fallback offline speech recognition using Sphinx.
- **show_to_do_list():** Reads the to-do list aloud and allows interaction to mark tasks as completed or not.
- **inform_task_status():** Announces the count of completed and incomplete tasks.

### Main Program (`__main__`)

- Greets users with "Hello, I am Jarvis. How can I assist you?" at the start.
- Recognizes voice commands:
  - "hello jarvis": Responds with a greeting.
  - "how are you": Provides its current state.
  - "what can you do": Describes its functionalities.
  - "show my to do list": Displays and interacts with the to-do list.
  - "inform me": Reports the count of completed and incomplete tasks.
  - "exit" or "goodbye": Terminates the program.
  - Handles unrecognized commands by prompting the user to repeat.

## Usage

- When the application starts, Jarvis will greet you and wait for your command.
- Speak one of the supported commands, e.g., "hello jarvis", "show my to do list", "inform me", etc.
- Jarvis will respond to your command and perform the requested action.
- You can exit the application by saying "exit" or "goodbye".

## Requirements

- Python 3.x
- SpeechRecognition
- pyttsx3
- PyAudio (for microphone input)
- Setuptools

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

