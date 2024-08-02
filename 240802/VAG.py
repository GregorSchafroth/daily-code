import requests
from PIL import Image
from io import BytesIO

api_key = "VF.DM.66ac8d5992ccb0c68bfaa36b.Kc6TJlWdkkjj855z"

projectID = "66ac8d291c1a38b862ae4c83"
versionID = "66ac8d291c1a38b862ae4c84"

buttons = []

def interact(user_id, request):
  global buttons
  
  url = f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact'

  payload = {
    'request': request
  }
  
  headers = {
    'Authorization': api_key,
    'versionID': 'production'
  }

  response = requests.post(url, json=payload, headers=headers)
  
  for trace in response.json():
    print("trace['type']: ", trace['type'])
    if trace["type"] == "text":
      print(trace["payload"]["message"])
    elif trace["type"] == "choice":
      buttons = trace["payload"]["buttons"]
      print("Chose one of the following:")
      for i in range(len(buttons)):
        print(f"{i+1}: {buttons[i]['name']}")
    elif trace["type"] == "visual":
        display_image(trace["payload"]["image"])
    elif trace["type"] == "end":
      return False
    else:
      print("unhandeled trace", trace)    
  return True

def save_transcript(user_id):
  import requests

  url = "https://api.voiceflow.com/v2/transcripts"

  payload = {
      "projectID": projectID,
      "versionID": versionID,
      "sessionID": user_id
  }
  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "Authorization": api_key
  }

  response = requests.put(url, json=payload, headers=headers)
  
  if response.ok:
    print("Saved Transcript!")

  print(response.text)

def display_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show() 
  
name = input("> What's your name?\n")
isAlive = interact(name, {"type": "launch"})

while(isAlive):
  print("len(buttons): ", len(buttons))
  if(len(buttons) > 0):
    print("Entering Button Path")
    buttonSelection = input("> Chose a button number, or just send a reply: ")
    try:
      isAlive = interact(name, buttons[int(buttonSelection)-1]["request"])
    except:
      nextInput = input("> Say something:\n")
      isAlive = interact(name, {"type": "text", "payload": buttonSelection})    
  else:
    nextInput = input("> Say something:\n")
    isAlive = interact(name, {"type": "text", "payload": nextInput})
  save_transcript(name)
    
