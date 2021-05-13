import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
print("[+]Welcome.\nDiscord: brn#0405\n\n[+]Waiting for lesson to start...")
def sign_in(meetingid,meetingpass):
    print("[+] Starting Zoom.")
    time.sleep(1)

    subprocess.call(r'Enter your zoom directory here')

    time.sleep(5)

    joinbtn = pyautogui.locateCenterOnScreen("screenshots/joinbtn.PNG")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(2)


    jnb = pyautogui.locateCenterOnScreen("screenshots/joinmtt.PNG")
    pyautogui.moveTo(jnb)
    pyautogui.click()


    meetingidbtn = pyautogui.locateCenterOnScreen("screenshots/asdw.PNG")
    pyautogui.moveTo(meetingidbtn)
    pyautogui.click()
    pyautogui.write(meetingid)
    pyautogui.press("enter")

    time.sleep(2)




    meetingpp = pyautogui.locateCenterOnScreen("screenshots/meetingpp.PNG")
    pyautogui.moveTo(meetingpp)
    pyautogui.click()

    meetingpassw = pyautogui.locateCenterOnScreen("screenshots/passcode.PNG")
    pyautogui.moveTo(meetingpassw)
    pyautogui.click()
    pyautogui.write(meetingpass)
    pyautogui.press("enter")
    time.sleep(15)

    joinaudio = pyautogui.locateCenterOnScreen("screenshots/audio.PNG")
    pyautogui.moveTo(joinaudio)
    pyautogui.click()




df = pd.read_csv("timings.csv")
while True:


    now = datetime.now().strftime("%H:%M")

    if now in str(df["timings"]):
        owd = df.loc[df["timings"] == now]
        passw = str(df.iloc[0,2])
        id = str(df.iloc[0,1])

        sign_in(id,passw)
        time.sleep(28)
        print("[+] Done.")
