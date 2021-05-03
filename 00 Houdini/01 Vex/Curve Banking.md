## Curve Banking
Tag: #vex #vex-vector 
Link : [Curve Banking](https://vimeo.com/222643398)

Create `up` `side` `tangent` vector first (use polyframe sop to create the tangent vector first)

```javascript
int prevId = clamp(@ptnum -1,0,@numpt);
int nextId = clamp(@ptnum +1, 0,@numpt);

// get previous position and next position
vector prevPos = point(0,"P",prevId);
vector nextPos = point(0, "P", nextId);

// get previous and next side vector
vector prevSide = point(0, "side", prevId);
vector nextSide = point(0, "side", nextId);

vector preDisp = prevPos + prevSide;
vector nextDisp = nextPos + nextSide;

float dist = length(prevPos - nextPos);
float displaceDist = length(preDisp - nextDisp);

f@ratio = (displaceDist/dist)-1;

f@ratio = clamp(f@ratio, -0.5, 0.5);
```
![[shot_210425_201509.png]]