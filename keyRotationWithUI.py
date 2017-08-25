#keyRotationWithUI.py
import maya.cmds as cmds
import functools

def createUI (pWindowTitle, pApplyCallback):
    windowID = 'myWindowID'
    
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)
    
    #Layout Definition
    cmds.window(windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,75), (2, 60), (3, 60)], columnOffset=[(1, "right", 3)])
    
    #UI Elements
    cmds.text(label='Time Range:')
    startTimeField = cmds.intField(value=cmds.playbackOptions(q=True, minTime=True))
    endTimeField = cmds.intField(value=cmds.playbackOptions(q=True, maxTime=True))
    
    cmds.text(label='Attribute:')
    targetAttrField = cmds.textField(text='rotateY')
    cmds.separator(h=10, style='none')
    
    cmds.separator(h=10, style='none')
    cmds.separator(h=10, style='none')
    cmds.separator(h=10, style='none')
    
    cmds.separator(h=10, style='none')
    cmds.button (label='Apply', command=functools.partial(pApplyCallback,
                                                            startTimeField,
                                                            endTimeField,
                                                            targetAttrField) )
    
    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID)
    cmds.button(label='Cancel', command=cancelCallback)
    cmds.showWindow()
    


def keyFullRot(pObjName, pStartTime, pEndTime, pTargetAttrib):
    cmds.cutKey(pObjName, time=(pStartTime, pEndTime), attribute=pTargetAttrib)
    cmds.setKeyframe(pObjName, time=pStartTime, attribute=pTargetAttrib, value=0)
    cmds.setKeyframe(pObjName, time=pEndTime, attribute=pTargetAttrib, value=360)
    
    cmds.selectKey(pObjName, time=(pStartTime, pEndTime), attribute=pTargetAttrib, keyframe=True)
    cmds.keyTangent(inTangentType='linear', outTangentType='linear')

def applyCallback(pStartTime, pEndTime, pTargetAttr, *pArgs):
    #print 'Apply button pressed'
    
    startTime = cmds.intField(pStartTime, query=True, value=True)
    endTime = cmds.intField(pEndTime, query=True, value=True)
    targetAttr = cmds.textField(pTargetAttr, query=True, text=True)
    
    print 'Start Time: %s' % (startTime)
    print 'End Time: %s' % (endTime)
    print 'Attribute: %s' % (targetAttr)
    
    selectList = cmds.ls(selection=True, type='transform')
    
    for objName in selectList:
        keyFullRot(objName, startTime, endTime, targetAttr)



createUI('My Title', applyCallback)






