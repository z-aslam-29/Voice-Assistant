import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import pywhatkit
from pywikihow import search_wikihow
from googletrans import Translator
import openai
import datetime


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        audio = r.listen(source)
        said = ''
        r.pause_threshold = 1

        try:
            print("Recognizing....")
            said = r.recognize_google(audio , language='eng-in')
            print('You said : ',said)

        except Exception as e :

            print("Exception :" + str(e))

    return said

def get_audio_Hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        audio = r.listen(source)
        said = ''
        r.pause_threshold = 1

        try:
            print("Recognizing....")
            said = r.recognize_google(audio , language='Hi')
            print('You said : ',said)

        except Exception as e :

            print("Exception :" + str(e))

    return said

def Translation():
    speak1("In what language you want to make translation")
    lang = get_audio()
    if "English to Hindi" in lang:

        speak1("say the line")
        line = get_audio()
        translate = Translator()
        result = translate.translate(line, dest="hi")
        Text = result.text
        speak_Hi(Text)


    elif "Hindi to English" in lang:
     speak1("say the line")
     line2 = get_audio_Hindi()
     translator = Translator()
     result = translator.translate(line2)
     Text = result.text
     speak1(Text)


def photo():
    speak1("Look at Camera and say Cheeezzz, clicking photo in Three seconds...")
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.waitKey(3000)

    ret, frame = cam.read()

    if ret:
        cv2.imwrite("image2.jpg", frame)
        cam.release()

    cv2.destroyAllWindows()

def click():
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.waitKey(500)

    ret, frame = cam.read()

    if ret:
        cv2.imwrite("image3.jpg", frame)
        cam.release()

    cv2.destroyAllWindows()

def camera():
    speak1("turning camera on, my lord")
    import cv2

    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        cv2.imshow("Frame", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    camera.release()

    cv2.destroyAllWindows()

def set_alarm():
    speak1("Please tell me the time to set the alarm, my lord")
    # listen for the user's input
    command = get_audio()
    # extract the hour and minute values from the input
    try:
        hour, minute = map(int, command.split(":"))
    except:
        speak1("Sorry, could not understand. Please try again, my lord")
        return
    # set the alarm for the specified time
    now = datetime.datetime.now()
    alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    time_diff = alarm_time - now
    time_seconds = time_diff.total_seconds()
    os.system(f'sleep {time_seconds}; afplay /System/Library/Sounds/Ping.aiff')
    speak1("Alarm is set, my lord.")

def whatsapp():
    speak1("Tell me the name of the person my lord")
    name = get_audio()



    if "person name" in name:
       speak1("tell me the message my lord")
       msg = get_audio()
       speak1("tell me the time my lord !")
       speak1("Time in hour sir")
       hour = int(get_audio())
       speak1("tell me the minute my lord")
       minute = int(get_audio())
       pywhatkit.sendwhatmsg("+91 His Mobile Number",msg,hour,minute)
       speak1("done my lord! messege is sending to" + name + "ser!")

    elif " person Name" in name:
       speak1("tell me the message my lord")
       msg = get_audio()
       speak1("tell me the time my lord !")
       speak1("Time in hour sir")
       hour = int(get_audio())
       speak1("tell me the minute my lord")
       minute = int(get_audio())
       pywhatkit.sendwhatmsg("+91 His Mobile Number",msg,hour,minute)
       speak1("done my lord! messege is sending to" + name + "ser!")


    else:
        speak1("tell me the phone number")
        phone = int(get_audio())
        ph = "+91" +phone
        speak1("tell me the message my lord")
        msg = get_audio()
        speak1("tell me the time my lord !")
        speak1("Time in hour sir")
        hour = int(get_audio())
        speak1("tell me the minute my lord")
        minute = int(get_audio())
        pywhatkit.sendwhatmsg(ph, msg, hour, minute)
        speak1("done my lord! messege is sending to" + name + "ser!")

def speak0(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 155)

    print(voices, )

    engine.say(text)
    print(text)
    engine.runAndWait()

def speak1(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[0].id)
    engine.setProperty('rate', 155)




    print(voices,)

    engine.say(text)
    print(text)
    engine.runAndWait()

def speak_Hi(text1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[2].id)
    engine.setProperty('rate', 155)




    print(voices,)

    engine.say(text1)
    print(text1)
    engine.runAndWait()


hour = datetime.datetime.now().hour

if hour >= 6 and hour<12:
    speak1("Good morning my lord!")

elif hour >=12 and hour<18:
    speak1("Good Afternoon my lord!")

elif hour >=18 and hour<24:
    speak1("Good Evening my lord!")
else:
    speak1("Good Night my lord")

speak1("jarvis here, command me, i am at your service!")
#speak_Hi("hello sir")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    Time = Time.replace("Jarvis","")
    speak1("the current time is")
    speak1(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    date = date.replace("Jarvis","")
    speak1("Current Date is")
    speak1(date)
    speak1("Month is")
    speak1(month)
    speak1("Year is")
    speak1(year)


def wishme():
    speak1("Hello young man or woman!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak1("I wish you a very,Good morning ")
    elif hour >=12 and hour<18:
        speak1("I wish you a very,Good Afternoon ")
    elif hour >=18 and hour<24:
        speak1("I wish you a very,Good Evening ")
    else:
        speak1("Good Night")


def task_executer():
 while  True:
  text = get_audio()
 #text = input('Enter here: ')

  if "Jarvis my son" in text:
      speak1('my lord,your desire')

  elif "Friday" in text:
      speak0('Your Grace, Its Friday Here, glad to hear you')
      speak0("I can assist you in AI mode.")

  elif "how are you" in text:
      speak1("I am good my lord !  How are you?")

  elif "who made you" in text:
      speak1("i was Created by My Lord, Aslam")


  elif " you can go" in text:
      speak1("ok sir will meet soon")
      break

  elif "YouTube search" in text:
      speak1("my lord ! This is what i Found sir")
      text = text.replace("Jarvis", "")
      text = text.replace("YouTube search", "")
      web = 'https://www.youtube.com/results?search_query=' + text
      webbrowser.open(web)
      speak1("Done my lord")

  elif " Google search" in text:

      speak1("my lord ! this is what i found")
      text = text.replace("Jarvis", "")
      text = text.replace("Google search", "")
      pywhatkit.search(text)
      speak1("done my lord")

  elif "launch" in text:
      speak1("tell me the name of website")


      name = get_audio()
      web = "http://www." + name + ".com"
      webbrowser.open(web)
      speak1("Done my lord")

  elif "play music" in text:
      speak1("tell me your favourite song")
      name = get_audio()
      name = name.replace("Jarvis","")
      pywhatkit.playonyt(name)
      speak1("done my lord")

  elif "WhatsApp" in text:
      whatsapp()

  elif "translate" in text:
      Translation()

  elif "remember that" in text:
      remebermsg = text.replace("remember that", '')
      remenbermsg = remebermsg.replace("Jarvis", '')
      speak1("you told me to remind you"+remenbermsg)
      remember = open('data.txt','w')
      remember.write(remenbermsg)
      remember.close()


  elif "anything you remember" in text:
      remember = open('data.txt', 'r')
      speak1("you told me that" + remember.read())


  elif "Google search" in text:
         import wikipedia as googlescrap
         text = text.replace("Jarvis", "")
         text = text.replace("Google search", "")
         text = text.replace("google", "")
         speak1("this is what I found, my lord")

         try:
             pywhatkit.search(text)
             result = googlescrap.summary(text,3)
             speak_Hi(result)


         except:
             speak1("sorry! no speakable data found")


  elif "how to" in text:
      speak1('gathering data for you')
      op = text.replace("jarvis", "")
      max_result = 1
      how_to_fun = search_wikihow(op,max_result)
      assert len(how_to_fun)==1
      how_to_fun[0].print()
      speak1(how_to_fun[0].summary)


  elif "date" in text:
      date()

  elif "time" in text:
      time()

  elif "friend" in text:
      wishme()

  elif "photo" in text:
      photo()

  elif "camera" in text:
      camera()

  elif "capture" in text:
      click()

  elif "set alarm" in text:
      set_alarm()

  elif "goodbye" in text:
      speak1("Happy to help you, my lord")
      #speak0("me too, my Grace!")
      quit()




task_executer()