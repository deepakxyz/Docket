Tags: #Node
Software: #Houdini 
Link: https://www.sidefx.com/docs/houdini/basics/intro.html#overview
Created on: 2021-03-02
___________________________________
# Introduction to Houdini
> On this Page
>  - Overview
>  - Nodes and networks
>  - Geomentry and attributes

## Overview

Houdini is an advanced procedural modeling, animation, effects, simulation, rendering, and compositing package.

Houdini’s power is based on **procedural workflows**. Working in Houdini involves creating networks of nodes connected together that describe the steps to accomplish a task. For example, a node that creates a box might be wired into a node that extrudes sides of the box, then a node that subdivides the polygons, then a node that edits the point positions. This gives you tremendous power:

-   You can go back to previous nodes in the network and change selections, change settings, or swap out assets. The changes automatically propagate through the network to change the final result. You never have to undo or start over and recreate your work to change a decision you made earlier.
    
-   It encourages rapid prototyping. You don’t have to throw away work you do exploring ideas… just reuse parts of the network or reconfigure the network to upgrade it to production quality.
    
-   Because Houdini is based on generating things procedurally, it has lots of tools for managing extremely large and complex scenes, with support for generating/loading geometry and adding detail at render time instead of keeping everything in memory.
    
-   You can package up networks and make them into new tools with their own interfaces, without having to write any code. In Houdini these tools are called [digital assets](https://www.sidefx.com/docs/houdini/assets/index.html "Digital assets let you create reusable nodes and tools from existing networks.").

## Nodes and networks

Houdini lets you work in the 3D view using the shelf tools without having to worry about nodes and networks. However, an understanding of networks is essential of getting th most out of Houdini.
![network_editor](network_editor.jpg)

Houdini’s networks are like a computer’s file system, where networks are like folders and nodes are like files. Nodes can be _subnetworks_ that contain other nodes.

The root network contains a few pre-made networks like `/geo` (the "scene" network) and `/out` (where render nodes go). Networks have a "type" (such as "geometry network" or "dynamics network") that controls what types of nodes you can put in the network.

The scene level (`/geo`) contains objects such as characters, props, and lights. [Geometry objects](https://www.sidefx.com/docs/houdini/basics/objects.html) are subnetworks that contain geometry nodes that define the object’s geometry. This two-level design is different from other packages such as Maya and 3D Studio Max where all nodes are in one level.

The scene level can also contain nodes that don’t represent objects in the scene, they're purely subnetworks. For example, when you set up a simulation, the nodes defining the simulation are inside a Dynamics subnet at the scene level.

Houdini’s [user interface](https://www.sidefx.com/docs/houdini/basics/ui.html) is divided into different types of [panes](https://www.sidefx.com/docs/houdini/basics/ui.html#panes), such as the 3D viewer, the network editor, and the parameter editor. Each pane can focus on a different network, but by default they're all set up to follow the same network as each other.

Each node has a user interface of settings called _parameters_ you can edit in the parameter editor pane to change the function of the node.

![parms](parms.png)

## Geometry and attributes
Houdini supports different types of geometry, such as polygons, NURBS and Bézier, geometric primitives such as circles and spheres, metaballs. Houdini refers to each "piece" of geometry of any of these types as a _primitive_. For example, a polygon face is a primitive, a polygonal curve is a primitive, a metaball is a primitive.

![[mountain.png]]
This is less-than-ideal terminology, because some "primitives" have editable components. For example, polygon faces have points and vertices.

Much of the information that makes up a scene is stored in _attributes_, hidden data stored on models, primitives, points, and vertices. For example, Houdini displays points at the position in space defined by their `P` (for position) attribute.[^new]

[^new]: This supports *vex* and it can be played in the wrangle node.


You can always view the actual attribute values on geometry in Houdini using the [geometry spreadsheet](https://www.sidefx.com/docs/houdini/ref/panes/geosheet.html).

![geometry_spreadsheet.png](geometry_spreadsheet.png)
![[houdini_p.png]]


## Vex
Vex inclueds an array datatype.[^hello] This is useful in several places:
- Supporting ramp paramters
- Reading capture data from surface nodes using the import() function.
- General prgramming, wherever arrays would be useful.

[^hello]: This is the seond note.

> **Note**
> Currently VEX does not support multi-dimensional arrays.

This example shows off some of the crazy things that you can do with arrays.
```javascript
surface 
crazy(
	string maps\[\] = { "Mandril.rat", "default.pic" }; export float alength = 0; 
	) 
{
 	vector texclr, av\[\];   texclr = texture(maps\[s+t > 1\], s, t);
	av = array( {1,0,0}, vector(nrandom()),
	 t, texclr, {.5,0,0});   if (fit(noise(s\*8), 0, 1, .3, .7) > t) 
		av = array(1, {0,1,0}, 0);
	Cf = spline("linear", s, av); alength = len(av); 
}
```

