```python
#import module(s)
import maya.cmds as mc

#add attribute per selection
selection = mc.ls(sl=True, long=True) #get selection with long name
for each in selection:
	shapeNode = mc.listRelatives(each, shapes=True, fullPath=True) #get shape of selection
	shadingGrps = mc.listConnections(shapeNode[0], type='shadingEngine')
	shader = mc.ls(mc.listConnections (shadingGrps[0]), materials=1)
	
	mc.select(shapeNode[0])
	mc.addAttr (longName="Cd", attributeType="double3", keyable= True) 
	mc.addAttr (longName='CdX', attributeType="double", keyable= True, parent="Cd") 
	mc.addAttr (longName='CdY', attributeType="double", keyable= True, parent="Cd")
	mc.addAttr (longName='CdZ', attributeType="double", keyable= True, parent="Cd")
	mc.connectAttr(shader[0]+".colorR", shapeNode[0]+ ".CdX")
	mc.connectAttr(shader[0]+".colorG", shapeNode[0]+ ".CdY")
	mc.connectAttr(shader[0]+".colorB", shapeNode[0]+ ".CdZ")

for each in selection:
    mc.select(each, add=True)
	
#export with alembic
start = 1
end = 1
root = "-root"+ " -sl"

attributes=["CdX", "CdY", "CdZ"] #created attributes list
attrString=""
for each in attributes:
    attrString += " -attr "+each 

save_name = R"C:\Users\Sigrid\Documents\maya\projects\tests\cache\Test_01.abc"#add directory

command = "-frameRange "+str(start) + " " + str(end) + attrString +" -uvWrite -worldSpace -sl"+ " -file " + save_name
mc.AbcExport (j=command)
```