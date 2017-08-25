#shieldObjectCreation.py
import maya.cmds as cmds

cylResult = cmds.polyCylinder(r=1.15, h=.15, sx=6)
cmds.polyBevel3(cylResult, oaf=True, ws=True, at=180)

shpereResult = cmds.polySphere(r=1.15, name="PowerCore")
cmds.move(0, 10, 0, shpereResult)

