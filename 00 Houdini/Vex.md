## Make a point at the center of each primitives
### Simple Method.
Run it over primitive.
```javascript
// it takes the average of all the points in the primitive.
addpoint(0,@P);

//  remove primitive along with its point
removeprim(0,@primnum,1); // can use even removepoint

```
Run it over primitive.
### Complex method.
```javascript
// create a list of all the primitive points
int primPoints[] = primpoints(0,@primnum);

// center position
vector center = 0;


foreach(int primPoint; primPoints){
    center += point(0,"P",primPoint);
    }
// remove the primitive and 1 removes the points too
removeprim(0,@primnum, 1);
// 
center /= len(primPoints);
addpoint(0,center);
```


## Create a point at the center of the object
Run it over Detailed
```javascript
addpoint(0,getbbox_center(1)); // connet it to the second input of the wrangle node
```

## Line Sop using Wrangle node
Run it over Detailed.
```javascript
int pointCount = chi('Points');
int points[];

// increase the array size
resize(points, pointCount);


for (int i =0; i < pointCount; i++){
    vector direction = fit01(chv('Direction'),{0,0,0},{1,1,1});
    float length = chf('Length');
    vector origin = chv('Origin');
    vector P = set((i*direction.x*length) + origin.x,
                    (i*direction.y*length) + origin.y,
                    (i*direction.z*length) + origin.z);

    int pointId = addpoint(0, P);
    points[i] = pointId;
}

addprim(0, "polyline", points);
```

### Adding all the point to a prim
```javascript
int points[];
resize(points, @numpt);
for(int i=0; i < @numpt; i++){
    points[i] = i;
    }

addprim(0,"polyline",points);
```