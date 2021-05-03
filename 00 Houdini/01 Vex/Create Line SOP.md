## Line Sop using Wrangle node
Tag: #vex-line #vex-add #vex-point

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