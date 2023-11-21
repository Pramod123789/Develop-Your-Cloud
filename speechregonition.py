import speech_recognition as sr
def myspeechrecognition(duration):# Initialize the recognizer
    r = sr.Recognizer()
    # Set the microphone as the audio source
    mic = sr.Microphone()
    # Adjust for ambient noise levels
    with mic as source:
        r.adjust_for_ambient_noise(source)
    # Set the recording duration (in seconds)
    recording_duration = duration
    # Start recording
    print("Listening....")
    with mic as source:
        audio = r.record(source, duration=recording_duration)
    # Perform speech recognition
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
            print("Could not request results from the Speech Recognition service; {0}".format(e))
    return text
