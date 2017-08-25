#keyRotation.py
import maya.cmds as cmds

def keyFullRot(pObjName, pStartTime, pEndTime, pTargetAttrib):
    cmds.cutKey(pObjName, time=(pStartTime, pEndTime), attribute=pTargetAttrib)
    cmds.setKeyframe(pObjName, time=pStartTime, attribute=pTargetAttrib, value=0)
    cmds.setKeyframe(pObjName, time=pEndTime, attribute=pTargetAttrib, value=360)
    
    cmds.selectKey(pObjName, time=(pStartTime, pEndTime), attribute=pTargetAttrib, keyframe=True)
    cmds.keyTangent(inTangentType='linear', outTangentType='linear')



selectList = cmds.ls(selection=True, type='transform')

if len(selectList) >= 1:
    #print 'Selected Items: %s' % (selectList)
    
    startTime = cmds.playbackOptions(query=True, minTime=True)
    endTime = cmds.playbackOptions(query=True, maxTime=True)
    
    for objName in selectList:
        #objTypeResult = cmds.objectType(objName)
        #print '%s type: %s' % (objName, objTypeResult)
        
        keyFullRot(objName, startTime, endTime, 'rotateY')

else:
    print 'Please select more than one object'