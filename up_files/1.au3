;ControlFocus("title","text","controlID") Edit1 = Edit instance 1
ControlFocus("��","","Edit1")

;Wait 10 second for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

;Set the file name text on the Edit field
ControlSetText("��","","Edit1","F:\selenium-git\pictures\1.jpg")
Sleep(2000)

;Click on the Open button
ControlClick("��","","Button1")