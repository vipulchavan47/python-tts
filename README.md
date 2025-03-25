# Text to Speech (TTS) Application

## Project Overview
The Text to Speech (TTS) Application is a desktop application built using Python's Tkinter library. This application converts the text entered by the user into speech and allows the user to save the speech as an audio file in different formats (MP3, WAV, OGG). The app also provides functionality to extract text from images (via OCR) and supports multiple languages and voices for speech synthesis.

## Features
- **Text to Speech Conversion:** Convert the text entered in the text area to speech.
- **Language Support:** Supports English, Hindi, and Marathi languages.
- **Voice Selection:** Allows users to choose different voices for speech synthesis (e.g., David, Tony, Meera, Kalpana, etc.).  (Windows by default provides two voices only so you can use id: 0 and 1 for that)
- **Speed Control:** Option to adjust the speed of speech (Fast, Normal, Slow).
- **OCR (Optical Character Recognition):** Upload an image, and the app will extract the text from the image (supports English, Hindi, and Marathi).
- **Save Speech:** Save the converted speech to a file in MP3, WAV, or OGG formats.

## Technologies Used
- **Python:** Programming language used to develop the application.
- **Tkinter:** GUI library for building the graphical interface.
- **pyttsx3:** Library for speech synthesis.
- **pytesseract:** Library for Optical Character Recognition (OCR) to extract text from images.
- **PIL (Pillow):** Library for opening, manipulating, and saving image files.
- **FileDialog:** Provides a simple way to open and save files.

## Installation Instructions

1. Clone or download this repository to your local machine.
   
2. Install the required libraries:

   ```bash
   pip install pyttsx3 pytesseract pillow
   ```

   Additionally, you will need to install Tesseract-OCR to use the `pytesseract` library. You can follow the installation guide for Tesseract based on your operating system:

   - [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)

3. Make sure the Tesseract executable is in your system's PATH, or specify the path to the executable in the code.

4. Run the application:

   ```bash
   python tts_application.py
   ```


---

### **Upgraded Version**
This project is an upgraded version of the original Text to Speech application. You can check out the original version of the project in the following YouTube video:

- **Original Project Video:** [Text to Speech Application - YouTube](https://youtu.be/fEL8ihL-GXg?si=ZwiE7ZILXNEdf0ek)
