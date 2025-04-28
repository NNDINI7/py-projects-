import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def record_text():
    while True:
        try:
            # Use microphone for input
            with sr.Microphone() as source2:
                speak_text("Please say something...")
                print("Listening...")

                # Adjust for ambient noise
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listen to input 
                audio2 = r.listen(source2)

                # Use Google to recognize audio
                MyText = r.recognize_google(audio2)
                print("You said: " + MyText)
                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            speak_text("Sorry, I could not process your request.")

        except sr.UnknownValueError:
            print("Unknown error occurred")
            speak_text("I didn't catch that. Please try again.")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = record_text()
    output_text(text)
    print("Text saved!")
    speak_text("Your text has been saved.")



































































# import speech_recognition as sr
# import pyttsx3

# #initialize the recognizer
# r = sr.Recognizer()
# def record_text():
#     #loop in case of errors
#     while(1):
#           try:
#                #use microphone for input
#                with sr.Microphone() as source2:
#                     r.adjust_for_ambient_noise(source2,duration=0.2)

#                     #listen to input 
#                     audio2 = r.listen(source2)

#                     #use google to recognize audio
#                     MyText = r.recognize_google(audio2)
    
#           except sr.RequestError as e:
#                print("could not request results: {0}".format(e))

#           except sr.UnknownValueError:
#                print("unknown error occured ")


#     return

# def output_text(text):
#     f=open("output.txt","a")
#     f.write(text)
#     f.write("\n")
#     f.close()
#     return

# while(1):
#     text = record_text()
#     output_text(text)

#     print("write text ")