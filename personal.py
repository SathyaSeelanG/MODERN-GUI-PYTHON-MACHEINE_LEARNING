import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import subprocess
import sys


engine = pyttsx3.init()
'''len(voices)-1'''

client = wolframalpha.Client('LRWJW6-436RP7LH87')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('web help: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if  currentH < 12 :
        speak('Hi,Good Morning!')

    if currentH >= 12 and currentH < 15:
        speak('Hi,Good Afternoon!')

    if currentH >= 15 and currentH <19:
        speak('Hi,Good Evening!')

    if currentH >= 19 :
        speak('Hi,Good Night sir! ')

greetMe()

speak('I am your assistant web help ,How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry ! try Writing your command ')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            speak(results)

        elif "time" in query:
            strTIme = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is (strTime)")
	    
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('openong gmail')
            webbrowser.open('www.gmail.com')

        elif 'open instagram' in query or 'open insta' in query:
            speak('opening instagram')
            webbrowser.open('www.instagram.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'who is your creator' in query or 'what is the name of your cretaor' in query or 'your creator name' in query or 'name of your creator' in query:
            speak("my creator MISTER NANDHA KUMAR ")

        elif "what is your name" in query or "name" in query or "your name" in query:
            speak("my name is web help")

        elif 'how are you' in query:
            speak(" I am fine,Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that your fine")

        elif 'joke' in query or 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'play music' in query or 'play songs' in query or 'play song' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play english music' in query or 'play english songs' in query or 'play english song' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play tamil music' in query or 'play tamil songs' in query or 'play tamil song' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Konjam']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play hindi music' in query or 'play hindi songs' in query or 'play hindi songs skava' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['ikvaariaa']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'open' in query:
            if 'file' in query:
                path="This PC"
                os.startfile(path)

            else:
                query=query.replace("open","")
                subprocess.call(query)
                webbrowser.open(query)


        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Nandha. further It's a secret")

        elif 'what is love' in query or 'love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by NANDHA")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister NANDHA KUMAR ")
            
	

        elif "Tell me motivation Quotes" in query or 'motivate me' in query:
            stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
            highMsgs = ['Dont worry dude,every hard time comes to an end']
            speak(random.choice(stMsgs))
            speak('I think thins Motivated You sir ... if Not')
            speak(random.choice(highMsgs))

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")

            except Exception as e:
                print(e)
                speak("I am not able to send this email")
		
	    
                
			

            
        elif 'send email' in query or 'send a gmail' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or'exit' in query or 'stop' in query or 'bye' in query or 'close' in query: 
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()

        elif 'what time is it' in query or 'what is the time skava' in query or 'what time is it' in query or 'time' in query or 'current time' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'what date is it' in query or 'what is the date skava' in query or 'what date is it' in query or 'date' in query or 'current date' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')

        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'lock window' in query or 'lock the window' in query:
            speak("Do you want to lock window")
            s=input("YES or NO")
            if yes in s or YES in s or Yes in s:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            else:
                myCommand()

        elif 'shutdown system' in query or "shutdown" in query:
            speak("Do you want to shutdown the system")
            s=input("TYpe YES or NO")
            if yes in s or YES in s or Yes in s:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            else:
                myCommand()

        elif 'empty recycle bin' in query or 'clean recycle bin' in query:
            speak("Do you want to empty recycle bin")
            s=input("Type YES or NO")
            if YES in s or yes in s or Yes in s:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            else:
                myCommand()

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Web Help from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "open camera" in query or "take a photo" in query or "take a picture" in query:
            ec.capture(0, "web help Camera ", "img.jpg")

        elif "restart" in query:
            speak("Do you want to restart the system")
            s=input(" Type YES or NO")
            if YES in s or yes in s or Yes in s:
                subprocess.call(["shutdown", "/r"])
            else:
                myCommand()

        elif "hibernate" in query or "sleep" in query:
            speak("Do you want to hibernate the system")
            s=input(" Type YES or NO")
            if yes in s or Yes in s or YES in s:
                speak("Hibernating")
                subprocess.call("shutdown / h")
            else:
                myCommand()

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            speak("Do you want to Log off or Sign off the system")
            s=input(" Type YES or NO")
            if Yes in s or Yes in s or yes in s:
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
            else:
                myCommand()

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "web help" in query:
            speak("WEB HELP 1 point o in your service SIR")
            myCommand()

        elif "weather" in query:
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else:
                speak(" City Not Found ")
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")		 
                                    
        else:
            query = query                    
                
            try:
                speak('Searching...')
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('google says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('any Command!!')
