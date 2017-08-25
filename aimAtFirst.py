#aimAtFirst.py
import maya.cmds as cmds

selectList = cmds.ls(orderedSelection=True)

if len(selectList) >= 2:
    print 'Selected Items: %s' % (selectList)
    
    targetName = selectList[0]
    selectList.remove(targetName)
    
    for objectName in selectList:
        print 'Constraining %s toward %s' % (objectName, targetName)
        
        cmds.aimConstraint(targetName, objectName, aimVector=[0, 1, 0])
        

else:
    print 'Please select more than one object'