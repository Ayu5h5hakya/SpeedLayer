import maya.cmds as mc

global layerNameField

def createLayer(args):
    layerName = mc.textField(layerNameField, query=True, value=True)
    mc.createDisplayLayer(noRecurse=True, name=layerName)

def showUI():
    window = mc.window(title="Layer utilities", widthHeight=(400,400))
    mc.columnLayout()
    mc.text(label="Collection of shortcut for layer related tasks")
    mc.text(label="Layer name")
    layerNameField = mc.textField() 

    mc.button(label="Create", command = createLayer, enable = True) 
    mc.showWindow(window)

showUI()