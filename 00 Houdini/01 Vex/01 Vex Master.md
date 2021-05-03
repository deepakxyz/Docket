# Vex - Houdini
- [[Curve Banking]]
- [[Create Line SOP]]
- [[Create Line along Normal]]



## Make a point at the center of each primitives
Tag : #vex-point #vex-add-point
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
Tag: #vex-add-point

Run it over Detailed
```javascript
addpoint(0,getbbox_center(1)); // connet it to the second input of the wrangle node
```



# Expressions

### Select point 0 at the line
Tag: #vex-select
Run it over *Group Expression*
```javascript
vertexprimindex(0,@ptnum)==0
```

### Delete some percent of tha point
Tag: #vex-select
Run over group by expression
```javascript
rand(@primnum+234)>0.5; // 50 percent of the prim
```
