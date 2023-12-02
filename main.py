
# In robot code (java):
# BooleanSubscriber goToCube = NetworkTableInstance.getDefault().getTable("sidecar").getBooleanTopic("Go to Cube").subscribe(false);
# new NetworkButton(goToCube).onTrue(new PrintCommand("冰淇凌"));

import tkinter.font
import networktables

# Creates the GUI
root_tk = tkinter.Tk()
root_tk.geometry("800x500")
root_tk.title("sidecar")#hi

# Initialize network tables and set default values FIX THE IP
networktables.NetworkTables.initialize(server="10.6.95.2")
nt = networktables.NetworkTables.getDefault().getTable("sidecar")
nt.putBoolean("Go to Cube", False)

def updateGoToLocation():
    if nt.getBoolean("Go to Cube", False):
        goToLocation_btn['bg'] = "grey"
        goToLocation_btn['text'] = "(RUNNING)"
    else:
        goToLocation_btn['bg'] = "purple"
        goToLocation_btn['text'] = "GO TO CUBE"


# Initialize GO TO CUBE button
goToLocation_btn = tkinter.Button(root_tk)
goToLocation_btn['width'] = 17
goToLocation_btn['height'] = 3
goToLocation_btn['fg'] = "black"
goToLocation_btn['bg'] = "purple"
goToLocation_btn['text'] = "GO TO CUBE"
goToLocation_btn['font'] = tkinter.font.Font(size=25, weight="bold")
goToLocation_btn['command'] = lambda: nt.putBoolean("Go to Cube", True)
goToLocation_btn.place(x=25, y=10)
goToLocation_btn.pack(side="top")

while True:
    updateGoToLocation()
    root_tk.update()
