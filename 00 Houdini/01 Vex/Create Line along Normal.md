# Create Line along Normal
```javascript
v@N = normalize(@P);
vector p, uvw;
int hits = intersect(0,v@P + v@N * 0.001, v@N,p, uvw);

if (hits <=0 ){
    int newpoint = addpoint(0,v@P + v@N);
    int newprim = addprim(0, "polyline", @ptnum, newpoint);
    setprimgroup(0, "strings", newprim ,1);
    
}
```