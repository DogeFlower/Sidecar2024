
# In robot code (java):
# BooleanSubscriber goToCube = NetworkTableInstance.getDefault().getTable("sidecar").getBooleanTopic("Go to Cube").subscribe(false);
# new NetworkButton(goToCube).onTrue(new PrintCommand("冰淇凌"));

import tkinter.font
import ntcore

# Creates the GUI
root_tk = tkinter.Tk()
root_tk.geometry("1500x800")
root_tk.title("sidecar")#hi

# Initialize network tables and set default values 
inst = ntcore.NetworkTableInstance.getDefault()
inst.startClient4("Sidecar")
inst.setServerTeam(695)
inst.startDSClient()

# connect to a specific host/port
inst.setServer("host", ntcore.NetworkTableInstance.kDefaultPort4)
table = inst.getTable("SideCar")

# init publishers + subscribers
scoreLocationPub = table.getStringTopic("Score Location").publish()
scoreLocationSub = table.getStringTopic("Score Location").subscribe("")

amplifyPub = table.getBooleanTopic("Amplify").publish()
amplifySub = table.getBooleanTopic("Amplify").subscribe( False)
#default value
scoreLocationPub.set("speaker")

# Initialize buttons
scoreInSpeaker_btn = tkinter.Button(root_tk)
scoreInSpeaker_btn['width'] = 20
scoreInSpeaker_btn['height'] = 3
scoreInSpeaker_btn['fg'] = "black"
scoreInSpeaker_btn['bg'] = "grey"
scoreInSpeaker_btn['text'] = "SPEAKER (RUNNING)"
scoreInSpeaker_btn['font'] = tkinter.font.Font(size=25, weight="bold")
scoreInSpeaker_btn['command'] = lambda: scoreLocationPub.set("speaker")
scoreInSpeaker_btn.place(x=25, y=50)

scoreInAmp_btn = tkinter.Button(root_tk)
scoreInAmp_btn['width'] = 20
scoreInAmp_btn['height'] = 3
scoreInAmp_btn['fg'] = "black"
scoreInAmp_btn['bg'] = "blue"
scoreInAmp_btn['text'] = "AMP"
scoreInAmp_btn['font'] = tkinter.font.Font(size=25, weight="bold")
scoreInAmp_btn['command'] = lambda: scoreLocationPub.set("amp")
scoreInAmp_btn.place(x=25, y=190)

halfCourt_btn = tkinter.Button(root_tk)
halfCourt_btn['width'] = 20
halfCourt_btn['height'] = 3
halfCourt_btn['fg'] = "black"
halfCourt_btn['bg'] = "pink"
halfCourt_btn['text'] = "HALFCOURT"
halfCourt_btn['font'] = tkinter.font.Font(size=25, weight="bold")
halfCourt_btn['command'] = lambda: scoreLocationPub.set("halfcourt")
halfCourt_btn.place(x=25, y=330)

climbAndTrap_btn = tkinter.Button(root_tk)
climbAndTrap_btn['width'] = 30
climbAndTrap_btn['height'] = 3
climbAndTrap_btn['fg'] = "black"
climbAndTrap_btn['bg'] = "red"
climbAndTrap_btn['text'] = "ENDGAME"
climbAndTrap_btn['font'] = tkinter.font.Font(size=25, weight="bold")
climbAndTrap_btn['command'] = lambda: scoreLocationPub.set("trap")
climbAndTrap_btn.place(x=25, y=500)

amplify_btn = tkinter.Button(root_tk)
amplify_btn['width'] = 17
amplify_btn['height'] = 3
amplify_btn['fg'] = "black"
amplify_btn['bg'] = "yellow"
amplify_btn['text'] = "AMPLIFY"
amplify_btn['font'] = tkinter.font.Font(size=25, weight="bold")
amplify_btn['command'] = lambda: toggleAmplifyButton()
amplify_btn.place(x=500 ,y=50)

label = tkinter.Label(root_tk)
label['text'] = "REPLACE WITH STRATEGY"
label['font'] = tkinter.font.Font(size=25, weight="bold")
label.place(x=0,y=0) 

def updateScoreLocation():
    if scoreLocationSub.get() == "speaker":    
        toggleScoreButton("speaker")
    elif scoreLocationSub.get() == "amp":
        toggleScoreButton("amp")
    elif scoreLocationSub.get() == "trap":
        toggleScoreButton("trap")
    elif scoreLocationSub.get() == "halfcourt":
        toggleScoreButton("halfcourt")
def updateAmplifyButton():
    if(amplifySub.get()):
        amplify_btn['bg'] = "grey"
        amplify_btn['text'] = "AMPLIFY (RUNNING)"
    else:
        amplify_btn['bg'] = "yellow"
        amplify_btn['text'] = "AMPLIFY"   
def toggleAmplifyButton():
    if(amplifySub.get()):
        amplifyPub.set(False)
    else:
        amplifyPub.set(True)
def toggleScoreButton(location):
    if location == "speaker":
        scoreInSpeaker_btn['bg'] = "grey"
        scoreInSpeaker_btn['text'] = "SPEAKER (RUNNING)"
        
        scoreInAmp_btn['bg'] = "blue"
        scoreInAmp_btn['text'] = "AMP"
        
        climbAndTrap_btn['bg'] = "red"
        climbAndTrap_btn['text'] = "ENDGAME"
        
        halfCourt_btn['bg'] = "pink"
        halfCourt_btn['text'] = "HALFCOURT"
    elif location == "amp":
        scoreInSpeaker_btn['bg'] = "purple"
        scoreInSpeaker_btn['text'] = "SPEAKER"
        
        scoreInAmp_btn['bg'] = "grey"
        scoreInAmp_btn['text'] = "AMP (RUNNING)"
        
        climbAndTrap_btn['bg'] = "red"
        climbAndTrap_btn['text'] = "ENDGAME"
        
        halfCourt_btn['bg'] = "pink"
        halfCourt_btn['text'] = "HALFCOURT"
    elif location == "trap":
        scoreInSpeaker_btn['bg'] = "purple"
        scoreInSpeaker_btn['text'] = "SPEAKER"
        
        scoreInAmp_btn['bg'] = "blue"
        scoreInAmp_btn['text'] = "AMP"
        
        climbAndTrap_btn['bg'] = "grey"
        climbAndTrap_btn['text'] = "ENDGAME (RUNNING)"
        
        halfCourt_btn['bg'] = "pink"
        halfCourt_btn['text'] = "HALFCOURT"
        
    elif location == "halfcourt":
        scoreInSpeaker_btn['bg'] = "purple"
        scoreInSpeaker_btn['text'] = "SPEAKER"
        
        scoreInAmp_btn['bg'] = "blue"
        scoreInAmp_btn['text'] = "AMP"
        
        climbAndTrap_btn['bg'] = "red"
        climbAndTrap_btn['text'] = "ENDGAME"
        
        halfCourt_btn['bg'] = "grey"
        halfCourt_btn['text'] = "HALFCOURT (RUNNING)"

while True:
    updateScoreLocation()
    updateAmplifyButton()
    root_tk.update()
