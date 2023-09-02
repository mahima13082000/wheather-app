import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f"ENTER YOUR CITY NAME")

url =  "http://api.weatherapi.com/v1/current.json?key=ea48052d07b04c1cbe952029230107&q="+input("ENTER YOUR CITY NAME:->")

df = requests.get(url)
data = json.loads(df.content)
print(f"YOUR LOCATION IS:->  {data ['location']['name']}")
print(f"THE CURRENT TEMPERATURE IN CALCIUS IN  {data ['location']['name']} IS:-> {data['current']['temp_c']}")
print(f"THE TEMPERATURE IN FAHERNEHITE IN  {data ['location']['name']} IS:-> {data['current']['temp_f']}")
print(f"THE REGION OF {data['location']['name']} IS:-> {data['location']['region']}")
print(f"THE COUNTRY OF {data['location']['name']} IS:->{data['location']['country']}")
print(f"IS DAY:-> {data['current']['is_day']}")
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f" Your Location Is{data ['location']['name']}")
speaker.Speak(f"the current temperature in calcius in {data ['location']['name']} is{data['current']['temp_c']} degrees")
speaker.Speak(f"the current temperature in fahernehite in {data ['location']['name']} is{data['current']['temp_f']} fahernehite")
speaker.Speak(f"the region of {data ['location']['name']} is{data['location']['region']}")
speaker.Speak(f"the country of {data ['location']['name']} is{data['location']['country']}")