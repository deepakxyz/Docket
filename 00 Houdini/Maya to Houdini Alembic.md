Tags: #export #import #alembic
Software: #Houdini 
Link: 
Created on: 2021-03-07
___________________________________
# Maya to Hodini Alembic Export
*Export alembic in maya and import it in houdini and seprate it with path attribute in houdini.*

## Add a python node.
Change the path from 
`/lou_v1/body/lou_body/lou_bodyShape`
To
`/lou_v1/body/lou_body`

@node: Python
```python
node = hou.pwd()
geo = node.geometry()

for prim in geo.prims():
	path = prim.attribValue('path')
	newpath = path[:path.rfind("/")]
	prim.setAttribValue("path",newpath)
```


## Seprate with catogary and set different color.
@node: Primitive Wrangle
```javascript
s@cat_name = ch("name");
// set random color for the object
int hash = random_shash(s@cat_name);
@Cd = set(rand(hash), rand(hash+2345), rand(hash+2356));
```