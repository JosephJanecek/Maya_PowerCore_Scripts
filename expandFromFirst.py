#expandFromFirst.py
import maya.cmds as cmds

selectList = cmds.ls(orderedSelection=True, type='transform')

if len(selectList) >= 2:
    targetName = selectList[0]
    selectList.remove(targetName)
    
    locatorGroupName = cmds.group(empty=True, name='expantion_locator_grp#')
    
    maxExpantion = 100
    
    newAttrName = 'expantion'
    
    if not cmds.objExists('%s.%s' % (targetName, newAttrName) ):
        cmds.select(targetName)
        cmds.addAttr(longName=newAttrName, shortName='expa',
                    attributeType='double', min=0, max=maxExpantion,
                    defaultValue=maxExpantion, keyable=True)
    
    for objName in selectList:
        coords = cmds.getAttr('%s.translate' % (objName))[0]
        
        locatorName = cmds.spaceLocator(position=coords, name='%s_loc#' % (objName) )[0]
        cmds.xform(locatorName, centerPivots=True)
        cmds.parent(locatorName, locatorGroupName)
        
        pointConstraintName = cmds.pointConstraint([targetName, locatorName], objName, name='%s_pointConstraint#' % (objName) )[0]
        
        cmds.expression(alwaysEvaluate=True, 
                        name='%s_attractWeight' % (objName),
                        object=pointConstraintName,
                        string='%sW0=%s-%s.%s' % (targetName, maxExpantion, targetName, newAttrName) )
        
        cmds.connectAttr('%s.%s' %(targetName, newAttrName),
                        '%s.%sW1' % (pointConstraintName, locatorName) )
    
    cmds.xform(locatorGroupName, centerPivots=True)
    
else:
    print 'Please select more than one object'