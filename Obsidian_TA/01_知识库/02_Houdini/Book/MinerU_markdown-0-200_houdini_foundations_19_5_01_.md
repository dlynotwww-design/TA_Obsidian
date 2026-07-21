## Houdini FOUNDATIONS

FOR FILM, TV & GAMEDEV 

VERSION 19.5 EDITION 

## Houdini FOUNDATIONS

FOR FILM, TV & GAMEDEV 

VERSION 19.5 EDITION 

ROBERT MAGEE 

## HOUDINI FOUNDATIONS

Author: Robert Magee Research: Michael Buckley, Marcia Utama Cover Art: Atila Torok 

Special thanks to Kim Davidson, Richard Hamel, Chris Hebert, Cristin Barghiel and everyone at SideFX who brings Houdini to life. 

## ISBN: 978-1-7753338-2-1

First Published in 2022 by SideFX Software 123 Front Street West, Suite 1401, Toronto, Ontario M5J 2M2 

## © SideFX Software

Writen for the features found in Houdini 19.5 Document Version 2.0 | December 2022 

© 2022 | All rights reserved. SideFX, Houdini, Houdini Engine and the Houdini logo are trademarks of SideFX Software Inc. registered in the USA and other countries. Autodesk, Maya and 3DS Max are registered trademarks or trademarks of Autodesk, Inc., in the USA and other countries. Unreal Engine and its logo are Epic Games’ trademarks or registered trademarks in the US and elsewhere. Unity is a registered trademark of Unity Technologies. Other product and company names mentioned may be trademarks 

of their respective companies. 

DISCLAIMER: Every reasonable efort has been made to obtain permissions for all articles and data used in this book, and to make it as complete as possible. This book should be considered “as is” and neither SideFX, nor its employees, oficers or directors shall be responsible or incidental for consequential damages resulting from the use of this material or liable for technical or editorial omissions made herein. 

## CONTENTS:

1 | OVERVIEW
Learning Houdini
The Houdini Workspace
Panes & Desktops
Nodes & Networks
Parameters, Channels & Attributes
Selecting Geometry
Transform & Edit
Modeling Tools
UVs & Textures
LookDev: Shaders & Materials
Solaris: Layout
Solaris: Cameras and Lights
Rendering
Time & Motion
Character Rigging & FX
Dynamic Simulations
Cloud FX & Volumes
Terrain & Heightfields
SideFX Labs
File Management
Expressions & Scripting
Tasks
HOUDINI DIGITAL ASSETS: Procedural Tool Building
HOUDINI ENGINE
Sharing with other Apps
FILM & TV PIPELINE
Animation and VFX
GAMEDEV & VR PIPELINE
Interactive Experiences
Products & Licensing
Comparison Chart
2 | MODEL, RENDER, ANIMATE
1. Explore the Houdini UI
2. Create a Soccerball
3. The For-Each Node
4. Setting up UVs
5. Layout: Cameras and Lights
6. Lookdev: Materials
7. Rig the Soccerball
8. Animate a Bouncing Ball
9. Lights, Camera, Action!
10. Set up a Rigid Body Simulation 

3 | NODES, NETWORKS & DIGITAL ASSETS 75
1. Create a Single Brick 76
2. Copy Bricks to a Point Cloud 78
3. Add Color and Switch to a Teapot 80
4. Color the Points using a Texture 82
5. Create a Brickify Digital Asset 84
6. Test the Digital Asset 87
7. Animating the Bricks 88
8. Loading HDAs into other Applications 90

4 | SMASHING WINE GLASS 91
1. Model the Wine Glass 92
2. Model the Bullet 94
3. Fracture the Wine Glass 95
4. Set up the RBD Simulation 97
5. Add Fluids to the Simulation 99
6. Cache and Re-time the Simulations 100
7. Set up and Render the Shot 103
8. Assign Materials and Render a Sequence 105

5 | DESTRUCTION FX 107
1. Model the Bomb 108
2. Model the Fuse 110
3. Animate the Fuse 112
4. Create an Animated Camera 114
5. Create a Soot Trail 116
6. Create Particle Sparks 118
7. Blow up the Bomb 120
8. Create the PyroFX Explosion 122
9. Export the Geometry to USD 124
10. Set up Shot in Solaris 127
11. Render the PyroFX 130

6 | TERRAIN GENERATION 133
1. Shape the Terrain using Heightfields 134
2. Add and Visualize Mask Layers 136
3. Remap and Erode the Terrain 138
4. Scatter points on the Terrain 139
5. Open the Terrain in Unreal 140 

7 | KINEFX RIGGING | FUR DUDE 141
1. Draw the Skeleton 142
2. Capture the Geometry 144
3. Add More Bones 145
4. Joint Orientations 147
5. Attach Capture Geometry 148
6. Paint Capture Weights 150
7. Capturing the Rigid Geometry 152
8. Create Capture Rig Digital Asset 154
9. Create the Animation Rig Asset 156
10. Add More Control Joints 157
11. The Main Controls 159
12. Inverse Kinematics for the Legs 162
13. Reverse Foot Setup 164
14. Promote the Leg and Spine Controls 167
15. Eye Controls 169
16. Animate the Rig 172
17. Add & Groom the Fur 175
18. Set up an Render the Shot 177

8 | PROCEDURAL ASSETS FOR UNREAL 181
1. Create a Simple Building 182
2. Import the Asset into Unreal 184
3. Copy to Points 187
4. Create another Houdini Digital Asset 189
5. Set up Instancing 191
6. Use Geometry to Drive Asset 193
7. Import RBD Simulation into Unreal 195

9 | BUILD A CITY WITH PDG 197
1. Create a City Grid 198
2. Generate and Display Work Items 199
3. Add Attributes 201
4. Create Buildings for the City Grid 202
5. Combine the Buildings 204
6. Isolate a Building 207
7. Wedge the City Core Location 208
8. Create Geometry for the Streets 210
9. Wedge Four City Maps 212
10. Render a Mosaic 213
11. Scale Up to Create More Content 215 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/44c1eb679ce62fb5534fe2055a5f9a538ddd026df98c722cdb1cf46280444ecb.jpg)


## HOUDINI FOUNDATIONS OVERVIEW

To create 3D animation and VFX for Film, TV, Video Games and VR, you need a combination of technical and creative skills. Houdini is the perfect tool for bringing these worlds together as you explore, create and refine your projects from concept to final sign of. 

While Houdini has a wide variety of tools designed for generating CG content, its node-based procedural workflow is what sets it apart. This approach makes it easier for you to create directable shots, explore multiple iterations and hit deadlines. As you learn Houdini, understanding how to work with these nodes and networks will be important to your success. 

## WHAT YOU WILL LEARN

This overview chapter contains general information about Houdini that will help you become familiar with important concepts and ideas. While you might not understand what it all means, this chapter will be a valuable reference point as you work through the foundation tutorials and build up your knowledge. 

 If you already work with 3D software then learning Houdini will be a transfer of existing skills. You will learn how to interactively build-up shots using the scene view and shelf tools, then how to work with the nodes and networks to take advantage of Houdini’s procedural nature. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3b36497d7e7278a757893844c17c3f0a28623ab5438426d0c1f64a041c39748f.jpg)


 If you are new to 3D and Computer Graphics then Houdini is a great package to start with. The Foundations material assumes some general knowledge, therefore you may want to read up on CG concepts that you are unfamiliar with. In the end, Houdini will help you achieve a deeper understanding of what goes on under the hood of not only Houdini but other 3D apps as well. 

Once you have finished the foundation lessons, visit SideFX.com for more tutorials. From the main menu, go to Learn > Learning Paths for a comprehensive list of lessons created by SideFX and members of the Houdini community. There are lots of lessons for you to explore as you build up your Houdini skillset. 

## DOWNLOAD HOUDINI FOR FREE

SideFX has a free learning edition for you to use as you work through the lessons. The Houdini Apprentice edition gives you FREE access to all of Houdini’s features with a few restrictions such as limited render size and user interface and render watermarks. 

You can download Houdini Apprentice from the SideFX website where you can also get the latest versions which are updated regularly: SideFX.com/download 

## INDIE ANIMATORS AND GAMERS

If you want to go beyond the free learning edition, Houdini Indie removes the watermarks found in Apprentice and ofers higher render resolutions up to 4K x 4K and limited commer cial use [less than $100K USD] of Houdini. The Indie program makes Houdini a great tool for developing personal projects and indie games. To learn more you can go to: SideFX.com/indie 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5b0c64ca89a376c7d9b63dfda5d0887976605b81e4792893aaac4dc639c1ab9f.jpg)


# Learning Houdini

Houdini is a computer graphics, or CG, applicati on which you can use to model, animate, render and simulate. In the process of learning Houdini, you will explore new ways of managing the creati ve process that involves the interacti ve manipulati on of nodes, networks and assets. 

Everything is procedural in Houdini, which means that modeling, character rigging, lighti ng, rendering and visual ef ects all benefi t from a node-based workfl ow where arti sts can build up networks of nodes to manage all the steps needed to complete a creati ve task. Networks can then “talk” to other networks to create even more sophisti cated systems. 

## GOING PROCEDURAL

In Houdini, every acti on you take is stored as a node. These nodes are then “wired” into networks which defi ne a “recipe” that can be tweaked to defi ne a repeatable outcome where each iterati on can generate unique results. The ability for nodes to pass important informati on down the chain, in the form of at ributes, helps give Houdini its procedural nature. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bfed2228de9e4f0cb96cc718a097177e522378f96882ea583252a942a192238d.jpg)


## KNOWN FOR VFX

Visual ef ects arti sts have traditi onally gravitated to Houdini because this procedural workfl ow is ideal for working with parti cles and dynamics. Oft en visual ef ects are designed to react to acti ons that are taking place in a shot and a procedural soluti ons “automate” these reacti ons. Therefore, Houdini provides studios with higher levels of producti vity and more control over the creati ve process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83266fef2a5d432eecef6c2f170ee1ca1f68d8df4f2130b2f7d88c590dc27e0c.jpg)



Houdini is also capable of working with large data sets which is criti cal as visual ef ects become more sophisti cated with many layers such as rigid body destructi on, fl uids, and parti cles all interacti ng to achieve the fi nal result.


## PROCEDURAL CONSTRUCTS

For moti on graphics projects, a procedural approach of ers lots of visually-stunning eye candy. These special ef ects are oft en the result of animati ng parameters on nodes and adding noise in interesti ng ways that you wouldn’t expect in real life. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b69c792e5083089ea018abcea22fff0dc498c861821f79997ff839270d2919f1.jpg)


## THE WIDER CG PIPELINE

Beyond VFX and moti on graphics, Houdini has bread-andbut er tools for all parts of the pipeline from modeling to rendering to character work and gamedev. Its procedural workfl ow supports you as you create all of your CG content. Along the way, you will benefi t from the ability to explore multi ple iterati ons and make changes deep into producti on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/25f2848f09e7f47af9dc2e71c0df14ed126f19fd84177becd58d4d9f485f3c84.jpg)



While the nodes are what makes Houdini unique and give it its power, there are lots of viewport and shelf tools that are used to work interacti vely while Houdini builds the networks.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9217412808c2576909ee0d67fff5d66886afe7e3470642b44ca0a97b7e4c9d9c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/49be77adce48886e20a9244ee53e5f0933c0625f2a10bb08c6bec1b081261df8.jpg)


## DIRECTABLE RESULTS

The reason you are able to make edits deep into producti on is because changes made to parameters on Houdini nodes will cascade right through the network to update the results. This directability is retained throughout the creati ve process and can be used to make last minute decisions that would be too costly in a traditi onal CG pipeline. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b1b92b01536f4c6e277d7839c94d37c3bd9de79b80402eb99562288b3321af65.jpg)


## TOOL BUILDING

Another benefi t of the node-based approach is that it is easy to encapsulate node networks to create custom nodes that are shared with colleagues without writi ng any code. Houdini’s re-usable networks can be wrapped up quickly and easily into special nodes called Houdini Digital Assets. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/193524007dd0efdf3a8c14063826a8c3d8ce301273fabf832a1b1a8fb9816ab3.jpg)



These assets open in Houdini, or in other applicati ons such as Autodesk Maya, 3DS Max, Unreal and Unity using Houdini Engine plug-ins, with the asset’s procedural nature left intact.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2dc730e2c6dcfd1d4a5d0d0b6ab47b8745533117af4a67d22e705fdd951cf19f.jpg)


## FULL ACCESS TO ALL YOUR DATA

As objects move through a typical animati on or visual ef ects pipeline, they accumulate informati on which is oft en stored as point or primiti ve at ributes such as velocity, capture weights or UV texture coordinates. While other 3D applicati ons hide this informati on and at empt to control it for you behind the scenes, Houdini gives you tools for working with and managing this data. This results in a much more powerful and fl exible approach that makes a huge dif erence down in producti on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bf82eba0647cb026f57024d0551aa97184abd0c55523bef3bd5928fbf3345e44.jpg)


## A NEW WAY OF THINKING

As you become more profi cient with Houdini, you will fi nd new ways to approach a shot or a game level that will make you and your team more producti ve. Houdini gives you the fl exibility to build tools that will support you throughout a project’s life cycle and instead of simply reacti ng to issues and problems, you will be able to anti cipate the pain points and use a procedural soluti on to work much more efi ciently. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/383a34d0e26c3eae4a54f4ba1854ec09de138f9a98a8e61cb36fc876e1e8e6a0.jpg)



Now that you have chosen to learn Houdini, you will fi nd yourself exploring a versati le applicati on that will redefi ne how you approach future projects. The key is to embrace this new way of working and be ready to explore CG at a level deeper than you ever imagined.


## DO I NEED TO WRITE CODE TO USE HOUDINI?

DEFINITELY NOT! In fact, because of Houdini’s node-based workfl ow, you will oft en be able to create results interacti vely that would require writi ng code in other 3D applicati ons. Houdini is very much an arti st’s tool and while it has a technical side that uses scripts and expressions, the out-of-box tools will let you accomplish amazing things. And the nodes let you easily go back and make changes which mimics how the creati ve process works. 

If you do want to work with code then Houdini supports a number of languages inside the Houdini interface. There are Wrangle nodes for working with VEX and Python and PyQT is supported as well. You can also use Houdini’s expression language hscript or you can mix all of them together to meet your specifi c needs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6fedbb88e754d192056a34928dc3cec55549e60607df1ede63dd46084140bb2d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/57713d8223887905bc84b35977ce669562fec284c724c7bf18f51b96ed2f134c.jpg)


# The Houdini Workspace

Houdini of ers a user interface experience that will be familiar for arti sts coming from other CG applicati ons with the biggest dif erence being the panes used to manage nodes and networks. The workspace is highly confi gurable and can be set up to support dif erent ways of working. 

Houdini gives arti sts many dif erent ways to view the bits and pieces that make up a 3D scene. From the Scene View where you look through a camera at your geometry to the Network view where you manage the procedural nodes and networks, you will fi nd many dif erent ways to make creati ve decisions while making sure each shot works at a technical level. 

## RADIAL MENUS

One way to access tools in the Scene View is the radial menus which you can access using the X, C and V hotkeys. Each of these brings up a radial menu with lots of opti ons for you to choose from. The main focus of each menu is as follows: 

 Snapping 

 Main 

 Views 

Once you learn how a radial menu works, you can access the tool with a quick sweep gesture without dwelling on the widget. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4c3181da3a54587821e2cb8d5c807b041b1560fcc2b0076fe50b1de10e5fbeb0.jpg)


You can change the custom menu at the top of the menu bar which says Main by default. On OS X this is the Radial menu. 

Tool Shelf - The shelf tools let you work with objects and geometry in the scene view. 

TOOL BAR: 

Selecti on Modes - Focus on scene, geometry, or dynamic objects. 

Select Tools - Select, Secure Selecti on 

Transform Tools - Move, Rotate, Scale or Pose or the Handle tool for node-specifi c controls. 

Snapping Tools - Turn on Grid, Primiti ve, Point or Multi -snapping. 

Viewing - Use the View tool to Tumble, Pan and Dolly or Render Region to render in the Scene View. Click and hold to change to 2D Pan and zoom. 

Output Tools - You can render or fl ipbook your scene with these tools. 

## SHELF TOOLS

At the top of the workspace, you will fi nd multi ple shelves fi lled with tools for creati ng and manipulati ng objects, geometry, cameras, lights and ef ects. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a08bbe0cd325d085a3ad724170d0b76f33cdc9ff217f43f172f59e3cb1d96e8b.jpg)


These tools work in the scene view and oft en involve some sort of scene view interacti on. Once you have used one of these tools, one or more nodes will be created which you can then refi ne in the Parameter and Network panes. 

The shelves provide a very important resource to new Houdini arti sts because the shelves reduce clicks and oft en put down networks of nodes that you can learn from. 

## TAB MENU

Another way to access tools in either the Scene view or the Network view is to press the tab key. This brings up a menu of available tools and nodes you can use in your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e3d69c342caad2afa9832998df584101fa49eaa1f0cb5381959f1445f9f63963.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83ccc94812c0b6943c7b70e50304cc1f631e384653bd419e964618e713b3a4b5.jpg)


## 3D VIEW TOOLS

Here are some of the hotkey combinati ons available while viewing. You can skip spacebar/alt if you are actually in the View tool: 

Tumble Spacebar or Alt[Opt] - Left Mouse But on [LMB] 

Pan Spacebar or Alt[Opt] - Middle Mouse But on [MMB] 

 Dolly Spacebar or Alt[Opt] - Right Mouse But on [RMB] 

You can fi nd the View tool in the toolbar. When you use the spacebar or alt keys, you temporarily evoke the view tool. This can be quite useful when you are selecti ng or manipulati ng in a view and need to quickly change your point of view. 

If you want to focus on viewing then you can press Escape to go to the View tool. Here are some other hotkeys, you can use to get your bearings: 

 Home Constructi on Plane 

Spacebar + H 

 Frame All 

 Home Selected 

Spacebar + A 

Spacebar + G 

## 2D PAN AND ZOOM

You can click on the 2D Pan and Zoom tool in the Operati on Control bar to change your view in 2D without altering your 3D camera positi on. The widget at the top left lets you click to pan and zoom or to reset the view with Ctrl - LMB click. This is a great tool for working with locked of cameras. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/18287fa3d81f9efd25ff5599cdd1eef16d4647b7f7d056a6d6dbf483e1fcaae7.jpg)


Viewport Display Menus - These tabs let you create and organize multi ple panes at the same ti me. 

Pane Tabs - These tabs let you create and organize multi ple panes at the same ti me. 

Operati on Controls - Use the Handle tool with this bar to access parameters from your selected node. 

Parameter Pane - This pane lets you set values, add expressions and keyframe selected nodes. 

Display Opti ons Bar - These toggles let you control scene display opti ons such as normals, point numbers or lighti ng. 

Scene View - Visualize your work and use handles to manipulate objects interacti vely in your scene. 

Network Pane - View and manage networks of nodes to work with the underlying structure of your scene. 

Playbar - Set the current ti me and edit keyframes on selected nodes. You can also use the Playbar to copy and paste keyframes. 

## FIRST PERSON CAMERA

While in the View tool, you can turn on a fi rst person fl y through mode similar to those used in videos games. 

 Toggle First person On/Of M 

 Dolly In/Out W/S 

 Pan Right/Left A/D 

 Look Around LMB 

## VIEWPORT DISPLAY MENUS

Change how objects appear and views are organized using the menus in the top right of the Scene view or the V radial menu. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/041a358a6fbb92015d53b5e7e29fd56296335a04ea1778d1ada3a0a6a3b4b07c.jpg)


Shading Menu - Choose from opti ons such as wireframe, fl at shaded, smooth shaded or smooth wire shaded. 

Object Display Menu - As you dive into networks, this menu sets whether you hide, view or see geometry ghosted. 

Views Menu - This menu lets you split your scene view into various views such as perspecti ve or orthographic views. 

## DISPLAY OPTIONS BAR

At the right side of the scene view, the display bar gives you access to opti ons for viewport display. Here are a few examples. 

Reference Plane/Ortho Grid - Turn on and of a grid that can be used for reference and for grid snapping. 

Constructi on Plane - Turn on and of a constructi on plane which is used to defi ne where you place objects or points. 

Lock Camera- Lock the current camera to the view so that view changes modify the camera transform values. 

High Quality Lighti ng with Shadows- Set the best quality of viewport rendering. 

Display Primiti ve Normals - Show the normals belonging to all primiti ves in the scene to determine their directi on. 

## DISPLAY OPTIONS

The Scene and Network views each have Display opti on panels that you can access by clicking on the icon at the bot om of the Display opti ons bar or using the following hotkey: 

## Display Opti ons

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f17dde71da42358abc2162f7d38cf6aea625efca8d86f2230d7e1e8dbb37b4a1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/24134fa833e002aa8229c03d9beee4fc7a7f653fa5bdcc29f9a551b504eeff36.jpg)


## Panes & Desktops

The Houdini workspace is broken up into Panes which of er unique ways of organizing your scene data. You can work interacti vely in a 3D view or analyze at ribute values in a spreadsheet. It is important to learn how these dif erent UI elements can be used to get your work done. 

## PANES AND PANE TABS

The Houdini workspace is divided into panes so that you can set up and explore your scene. Pane tabs let you overlap several panes within the same zone to keep them handy but not visible by default 

You can access a pane tab by clicking on it in the workspace. You can close it by clicking on the x. The + menu can be used to change the pane you are looking at or to add new panes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c5c0ddaf725959d0222d5daf861a07a6919fe99b57a3a9e56f0254d62f0af13.jpg)


## PANE TYPES

RMB-click on the pane tab to change its type. There are many pane types to choose from. Here are some of them which have hotkeys. Some of the other ones are listed here. Refer to the documentati on to fi nd learn more about all of the others. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a9cf7dcda4866e5e0b49b4f6facd9fb010b744cdc758cb78de9bbde57ac966cd.jpg)


Network View [Alt-2] - This view lets you see the nodes and networks and connect, rewire, and reorganize them to suit your needs. 

Parameters [Alt-3] - Set values on parameters, add expressions and control the properti es of your nodes. 

Tree View [Alt-4] - This is a hierarchical view of the nodes. This can be a great way to understand how scene hierarchies work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f68b653e6c96d7752104c371394516a9b072188ff8e1fc024a07d45a79978264.jpg)


Viewers > Scene View [Alt-1] - Work interacti vely in 3D space. This type of view can be set up with one or more viewports. You can have more than one scene view panels open at the same ti me to look at your scene from dif erent points of view. 

Composite View [Alt-0] - View images and composites created using Compositi ng [COP] nodes. 

Viewers > Moti on FX View [Alt-^] - This lets you view moti on created using Houdini’s channel operator [CHOP] nodes. 

Solaris > Scene Graph- This pane shows you the USD scene graph when working with Solaris [LOP] nodes. 

Solaris > Render Gallery - This pane lets you save test renders then revert back to the seti ngs of each image aft er reviewing them all. 

Solaris > Light Linker - Connect lights and objects. 

Render Scheduler - This panel shows you Renderings that are completed and in progress. You can pause and kill renderings here. Material Palet e [Alt-7] - This palet e lets you see all the materials in your scene and select and assign them to objects and geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/875c19e93fbbb1b47c47658be7cdbb2de40336d8e87d9d9bed9321625b8f8f70.jpg)



Animati on > Animati on Editor [Alt-6]- Manage keyframes and animati on curves. The editor also has Table and Dope sheet views.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/75779e3a4f9fdbd08277b99324e9795b73da4cfc8f577e07c599ab0304caeab5.jpg)


Animati on > Channel List - Create channel groups and manage the scoped channels as you animate in Houdini. 

Animati on > Autorigs- This pane gives you access to tools for building your own rig out of modules for biped, quadruped and facial rigs. 

Animati on > Character Picker - You can use this pane to make it easier to select parts of a character rig. 

Inspectors > Geometry Spreadsheet [Alt-8]- A view of the at ribute values you have on your geometry. This could include UVs, normals, or custom values you have set yourself. 

Inspectors > Data Tree- This view gives you access to a light bank, Material Stylesheet and Object appearance list. 

Mantra Rendering > Render View [Alt-9] - Start interacti ve Mantra renderings, that will update when you change something in your scene. 

Mantra Rendering > Take List- This list lets you explore dif erent “takes” by making changes to specifi c parameters. You can then manage the takes to focus on your preferred creati ve choices. 

TOPS > Task Graph Table - The Task Graph Table shows the metadata of all work items in the graph, or all work items in a parti cular node. 

Misc > Orbolt Asset Browser - This browser lets you access assets from Orbolt.com. To use this pane you need to log in with an orbolt.com account. 

Misc > Textport - You can use this pane to type commands. 

Misc > Python Shell -You can type Python commands using this pane. 

## ORGANIZING AND COLLAPSING PANES

Both panes and tool bars can be collapsed and expanded by clicking on the arrows found in their UI. Whole panes can be collapsed to the left or right and you can fl ip the contents using the center grip. These opti ons let you focus on certain panes by hiding others using a single click of the mouse. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a307423805aae81e936ebf81eff06db8bd6556871af2d982f82aebc254dbdf9c.jpg)



LMB-click here to collapse down


## PANE MENU

At the top left of each pane is a but on for maximizing and minimizing the pane and an arrow which gives you access to the Pane menu. This menu lets you tear of the pane or a copy of the pane, close, or split your pane. You also have opti ons for determining the UI of each pane. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c3b0415fc6390b6724ac44d388c9353db91444f14f2ffc0f1f2a3528f8748011.jpg)


## DESKTOPS

As you open up tabs, add dividers and organize your pane tabs, you start to set up your own workspace. To save any layout, go to the Desktop menu (Windows > Desktop on OSX) where you can access saved desktops, save your own and manage them as you work. When you save a desktop, it will save the Pane layout, Radial menus and visible Shelf sets. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c4674d52dec50adc85966bffca53369f5c75aad72f49fdd05ff4a43c2766eb3d.jpg)


When you save your scene, it remembers which Desktop you are looking at but not any changes to the pane layout while working. These changes will go away unless you explicitly save them to the desktop or create a new desktop. 

## SHELVES AND SHELF SETS

To manage the shelves at the top of the workspace, access the menu found under the arrow icon. You can use this to work with Shelf sets. You can also bring up shelf sets that might be hidden in your desktop. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b7a460da8e12aea9509def54d2f2ab759d000d1945ddd103a5408b92365c972d.jpg)


## COLOR SETTINGS

You can customize the look of the Houdini UI by choosing a color scheme for your workspace. Select Edit > Color Seti ngs to bring up the opti on window then you can choose from the default Houdini Dark or Houdini Light. Click on the Download but on to choose from a list of color schemes created by the Houdini community. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/520df49032bc51cdee169c66baf80509d059c35ef74cf65348d018e247813fb0.jpg)


# Nodes & Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9a5d915fd5d3cd2ae8578ec4121e39e675dada8dd2f3bc581f506638ba0b7a4a.jpg)


With Houdini’s node-based workfl ow at the heart of its procedural architecture, the ability to work directly with these nodes and networks becomes very important to using it ef ecti vely. While the idea of nodes might sound technical, they are actually quite arti st friendly and easy to work with. 

As you use tools in Houdini, nodes are created and wired with other nodes. The resulti ng networks of er a history of your acti ons while providing a simple way to make changes and refi ne your work. Learning how to work ef ecti vely with the node networks is an important part of working with Houdini. 

## NODE FLAGS

Each of the nodes have various fl ags which determine if it is displayed, locked or bypassed. You can evoke these by either clicking on the fl ag itself or using the radial node menu. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c21ebca7f5a54ee64226a5713520d1370c492c59396eeda8723e66081ae6d97c.jpg)


Display Flag [R] - This fl ag lets you choose the display output node for the network and is highlighted with a hollow ring. The Render fl ag [T] sets which node will be output for rendering and is highlighted with a solid circle. You can set this separately from the Display fl ag by Ctrl-clicking on the Display fl ag. 

Template Flag [E] - This fl ag displays the node in grey and can be used for reference or snapping. 

Freeze Flag - This caches at the locked node and all nodes earlier in the chain are ignored when the network is cooked. 

Bypass Flag [B] - This fl ag lets you ignore the node when the network is cooked. 

## CONNECTING AND DISCONNECTING NODES

When you work in the Viewport, nodes are oft en placed and wired together automati cally. When you want to reconfi gure how a network is set up, you will need to connect and disconnect nodes by hand. 

Here are some ways to interact with nodes and connecti ons in the Network pane: 

 Connect Node 

 Connect Nodes 

Insert New Node 

 Insert Node 

LMB-drag from output to input J drag across the nodes 

RMB on an output or connector 

LMB drag and drop onto connector wire 

 Disconnect from Wires 

 Cut Wire 

 Move node 

LMB select then Jiggle node(s) 

 Copy selected nodes 

Y drag across connector wire LMB-drag 

 Reference Copy 

Alt + LMB-drag 

Alt + Shift + Ctrl + LMB-drag 

Dot nodes can be used to organize your networks: 

 Add Dot Alt + LMB wire 

 Pin/Unpin Dot Alt + LMB dot 

## NODE GALLERIES

The galleries of er quick access to nodes that you want to add to your network directly. The galleries contain those nodes used the most in day-to-day work while the tab key gives you access to all the available nodes. 

You can create your own galleries using the Windows > Gallery Manager and you can add items to your galleries by RMB-clicking on a node then choosing Save to Gallery... 

Nodes saved in the Mat network will also be available in the Material Palet e as long as they are given the proper keywords such as Mantra for Mantra materials. 

## NETWORK VIEW

Network Path - The path leading to the current network level. You can also use this bar to navigate to other networks. 

Pane menu - These menus and icons are for organizing your network. 

Network Background - Use the Pane menu to add an image or set up a grid to help you organize your nodes. 

Network Box - Group related nodes then quickly collapse and expand them. 

Sti cky - Add notes to help other arti sts read your network or to of er ideas for their networks. 

Node Gallery - Drag nodes from here to your network. Use the fi lter at the bot om to fi nd the node you need. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/18461b4333263a2999a223e879077572b857a9e2bd6f4f5f3af6d9ed22bcb798.jpg)


<table><tr><td>■ Scene</td><td>Objects</td><td>OBJ</td></tr><tr><td>■ Geometry</td><td>Surface Operators</td><td>SOP</td></tr><tr><td>■ Solaris</td><td>Lighting/Layout Operators</td><td>LOP</td></tr><tr><td>■ Materials</td><td>VEX Builder</td><td>MAT</td></tr><tr><td>■ Motion FX</td><td>Channel Operators</td><td>CHOP</td></tr><tr><td>■ VEX</td><td>VEX Builder</td><td>VOP</td></tr><tr><td>■ Outputs</td><td>Render Operators</td><td>ROP</td></tr><tr><td>■ Tasks</td><td>Task Operators</td><td>TOP</td></tr><tr><td>■ Dynamics</td><td>Dynamic Operators</td><td>DOP</td></tr><tr><td>■ Compositing</td><td>Compositing Operators</td><td>COP/IMG</td></tr></table>

## NETWORK TYPES

Houdini includes diferent kinds of nodes which each work in their own context. The network type is labelled in the top right corner of the network view. Nodes from each type can connect to other networks. While the diferent types of nodes are similar in how they are wired together, they each have unique capabilities: 

As you work with Houdini, you will begin to learn how to use this “secret” language to talk about the node types and how they apply to working procedurally. 

## NETWORK PATHS

Nodes are organized hierarchically with some nodes nested in other nodes known as network managers or subnetworks. To help you manage these hierarchies, a browser-like path is available at the top of most panes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/17b81416d45c7944c19b7c94afd2694dc9773f5e345f395c4673c0adce186b11.jpg)


Use this path to navigate up and down the hierarchy or to other networks. By default, the path changes as you make selections in the scene view although you can Pin down a path to keep it focused. You can also drag the Target icon to a pinned pane to sync up their paths. 

## NAVIGATING NETWORKS

To jump between network types there are a number of diferent approaches you can take. Some of these happen naturally as you work with objects in the scene view and others ofer shortcuts which allow you to work more quickly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d4e967de6ce03cd971127d23ecdfc1c7fdaba7478f93ab3e0db822291553658f.jpg)


Selection Modes - As you select in the scene view, the network editor jumps to the location of the selection. Diferent selection modes will in turn take you to diferent network types as you make a selection. 

Network path - You can LMB-click on a parent node to navigate back up the path or LMB-click on the container node to access parallel nodes or dive into the contents of other container nodes. 

Radial menu - Press n to get a radial menu that lets you navigate up, down and to diferent network types. 

Hotkeys - These help you navigate up and down as you work with a selected object. 

 Dive in 

 Jump up 

 Toggle Objects/Geometry F8 

 Previous or Next Network 

Quick Marks- These let you quickly set and return to network locations. You can use them as-needed and then override them or forget about them. They are not saved with the scene file. 

 Set a Quickmark Ctrl + 1, 2, 3, 4 or 5 

 Return to a Quickmark 

 Go Back to Previous View 

1, 2, 3, 4 or 5 

## SELECT AND VIEW HOTKEYS

In the network pane, you will need to pan and zoom around to work with the complete network. Here are the key combinations for these actions. 

 Pan MMB 

 Zoom RMB 

 Select Nodes LMB 

 Add to Selection Shift + LMB 

 Remove from Selection 

Node - This represents an operation that contributes to the final output of the network. 

Network Type - Shows which network type you are working in. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ce19fb56e9b6c3ce03e9d8ec75c4cbb1b45fac217248efab71bef0f7dca5dc3f.jpg)


Connector - The connecting lines show how your nodes are linked together and how the data is moving through the network. 

Dot - You can add dot connectors to make it easier to organize your nodes. 

Display Ring - This small circle shows which node is displayed in the Scene view. 

Render Ring - This large circle indicates a render node even if another node is displayed. 

Comments - Node comments can be displayed to help other artists understand your thinking. 

Paletes - Butons on the menu display Paletes that let you set the color and shape of nodes. 

## LEARN ABOUT YOUR NODE

Bring up the Info Box using either the Radial Menu or MMB-press on the node. This panel gives you info about the node’s contents, groups, atributes and other important facts. This panel also highlights any errors that are interfering with your workflow. 

This panel will close automatically but you can click on the Pin icon to keep it visible as you work. You can add comments and display them in the Network view using this panel. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0a69db2d9373cbd1448c68c8ac95d7556d9e8c84ecc7a3315b5d4dacc4397872.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eb67c022a488ae0814742576e98087f5b74bdf5486e711055da77c7d81b3c705.jpg)


# Parameters, Channels & At ributes

All of the nodes in Houdini are driven by parameters, channels and at ributes to help you achieve the results that you want. The terminology used in Houdini may dif er from other 3D applicati ons therefore it is a good idea to take a moment to understand them in a Houdini context. 

## PARAMETERS

Parameters refer to the values, sliders, but ons and checkboxes found on Houdini nodes. These are someti mes referred to as at ributes in other applicati ons but Houdini uses at ributes in a dif erent way. 

You can change parameter values in the Parameter pane or using handles in the viewport. There is a RMB menu on each parameter that gives you a number of important opti ons such as copying and pasti ng and reverti ng to defaults. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b89f5e1c81f001e5ad5f12e71325e22660f2069e38872fa717579eaddb729d02.jpg)


## SEARCHING PARAMETERS

A node might have a large number of parameters and sorti ng through them all can take ti me. If you click on the magnifying glass in the top right, you get a search bar that lets you fi lter the parameters based on name and content. You can fi nd parameters using expressions, overrides and even a raw value. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ac9aee06f15f66a7c795fcb3f094c7e9213683922e5bb88e9f0c95b679a29f15.jpg)


## CHANNELS | KEYFRAMES

You can set a keyframe on a parameter by pressing the Alt key and LMB-clicking on the name or value fi eld. Once you have set a keyframe, the parameter’s fi eld changes color and you have created an animated channel. There will now be keyframes associated with the parameter which you can access in the Animati on editor. 

## CHANNELS | EXPRESSIONS

Instead of a raw value, you can add expressions into the parameter using either hScript or Python. There is a menu in the top right of the Parameter pane for choosing which language you want to use. You can press Ctrl-E to bring up an expression editor with a number of scripti ng tools to make it easier to work. 

## Translate(ch("./box_object1/tx")+5)/2

## REFERENCE SCENE DATA

You can also RMB-click on a parameter and choose Reference > Scene Data to bring up a window for choosing specifi cally what you want to link to. Once you have made a choice from any node in your scene, to create a channel reference. This method lets you create references without worrying about the exact syntax needed to write the proper expression. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4ede12ee788b700e2009501056ec0608fdab7cb7903e4a7f77febdc52d4744a6.jpg)


## PARAMETER PANE

Navigati on Bar- This bar lets you see where the node is located in the scene hierarchy. 

Node Type and Name - Here you can see the node type and set its name. Clicking on the icon gives you a menu for working with the node. 

Search Bar - Click on the magnifying glass icon to search parameters by name or by content. 

Changed Parameter - when a parameter has been changed from its defaults then its value is bolded. The folder tab name is also bolded. 

Animated Parameter - when you have keyframed a parameter it is highlighted in green. 

Locked Parameter - You can RMB-click on a parameter to lock and unlock it. It will be highlighted in grey 

Select to Match - These icons let you match these parameter values to other objects. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/43c46a247d13ecc97fcc30f5b0f43f3138468691533c3bf03f55c7428e72ef87.jpg)


## CUSTOM PARAMETERS

If you click on the Gear icon in the top right of the Parameter pane, you can choose Edit Parameter Interface. Here you can add custom parameters which can then be linked to other parts of your node network. 

## ATTRIBUTES

Atributes let you atach data to your geometry that can be used by nodes down the chain to complete an operation. A fuel atribute can drive a Pyro FX simulation or a UV atribute sets up texturing. Some atributes are created by Houdini nodes or you can create custom atributes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e32f48a8ba7925d94b15fe9b6c16fdd6d940c80d0c92db6ad4f4a5e07b36ca24.jpg)


Type - You can set up float, integer or string atribute types amongst others. 

## ATTRIBUTE RANDOMIZE

Atribute Randomize lets you create an atribute and immediately randomize its values. For instance here you can see the Color, rotation and Scale of these boxes being randomized. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/979dd4bcb19399c0c04b97314a01d4be8e49820b5cc6c4900693b3cec54facad.jpg)


## GEOMETRY SPREADSHEET

You can view all atribute values, even invisible ones using the geometry spreadsheet. 

Navigation Bar- This bar lets you see where the node is located in the scene hierarchy. 

Node Name - This shows you which node is currently selected and which node is generating these atribute values. 

Atribute Class Butons - Use these butons to filter which kind of atribute you are looking at. 

Point Number - Here are the geometry point numbers to help you determine where the atribute is on your model. 

Atribute Values - These are the values at this point in the node network chain. 

Filter - You can type parameter names here to filter the list when you are working with lots of parameters. 

## ATTRIBUTE TRANSFER

Within a node chain, atributes are atached to geometry then used by other nodes. You can also pass atributes to other pieces of geometry using Atribute transfer. Here the sphere is passing color atributes to the boxes based on a defined threshold value. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1d72a6a0212d6c28c86e9f1baf9ec95e7e37ccdaa9a92371a08e68abe1cdc12c.jpg)


## ATTRIBUTE WRANGLE

Houdini has a wide variety of nodes that let you create and work with atributes. You can also use the Atribute Wrangle node to use a script-based approach to this work. For a lot of Technical Directors this may be the most comfortable way to work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9ebb9dd9fd6c62e4607345dc4620800d1b4675fe5c852296e7ca8694c5d83cc1.jpg)



For artists, working with nodes will make it easier to deal with this kind of information. A lot of Houdini’s power is found in the proper use of Atributes and you will eventually need to learn about them.


<table><tr><td colspan="8">Geometry Spreadsheet</td></tr><tr><td colspan="8">obj sphere_object1_fluid</td></tr><tr><td colspan="8">Node: attributes Group View Intrinsic Attributes:</td></tr><tr><td></td><td>P[x]</td><td>P[y]</td><td>P[z]</td><td>custom</td><td>v[x]</td><td>v[y]</td><td>v[z]</td></tr><tr><td>5329</td><td>0.219723</td><td>0.0206722</td><td>0.0375</td><td>0.816298</td><td>0.5013</td><td>-2.82461</td><td>-0.581617</td></tr><tr><td>5330</td><td>0.223434</td><td>0.00344996</td><td>0.0769753</td><td>0.49707</td><td>0.568743</td><td>-2.63877</td><td>-0.592857</td></tr><tr><td>5331</td><td>0.234992</td><td>0.0581722</td><td>0.0375</td><td>0.257857</td><td>0.562976</td><td>-2.8259</td><td>-0.540009</td></tr><tr><td>5332</td><td>0.262858</td><td>0.03207</td><td>0.0919361</td><td>0.712832</td><td>0.601334</td><td>-2.64274</td><td>-0.53761</td></tr><tr><td>5333</td><td>0.261589</td><td>0.1125</td><td>0.0375</td><td>0.86551</td><td>0.818694</td><td>-2.53111</td><td>-0.20071</td></tr><tr><td>5334</td><td>0.289717</td><td>0.1125</td><td>0.0834052</td><td>0.87321</td><td>0.845397</td><td>-2.4896</td><td>-0.170334</td></tr><tr><td>5335</td><td>0.3375</td><td>0.0375</td><td>0.115799</td><td>0.659754</td><td>0.640353</td><td>-2.5884</td><td>-0.369587</td></tr><tr><td>5336</td><td>0.3375</td><td>0.1125</td><td>0.100003</td><td>0.25833</td><td>0.891779</td><td>-2.43301</td><td>-0.0753031</td></tr><tr><td>5337</td><td>0.341473</td><td>0.204885</td><td>0.0421855</td><td>0.144889</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5338</td><td>0.3375</td><td>0.169474</td><td>0.0825136</td><td>0.498767</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5339</td><td>0.369121</td><td>0.226918</td><td>0.0203092</td><td>0.0298898</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5340</td><td>0.443519</td><td>0.0160402</td><td>0.0375</td><td>0.20396</td><td>0.568284</td><td>-2.56199</td><td>-0.120951</td></tr><tr><td>5341</td><td>0.41495</td><td>0.042021</td><td>0.0930402</td><td>0.753424</td><td>0.765839</td><td>-2.53459</td><td>-0.142635</td></tr><tr><td>5342</td><td>0.4125</td><td>0.1125</td><td>0.0954815</td><td>0.19528</td><td>0.926129</td><td>-2.34464</td><td>-0.0161053</td></tr><tr><td>5343</td><td>0.408423</td><td>0.203871</td><td>0.0421855</td><td>0.197239</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5344</td><td>0.4125</td><td>0.17145</td><td>0.0836806</td><td>0.150603</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5345</td><td>0.380705</td><td>0.226918</td><td>0.0203092</td><td>0.760528</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5346</td><td>0.45426</td><td>0.0535402</td><td>0.0375</td><td>0.89639</td><td>0.834279</td><td>-2.45458</td><td>-0.0683122</td></tr><tr><td>5347</td><td>0.451705</td><td>0.070835</td><td>0.0769204</td><td>0.405407</td><td>0.911747</td><td>-2.38925</td><td>-0.0390606</td></tr><tr><td>5348</td><td>0.460437</td><td>0.1125</td><td>0.0375</td><td>0.532263</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5349</td><td>0.453485</td><td>0.1125</td><td>0.0788837</td><td>0.731012</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr><tr><td>5350</td><td>0.456177</td><td>0.162069</td><td>0.0375</td><td>0.455307</td><td>0.934452</td><td>-2.31883</td><td>-0.00282227</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fc0545aee6e338557ea9ea1c639462886780853489a79de274def2207e0c97db.jpg)


## Selecti ng Geometry

Working in Houdini involves the selecti on and manipulati on of many dif erent elements. There are a number of tools and opti ons available to help you work efi ciently with objects and geometry components such as points, edges and primiti ves. 

## SELECT TOOL

The Select tool lets you focus on making selecti ons therefore it doesn’t have any manipulati on handles. 

 Select Tool Tap S 

When working with tools such as Move or Rotate and Secure Selecti on is on, you need to invoke the Select tool to make a selecti on. Toggle Secure Selecti on to Of to select freely. 

 Evoke the Select tool while in other Tool Press and Hold S 

 Toggle Secure Selecti on ~ 

## SELECTION TYPES

There are dif erent shortkeys for adding, subtracti ng or toggling your selecti on as well as for selecti ng all or none. These techniques play an important part in this workfl ow. 

 Select 

 Add to Selecti on 

LMB 

Shift + LMB 

 Remove from Selecti on 

Ctrl [Cmd] + LMB 

 Toggle Selecti on 

Ctrl [Cmd] + Shift + LMB 

 Select All A [Object Level] / N [Geometry Level] 

 Select None N [Object Level] / Shift + N [Geometry Level] 

## SELECTION TECHNIQUES

In the viewport, you can choose from four dif erent selecti on types that of er dif erent ways of accessing geometry. 

 Box Select F2 

 Lasso Select F3 

 Brush Select F4 

 Laser Select 

There are also some selecti on fi lters that let you focus on visible geometry or select groups. You have a wide range of selecti on opti ons to help make this easier as you work. 

 Select Visible Geometry Only Shift + V 

 Select Fully Contained Geometry Only Shift + C 

 Select Groups or Connected Geometry 9 

Select Whole Geometry Choose in Operati on Control bar 

 Select by Normals Choose in Operati on Control bar 

## SELECTION MODES

Selecti on modes, give you access to objects and components. They also let you easily jump from object level to geometry level using a the but ons in the toolbar or the hotkey. 

Objects - The object network level is where you work with an object’s transforms. In any tool other than the View tool, the following hotkey will bring you back to the Object level: 

##  Objects

Geometry - You can use any of the following hotkeys, when not in the View tool, to jump into the geometry level with the chosen components available for selecti on. 

 Points 2 

 Edges 

Primiti ves [Faces] 4 

 Verti ces 5 

## TWEAK MODE

Only one geometry selecti on modes can be acti ve at a ti me. If you are working with an Edit node then Tweak Mode lets you choose any combinati on of points, edges and primiti ves. 

Each of the selecti on modes comes with opti ons which let you alter how you interact with your scene. You can access these opti ons by either LMB or RMBclicking on each mode’s icon. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ed28af4f1cc755834f917f14b1781bd22a5a0735ad19dab6b2bda25edcf988a0.jpg)


While working with components, this menu lets you choose to show Display or Current Operators. These same opti ons are available at the top of the Scene view when working with the Edit node. 

This menu is dif erent at the object level where it includes some fi lters for dif erent kind of objects as well as opti ons for more easily selecti ng materials, constraints and Digital Assets. 

Show Display Operator Show Current Operator 

## SELECTION OPTIONS

Edit | Components You can choose which components you want to work with from this collecti on of but ons. Here edge selecti on has been chosen. 

Select Tool - The Select tool lets you make the selecti on. To access it press the S hotkey. 

Secure Selecti on - This locks your selecti on when using other tools. To invoke the Select tool with it on, press and hold on the S hotkey. 

Selecti on Types - You can use this top bar to change your type of selecti on. You can choose from Box, Lasso, Brush or Laser. There are also some fi lter opti ons. 

Edge Loop - To select an edge loop you can double-click while selecti ng edges. To select parti al loops, select one edge then press A and then an end edge. This works with points and primiti ves. You can also select point loops or primiti ve loops using the same technique. 

## HOW SELECTIONS ARE USED BY TOOLS

When you make a selection in the viewport then use a tool, a node is created and the selected points, primitives or edges are listed in the node’s Group parameter. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d0c2bf1515c7e86d3ddca5f7dbe725e06cf106e432c2539d9883464fead1d338.jpg)


For example here we see primitives 5, 6, 9 and 10 are being used by a polyextrude node. You can see them listed in the Group node and then used to extrude the faces. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1aac939593906d2bd4b6cd0c271472ab19e85e86a603fa7bc21aa7f6e3b7a535.jpg)


If you were to change the topology of the incoming geometry node then there might be more or less faces and the extrusions will have moved to a diferent location. This may not be what you want and you may need to reselect faces. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/47167a77df88a03f3202720b8a8de6e93fa1319bda7fde3867d6032406cdafee.jpg)


To do this, you can select polyextrude, press Enter to go to the Handle tool and press ` to go into re-select mode. Select new primitives then press Enter and your new selection will be used in the Group parameter. 

## SELECT ALL AND THE GROUP FIELD

To select all of the primitives on incoming geometry, leave the Group parameter blank. If the topology of the incoming geometry changes, everything will be operated on by the node. 

Using Select All [N] in the viewport will usually ensure that this field remains blank when a tool is used. With some tools, the Group field will show all the selected parts and you would have to clear the field manually to make it blank. 

## THE GROUP NODES

Group nodes let you refer to a defined selection of points, vertices, polygons, or edges by name. You can define a group interactively, by selecting components in the viewer, or mathematically, using ranges or an expression. The group name can then be assigned to the Group parameter instead of using point or primitive numbers. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/356f868a1898b921b6b2cdb4b79af8a95c9ec3a05c1f53536040efc9d1cee28f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c89cac57353a111f85044466b5285b8a45c53f603c47ac700442280f1da7d908.jpg)


Here are some Group nodes for you to choose from: 

Group Create - Use interactive selection, a bounding box, face normal direction or edge angles to populate the group. 

Group by Range - This lets you choose a range and a simple patern to populate the group. 

Group Expression - With this node you can use a vex expression to define the membership of the group. 

 Group Paint - This node lets you use an interactive paint interface to choose the geometry for the group. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9b60a3a4085de4c2eb3067356611fdade762a4f110e031f044cb3850817535df.jpg)


Shading Options - The shading options determine what you see in the Scene view. In this case, we are using Smooth Wired Shading. 

RMB Menu - While in the Select tool, this menu gives you access to selection options such as inverted selections, boundaries or growing and shrinking your selection. 

Display Filter - This filter lets you turn of things you don’t need such as bones, null objects, lights or cameras to let you focus on the work at hand. 

Display Options - While selection modes will show you edges or points to help you select, they will not be visible when using other tools. Use these options to keep them visible even when not using a specific modeling tool. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/00b3e396739bcaba9669d811425372122940ea6bba1c5fc688db41f1d88c207c.jpg)


## Transform & Edit

From basic transformati on tools for objects, to the pose tool for animati on rigs and the edit node fo reshaping geometry, there are a number of dif erent tools that let you use interacti ve handles in the viewport. In Houdini, these handles are ti ed closely to the node you are working with. 

## TRANSFORM TOOLS

The transform tools give you handles that you can use to manipulate objects or reshape geometry. When you transform objects, the parameters at the object level are updated to refl ect your changes. 

 Move T 

 Rotate R 

 Scale E 

 Pose Ctrl-R 

 Handle 

The Handle tool gives you access to handles that are specifi c to your selected node. While using these tools, you can re-select by pressing and holding S, making a new selecti on then releasing S and conti nuing to transform. 

## TRANSFORM HANDLES

When you are working with a Move handle you can work with a single axis, two axes or move along the camera plane using the center. Rotate and Scale handles of er similar controls. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/16484ce06db5afa5f582dc9a87ae7bd1cc4c1e3f4a47309e1fd041419e05c8d6.jpg)


## EDITING GEOMETRY

Edit | Components You can choose the components you want to edit using these but ons. The Points opti on has been chosen here. 

Move Tool - The Move tool lets you translate the selecti on using the Scene View handle. 

Move Handle - This handle lets you move along one axis using the lines or two axes using the square dots. RMB-click on the handle to access the handle opti ons. 

Soft Edit Radius - when moving points on a surface, you can use this radius value to create a soft fallof as you move the points. The Soft Edit Radius doesn’t work with primiti ves or edges. 

## MMB TRANSLATION

If you don’t want to click directly on handles, you can use the Middle Mouse But on in open space combined with a drag to move it along the constructi on plane. To change this to translate along nearest axes go to Edit > Preferences > Handles and set Translate Handle to Map Drag to Axis. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/23c0c67406383d46552df34d2f5d4560ba2c47f815aa8f35c7c747999f732ae1.jpg)



MMB-Drag up/dwn Moves along Y axis if the preference is set to Map Drag to Axis


## POSE TOOL

When you are animati ng, you can use the Pose tool to work with bones and to display moti on path handles that reveal the moti on of an object. You can then use tangent handles and keyframe points to modify the moti on in the viewport. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5757aea8614c9de5713fc2e2e6929b6bdb6d9c1f9ca11007c3ae9ba2fdafde11.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/99a9ed484002c347732877b67c745b11c7e895d6585e3e9e3bdf1976ad2520fd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/890fed48eba8793a976ed476ca2890a9dd54c9e992e7430207938b3d584890b1.jpg)


## EDIT NODE

If you try to move geometry components then an Edit node is placed down to accept your transformati ons. In additi on to transforming the geometry, you can slide on surface, work perpendicular to the normals or sculpt the surface. 

Edit T/R/E 

Slide on Surface L 

 Peak H 

Sculpt B 

## SOFT FALLOFF

When you are transforming points, you can use the Soft Edit Radius to create a fallof . There is a visualizer that is evoked to show you where the fallof is occurring on the surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/33aff4a63312edd11907dd0871175f2a0772a5620b5d8b2f92b2829cfcb0b691.jpg)


## EDIT OPTIONS

If you RMB-click while in the Edit node, you can access opti ons for transforming your selecti on. You can make a circle or straighten the selecti on. These opti ons work with points and edges but not always with primiti ves. 

 Make Circle 

 Evenly Space Selecti on 

 Relax Selecti on 

 Straighten Selecti on 

Shading Opti ons - The shading opti ons determine what you see in the Scene view. In this case, we are using Smooth wired Shading. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d97551d17b5833745497d986510a46472ddce9928aaa6fa31254a7753a5b0f7c.jpg)


Sloppy Selecti on - Three of the component but ons can be selected at the same ti me if the Edit node is using Sloppy selecti on which makes all of them available for a more fl uid selecti on process. 

RMB Menu - This menu gives you access to Edit tool opti ons such as which type of edit you want to focus on. This informati on is also available on the top bar of the Scene view. 

Component Selecti on - You can also select the component type using this menu. This of ers you the same opti ons you would fi nd on the main toolbar. 

Edit Opti ons - You can use this menu to edit the components using operati ons such as Make circles and Straighten the selecti on. 

## HANDLE TOOL

Aft er using a shelf tool, you oft en fi nd yourself in the Handle tool. Or you can select a node in the network and press the Enter key in the Scene view to go into the Handle tool. This brings up a handle which focuses on the specifi c parameters for the selected node such as the distance parameter on a polyextrude node. 

Show Current Operator - By default when you select a node other than the display node, it becomes the current node and you get a wireframe display of the geometry. You can then use the handle to manipulate this intermediate node while evaluati ng the results on the shaded surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7cc1e8d7e2116f1c83ba43b9c3fe1850e04b8597611b888365f0780147ff2713.jpg)


Show Display Operator - Another opti on is to always show the Display Operator. In this case, selecti ng a node in the chain does not show the wireframe and the handles stay focused on the display node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/abec6595d963d04f17225a4367bfbc1cc7d8cb3e9fb53d3805dc046624ba7aa8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5a4dc88168b13ab1b794b3594f3c6f0300965147e96bfc02d3396a24b805a2b7.jpg)



You can change parameters in the parameter pane for the current node but the handles will conti nue to work with the parameters on the display node.


HANDLE OPTIONS All handles have a menu that can be accessed by RMB-clicking on any part of the handle. This menu gives you opti ons for aligning the handle, detaching it from the parameters of the node, pivot mode and more. You can use these opti ons to customize how the handle works. 

You can also keyframe parameters on a handle and promote all parts of the handle to a Digital Asset. By promoti ng the parameter the handle will be accessible at the asset level. 

# Modeling Tools

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/67d83e04ab1be2edcf036a21f429b479d03e3381f8fc45fde7e647905cd92330.jpg)


Houdini has a lot of tools for creati ng, shaping and deforming geometry to achieve a desired look. Here are just a few of the many tools you will use on a regular basis when building models in the geometry, or SOP, context of Houdini. 

## CREATION

To start creati ng geometry, you can start with some basic shapes or draw a curve. In each case you get an object with a geometry/SOP node inside with the tool’s name. You can access these on the Create shelf or in a radial menu. 

Primiti ves - Houdini includes Box, Sphere, Tube and Torus primiti ve shapes along with a variety of Platonic solids 

Grid - The grid tool of ers a great starti ng point for a wide range of models. You can set its shape and size at the geometry level. 

Curve - Draw a curve by laying down control points then create a Bezier, NURBS or poly curve. 

## POLYGON MODELING

Polygons are one of the most popular geometry types especially in video game projects where they are mandatory. Houdini has a comprehensive set of poly modeling tools which you can use to develop your models. 

PolyDraw - This tool lets you interacti vely draw a polygonal mesh on the constructi on plane or by snapping to existi ng geometry. 

PolyExtrude - Push or pull on one or more polygons to reshape the geometry. Control the extrusion profi le to get a wide variety of shapes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ef795eb21269b09b30a46b43359e8f8252421077d72223540cc9144bf73222bd.jpg)


PolyBevel - Bevel selected edges to create chamfered or rounded bevels. You can oft en use the output group from a previous node such as Polyextrude or Boolean to automati cally fi nd the right edges. 

PolyBridge - Connect two sets of polygons with control over the shape of the bridge. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/660ea9cdd5d677bc39eb05e0af5f311269c3dca706006b4911bdd400515c364d.jpg)


PolySplit/Edge Loop/Knife - These tools let you split polygons to add more detail to your model. 

PolyExpand 2D - Take curves and edges that sit on a 2D plane and creates geometry based on a desired of set value. 

PolyReduce - Create dif erent levels of detail by reducing the number of polygons while preserving quads and UVs. 

PointWeld- Interacti vely snaps groups of points to another target point, and merges them. 

## UTILITY NODES

Because of Houdini’s procedural nature, modeling acti ons like copy, clip and mirror create nodes in your network. This can makes it easier to go back and make changes later on. 

Clip - Cut your model based on a clipping plane. You can set the directi on of the clip and whether you keep one half, the other or both. 

Mirror - This tool fl ips the geometry based on a clipping plane. There is an opti on to fusing the points aft er mirroring. 

Copy and Transform- This node will let you create multi ple copies based on transformati on values. 

Blast - This node lets you delete polygons from your model. You can choose to remove or keep the selected polygons. If you press the Delete key when points or a polygons are selected they will be blasted. 

Dissolve - This tool lets you remove edges without breaking up the surrounding geometry. Pressing the Delete key when an edge is selected will dissolve it. 

## Q SUBDIVISION SURFACE MODELING

In Houdini, you can model with polygons then display and render them as subdivision surfaces using opti ons found on the Render tab on the object’s parameter pane. You can also create a Subdivide node at the geometry level to add polygons to give you a more detailed topology to work with. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9cfe27e7bf50ff3ccf0b9ffd78a943c6fa15007d0bc30fba09e70c5eb286ca67.jpg)


## SURFACING TOOLS

There are tools in Houdini that will take profi le curves and build surfaces. Those input curves can be either bezier, polygonal or NURBS or a mixture of them. 

Revolve- Create geometry by revolving a profi le curve around an axis. There is a handle available for tweaking the results. 

Skin - Take a series of profi le curves and turn them into a surface. Rails - Copy one or more profi le curves along two or more rail curves, then Skin the results to get a surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4360aa4c7f1b3a86950ca509960569cb62c7ff8f119b938da8667b24d398e8de.jpg)


## BOOLEANS

Subtract, Union or Intersect geometry using the Boolean tool. This node can handle very complex topologies and can be used to break up a surface for destructi on using rigid body dynamics. This oft en creates more realisti c results compared to the Voronoi-based Shat er node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f6b857563ad941e146cc1b6cd37d913020fab3cb4e186ef09eeb71499b9d52e4.jpg)


The Boolean tool can create output groups that you can use to feed other nodes such as the Polybevel node. This way any updates you make to the boolean will update properly when it feeds into the second node. 

## DEFORM TOOLS

While you can shape your geometry by editi ng points directly, there are ti mes that you need a more generalized approach. The following nodes provide opti ons for shaping your geometry procedurally. 

Bend - This node lets you set a capture range and directi on then bend, twist, taper and squish the encompassed geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/217711dbc07a4d273d11c213facc037f74d55ff31e1b06784432142ed2df77cc.jpg)


Lati ce - This builds a lati ce around your geometry then lets you edit points on the cage to reshape it. You can also use a custom cage. 

Mountain - Apply a noise functi on to deform the surface to create a random result. The points are actually being moved with this node. 

Ripple - This node creates a ripple shape in your geometry. 

Waves - This node adds noise functi ons to create a wave-like pat ern that animates over ti me. Perfect for creati ng realisti c oceans. 

## COPY TO POINTS + SCATTER & ALIGN

A typical Houdini workfl ow is to Scat er & Align points on a surface then Copy to Points. At ributes for scaling and rotati ng the objects can then be applied to create a more organic result. This is oft en used to create landscapes with trees and rocks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7c2ac711b763d1c36ae9ec086a4cfb181e69fe95c0a4f4bd9e9fe480f7907614.jpg)


## TOPOBUILD

Houdini has a Topobuild node that lets you draw polygons directly onto high-resoluti on geometry that you either scanned or created in an applicati on such as Pixologic’s Z-Brush. You can create a cleaner topology for animati on then bake the details from the original model into a normal map. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0e539d638e2ed9995c172117f0da54b970fc104cddfd763c5415f0b87712ad49.jpg)


## VOLUMES

Volumes allow you to store values for voxel, or three dimensional pixels, in a space. These are oft en used to support collisions when using dynamic tools or to create clouds. They can also be used for modeling to combine multi ple shapes into a single volume which you then convert back to a surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/04cff1e17f5903cf57bf26287e8b94f968f820564d565606e5dbbf8c99aca4ac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3ce2fcb558fc17bf413ce8723765eb180a3233c0d91435ee1a11591240cfa296.jpg)


## GEOMETRY TYPES

Houdini supports a number of dif erent geometry types including Primiti ves, Polygons, NURBS and Beziers. You can Convert back and forth between them and you can have more than one geometry type merged together in a single object. 

Polygons models can be set up to display and render as Subdivision Surfaces using PIXAR’s OpenSubdiv standard. Both Subdivisions and NURBS will render in Karma and Mantra as perfectly smooth without relying on any tessellati on seti ngs. 

Primitive 

Polygon 

Polygon Mesh 

Mesh 

NURBS 

Bezier 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c8d54a2e8abce814aabbbcac9f77f336498a9748180c6cf984a11e8cf91f0ef.jpg)


# UVs & Textures

To make 2D maps fit properly onto 3D objects, UV coordinates are needed to define a flatened view of your geometry. When you first create geometry in Houdini it will not have any UVs. Even primitive objects do not have any built-in UVs. This means that you will need to add them at the geometry level using one or more SOP nodes. 

## UV TEXTURE DISPLAY

Since geometry in Houdini does not have UV texture atributes set up by default, you need to add them using UV tools. Once you have UVs set up, you will see a texture grid on your geometry because Show UV Texture is on in the Display Options bar. You can toggle it of if you don’t want to see the UV texture or change it to a color texture. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c7461e416cb23d707133628bac00ce32ebe03200cea7a882f5f1018e6141ed69.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/95acba71341a1118271c4927f729a95010005c477293c5d50912a1c43e7847d8.jpg)


## UV PROJECT

This node let you assign UVs using one of several projection techniques. Once you choose your projection type you can initialize the projection to match your object. This may invert the UVs and you will need to set a rotate x value of -90 instead of 90. Above you can see an Orthographic projection and below you can see a Toroidal projection. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ef0276657040f6e60792ebff7b6e11caa9ee75e2d719676368ee0355892f9d16.jpg)


## UV FLATTEN

UV Flaten unwraps your geometry based on predefined boundaries created using selected edges or edge groups. The results can then be tweaked by pinning points in the UV view and adjusting the islands to get the look you want. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/671f62fb451e4411d5d877f5af4b638062731aac5110028e23ca3e2de693b70b.jpg)


## UV EDIT & DISTORTION

To edit individual vertices or groups of vertices you will use either the UVedit or UVtransform nodes. The UVedit node lets you perform many edits using a single node while UVtransform allows one edit per node which can provide a more procedural result. You can use Display > UV Distortion from the UV Viewport menu to see whether you are editing too much. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7d4d378f7ed5a9d938db5a26b430dffc7b00c2f7c01e002543f8345c225cbc69.jpg)


## UV LAYOUT

UV layout will let you create UV islands and pack them into UV space as eficiently as possible. This lets you maximize how much of a texture is being used on your geometry which is important when optimizing for both rendering and gameplay. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/06a76744861cd2d283ea2c320f68dae6151b9a324629943f7cd4feb631ec9548.jpg)


You can use the region handle to put a the UV layout into a particular part of your UV space. Subsequent layouts can then work around this layout using the Pack Islands in Cavities option. 

## UDIMS

In addition to working with a Single UV tile, you can use UDIMs to spread your UVs over many tiles. This technique lets you create more detailed texture maps because your UV islands are not packed in too tight. Properly numbered texture maps will then be assigned to the appropriate tile. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ae78a64d0c9cfd37ef803343146e832f1b8d10d0239abc0643098a6dae13d8db.jpg)


## UV ATTRIBUTES

Earlier, you learned how at ributes can be assigned to geometry that carry important informati on down the line. UVs are vertex at ributes that let you wrap texture maps around your model and are also carried down your network. 

These at ributes are visualized in the UV viewport and analyzed in the geometry spreadsheet. These at ributes work with various SOP nodes including the at ribute wrangle node which lets advanced TDs manage their UVs using scripti ng. 

## UV SETS

You can create more than one UV set on the same geometry. When you use the UV nodes, you can set the UV at ribute. By default this is uv but you could create a uv2 to create a second set. These dif erent UV sets are used when you assign textures in VOPs so that dif erent texture maps use dif erent UV at ributes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f68d6255a760312f43f32f387ef74b298b7adcf5e8d918547dbd327fdd55f44c.jpg)


In the two images shown here, the fi rst uses a toroidal projecti on and is assigned to a uv UV at ribute while the second uses a planar projecti on and is assigned to a uv2 UV at ribute. These UV at ributes can have any name, for instance, it could be bob instead of uv2. 

## UV VIEWPORT MENU

The UV viewport menu lets you display UVs based on the UV at ribute. You can also use this menu to fi gure out the background image which can either be the default UV grid or a texture map pulled from an assigned material. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eaecb0ba0fde43a9acf7496c012f91a17949f21ce3a6da685a4216b6c085a3a6.jpg)


This menu also has display opti ons for displaying UV Overlap, UV Backfaces and UV Distorti on. These can be helpful when evaluati ng your UVs to decide if more tweaking is required. 

## ATTRIBUTE TRANSFER

One of the SOP nodes that can be used to manage at ributes is At ribute Transfer which lets you take the UV at ributes from one piece of geometry and transfer them based on proximity to another. 

This can be useful when the topology of a model has changed but you want to preserve some of the work you did creati ng UVs for the original model. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9be5d9328864c0f17233d88de31b481f0ec1f1fe3d422e79135bef7454bda57c.jpg)


## SCENE VIEW | UVS

Current Tool - At the top of the Scene View, you will fi nd the selected node when the Handle tool is acti ve. 

Background - The background of the main ti le can be set using opti ons found in the UV menu. 

Outside Main Tile - Polygons positi oned in the area outside the main ti le would overlap the same area on the main ti le because the texture repeats unless you are using UDIMS which cover more than one ti le. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dfd06776c34142400ce320a8e39cb945d2cf3480e3407d0e2b320efd75bc9640.jpg)


UV menu - when you are in the UV view, this menu gives you a number of dif erent opti ons for working with UVs. View menu - Use this menu to choose the UV view for this viewport. 

Layout Handle - This handle is part of the UV Layout node and lets you focus the UVs to a certain part of the ti le. 

Pack Around - The UV layout will pack your UVs around any existi ng geometry that has already had its UVs set. 

# LookDev: Shaders & Materials

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cfab5cf5b2efcc53b80881ff9d43a8630117cdf7394a6fe3d7aa408324a64ffa.jpg)


To render objects in your scene, you must assign materials, also known as shaders, to your geometry. In Houdini, these materials and shaders are created in the mat/vex builder networks. The ability to build up materials using nodes is a powerful tool when defi ning the look of a shot. 

Houdini organizes dif erent types of nodes into network types and for materials you will use the network type. This is where you can set up VEX operators for Karma and Mantra or Material X for Karma. Material X is an open standard, that originated at Lucasfi lm,<sup>®</sup> which is used or the transfer of lookdevelopment content between applicati ons and renderers. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9ba102cf2ac0faf614ec784e3c6f10b4f044991af04e766b99f01963d0eddb04.jpg)


## THE MATERIAL PALETTE

You can add VEX-based materials using the Material Palet e then assign them to objects by clicking and dragging. This pane has a workspace for managing the materials in your scene which is organized into tabs that represent dif erent subnetworks such as Material Library LOPS. Use the tab key to add Material X shaders to material networks. Once they are in place they will show up in the Material Palet e. 

## ASSIGNING MATERIALS IN LOPS

To assign a material in the Solaris LOP context, fi rst create a Material Library LOP which contains a /mat network. You can assign the material using this node or use an Assign Material LOP later in the chain. The Material Palet e will let you drag from the gallery to the library or in LOPS you can use the arrow but on to access a list of materials in your scene graph. 

## PRINCIPLED SHADER

In the Material Palet e, you will fi nd the principled shader, a material based on the Disney “principled” BRDF by Brent Burley. This shader is “principled” rather than physical in order to make it easier for arti sts to work with. 

The Principled Shader has been pre-built to include the ability to assign textures directly to parameters such as base color, bumps, normals, displacements and more. The texture maps you assign will be displayed in the viewport and you can achieve a wide variety of looks right out of the box. 

You can extend this material by feeding it with other VOPs but that isn’t necessary in all cases. Many of the materials found in the gallery are variati ons on this shader. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7ab71292cac26332bbb02c713e6978cc557bec746630d0dbb3e1515d03a5d596.jpg)


## PRINCIPLED SHADER CORE

The Principled Shader Core node sits inside the Principled Shader and contains the main features of the shading model but doesn’t have all of the texturing features built-in. 

To build a robust shader from scratch using this node, you would need to add VOP nodes using Houdini’s shader building tools. You can accomplish this by either wiring nodes together in the Node view or adding them using the Shader FX menus. 

## MATERIAL PALETTE

Materials in Gallery - The Materials listed here are saved to disk in a gallery fi le. You can drag these into the scene area found on the right or onto objects in the viewport 

Material in Scene - This is where you fi nd materials that are part of your scene fi le. They can be assigned to objects by dragging from here into the viewport. 

Material Library LOP - Materials set up in the LOP context can be placed into Material Libraries - you can drag materials into here from the gallery. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/28284f9727d0ed7d676388500d0ccff549c1229489d6964f8d15ced206a1796b.jpg)


Update Material Icon - To update all material icons you can click on this but on or RMB-click on material to do it one at a ti me. 

Assign Material - If you select an object in the scene and the material in the palet e then you can use this but on to assign the material. 

Double Click to Edit - If you double-click on any of these materials, you will jump to a Node View where you can make edits at the /mat level. 

## LAYERING MATERIALS

You can layer materials to create a unique look for your object. Using a Layer Mix node, you can combine two dif erent materials into a single look. For instance, a shiny metal material and a mat e rust material can be layered using this technique. You can then texture an alpha channel and you can choose to mix the surface, the displacement or both. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/988f44cd5baec0ab818c3b4646b6c70be91d10285a6709cb4955bf27cb94b59c.jpg)


## MATERIAL BUILDER

If you want to turn your layered nodes into a new material then you can select them and choose Edit > Collapse Selected into Material. This puts the nodes inside a material builder where you can conti nue to tweak it. At this level, there are output and collect nodes to make the network work efi ciently. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/77de4616819433482f8c8c853ef0814a536073ee6da359c2c05a3271a62fefa3.jpg)


## MATERIALS AS DIGITAL ASSETS

You can make materials even more efi cient by saving them out as Houdini Digital Assets. In the Asset Properti es pane, you can go to the Save tab and choose Save Cached Code so that the material is pre-compiled when you render with Mantra. You can also load texture maps into the digital asset then reference them from inside the asset fi le. Turning materials into HDA’s can make it easier to share with your team. 

## SHADER FX MENU

While working with material VOPs, you can add nodes in the Network view and wire them together or you can use the Shader FX Menu by clicking on the icon at the far right of each parameter. This menu lets you focus on the parameter that you want to work with and create the node in context. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f87919f75f923bbde88f3e5a72c1bcab74ed216ae6af200669867eea492b8517.jpg)



In the Parameter Pane, you can see what type of connecti on each parameter has by looking at the icon on the far right:


 No Connecti on 

 Parameter Node 

 Connected with other Nodes 

 Hidden Connecti on 

## PROCEDURAL MATERIAL ASSIGNMENT

When working in producti on with lots of data, it is oft en necessary to take a procedural approach to assigning materials. With Solaris and Karma, you can accomplish this using nodes such as the Assign Material LOP or Material Variati on LOP. 

If you are working with Mantra, materials can be assigned to the object using the Data Tree panel which gives you access to Material stylesheets. Stylesheets let you use rules to assign materials and textures to large groups of objects. 

<table><tr><td colspan="2">Material Style Sheets</td><td>Filter:</td><td colspan="4">New Style Sheet...</td></tr><tr><td></td><td></td><td></td><td>Type</td><td>Value</td><td>Override Name</td><td>Override Type</td></tr><tr><td>Pig Looks</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pig_Styles</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Imported Files</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shared Scripts</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Shared Override Sets</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Base Material</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Style</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Target</td><td></td><td></td><td>Primitive</td><td></td><td></td><td></td></tr><tr><td>Data Binding</td><td></td><td></td><td>Primitive</td><td></td><td>packed_id</td><td>Automatic</td></tr><tr><td>Sub-target</td><td></td><td></td><td>Material Parameter</td><td></td><td>baseColor</td><td>Script From S</td></tr><tr><td>Override Script</td><td></td><td></td><td></td><td></td><td>id</td><td>Automatic</td></tr><tr><td>Data Binding</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## SHADER BUILDING

Node Path - This will confi rm your current path and help you navigate into and out of the material network. 

VOP Nodes - In the material context, you can start with material nodes then wire in VOP nodes to customize the texturing of the material. Once you are fi nished you can choose to collapse all of this back into a material builder node. 

Node Connectors - You can add nodes to this area using the Shader FX menu which can be accessed by MMB-clicking on the dot. RMBclicking on the dot gives you a full node menu. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9d4565ef44a7125d5c9d4b58fceb5fa54569a939ed9078da5f0132f6134d0ad2.jpg)


Principled Material - This is a typical material which can be assigned on its own or fed into the Layer mix. 

Layer Mix - The Layer output on the materials can be fed into this mix node. You can assign this to your geometry. 

Material Flag- If you want the layer mix to show up in the material palet e then check this fl ag. 

Alpha - Here the layer mix node’s alpha is being fed by VOP nodes to create the alpha mask for the two layered materials. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c9d42babd5024afe3717539e4330d784e5eae2a8d04291d45dbcb9045029f36.jpg)


# Solaris: Layout

Solaris is the context in Houdini dedicated to Lookdev, Layout and Lighti ng that has USD at its core. Objects and geometry brought into this context become USD and you can use specialized nodes for positi oning objects, instancing geometry and managing shot layout. 

## SOLARIS: LOPS

The Solaris environment can be found in the <sub>/stage</sub> network or by creati ng a LOP network. Here you will place nodes for bringing in geometry, assigning materials and adding lights and cameras. These nodes let you create sequences and shots using shared assets and procedural edit nodes to customize seti ngs for each shot. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ac56c6f98ed1804a3c6fa94b53fe42ed04f7eab455a72882678d51dd2a0d5f8f.jpg)


At its core, the Solaris environment converts everything into USD [Universal Scene Descripti on] which is an open source initi ati ve created by PIXAR. The Solaris/LOPS context allows you to work with USD nati vely using procedural nodes to manage USD concepts such as references, payloads, layers, collecti ons, variants and level of detail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9741cbaa6389a09746ea2e9c3f64298a1c57cfc19e349ee26e613f0a7a3753fe.jpg)


LOP networks can then be rendered using either Karma or other Hydra-compati ble renderers. Hydra is the technology that lets you render your USD to the viewport for interacti ve explorati on or to disk for fi nal renderings. 

## SCENE IMPORT: OBJECTS TO LOPS

For arti sts used to working at Houdini’s Object level for layout and lighti ng, the Scene Import LOP node makes it easy to bring your geometry, lights and cameras into LOPS to render. If your goal is to create a controlled USD scene graph then you may want to take another approach but for quick access to Karma and other renderers the Scene Import node works fi ne. 

## PREPARING ASSETS FOR USD

Another approach is for you to confi gure props using either a Component Builder LOP network or the USD Export SOP. This would be geometry and materials set up on a prop-byprop basis then exported as USD for use in the layout stage. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3424b3c1c1898bd15e03a3f428f425d14ed8cc62bc2209edd1d8d912931cb0f9.jpg)


For some of the props, you will use variants to create dif erent variati ons that can be chosen during layout. There are LOP nodes that let you set up this USD concept. 

Once you have the props set up as USD, the fi les can then be brought into a larger layout scene fi le using Sublayer or Reference LOPS then Edit LOPs can be used to positi on the props. If the assets are prepped properly then they will come in with geometry, materials and variants set up and ready. 

## SOLARIS DESKTOP

Stage - The Stage view provides a place for viewing your layout and lighti ng and to interact with primiti ves, lights and cameras to set them up properly. 

Viewport Render - On the stage, you can render using Houdini GL or Storm the USD GL soluti on. You can also render interacti vely to karma and Hydra compliant 3rd party renderers. 

Scene Graph - The USD structure of ers a renderable scene graph that can be inspected using this panel. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8efeb7fe5428d5eb99bfbc9fad75d28595232d7e829e943f6a0c4691d901db70.jpg)


Stage Manager - This node lets you load USD fi les to be positi oned on the stage. 

LOP Nodes - All your acti ons in LOPS are accomplished using procedural nodes that make it easy to step back and make changes. 

Scene Graph Details - As you select items in the Scene Graph you can check for details that inform you of its status in the pipeline. 

## STAGE MANAGER

The Stage Manager is designed to be a one-stop node for referencing USD assets from disk, transforming them in 3d space, and adjusting your scene hierarchy. This does involve a flatening of the inputing layers which will block up-stream changes from coming through. This lack of flexibility is balanced by the rapid setup possibilities of this node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fe1be9c277fd93c943601cdd938837e924e9ca824b290a3b908b98735f1694f7.jpg)


## PHYSICALLY-BASED EDITS

Once you have all of the props loaded onto the Stage, you can use the Edit LOP to begin moving them around. The edits become a separate non-destructive layer which keeps the referenced assets intact in case you need to step back. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c9576c9a597bea800f54443296061edbe48a03a5b8feb6678c61b041873c564f.jpg)



In the Edit LOP, there is a Use Physics option that lets you leverage the rigid body capabilities of Houdini to detect collisions and make it easier to position objects in a realistic manner. This lets the artist achieve a natural organic look while working interactively in the 3D view.


## INSTANCING

There is an instancing solution in USD that can be utilized in LOPS. The Instance LOP lets you input one or more objects that will be distributed to points set up inside the LOP. These points can be created by importing geometry from your scene then scatering points on surfaces extracted from the model. 

Materials can be assigned to the instances using a variety of methods including the Material Variation LOP which also ofers per-geometry render properties. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bd635949275c348d5686b38b4d8c195df48dafdf4d0af06ea027ac388e89cf2b.jpg)



You can also use the Layout Asset Browser and the Layout LOP to use a brush workflow to place, edit and transform instance points that reference the assets you choose in the browser.


## EXPORTING USD

At various points in your LOP graph, you can inspect the USD code by RMB-clicking on the node and selecting LOP Actions > Inspect Active Layer. You can also inspect the Flatened Stage. When you export to USD, you can break out all the layers or save it as a single flatened graph. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0506f3d100cfe12b10a0fd1071e4092534d49a7c7ab8dfb7420579fefc2c2abb.jpg)


## SCENE GRAPH

Stage - This is the top level network context for creating LOPS. You can also do all of this work in LOP Networks. 

Scene Graph Path - These represent the USD layers and sublayers that define the look of the stage. These are most likely diferent USD files on disk being referenced into a shot. 

Primitive Type - Each primitive comes with a type or schema that defines how it works. This can help you determine the contribution each layer is making to the stage. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7734afff501439761b17ec2fa78bebad10959cc8e0c67b23a7d4a25f157b113e.jpg)


Draw Mode - Here you can change the display of any element in the path to either Full Geometry, Bounding Box or Textured Cards. 

Display Options- Here you can set the visibility or activation of each layer. It is not possible to delete anything from the scene graph therefore hiding or deactivating is necessary. 

Variants- If a Layer has variants then the chosen one is displayed here. 

# Solaris: Cameras and Lights

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ae1a31de65df4a49fc904efd9c54701ab285ed83795ef290e812e002bffa4f3e.jpg)


Before you render a shot, you need to look through a camera and light your scene. There are lights and cameras in the Solaris/LOPS context which is especially designed for layout, lookdev, lighti ng and rendering with Karma or at the object level for rendering with Mantra. 

## CAMERA

Cameras can be accessed from the LOP Lights and Cameras shelf. Press Alt-click on the shelf tool to convert your current view into a camera view. If you create the camera node in the Network view, click on the No Cam menu in the top left of the viewport to look through it. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83cd5d901817bf77af6cbc4418a25c40aa2a8beaf6e445f0de6907e392aa9caa.jpg)


To adjust the camera, you can use the Camera handles either from another view or while looking through the camera. There is a lock camera to view but on in the Display Opti ons bar that lets you use the View tools to repositi on the camera. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/556f53dcb11fd2fb29caaaa99daa83c301ef1dec8e8e5cb7d86772b22bf81f7b.jpg)


There is a lock camera to view but on in the Display Opti ons bar that lets you use the View tools to repositi on the camera. Just make sure that you don’t leave this on later otherwise your camera view may get changed by a simple view change. Once you like a camera view, you may want to lock its transform values to avoid losing it to a view change. 

## CAMERA PROPERTIES

The Cameras in the LOP Context have key properti es that determine how the camera will generate images. 

## View Tab

 Projecti on - Choose between perspecti ve or orthogonal projecti on. 

Focal Length - Determines the length of the lens. Smaller values create wider shots and higher values create long shots. 

Horizontal/Verti cal Aperture - Aperture is a gate that controls how much light goes into your camera. 

## Sampling Tab

 Shut er Open/Close - Determines how long the shut er is open which has an ef ect on moti on blur. 

 Focus Distance - Distance from the camera to the focal plane. Determines which objects are in focus when using Depth of Field. 

 F-Stop - Lens aperture. Default is 0, which turns of focusing. 

Press Shift + F to show a visualizati on of the focal plane and how it intersects geometry. When looking through a camera, you can Shift -click or drag on a surface to move the focal plane to intersect that point. Otherwise, you can use a handle on the focal plane to move it and set your Depth of Field. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/93bb5dfac2c4ce0388be68d989635a7ab4e63a8be84aeb0aa00dca3271cf6226.jpg)


## LIGHTING SETUP

Viewport Rendering - To make lighti ng decisions, it is important be able to render in the viewport using either karma or other renderers such as RenderMan or Arnold. 

You can also use HoudiniGL but this is not as ef ecti ve as one of the main renderers. 

Light Handles - You can step back and manipulate lights in the view in a similar manner to cameras or you can use special controls to set lights right in the camera view. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0139382de40e851a681e4205ddffb60739bc8bf23af938e28cecb46104b4208b.jpg)


Primiti ve Path - This sets where your light will be in the USD scene graph. 

Light Type - You can choose your light type from this menu. The Light LOP gives you access to all the light types and you can switch between them. 

Light Parameters - There are a range of parameters for controlling light properti es such as cone angle and intensity. 

Light LOP Nodes - Every light is added into the network as a LOP node. 

## LIGHTS

Lights can also be accessed from the shelf and have similar handles to help you positi on them. There are a number of dif erent light types in Houdini to choose from. 

Point Light - Emits light from a point in all directi ons and is similar to a light bulb. 

Spot Light - Radiates a cone shaped beam of light from a point in a certain directi on. 

Area Light- Automati cally distributes a number of light sources over a specifi ed area. There are fi ve area light shapes to choose from: Line, Tube, Grid, Disk an Sphere. 

W Geometry Light- This object emits light into the scene using a geometry object’s surface shader for the colors of the emit ed light. 

Distant Light- Emits parallel rays of light, which are similar to the rays of the sun. 

Environment Light- Casts light into the scene as if from a surrounding hemisphere or sphere. 

## LIGHTING WHILE IN THE CAMERA VIEW

When you have a Light or Light Mixer LOP selected and displayed, you can set many of its properti es while looking through the camera. You can use the Specular [Shift -S], Dif use [Shift -D] or Shadow [Shift -F] opti ons that let you click on surfaces in the scene to set up the light. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ed073ced6e7f787ac06a6321e01bd47470b679c899c924af564fe277710382d1.jpg)


You can then use Ctrl-drag to change the distance of the light from your shot and Ctrl-Shift -drag to change the brightness. Doing this in the viewport lets you stay focused on the shot you are working on instead of pulling away to drag on handles. 

## LIGHT MIXER

Light List - This list shows all the lights feeding into the mixer. 

Collecti on - You can organize lights into collecti ons so that they work as a group in the mixer. 

Solo Lights - Click on the star icon to solor the light or the collecti on. 

Intensity Slider - The fi rst slider gives you control over the intensity of your lights or light collecti ons. 

Exposure Slider - The second slider gives you control over exposure which of ers a tweak to the intensity. 

Light Color - Click here to ti nt the light or the collecti on of lights. 

## LIGHT LINKER

Linking lights to specifi c objects is a great way to control the lighti ng of the shot and this can be accomplished in Solaris using a Light Linker LOP. This node includes an interface for making the object/light connecti ons that you need. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/59f95ab25c32de60ddebcf42979afdaed81c2ea899be1814e378c0f12b49f2e1.jpg)



You can use collecti ons of lights to apply the linking more efi ciently using rules that defi ne the interacti ons between primiti ves and lights.


## INSTANCING LIGHTS

Within the Solaris/LOP context, you can use Houdini’s procedural geometry nodes to create points then Instance Lights to those points. You can then add at ributes to the points to create ef ects such as a rotati ng intensity you might fi nd in an old school marquee. This approach makes it easier to set up the lights and even easier to add ef ects and make changes to meet the needs of the shot. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c0e785b0670b782be3776c4f4e66859e86ca6789cf40196b78065292a3b9cd3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/93d28f1403ec80d86de0eb65b9310da83edd7d96c27fded82142ed3793157d96.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f51739e66d51bbd6feabbfe0b62655f5ed73fe177e096f023d7bd4be6e82cc7d.jpg)


# Rendering

When you render a shot, you are digitally photographing or filming your 3D objects using cameras and lights to generate either an image or a sequence of images. Game artists may also use rendering to render game cinematics or to bake textures from a high resolution to a low resolution object. 

## KARMA

Karma is a physically-based ray-tracer built to work with USD files in the Solaris/LOPS context. It works on the CPU and includes features such as adaptive tesselation for displacement and subdivision surfaces, multi-segment motion blur, instancing, hair & fur and strong volume rendering support. 

Karma works with Hydra,the USD imaging framework. This makes it available in the Viewport for interactive updates or you can render to disk using a Karma node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/35c1cb24d0e32a2e2b7e89090a1dae3c7c0e8bc6e4ee7a23a39b8f73dbdf3313.jpg)


Karma works with shaders created using VEX, USD preview and Material X. 

## KARMA XPU

Houdini 19.5 includes a beta version of the Karma XPU render engine. This hybrid GPU/CPU renderer is being released in Alpha. Many features are still under development and this engine is for testing purposes only. You can choose XPU in the Scene view’s Display Options or in the Karma node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c281435304aaf7d1aacd3394cc6d32126add153ff30f8cfa74b905714e429cc2.jpg)



Karma XPU works with USD preview shaders and Material X but does not work with VEX.


## 3RD PARTY RENDERERS

With its support for USD, Solaris makes it possible to render to other Hydra delegates such as RenderMan, Autodesk Arnold, V-Ray, Maxon RedShift and AMD ProRender. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/485bfedff7ca11f19251cd976ef14622826a8887786d772f935b33a20948fb40.jpg)


## VIEWPORT RENDERING

One of the key benefits of the Karma renderer is the ability to use it in the perspective view. By choosing Karma, you get interactive rendering that helps you make lighting and lookdev decisions within the Solaris/LOPS context. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/73382cfd23374fece0059d4dd32a85c4b3559a76e96c4b3b608386acdb9639c6.jpg)


## VIEWPORT | KARMA

Render Setings - To render to disk, you can use the Karma LOP to define your render setings. Here you can set a path for rendering to disk, camera setings and more. 

Karma LOP - Add the Karma LOP to the end of a Solaris node network. Diferent versions of this LOP can be used to set up unique results such as test renderings or final shots. 

MPlay - You can either render from both Karma and Mantra to MPlay directly or render to disk then open up with MPlay to review the results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/189ba262671fbd9bd0d212f9f9272d36617f73b692fc6b47cfa0a13b795a6998.jpg)


## RENDER SETTINGS

When rendering the Stage, you use the viewport render setings. To create the final look of your rendering, the Karma LOP can be used to set a frame range, camera resolution, denoiser and higher quality render setings. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7777d9f25fe7c1f67d6702bb5fa9cdcf274e07bf28ef1c099449a24871379ec4.jpg)


## RENDER GALLERY

The Render Gallery lets you take Snapshots of your progress. Each snapshot contains all the setings of the look and at any time the scene can be reverted to match the snapshot. Snapshots can then be labelled and filtered for easy access. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2e9390fa778ccb8ee7b28a19811f848f6718745fcfaa3a571ce5551a285d68b.jpg)


## MANTRA

Mantra is the Houdini renderer developed before Solaris was introduced. It is a physically-based rendering engine that is deeply integrated with highly eficient rendering of geometry, instances and volumes but it does not work in Solaris/LOPS. 

## OUTPUT NODES

To render out a shot, you will need to create a render output node. You can do this by choosing Render > Create Render Node > Mantra - PBR. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e4849c8271b9bfed76c5f398a25d38b70837ae4a86095295e06e27fb9fb325b0.jpg)


You can also add a Karma ROP to the output network using the tab key. This has a LOP network inside it that grabs all the visible objects from the object level. 

You can use ROP nodes to render to disk or to Mplay. These nodes contain many of the parameters that you need to control the final image such as sampling, noise level and overall render quality. 

It is possible to have a diferent ROP per object or group of objects and you can use them to select Mates and Phantom objects. You can create ROP dependencies by wiring diferent nodes together. If you press the render buton on the last node in the chain then all the other nodes will render first. 

## RENDER OUTPUTS | AOVS

On the ROP, you will find controls for seting up Image Planes to create render layers for Direct lighting, Indirect lighting, Shadows, Depth etc. Both Karma and Mantra can render out these passes which can be loaded in Houdini’s compositing context, COPS, or in an external compositor such as Nuke. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/994b19a94fd15735a4211b172548bbca9263fa5b851eef68499b2808e23224f0.jpg)


The Background Plate LOP can be used to mate objects in order to leave holes in the scene to make the background visible. This geometry can take shadows and contribute to reflections to create a more realistic fit for your objects. 

## MPLAY

MPlay lets you view images rendered in Karma, Mantra or other renderers. 

Main Menu - This menu lets you load images or sequences of images to preview them. You can also save them out to another format if needed. 

Render Layers - This menu lets you display diferent render layers such as color, normal, difuse_direct or reflect-direct. 

Playbar - If you have loaded up a sequence of images then you can use these controls to play and scrub through the sequence. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1ccfa712c587c64fee4b97b1b810c2ecbee85c728f9c6290f270cdea9a1db83b.jpg)


Render Time - Since you are sometimes rendering directly to this view, render time info will be displayed. 

View Options - MMB-drag to pan and RMB-drag to zoom in and out of the image. 

Channels - You can click on these butons to focus on red, green, blue or alpha channels or to see them combined. 

Gamma Setings - Set the brightness, contrast and gamma for the viewport. By default a gamma of 2.2 is used to support a linear workflow. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0318860f3bed1c422768240dc1e3f2aeb74c92c2c6d274b8854d0ed2aca39ff1.jpg)


## Time & Moti on

Animati on involves changes happening over ti me. Whether it is an object’s positi on, shape or color, once changes occur over ti me, you are animati ng. Houdini has a variety of tools for keyframe-based workfl ows in additi on to Moti on FX & CHOPs for more advanced manipulati on of ti me and moti on. 

## Or SETTING KEYFRAMES

Keyframes let you set specifi c parameter values at a specifi c points in ti me. As these values change, the objects in your scene are animated. You can then use animati on curves to determine the in-between quality of the moti on. Here are a few main hotkeys used to set keyframes on your objects while working in the scene view: 

 Set keyframe 

 Toggle Autokey Alt + k 

 key Handle Ctrl + k 

 Key Translate Shift + T 

 Key Rotate Shift +R 

 Key Scale Shift + E 

You can also set keyframes in the parameter pane by pressing the Alt key and clicking on either a parameter name or parameter fi eld or by RMB-clicking on a parameter and selecti ng Keyframes > Set Keyframe. This lets you set keyframes one parameter at a ti me 

## THE PLAYBAR

The Playbar is at the bot om of the main workspace and lets you playback and scrub through your animati ons. Time is measured in frames with a default rate of 24 frames per second. 

At the left are the playback controls. Here are some hotkeys for quickly seti ng up playback and moving through ti me. 

 Play Forward  

 Play Back 

 Next Frame 

 Previous Frame 

 First Frame Ctrl +  

 Next keyframe Ctrl +  

 Previous keyframe Ctrl +  

The Playbar can also be used to edit keyframes. You can RMBclick on the frame range in the Playbar to access opti ons such as Cut, Copy and Paste of keys along with special pasti ng such as Replace, Cycle, Repeat and Stretch. All these opti ons also have their own hotkeys which you can fi nd on the menu. You can accomplish a lot working in the Playbar before moving to the Animati on Editor. 

## CHANNELS

When you set a keyframe or display animati on curves in the Animati on Editor, you are working with channels. 

If you select an object that has keyframed channels then they become acti ve and the keyframes are loaded into the Playbar or Animati on Editor. If you deselect the object then the channels will no longer be selected unless you pin them. 

You can pin channels using the Channel List which is available on the right side of the Playbar, the left side of the Animati on Editor or in the Channel List pane. In this list, you can select one or more channels to refi ne which of them you are keyframing and editi ng. 

## CHANNEL LIST PANE

The Channel List pane, lets you work with Channel Groups, Animati on Layers and Acti ve Channels. You can use the list to create groups of channels so that they can be more easily accessed. You can also use the groups to pin channels so that they are available even if you select dif erent objects. This is a useful pane if you are seti ng keyframes on characters. 

## FLIPBOOK

As you animate your scene, you will want to preview the results in moti on. The Flipbook tool found on the toolbar on the left side of the Scene view lets you capture frames from the viewport then playback the results as a movie in realti me. 

## PLAYBAR

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9860f698d1dfbe9610c825c4b838610d0cccfb0cc8cf2be127a04151ea7bbd8f.jpg)


The Playbar is where you scrub through ti me and create and edit keyframes. The Playbar can also be used to make quick edits, while the Animati on Editor is used for more comprehensive refi nements. 

Current Time 

These controls let you quickly play, pause, and move to next key. Belo that are but ons for Animati on opti ons and Real Time playback. 

The current ti me is shown in the fi eld and on the black marker in the frame range. The marker can be used to scrub through the Playbar. 

Frame Range 

The overall range is defi ned by the Animati on controls but on at the far left . Then the visible range can be reduced using the handles at the bot om of the range. 

Edit Keys 

As you set keys, they are shown in the Playbar. Press the shift key to select keys with the LMB and then edit the keys by dragging with the MMB. 

Set Key 

The Set Key but on will set keyframes when you click here. Click on the small arrow to bring up a menu of opti ons such as Auto key. 

## ONION SKINNING

Onion Skinning lets you display a ghosted version of your object on the frames before and after the current frame. Turn it on using the Misc tab on your object while the onion skinning options such as Frames Before, Frame After and Frame Increment can be found in the viewport’s Display panel [d] under the Scene tab. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1728534ecd0a691b99d1b10d973eb720e3b3820095e3590fe1ba18d4aebafe7f.jpg)


## MOTION PATH HANDLES

When using the Pose tool to animate, you can click on the Motion Path option to bring up handles that let you see the animation of the selected object over time. You can also use the handle to manipulate the shape of the motion. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4ae3894a2960863f7ccaf4f1d20cd48d72569ff21a71bc461abc41a95713753e.jpg)


## ANIMATION EDITOR

Selected channels are loaded into the animation editor where they are represented as keyframes and animation curves, or as a spreadsheet or a dope sheet. The keyframes can be selected and edited and the curves can be shaped using tangent handles. The curves define the motion in-between the keyframes and play a key role in defining the quality of the motion. 

While working with channels, you can view the keyframes and animation curves using these hotkeys: 

 View All/Home 

 Pan 

 Zoom 

## MOTION FX

While keyframes and animation curves are stored in the parameters of your nodes, you can also use channel operators (CHOPs) for a more procedural node-based approach to working with motion. 

The easiest way to create a channel operator is to RMB-click on a parameter and select from the Motion FX sub-menu. You can also apply these efects to channel groups when working in the Channel List. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a5853f9409d044c0d77ee0bb9cdab47838b26cb3994081f478294185435a3417.jpg)


Motion FX can be applied to keyframed motion which is extracted and stored in a Channel CHOP. You can then apply efects such as cycle, noise, smooth, limit or lag to the existing motion. On the Constraints shelf, you have tools which let you have one parameter either look at, lag or jiggle behind another. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/248ddccf7c712eac70ffb41f176a975980eefca9aec81e3f5cb962c9e7994c6c.jpg)



This non-linear approach to working with motion ofers a unique way of working that can be very flexible.


## ANIMATION EDITOR

Editor Options - This editor can be shown as a graph, a dope sheet or a table. 

Channel Groups - This area of the graph shows channel groups which make it easier to select and pin channels. 

Animation Layers - This area lets you layer diferent channels on top of each other to create multiple iterations. 

Channel List - Channels on selected objects show up in this area. You can then select the names of channels you want to see in the graph. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9691a88a21f32c73150ca317eddf66ecd917fa5c57e0e95da08ad8b130fae97a.jpg)


Key Handles - Move the key back and forth in time using the vertical bar or edit its value using the box. 

Tangent Handles - They define the tangents coming in and out of a keyframe to help you shape the curves. 

Curve - The animation curves determines the motion in-between the keyframes, which defines the quality of the motion. 

Curve Functions - These let you set various display options for the animation curves and handles. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/52cd1bc215437e54cde74ba15df809117b8285fd739fcdea7c36680553b105f2.jpg)


# Character Rigging & FX

Houdini includes a wide range of rigging tools for creati ng characters and creatures that can then be wrapped into Houdini Digital Assets to be handed of to animators. Houdini also has Character FX tools such as hair, fur, muscles, cloth and crowds to enhance the look of your characters. 

## BONES

In Houdini, you draw and edit bones using the Bones tool and the Bones from Curve tool found on the Rigging shelf. Each bone chain is made up of a chain root and bones. Whereas other 3D apps are joint-based, Houdini uses Bone nodes that have parameters for Length and Rest Angle. 

You can also use the Bones tool to add inverse kinemati cs to the chain which adds an end ef ector and in some cases a twist ef ector. The kinemati cs are driven by Channel Operator or CHOP nodes which exist in their own subnetwork. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f1970587789dc59eb8a3f9e2598d5344890e2e6cdfa992f4edac63c5650edb79.jpg)


## CAPTURING GEOMETRY

The character’s geometry can then be captured to the bones to create the deformati ons needed to convey realisti c moti on. Houdini bones include Capture Regions that you can set up to encompass your geometry while creati ng the right overlap at the joints. This process results in weighted at ributes being assigned to the points that get fed into a Deform node that controls the geometry when the bones are moved and rotated. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/288d296a5aa9871781e2c38498150d18c0a9dd563d725aad9faf328680133ad2.jpg)


At fi rst, captured geometry might not get you exactly the look you want, therefore you would use various tools to Edit and Paint Capture Weights. This lets you smooth out the weighti ng at the joints to create more realisti c bending. You can also smooth out the ef ect of point deformati ons using a Delta Mush node that wires into the Deform node. 

A new technique called Bone Capture Biharmonic allows you to capture geometry without requiring extensive point weights to get a desirable look at the joints. This method sets up biharmonic functi ons on a tetrahedral mesh to create a much more holisti c soluti on. 

## DIGITAL ASSET CHARACTERS

To rig a Houdini character and share it with the animati on team, you will need to wrap up the bones, geometry and materials into a Houdini Digital Asset. 

This creates a fi le on disk that can be easily referenced by animators into multi ple shots. Handles and key parameters are made available at the top level so that Animators can set keyframes without worrying about the inner workings of the rig. You can also save Pose Library and Character picker setups into the asset for quick access. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7d8526c7eceefe038a57789f521353f0de706be0bbcc2b708d30296c372b925d.jpg)


Changes made to any part of that character are saved into the asset and all shots will be updated. This creates a robust character pipeline that is easy to manage. 

## KINEFX

KineFX is a character toolset designed to provide a procedural foundati on for retargeti ng, moti on editi ng, and in future releases, rigging and animati on. Set in the geometry context, these new workfl ows make rigging a fast, plug-and-play experience with unlimited fl exibility and caching capabiliti es. 

Implemented in the geometry [SOP] context, KineFX treats joints as regular point geometry with edge connecti ons defi ning the rig hierarchy. You can bring rigs in from the object level of Houdini or import FBX characters. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e5b47c75914415d3692c0f70a24b61d85d7eba814340ed85639804a0e2737e9c.jpg)


## CHANNEL GROUPS

When you animate in Houdini, channels that are scoped can be keyframed and displayed in the Animation Editor. Generally these channels are based on your current selection. You can also put together Channel Groups that let you scope and pin down channels to assist with keyframing. 

When you have a character set up as a Digital Asset, you can click on its icon at the top left of the parameter pane and choose Parameters and Channels > Create Nested Channel Groups to create groups using the asset’s folder hierarchy as a guide. A well designed character asset makes this easy. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e254aca13e3ee651093d7122974ceaf34e52da8fde1283a25ee0f769ca5f2453.jpg)


## CHARACTER FX | HAIR & FUR

Houdini has a hair and fur toolset that you can use to setup and groom your character starting with the Add Hair tool. These tools also let you work with guide hairs and then animate them using wire sims to create added realism. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6542b9e05e3a13d2220e4f606e6edf2b6d0cce78b98410db2e613b2b5b165666.jpg)


## CHARACTER FX | MUSCLES & SKIN

Houdini lets you add muscles to an animated creature and then apply them as a skin deformer without requiring any simulation. Start by creating simple muscle forms using the Muscle nodes in the geometry context. 

You then adjust the muscle’s shape and placement, atach it to your character rig then enable automatic secondary animation or jiggle. Houdini’s muscle system has been designed to serve both FEM (dynamics simulations) and non-FEM (skin deformer) workflows while using a unified set of Digital Assets. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/52454aaf1a69200c5699bc48bc9ebaa884927dfec4db27ae258ac6b605a05ddc.jpg)


## CROWD SIMULATIONS

A crowd simulation begins with agents that are made up of a character skeleton, skin geometry, and animation clips. These are assigned to points, where simple rules can combine to create complex behaviors and the agents can interact with other dynamic elements. For example, an agent might be struck by a passing car and become a rag-doll or a crowd might be triggered to react to an action on the field. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c89576b6e8bdcf6636325080c80394420bd4f0220d602aa06d4701bbaa5f6258.jpg)


## CHARACTER PICKER

This pane lets you create an interface for choosing parts of your rig. This can then be saved into a file that you add to your Digital Asset file on disk. 

Tabs - Set up multiple tabs for diferent areas of the body such as hands, feet or face. 

Controls - Place markers for the diferent handles on your rig then add text or color to help you distinguish between them. 

Background Image - Add a visual representation of your character to properly associate the markers with the parts of the body. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/70a6726831d35e8ac94db0fba789ef24c27ab7d66eac32dfd544fa1442f802b0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9df53056138f01449ce6bd6ca4809247a415531c280a9c1909d38c1b747a2d1b.jpg)


## POSE LIBRARY

The Pose Library pane lets you capture poses and clips from your character for future reference. You can go to a frame in your Playbar and apply the pose by clicking on it here. 

Pose - These save out a pose taken from a single frame. All of the parameter setings at that pose would be applied to the character in your current scene. You would then use this to interpolate to another pose. 

Clip - A clip contains a set of keyframes for a longer time period. These might be a walk cycle or a particular movement like a back clip. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bb24af5cf14db5243f71aab2873b5924c30e6be468f60a81450a5fb73c54691d.jpg)


# Dynamic Simulati ons

Whether you are creati ng Bullet Rigid Body destructi on, Pyro FX fi re and smoke, Vellum Soft Bodies or FLIP fl uids, Houdini lets you work in an integrated dynamics environment. Dif erent solvers know how to talk to each other to allow for more directable results. 

## SHELF TOOLS

Seti ng up dynamic simulati ons involve a network of nodes in the Dynamic or DOPS context, as well as nodes at the Geometry or SOPS context. It is always a good idea to use the shelf tools because they will add all of these nodes for you and reduce the number of clicks needed to set up a sim. You can then dive into the networks to explore all of the nodes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/93b5cab8a1dbf9f727be76719c309c9bdab5200328ba93c91e69f6864e2252aa.jpg)


The shelf tools are great for seti ng up groups of nodes automati cally. Seeing how these shelf-built networks are put together can be very useful later if you choose to set up DOP networks from scratch. 

## DYNAMIC SOLVERS

At the center of any simulati on is the dynamic solver. It is the brain of the simulati on and takes all of the dynamic objects, forces and collision objects and integrates them to create the fi nal result. The shelf tools put these solvers into a Dynamic Network and wire up the nodes for you. 

Rigid Body Solver- Simulate rigid objects falling and colliding using the efi cient Bullet solver or Houdini’s built-in solver. 

Stati c Solver- For situati ons where you want objects to work as collision geometry but not be af ected by the simulati on. 

Flip Solver - This solver creates FLIP Fluid simulati ons to create splashing and wave ef ects. 

Whitewater Solver - Aft er completi ng a FLIP solve, you can run this solver to create foam, spray and bubbles. 

Vellum Solver- A type of POP Solver that includes integrated support for cloth, hair, grains, fl uids and soft bodies such as balloons. 

POP Solver- Used for parti cles and grains, this solver simulates a wide range of dif erent parti cle-based scenarios. Grain simulati ons can also be used for soft body and cloth-like simulati ons. 

Wire Solver- You can use this solver for hair and fur or other wiry objects such as the rigging of a ship or the branches of a tree. 

Finite Element Solver- Simulates the physics of conti nuous materials or solids as determined by tetrahedrons. This solver is used for muscles, soft body sims and destructi ons shots such as breaking wood. 

Cloth Solver- Create cloth simulati ons that can collide with deforming geometry such as a character. 

SOP Solver- Use a SOP network to evolve an object’s shape over ti me such as a wall being dented as it gets hit by objects. 

## OPENCL

You can use the GPU for faster sim ti mes using OpenCL on solvers such as the POP Grain node, the Pyro solver (Advanced tab) and the FLIP solver (Volume Moti on > Solver tab). 

## FORCES

To create dynamic moti on, forces are needed to “get the ball rolling.” The most basic of forces is gravity although other external forces such as fans, fl uids and magnets can also play a role in initi ati ng moti on in your simulati on. 

Gravity Force A downward force on objects which works as if they were inside a gravity fi eld. 

Drag Force - Applies force and torque to oppose an object’s existi ng moti on to slow it down or dampen its momentum. 

Uniform Force- A precise amount of force and torque that can be augmented by a noise DOP to add turbulence. 

Fan Force- Applies a cone-shaped force on objects. 

Fluid Force- Deform soft bodies such as cloth or wires with fl uids. 

Wind Force- A pushing force that will increase the velocity of objects up to but not beyond its own speed. 

Magnet Force- At racts or repels objects using metaballs to represent a force fi eld. 

Vortex Force- Creates a vortex-like force that causes objects to orbit around a curve much like objects around a tornado. 

## DYNAMIC OBJECTS

When you select an object and use a shelf tool to add it to your simulati on, Houdini creates a Dynamic Object that uses the object’s geometry and adds dynamic properti es such as density, fricti on, and bounciness. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a6e7c8feb6d957704216d711871c12d840b5d755bd03afb83c0acc5ca00bdc34.jpg)


## ACTIVE VS STATIC

Acti ve dynamic objects are af ected by forces and collisions while Stati c objects are not. If you want to use animated or deforming geometry then you must defi ne this on the dynamic object using either the Initi al Object Type menu or the Use Deforming Geometry checkbox. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5cde328be6d79ef5d7b6360ba0e81e12978840868f007ec3ef12b5da6ce2f69c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2454bbe1e996bc7e35a2e0f56c868c4c49ca330c11757b403a5206ba17ca5c0b.jpg)


## COLLISIONS

Collision objects are also a big part of any simulation. You can set up a Ground Plane to create a continuous surface for collisions or use either static or deforming objects. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ca57d1506db16e2800203813bea498f0842520f34a22e6e397c8f366e4f4ea89.jpg)


On each Dynamic Object, there are also setings for displaying and optimizing the collision volume. While you often want collisions to be as accurate as possible, you need to balance that with the need for faster simulation times. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/598d89d6a75bf1c0502a223d3ddde1e1ea63994184fd5357ce8c9a6d7cc73dd2.jpg)


## RIGID BODY CONSTRAINTS

On the Rigid Bodies shelf, you will find a number of constraints that can also be used to influence a simulation. These include Pin, Spring and Slider Constraints. You can also use Glue Objects when you set up a rigid body sim to hold objects together unti you either “loosen up” the glue or a collision occurs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d22a5b38f7f615e1a0bd9c90a1ae4b482596c68bb1392dc550c44267863668bd.jpg)


## PLAYBAR FEEDBACK

To start a simulation, you press Play in the Playbar. As the simulation progresses, the Playbar is highlighted to show how much of the sim has been cached to memory. You can then scrub through that area without re-simming. 

## H11□マコ三31

## CACHING TO DISK

Once you have completed a simulation, you can either lock it down by saving out a sim file from within DOPs or more commonly, write out the simulated geometry to a bgeo sequence using the File Cache node. This will make it easier to work with the results of a sim during the lighting and rendering stages of production. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/17b88fe5f5bdf9ec2fb5872a55e79d837cecbc69bcaa741dec68989866b4b9fe.jpg)


## REALTIME FX FOR GAMES

In games, you need efects, such as explosions, to be optimized for real time in the game engine. Check out the SideFX Labs Tools to learn more about converting diferent kinds of Houdini sims such as rigid bodies, Pyro FX and Fluids into game ready art. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/99fb079beb9312d71c2e39998a615dd29a94d531a420afd4596da5ba16957a6b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ef9bb0652edb681963e3d02be0d351811646c957856958cdd24b10ea2eb16233.jpg)


## AUTODOPNETWORK

When you use a shelf tool to create a dynamic object, collision object or force, the AutoDopNetwork is created to combine all of the parts. 

Static Objects - These nodes set up the properties of the ground plane and a static collision object. 

Static Solver - This solver keeps the incoming objects still while dynamic objects interact with them. 

Merge Node - Brings together parts of a dynamic system. During simulation nodes are evaluated up and down the chain so that everything interacts. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d66133d6b2b7b670b1c3c32735afdefd8a065f0ca0240c2e03c97ac56632ca91.jpg)


Dynamic Object - This node brings geometry into the DOPs environment and assigns basic properties. 

Rigid Body Solver - The solver that generates the simulation of the participating objects. 

Forces - The nodes that influence the dynamic objects using forces such as gravity or wind. 

Output node - You can use this node to output .sim files if you want to cache out the simulation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ffea3d7d7410b566368b6a4a252d62f4dc07888e8af19c5d35663cea48cbfdc0.jpg)


# Cloud FX & Volumes

A big part of visual ef ects in Houdini is the use of volumetric data. In Houdini, volumes oft en sit under the hood to help tools get the job done but it is a good idea to learn what they are and, in ti me, learn how to work with them directly. 

With volumes, you describe objects using voxels rather than points and polygons. A voxel is a 3D pixel, a cubic grid where each voxel contains informati on that informs how the volume will be displayed which makes it ideal for wispy cloud-like shapes. The visual quality of a volume-based object is defi ned by the resoluti on of that 3D grid. With more resoluti on, the results are of a higher quality but performance may be af ected. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cc1969c56ad8059715a068ea7e8110da33f8f560ec9c1a2142133b3592d43b15.jpg)


## ISO OFFSET

The Isoof set node found in the geometry context lets you take any manifold Polygon geometry and construct a Houdini Volume for Houdini to use. You can choose from a variety of dif erent Output types to see the shape as fog or a tetra mesh. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/19aea8e6ce5b20f363fa4b17466396e87c6d1c47897dcfbf074e7bcf2345ba7b.jpg)


## CLOUD FX

This toolset converts geometry into a cloud-like VDB volume complete with lighti ng. The Cloud Rig tool can be useful for shaping an individual cloud, or simply as a way to bet er understand lower-level tools such as Cloud, Cloud Noise and Cloud light that all contribute to the fi nal look. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3537f212bc376316e066fad3d05a8e38b76fe0b665dc0b016e74b3bd60957798.jpg)


The resulti ng network imports the cloud source then applies these other nodes to create the cloud-like ef ect using Houdini Volumes and VDBs. Houdini also comes with a Sky Rig tool that fi lls the sky with volumetric clouds. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/91c412648a20f9cf98001b40d56c93e73e571b2f3434a361d9ce36aaf06c0c06.jpg)


To create a cloudscape for a game engine such as Unreal you can use a Sky rig in Houdini, then convert it to a mesh and use it as a spawn surface. There is a tutorial on the SideFX website by Andreas Glad that teaches this approach. 

## OPEN VDB

“OpenVDB is an Academy Award-winning open-source C++ library comprising a suite of tools for the efi cient storage and manipulati on of sparse volumetric data discreti zed on threedimensional grids. It is developed and maintained by DreamWorks Animati on for use in volumetric applicati ons typically encountered in feature fi lm producti on.” - openvdb.org 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ca5caa6d44cf9344b7a2e3387440f606f09f3e0147f277fad5c7bdf09bc16f53.jpg)


Houdini has a variety of OpenVDB Volume nodes available in geometry [SOP] networks that convert geometry into volumes. 

## VOLUMES UNDER THE HOOD

Many of the tools in Houdini make use of volumes under the hood where you can’t see them. Here are some of the areas where volumes are making contributi ons to your work. 

Colliders - By default, volumes convert geometry into colliders for dynamic simulati ons. 

 Simulati on Fields - Volumes defi ne fi elds such as density or velocity that contribute to dynamic simulati ons. 

 Hair and Fur tools - These tools use volume data to assist with grooming calculati ons. 

Terrain - Heightfi eld tools use 2D volumes where each voxel contains the height of the terrain at each grid point. 

 Rendering - Volumes create water depth and fog ef ects in Mantra. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2d6b61529a7eb8a4e3e53ed7b13ed3924808fced8a864584a2e3a4651f656ef6.jpg)


# Terrain & Heightfi elds

Procedural terrain generati on in Houdini is achieved using a collecti on of heightfi eld nodes that let you layer shapes, add noise and run erosion simulati ons to defi ne the look for your digita landscapes. This a workfl ow that is similar to compositi ng, but you do all your work with 3D shapes. 

Houdini provides a variety of geometry nodes for generati ng and shaping terrain. These tools represent terrain using 2D volumes where each voxel contains the height of the terrain at that grid point, called heightfi elds. The data passing through a geometry network can contain multi ple heightfi elds. You can access these tools using the Terrain desktop. 

The Houdini viewport lets you visualize the 2D heightfi eld as a 3D surface, and the mask fi eld is displayed as a red ti nt on the 3D surface. There is a dedicated Mantra procedural for rendering heightfi elds and they can be used as collision surfaces for dynamic simulati ons. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c3970a45e62fc2178459a81af96e8e54a8542697221f09bf03fd230ad6bbd5ea.jpg)


## PATTERNS

Aft er laying down a Heightfi eld node to defi ne your base resoluti on, the Heightfi eld Pat ern node gives you access to a number of starter shapes. You can set up linear, concentric, or radial ramps, linear steps, radially symmetrical shapes such as stars and voronoi cells. 

These shapes can then be blurred and distorted to get shapes that you can use to begin your terrain. You can also combine and layer elements to achieve even more sophisti cated results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ac71e4d7be20264c5e976e67420e27f6da28756032703b8729e1be94fa6380e8.jpg)


## NOISE

As you build up your terrain, you can then add noise to layer in a natural look. You can choose from a variety of dif erent types of noise including, Perlin, Sinusoid, Worley and more. This adds realism to your terrain and by combining dif erent shapes with dif erent kinds of noise, you can achieve a wide variety of hyper realisti c results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2dc9e4bafdd48e55908367ff4930b838dad19908a663495cde382eea2fc578e.jpg)


## MASKS

The heightfi eld tools also use a secondary type of 2D volume, where each voxel contains a mask layer. Most terrain nodes take a second input that can contain a mask layer to control which parts of the terrain the node will modify. 

You can use a variety of dif erent methods to create masks and then use them to assist you as you add detail and shape the terrain. You can also draw or paint masks onto the heightfi eld. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/34c4dfbf4188d1a60ed6bd84b34d8f448307e68c042c76c8d826a565cad6eb23.jpg)


## EROSION

The Heightfi eld Erode node uses rainfall, the erodibility of the soil, and entrainment rates as variables to simulate erosion and deposit buildup. This node works iterati vely during playback. It will appear to have no ef ect on the fi rst frame. You need to press play in the Playbar to watch as it sims the erosion. 

## EXPORT OPTIONS

There are a couple of dif erent ways to export your terrain for use in another applicati on such as a game engine. You can use the Heightfi eld Output node to export height and/or mask layers to disk as an image then bring these in as textures. 

You can also create Houdini Digital Assets that will open up in applicati ons such as Unreal and Unity using the Houdini Engine plug-ins. In the game engine, these Digital Assets will interact with built-in Terrain tools. 

# SideFX Labs

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/84826e3a266a5b3293702d171ca389173b025a1bb36002919673126829fbdb9b.jpg)


SideFX Labs is a collecti on of high level tools aimed to speed up arti st and gamedev related workfl ows in Houdini. There are a growing number of tools being developed that range from Mesh Processing, Realti me FX, UVing, to creati ng Moti on Vectors from simulati ons. 

While all of Houdini can be used to generate content for fi lm, TV and games, the Labs toolset addresses arti st-specifi c tasks that may not be available in Houdini today. These tools are developed separately from the regular Houdini development cycle and become available the moment they are ready for testi ng. They can be downloaded directly from within Houdini or accessed through the SideFX Labs github page. 

## DOWNLOADING THE TOOLS

The Labs tools can be installed with Houdini or accessed from the SideFX Labs shelf tab. It not visible on most desktops so you will need to add it. Once it is visible, click on the Update Toolset but on. This will pop up a dialog prompti ng you to install. Since many tools are in beta, you may want to turn Of the Producti on Builds Only opti on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/518997e6e306b1fc2bde7ef86dc69aa57a33958ed1c1cd7a51f5b4f3410ea85e.jpg)


The shelf will be populated with many of the tools but some are only available when you press tab in the Viewport or Network view. These nodes are prefaced with Labs to make them easy to fi nd. 

## FX TOOLS

Houdini is known for its strong FX tools and SideFX Labs has tools to process the results for use in a realti me environment for games or virtual producti on. Labs has a range of tools to help opti mize and export your sims to textures, fb x, csv, etc. 

Vertex Animati on Textures - The Vertex Animati on Textures ROP will export a mesh and textures to be used with a realti me material that can playback complex animati ons for cloth, rigid body destructi on, fl uids and parti cles. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/93544df7574912200f99a4481c0013efd8ddb1680dbde8787e137db25f34c432.jpg)


Flipbooks Texture - Fast GL or Karma based creati on and preview of texture atlases for Pyro FX. 

Destructi on Cleanup - Prepare rigid body simulati on results for export, reducing redundant geometry, cleaning normals, cleaning at ributes. 

Skinning Converter- Skinning Converter is a SOP that can convert any non-changing topology deforming mesh sequence into a bone based animati on. 

Make Loop - Takes a mesh, points or volume that is animated and loops them. 

Volume to Texture - The Volume Texture tool lets you write out a texture that can be used with Ryan Brucks’ volume plugin in UE4. 

Flowmap - This uti lity tool sets up a fl owmap template on your input geometry. 

Flowmap Visualize - A high quality realti me preview of a fl owmap texture in the Houdini viewport. 

Flowmap Obstacle - The fl owmap obstacle SOP allows for easy modifi cati ons on the fl owmap based on geometry. 

Niagara ROP - All-in-one HDA to extract and write out impacts, split data and interpolati on data from a bullet sim to be used with the UE4 Niagara data interface. 

Gamedev Procedural Smoke - The procedural smoke SOP will generate an animated volume to represent smoke. 

ROP Vector Field - Generate UE4 compati ble vector fi elds from volumes or point clouds. 

## MESH PROCESSING

There are a lot of steps to get quality meshes into your games - photogrammetry, topology cleanup, mesh reducti on, uv layout, baking maps. Lab tools let you simplify that process with wrapped up workfl ows and integrati ons with popular soft ware. 

AliceVision Photogrammetry - AliceVision is a Photogrammetric Computer Vision Framework which provides a 3D Reconstructi on and Camera Tracking algorithms. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/37beb8f0ac60fcde23249cfe7bc77d9a1da23ed5d3ebb9043fb2a9c5392b9f6c.jpg)


ZBrush Bridge - GoZ is Zbrush’s fast fi le transfer feature that lets you send meshes between Houdini and Zbrush seamlessly without having to deal with fi le paths or extensions. 

Delete Small Parts - Removes parts based on connecti vity and size. 

X Delight - Removes ambient lighti ng informati on found in high-res photogrammetry scans. 

GameRes - Full Pipeline Node to Take High Res Models to Low Res. 

Maps Baker - Generates textures bakes from a high resoluti on to low resoluti on model at near interacti ve speeds. 

LOD Hierarchy - Create and export an LOD Hierarchy as FBX. 

Mesh Sharpen - This tool sharpens the geometry based on the curvature found on the mesh. 

Edge Damage - This tool will add edge wear to your geometry. 

## WORLD BUILDING

Digital worlds are becoming bigger and more complex and it is important to have an efi cient world building workfl ow. Whether you want to recreate New York City, grow a dense forest or add interior details to your sci-fi adventure there are Lab tools for you. 

Physics Painter - Physics Painter is a SOP that allows users to paint physics objects onto any other object. 

Building Generator - Convert low-resoluti on blockout geometry into detailed buildings using a library of user defi ned modules. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d4ba5aabcca1e09d867bc2d508e16b4f4e9ae43b7e528dffe8e04c7d2ec189d7.jpg)


OSM Import - Open Street Map is a great database for city street data. This node efi ciently loads the OSM fi les into Houdini as well as all of the dif erent tagged at ributes on the buildings and streets. 

OSM Buildings - Generate Buildings from OSM Data. 

Tree Tools - The Tree Tools in Labs consist out of several tools that can be used together to create intricate branching structures such as trees, bushes, plants and much more. 

Cable Generator - Given a curve that represents the high ‘pin points and low ‘sag’ points of a cable, this sop will generate sagging cables, with user defi nable cable count, shape, color. 

Curve Branches- Scat ers curves over curves, with many intuiti ve controls to go from clean geometric branches to organic vines. Duplicates of this sop can be chained together for recursive growth, approximati ng the look of L-Systems but much more controllable. 

Dirt Skirt - Create a geometry ‘skirt’ where an object and ground plane intersect, to be used as a soft blend in a game engine. 

Lot Subdivision - Divide polygons into panels. Useful for city blocks or greeble. 

MapBox - Generate color, height and Open Street Map (OSM) curves using data provided by mapbox.com. 

SciFi Panels - Example HDA to generate Sci Fi Paneling. 

Snow Buildup - Adds geometry to an input mesh to mimic the build up of snow. 

Terrain Texture Output - The Terrain Texture Rop SOP renders image data from a heightfi eld. 

## MODELING

The Labs Tools includes a variety of modeling tools designed to make it easier to create game-ready geometry. 

Decal Projector - Project a decal (localized piece of geometry and a texture) onto geometry. 

Calculate Slope - Calculate the slope of a surface by comparing to a directi on, and opti onally blur and remap the result. 

Curve Sweep - Sweep a profi le along input curves, with simple controls for profi le type, width, and twist behavior. 

Extract Silhouet e - Create an outline of an object projected from one of the axes, xyz. 

## UV MAPPING

Texture UVs are a big part of creati ng game art and these tools augment Houdini’s existi ng UV toolset to make you faster and more efi cient. 

Auto UV - Automati cally generates the seams for an object and immediately runs a UV Flat en aft er the fact. 

Inside Face UVs - Create UV’s for inside faces of fractured geometry. 

UV Transfer - Transfer uv’s between a source and target geometry. 

UV Visualize - Helper script to visualize UVs. Including features such as: Visualize Seams, Warp between UV space and Model Space, Modify the ti ling of the grid texture and Visualize Islands. 

Texel Density - This tool calculates the current texel density of an asset per primiti ve based on the asset and project resoluti on. 

## INTEGRATIONS

These tools make it easier to import and export data into Houdini and out to game engines. 

Substance COP - The Substance Plugin for Houdini lets you load Substance Archive fi les into Houdini in COPs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4ca5da548ef36adbd4fd76cc538a304d143de230dece3df9c3564f9b87ea852d.jpg)


Rizom UV- The RizomUV Bridge is a set of 4 dif erent SOPs that facilitate the communicati on between Houdini and RizomUV. 

Quad Remesher - The QuadRemesher node is a wrapper around Exoside’s QuadRemesher command line interface. 

Instant Meshes - Reads in DDS (DirectDraw Surface) Files. 

Sketchfab - Uploads geometry to Sketchfab. 

3D Facebook Image - Quickly render a 3D scene to a 2.5D image that can be uploaded to Facebook. 

Marmoset ROP- The Marmoset ROP allows you to quickly generate an mview inside Houdini. 

Gaea Tor Processor - The Gaea Tor Processor allows you to load up build .TOR fi les made in Gaea. 

## UX

Some Labs tools are specifi cally designed to enhance the user experience for arti sts working with Houdini. 

Crash Recovery - Found under the File> menu, this functi onality allows for quick recovery from an unfortunate crashed fi le. 

Network Paint - Allows for colorful annotati ons of the network by simply drawing in the network editor. 

Sti cker Placer - Helpful for annotati ng networks by placing numbers, icons and user-created graphics. 

External Script Editor - Sets up a live connecti on with an external IDE when working with VEX, Python, OpenCL and expressions. 

## AND MUCH MORE...

More Tools are being added on a regular basis. Go to SideFX.com/labs 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/98647e4a36a8bea49d06402ed7eb7ff6beed240d6d0a85a5a4bd10a7d5dd7085.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2872a955ab418a0d7f4ff62b75f2f92a70e8ef71d21eb8ba4b096d16e14c2f5f.jpg)


## File Management

Understanding how to manage all of the files you create while working with Houdini is very important to your success as an artist. A typical scene file can have outside dependencies on disk and managing these is important especially if you are moving your files to a diferent computer. 

## PROJECT DIRECTORIES

While Houdini can work with files scatered all over your hard drive, this will make it harder to share your work and manage file dependencies. It is beter to set up project directories using File > New Project or use File > Set Project to choose an existing project directory as the home base for your work. This will make it easier to set up local dependencies with respect to all of the required project files. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e5dfe29d786a92cbc70566b0acea6997849ffddfd249ccbe1bc5cc8be45f1b5e.jpg)


## SCENE FILES | .HIP

The main file type when working with Houdini is the .hip file. This file contains all your nodes and networks and is the file type used when you save your work. 

Show sequences as one entry 

File soccerball_02.hip 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8296edd810a5199ec564b2a8f19bd599c124fbd772ed402e3d4565d96995e4dd.jpg)


Show files matching *. hip,*. hiplc,*. hipnc,*.1 

## UNIVERSAL SCENE DESCRIPTION | USD

In Houdini, the Solaris lighting and lookdev environment works with USD [Universal Scene Description] which is an open source initiative created by PIXAR. In Solaris, USD is native and you can use procedural nodes to manage references, payloads, layers, collections, variants and level of detail. 

## HOUDINI DIGITAL ASSETS | .HDA

You can also encapsulate then save out Houdini networks into Houdini Digital Asset or .hda files. Parameters from inside the asset can then be promoted to the top level to create a custom UI for the asset. These files can be easily shared with other artists and provide a robust referencing architecture as your assets evolve through the life cycle of a project. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0354edb9dd1af608a2a541f56245a2e413aadfdd40aa0eb7bd317a339e1b0883.jpg)


To create and load assets you can use the Asset menu. You can also manage assets loaded into your scene using the Asset Manager found on that menu. If you have two HDA files loaded into your scene that have the same name, Houdini will choose one of them based on rules set up in the manager. Changes made to an asset definition in an HDA file will be automatically pulled into scenes that reference that file. Note that older Digital Asset files may have a .otl extension which will work exactly the same as .hda files. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8c8a0a453c36e1b7fb60df39f4a55573c4ea08e917ddefb10eaa3205fe648019.jpg)


## APPRENTICE AND INDIE FILES

Houdini Apprentice and Houdini Indie use diferent file types that cannot be opened in a commercial version of Houdini. Apprentice uses .hipnc (non-commercial) for scenes and .hdanc files for assets and Indie uses .hiplc (limited commercial) for scenes and .hdalc files for assets. 

Show sequences as one entry 

File indie_file.hiplc 

Show files matching *.hip,*. hiplc,*.hipnc,*. 

## BACKING UP YOUR WORK

By default, Houdini creates a numbered backup of your scene files and Digital Asset files every time you save. This gives you a file to go back to if you want to review an early iteration or if something happens to your working file. You can also set up Houdini to AutoSave in the Edit > Preferences > Save and Load Options. Just remember that all those backup files take up disk space and you will want to clear them from time to time. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/623d0bdcb38750ca1c388d5a85fde111d41e68ee1dcc58e1ab6ea3abb454e1d7.jpg)


## FILE SOP

When you import geometry into Houdini using File > Import > Geometry it puts down a File node at the geometry (SOP) level. This file maintains a connection to the file on disk and changes made to that file will also update in your Houdini scene. If you want to break this connection then you would need to lock the File node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/098ba0104a4b96b312e4e7d35bac94ca8069acc8aad326d06d88f19540e2636b.jpg)


## FILE DEPENDENCIES [$HIP/$JOB]

When you work with nodes that reference files on disk such as geometry or texture files, the path you use will determine what happens if you move the project directory to another computer or to the cloud. A direct path will break if you move the files therefore you should either use $HIP which uses the scene file as the “home base” for the path or $JOB which uses the project directory. You can use Render > Preflight Scene to check to make sure that your scene file is set up properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5c8fd3fa99f4c6a0acf27159cba59225af6702c7d104fbd1a77de7908767c975.jpg)


## DISK SPACE MANAGEMENT

Large scene files, backup files and large simulations can take up lots of disk space. Be sure that you are not filling up too much space on your computer which could lead to instability issues. Try to use external drives to save out the largest files and leave the main disk on your computer with enough space to accomplish your day-to-day work. 

## INTEROPERABILITY

To import and export from Houdini, there are a wide variety of file formats that you can use. Here is a list of some of the main formats you will work with in a typical Houdini pipeline. 

Houdini Files - Here are some file formats, other than .hip and .hda that work exclusively in Houdini. 

.bgeo - This format saves geometry along with related atributes such as UVs, velocity and normals. Animations and simulations can be saved out as numbered bgeo files to save out motion. A bgeo.gz file is a compressed version of this format. 

.sim - These files let you save out simulation data to cache the sim to disk. Some people use these files while others use .bgeos to cache sims. 

.ifd - This is a scene description format that is created when rendering to Mantra. Typically these are created while rendering in Houdini but sometimes they are saved to disk to be rendered by Mantra directly. 

.pic - This is an image file format that was used by Houdini in the past. It was replaced as the default format by the open source EXR. 

.rat - This image format is ideal for texture maps being rendered in Mantra. All textures get converted to this format anyway so it speeds up rendering to convert to this format using Mplay. 

Image Formats - These industry-standard formats are used to render out shots and for texture maps. 

.exr - OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial Light & Magic that is now the default format for saving out renderings from Houdini. 

.jpg/.png - These formats are used to publish images to the web .tga/.tif - These formats are often used to texture map video games. 

Geometry Formats - When importing and exporting geometry, these formats are the most popular. 

.usd - This is the format used in Solaris/LOPS and provides an open source interchange format for sharing with other applications. 

.abc - Alembic is an open computer graphics interchange framework. .fbx - This format owned by Autodesk is popular when exchanging data with game engines and other 3D applications. It can hold geometry, rigging, motion and shader information. 

.obj - This is an simple geometry format originally created by Wavefront. 

## PREFLIGHT PANEL

From the Render menu, select Preflight Scene to evaluate your scene setup. 

Referenced Files - The preflight panel can either reference $HIP or $JOB when verifying file references for your scene file. 

Greenlit Reference - If the reference is relative to either $HIP or $JOB then it will be displayed in green to indicate it is working. 

Incorrect Reference - If a file reference is a direct path and not relative to $HIP or $JOB then it will be displayed in red and will need to get fixed before sharing your project with other artists or on the cloud. 

Edit Expression - Click on any file name then on the right click on the expression to open up the edit expression window. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/52c77eb967e097b4db5e64eed5d1139453887e238d1a2e1dddfd1829f0490f3f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d3040b8ec6ef7ba4e133643dc64f9b2b431cbbeef2824497049772402e43a8fe.jpg)


# Expressions & Scripting

Houdini is a production-level solution which means that scripting will play an important role in your work. Artists can usually get by with simply writing expressions while technical directors will spend more time using these techniques. Houdini includes support for Hscript, Python and VEX. 

## HSCRIPT EXPRESSIONS

HScript is designed to be a fast and concise way to retrieve and manipulate information that can be used to write expressions. An expression is typically any value that is not either a simple string or number. This can be something as simple as a variable, a math equation or an expression function. 

Rotate360*ch("tx") 

Translate .333 Rotate 119.88 

You can enter expressions directly into a parameter by simply typing into a field. When you press Enter the field highlights in green. You can click on the parameter name to toggle back and forth between the expression and the result of the expression. 

If you are creating channel references then you can RMB-click on a parameter and choose Copy Parameter then go to the parameter you want to link it to and choose Paste Relative References. 

You can also achieve this by RMB clicking on the second parameter then choosing Reference > Scene Data. This opens up a panel where you can choose data from other objects and nodes and an expression will be built for you. This method can even set expressions on multiple parameters. 

## EXPRESSION EDITOR

Depending on the complexity of your function, or the type of parameter, you may instead choose to use the Expression Editor. The expression editor can be opened by RMB-clicking on a parameter and selecting Expression > Edit Expression, or by placing the mouse over the parameter and pressing Alt - E. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab6f93aedb0cdd1c853be934e83c6f4d8287fc8f5deff546053641ca9814caef.jpg)


## PYTHON

Python is a popular scripting language that is well known in the CG industry that supports integration and standardization. This makes it perfect for tool development. 

Python in Houdini is built on the Houdini Object Model (HOM) which is an API that lets you get information from and control Houdini using the Python scripting language. In 

Python, the <sub>hou</sub> package is the top of a hierarchy of modules, functions, and classes that define the HOM. The <sub>hou</sub> module is automatically imported when you are writing expressions in the parameter editor and in the hython command-line shell. 

You can also use it to write expressions in Houdini. To do this, change the expression language option at the top of the parameter pane for the node. 

Geometry box_object1 

Transform Render Misc 

There is also a Python Shell Panel which you can use to enter Python commands. You can also import the  module into a regular Python shell to integrate Houdini into your existing Python-based scripts. 

## TOOL SHELVES

The shelf tools are also set up using Python. You can see this code by RMB-clicking on any shelf tool and choosing Edit Tool. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/63ad2bda595e392ce252043e48d77044988a4a3258ffa79b2fe748d04795812d.jpg)


kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5) sphere = soptoolutils.genericTool(kwargs, 'box') sphere.parm("type").set("polymesh") sphere.parm("divratel").set(2) sphere.parm("divrate2").set(2) sphere.parm("divrate3").set(2) 

## PYSIDE/PYQT

The Python Panel Editor pane lets you create, edit and delete PySide2 or PyQt5 interfaces. The editor also lets you manage the entries in the Python Panel interfaces menu as well as the entries in the Houdini pane tab menu. The panel comes with some sample code that you can try out for yourself. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/201d0ec267b2bb6cce12157a91b2506bb265534b88adc96ff042a120ca276e66.jpg)


## PYTHON STATES

You can also write viewer states in Python that let you customize user interaction in the viewport for your node. You can use these to build more artist friendly interfaces for tools and you can refer to the documentation for more detailed info. 

## VEX

VEX is a high-performance expression language used in many places in Houdini, such as writing shaders. VEX evaluation is typically very eficient, giving performance close to compiled C/C++ code. 

VEX is not an alternative to scripting, but rather a smaller, more eficient general purpose language for writing shaders and custom nodes. VEX is loosely based on the C language, but takes ideas from C++ as well as the RenderMan shading language. 

VEX is used in several places in Houdini: 

Modeling – The VEX SOP allows you to write a custom surface node that manipulates point atributes. This can move points around, adjust velocities, change colors. As well, you can group points or do many other useful tasks. 

Rendering – Karma and Mantra use VEX for shading computation. This includes light, surface, displacement and fog shaders. 

Compositing – The VEX Generator and VEX Filter COPs allows you to write complex custom COPs in VEX. The expressions evaluate very close to C/C++ speeds and run 1000’s of times faster than the Pixel Expression COP. 

CHOPs – The VEX CHOP lets you create custom CHOPs. The CHOP functions can manipulate arbitrary numbers of input channels and process channel data in arbitrary ways. In some cases, the VEX code can run faster than compiled C++ code. 

Fur – Procedural fur behavior is implemented with VEX. 

## VOPS

If you want to use VEX but don’t want to write the code then you can use the VOP context to use a node-based interface. You can do this in the SOP context using an Atribute VOP node that lets you dive in and use VOPs to create VEX code. You can take input geometry and manipulate it. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1a1652abae174848a77278d55567f88973a88c46ab4cafb617a502405df92288.jpg)


You can use parameter vops to build interface element such as float sliders that are then available at the SOP level. This way you can execute the VEX code without diving back down to the VOP level. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/75f8b0598b59a6bdf174ce0eb5c326ee4698741d9d704443c85554676ce17a90.jpg)


The VOPs context is designed to give artists an interactive way of creating VEX code. For people with a scripting background, it might make more sense to write the code directly into a Wrangle node. 

## WRANGLE NODES

You can also use a wrangle node such as the Atribute Wrangle which provides a low-level node that lets coders who are familiar with VEX tweak atributes. There are also wrangle nodes for working with channels, volumes and deformations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/591b50f0bcb9ada7ac00e328339654695d0758a5f8008307732f51114909896c.jpg)


If you are interested in learning how to work with wrangle nodes, you should take a look at Entagma.com where you will find lots of great tutorials that generally take a more technical approach to creating content but with an artist’s mindset. 

## COMPILE BLOCKS

In geometry networks [SOPs], you can put a part of the network inside a compiled block that makes it function as eficiently as if you had writen code. This imposes a number of restrictions on how the network can work, but can potentially deliver big benefits in the right circumstances. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/af9884aabdf8cc34f455bc62d113bd65bbb21abab70acb39a2d01a3e57525919.jpg)


## HOUDINI DEVELOPERS KIT | HDK

An even deeper way to work with Houdini is to use the HDK which is the same comprehensive set of C++ libraries that SideFX programmers use to develop the Houdini family of products. With the HDK, you can create plug-ins which customize diferent areas in the Houdini interface. Here are some examples of what you can do with the development kit: 

 Add custom expression functions 

 Add custom commands (hscript or HOM) 

 Add custom operators (SOPs, COPs, DOPs, VOPs, ROPs, CHOPs, and even Objects) 

 Add output nodes to support a non-standard Renderer 

 Add custom lighting or atmospheric efects to the renderer 

To learn more about working with the HDK, go to the SideFX website and choose Support > Documentation > HDK. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fa204b78d55f823caf7475ba77418b71de9f2171bf83339ffe094ee0b42ec132.jpg)


With the Task Operators or TOPs, you can organize and schedule tasks then distribute them intelligently to your compute farm. This allows for parallel processing of data while maintaining a dependency graph that shows how each task relates to proceeding tasks. 

## PROCEDURAL DEPENDENCY GRAPH

TOPs is a network type in Houdini built using the Procedural Dependency Graph, a technology which makes it possible to describe complex dependencies visually with nodes, then generate a set of acti onable tasks which can be distributed to a compute farm with the help of a scheduler. Once you evaluate the results, it is possible to make changes to parts of the graph without re-cooking the whole network. 

## TOP NODES

Task or TOP nodes let you manage pipeline tasks with the ulti mate goal of parallelizing the processing and distributi on of each task. As a TOP node generates a task, the task is displayed as a dot. Once the task is cooked then new tasks can be executed on this node and on children TOP nodes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d96b9a9bd156310f655e6b86d35a6dfd57fcb23fd0a95a8a3807dd561f9173de.jpg)


## SCHEDULERS

Scheduler nodes take tasks that have met required dependencies and assigns compute resources. As each task is completed, the scheduler informs the task graph, which in turn informs the PDG graph to move on to the next available task. PDG supports industry-standard schedulers such as HQueue, Deadline, Tractor, or any scheduler plugged in with Python. 

## COOKING TOP NODES

Once you wire together a task graph, you will want to cook the nodes. You can either cook a node in the middle of the graph or cook the output node at the end of the chain. 

 Cook Selected Node Shift -G 

 Dirty and Cook Selected Node Shift -V 

## Tasks ×00244 8 running  41 waiting

Use the Task Bar to monitor your progress. On the TOP nodes, you can RMB-click on a task dot and choose to Cook or Dirty the task. When you dirty a task, it means that if you recook the network those tasks will be recomputed. Clean tasks will not be recooked which is one of the benefi ts of TOPs because you don’t have to redo work that is already completed. 

## DEPENDENCIES

When you click on a task dot in the graph, you will see a thin line that connects to upstream tasks it is dependent on and downstream tasks that depend on it. 

If there are changes upstream then tasks may be automati cally dirti ed and this will in turn dirty tasks downstream where there are dependencies. This process is an important part of how PDG graphs work as an ef ecti ve pipeline tool. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4880ab2c50a1161b4787204f42ff52af1e4dd7d46ffd058b77d184faf5b9c4f4.jpg)


## TOP NODE

Input - The node takes the informati on feeding into the Input and breaks it into one task for every piece of data. 

Progress Wheel - The progress wheel shows you how many tasks are completed, how many are in progress and how many are in the queue. 

TOP Node - This is the node that is currently being cooked. It contains the instructi ons for the tasks being executed. You can RMB-click on the node for a menu of supporti ng acti ons. 

Tasks - Each task is represented by a small dot. The coloring indicates their current status and you can RMB-click on a task dot to learn more about that one part of the graph. 

Output - Once tasks are completed, the output passes the results on to the next node even if other tasks on this node are sti ll acti ve. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/70acd203ec98d1a23b10f2b035c5e4b156866e706e00508c16ea6f9c0b8cfbfd.jpg)


## TASK GRAPH TABLE

If you RMB-click on a node, you can choose to Open Task Graph Table. This gives you an itemized list of tasks along with information such as index, state, cook time and priority. Clicking on items in this window will highlight the task dot on the node in the Network view. 

<table><tr><td>Node Name *</td><td>Name</td><td>Index</td><td>State</td><td>Cook Time</td><td>Output Size</td><td>ldaparms_string</td><td>hdaparms_floats</td><td>writeoutput</td><td>hdasopnar</td></tr><tr><td>create..fetch1</td><td>create..fch1_1</td><td>51</td><td>Cooked</td><td>5.50952</td><td>45.6KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_1</td><td>38</td><td>Cooked</td><td>5.483</td><td>54.3KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_2</td><td>17</td><td>Cooked</td><td>5.48691</td><td>31.4KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_3</td><td>69</td><td>Scheduled</td><td>-1</td><td>0.0B</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_4</td><td>39</td><td>Cooked</td><td>5.68467</td><td>18.5KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_5</td><td>27</td><td>Cooked</td><td>5.9889</td><td>23.1KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_6</td><td>47</td><td>Cooked</td><td>5.49376</td><td>65.6KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_7</td><td>23</td><td>Cooked</td><td>5.54583</td><td>24.8KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_8</td><td>70</td><td>Cooked</td><td>5.50042</td><td>34.1KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_9</td><td>63</td><td>Scheduled</td><td>-1</td><td>0.0B</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_10</td><td>10</td><td>Cooked</td><td>5.48014</td><td>24.4KB</td><td>file</td><td>t</td><td>1</td><td></td></tr><tr><td>create..fetch1</td><td>create..1_1_11</td><td>12</td><td>Cooked</td><td>5.49007</td><td>29.4KB</td><td>file</td><td>t</td><td>1</td><td></td></tr></table>

## IMPORT/EXPORT DATA

To get data into the TOP graph, there are a number of diferent options giving you access to geometry, images, scripts and other kinds of data. Houdini Digital Assets can be used to apply procedural networks or you can connect with other parts of Houdini to import and export data. 

## WEDGE NODE

A key workflow in PDG is wedging that lets you quickly create multiple iterations of a design. You can then process all of the diferent options through the TOP graph then collect them at the end for final output. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ba769b81a77a9d30630b440bb1027b60c5fe1588457223e8d715cb1ef8483b92.jpg)


## OUTPUT IMAGE MOSAICS AND MOVIES

In TOPS, you can interface with ImageMagik to create a contact sheet that can be used to evaluate design iterations to make the best choice or to generate prop variations to richly populate your scene. You can use an overlay to pull info from the network to help you make the best decision. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9c7d8e24c8bb06e444755aa821cb68ff69346f2256c79d00c01028d09c82cf38.jpg)


## INTEGRATIONS WITH OTHER APPS

TOPs includes nodes for working with other applications such as Shotgun or Autodesk Maya. This allows your network to extend beyond Houdini to help with all parts of the pipeline. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a3aca3966040985d16020a41619eb0b197845a353645ecd6c5c9c68bd4fed3c6.jpg)


## PILOT PDG APPLICATION

While TOP networks can be set up and executed from within Houdini, wranglers who are managing the farm or pipeline TDs who are exclusively creating TOP networks can use PilotPDG. Tasks that are Houdini-related will call on Houdini Engine to work non-graphically to complete the task. 

## TOP NETWORK

This network type lets you manage and view the network being processed. 

Task Bar- The task bar lets you start and stop a network and monitor its progress. 

Scheduler- The scheduler node determines where your data is being processed and how many nodes are participating. 

Completed Tasks - When a node is finished processing all its tasks, a check mark appears. 

In Progress Tasks - While in progress, you can see which tasks still need to be completed. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fc6f091370680c93c61c423cdde2c83a9155eb65f9950afbcbac83db9742eb01.jpg)


Network Path- This shows you the path to the TOP network where the graph is set up. 

TOP Menu- This menu includes a range of options for organizing and processing a TOP network. 

Progress Bar - This bar lets you see the progress of the overall network tasks. 

TOP nodes - These nodes are where specific commands are turned into tasks and sent by the scheduler to be completed. 

Dependency Line - You can click on a task to see how it connects to other tasks in the network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0e7e303033f755a7b55c09e154373a0ecdd5dc968c5dc214a7fb1840f4d72781.jpg)


# HOUDINI DIGITAL ASSETS Procedural Tool Building

Networks of nodes give Houdini its procedural nature and defi ne a recipe that can be applied over and over. Houdini Digital Assets let you wrap up these networks to create custom tools and smart assets. These arti st-built tools can be used repeatedly to increase producti vity across your studio. 

One of the things that Houdini’s node-based workfl ow is great at is allowing arti sts to avoid repeti ti ve steps and to generate multi ple iterati ons by making changes to an existi ng network of nodes. This lets you achieve results that are unique without starti ng the whole process from scratch. 

Houdini Digital Assets take this one step further by leti ng you encapsulate a network or collecti on of networks into a single node with parameters that have been promoted to the top level. This node is then saved to disk which creates a shareable fi le that other arti sts can load into their scenes. 

## ARTIST BUILT TOOLS

The process of creati ng a Houdini Digital Asset works with the interacti ve tools in Houdini. You build a high level interface by dragging parameters from nodes to an asset properti es panel which allows you to create custom tools without writi ng any code. This means that technical arti sts can build custom tools then deploy them quickly to colleagues. 

A Houdini Digital Asset might be a procedural prop such as a staircase or a piece of furniture, a visual ef ect such as an explosion, or a more generalized tool such as a populate tool for scat ering objects over a surface. Whether you are creati ng content specifi cally for your current project or building a larger toolset for all your projects, your arti sts can build a collecti on of Houdini Digital Assets to meet your producti on needs. 

## PIPELINE FRIENDLY

When a Houdini Digital Asset is loaded into a scene fi le, it references the .hda fi le on disk. This means that changes made to the asset will be picked up automati cally by everyone who is referencing that fi le. 

This makes it very easy to deploy updates throughout your pipeline. Now arti sts can point to a single asset on disk knowing that once it gets updated with the most current iterati on, they will immediately have access. 

Houdini Digital Asset fi les can also hold more than just the asset defi niti on. You can store images, geometry fi les and scripts that are used by the asset. This ensures that all the relevant parts are available when other people work with the asset. 

## CONTENT LIBRARY & ORBOLT

The Content Library is an online asset repository which hosts 2D and 3D assets, from complete scene fi les, to fully-rigged props, to render-ready visual ef ects, animatable characters, game assets and more. Go to Get > Content Library on the SideFX website to access it. 

Orbolt an online asset marketplace that of ers a wide variety of digital assets. There is a panel in Houdini where Orbolt assets you download or purchase can be stored and made available as you work. 

## CREATING DIGITAL ASSETS

1 Create nodes and networks in Houdini 

2 Package up the networks to be saved out as a Houdini Digital Asset [.hda] fi le that can be shared with other arti sts. 

Build an interface for your asset by promoti ng parameters and handles to the top level of the asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/546d75f6d0f25ec41b84ef8b5ea42e320f18816e06e1d03a5ecc8a08dbdf4e04.jpg)


SAVE AS Houdini Digital Asset 

Load the .hda fi le back into Houdini to use the asset. Only those parameters promoted to the asset level can be used. All others are locked. 

You can use the asset in any number of Houdini scenes. If you make changes to the HDA fi le then all other assets can be easily synced to the changes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5e07bff640975648198430b1083a77abef4aa6a938592a8a151bcea6f1b22e9f.jpg)


Houdini Engine brings a procedural node-based approach to your favorite app. This technology lets you share Houdini Digital Assets with colleagues who can load them directly into 3D apps such as Autodesk<sup>®</sup> Maya<sup>®</sup> or 3DS MAX<sup>®</sup> or into game editors such as Unity<sup>®</sup> or Unreal.<sup>.®</sup> 

The benefi ts of Houdini Digital Assets can be experienced by arti sts using other applicati ons thanks to the Houdini Engine plug-ins. Created with the Houdini Engine API, these plug-ins allow host applicati ons to load .hda fi les and all of the handles and controls. When parameters are set on the asset, Houdini works “under-the-hood” to cook the nodes and networks then deliver the results back to the host. 

## HOUDINI ENGINE API

This is made possible by the Houdini API which is used to create plug-ins for host applicati ons. HAPI is a fl at and small API that is easy to learn and is available on github for developers that want to create their own proprietary plug-in. 

## HOUDINI ENGINE PLUG-INS

There are a number of Houdini Engine plug-ins that arti sts can access either through the Houdini installer or online. These have been producti on tested and can be used confi dently by arti sts and studios. 

Each of the plug-ins are designed to create a bridge between the features in a typical Houdini asset and the nature of the host applicati on. For instance a cloud asset that use volumes would work fi ne in Maya but would not make sense in Unity or Unreal where volumes are not supported. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/834aa66440313df3cfca0fa1105e16663baacc0fd59389726e4f2afbf7d8beb5.jpg)



A Houdini Digital Asset loaded into Autodesk Maya using the Houdini Engine


Plug-ins that work with FREE Houdini Engine for Unity/Unrea or FREE Houdini Engine Indie licenses: 

 Unreal 

 Unity 

Plug-ins that work with Houdini Engine licenses or FREE Houdini Engine Indie licenses: 

 Autodesk Maya 

 Autodesk 3DS Max 

 Proprietary Plug-ins 

## HOUDINI ENGINE PIPELINE

1 Load the .hda fi le into a host applicati on using the Houdini Engine plug-in. 

2 The Host Applicati on accepts the asset and interfaces with the Houdini Engine. 

3 The Houdini Engine calls on the Houdini library fi les to “cook” the nodes and network inside the asset. 

4 <sup>When</sup> <sup>an</sup> <sup>asset</sup> <sup>is</sup> <sup>loaded</sup> <sup>or</sup> <sup>a</sup> parameter is changed then the Engine grabs the Houdini libraries, cooks the nodes, then delivers the results back to the Host. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bcb31855cbf36567f27a911c435f08cc0b7590d77b2dc7624f9ddfa93c123b0f.jpg)


Host applicati ons with Houdini Engine plug-ins 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4406580b8b2ecda2ea66eccc97af56ed80007a8ce51b671d7fb07cf2f84012ef.jpg)


# FILM & TV PIPELINE Animati on and VFX

Whether you are creati ng live acti on plates enhanced with visual ef ects or full CG shots, the ulti mate goal of Film and TV projects is moving pictures. These pictures are created using assets such as characters, sets and ef ects which all come together in a fi nal compositi on. 

Houdini is a full featured package that contributes to all stages of a Film & TV pipeline. From modeling to rendering to animati on and fi nal compositi ng, Houdini has procedural tools that support your creati ve process. Over the years, VFX is one area where Houdini is known as an industry standard. SideFX has been honored with several Scienti fi c and Technical Achievement awards including an ACADEMY AWARD OF MERIT Oscar. 

Other areas such as procedural modeling, lighti ng or character work conti nue to get stronger to the point where a growing request from studios is more skilled Houdini arti sts. 

## HOUDINI CORE / HOUDINI FX

There are two commercial versions of Houdini that you use in your pipeline. Houdini Core covers all of Houdini’s tools except for DOPS, and Houdini FX has a full toolset. Scenes and VFX created in Houdini FX can be staged, animated, lit and rendered in Houdini Core. This gives you a robust pipeline with Houdini FX licenses for your FX arti sts and Houdini Core licenses for everyone else. 

One soluti on is for senior technical directors to use Houdini FX to solve a parti cular producti on challenge then wrap up the resulti ng nodes and networks into Houdini Digital Assets. An arti st-friendly UI is then built to support the animators and VFX arti sts who can then use the more cost ef ecti ve Houdini Core to execute shots. 

## INTEROPERABILITY

Most studios are equipped with a variety of 3D applicati ons to each handle a dif erent part of the pipeline. Houdini has a lot of strong interoperability tools to allow for this interchange of data. Whether they are using USD, Alembic, FBX or EXR, your arti sts can easily work back and forth with a wide variety of DCC applicati ons. They can also use the Houdini Engine plug-ins to bring the Houdini Digital Assets into other applicati ons, such as Autodesk<sup>®</sup> Maya<sup>®</sup> or 3DS MAX,<sup>®</sup> while maintaining the asset’s procedural controls. 

Smaller studios may want to avoid extensive fi le exchange, especially with ti ght deadlines, therefore Houdini provides a full featured procedural “pipeline-in-a-box” that can take you through all of the stages under one roof. 

## DISTRIBUTED RENDERS AND SIMS

Rendering images and simulati ng VFX can be ti me consuming, especially as you aspire towards photorealisti c results. For this reason, Houdini lets you distribute both rendering and simulati on tasks to a compute farm using Houdini Engine in Batch mode. 

Distributed simulati ons allow you to work faster or to handle ef ects that would max out the memory on any one computer. By slicing the sim and distributi ng it, memory is managed without compromising the fi nal result. Studios should defi nitely consider using Houdini Engine to simulate on the farm. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/da49d79bdcfa37f23b383347465719b40d12648f39769274ee71edfd38dc3c85.jpg)


# GAMEDEV & VR PIPELINE Interacti ve Experiences

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c865adf7ca5161b4ac22dc3d7636ca3a819334d936b5b565a442a27dff845ca3.jpg)


In Video Game and Virtual Reality projects, the main focus is creati ng interacti ve 3D worlds built using content that is highly opti mized for a smooth gameplay experience. This creates a dif erent kind of pipeline compared to rendered out game cinemati cs which are more like fi lm. 

At the core of a games pipeline is a game engine like Unreal or Unity. The engine is where the game art and the game interacti ons are put together to create a playable experience. Houdini can be used by game arti sts to create terrain, design and populate levels, build procedural models, build and animate characters and create Realti me FX such as fi re, fl uids and destructi on. 

## EXPORTING TO GAME ENGINES

There are two ways of geti ng content from Houdini to a game engine. The traditi onal approach is to export out to a format like FBX or OBJ and import this into the engine. You would create procedural systems in Houdini then fl at en out the results. 

## The second approach is to create Houdini Digital

Assets and load these into the game engines using the Houdini Engine plug-ins for Unreal and Unity. These assets import into the game editor with their parameters and controls intact. You can therefore make changes inside the game editor and the Houdini Engine works in the background to update the artwork. 

This proceduralism is available to game arti sts inside the editor then when the game is compiled the artwork is baked down. The Houdini Engine is not a runti me soluti on and you cannot access it as part of the gameplay. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/de59f2a34f41636e6294200fc9f7c58719beb7c513d5a2aa474414926e186bce.jpg)



Houdini Digital Assets loaded into Unreal using the Houdini Engine


## REALTIME FX

Houdini is known for VFX and it is a great tool for creati ng FX for games. But these FX need to be opti mized using techniques such as texture sheets, fl owmaps and vertex animati on textures. This way the footprint for the ef ect is as light as possible and does not take away from the frames per second of the game. The SideFX Labs Tools menti oned earlier in this document have been designed to support these kinds of workfl ows. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e9cbd17baeca6bec9b290f4bf63eb6b0028f0cb7f5cafe0f96162e37b0d56735.jpg)


# Products & Licensing

As you begin working with Houdini, it is useful to understand what Houdini products are available for you to work with. Whether you are a large studio, small studio or a team of indies just geting started, there are diferent Houdini products to suit your needs. There are also versions of Houdini for school labs and for students who want to learn for free. 

## COMMERCIAL LICENSES

Houdini Core – Designed for modelers, lighters, character riggers, animators and game artists, Houdini Core also includes features such as compositing and motion editing. Scenes created in Houdini FX can be opened and rendered in Houdini Core which makes it an ideal lighting tool for your VFX. 

Houdini FX – Houdini FX has all the tools found in Houdini Core but adds particle and dynamic simulation tools. With its procedural workflow, Houdini FX lets you create fluids, Pyro FX, grains, cloth, hair & fur, crowds and soft body efects. 

Houdini Engine – Houdini Engine gives you command-line access to run in batch mode to batch process renderings and distributed dynamic simulations. Houdini Engine also lets you load Houdini Digital Assets into other digital content creation applications, such as Autodesk<sup>®</sup> Maya,<sup>®</sup> Autodesk<sup>®</sup> 3DS MAX,<sup>®</sup> Unity<sup>®</sup> or Unreal.<sup>®</sup> 

## INDIE LICENSES

Houdini Indie – Houdini Indie makes all of Houdini’s animation and VFX tools available under a limited commercial [less than $100K USD] license to animators and game makers who want to use Houdini during the incubation stage of their business. 

Houdini Engine Indie – Your Houdini Engine Indie license can be used to run Houdini Indie in batch mode or to load Houdini Digital Assets into other content creation apps. 

## LEARNING LICENSES

Houdini Education – Houdini Education is a full-featured version of Houdini FX designed for use by schools and training centers as well as students. Houdini Education will also open files created by using Houdini Apprentice. 

Houdini Apprentice – Houdini Apprentice is a free version of Houdini FX which can be used by students, artists and hobbyists to create personal non-commercial projects. With Houdini Apprentice, you have access to virtually all of the features of the award-winning Houdini FX to develop your skills and work on personal projects. Apprentice lets you save to disk and render out with a word mark. 

Note: Scene files and Assets created in Indie, Apprentice or Education cannot be used in commercial Houdini. The file formats are diferent and the EULA [End User License Agreement] prevents you from sharing files between diferent license types. 

## LICENSE TYPES

Workstation [Node-Locked] – This license type can be used on a single computer and can only be accessed either from a local server or from SideFX.com. 

Local/Global Access [Floating] – These licenses can be set up on a server and shared with a team of artists. When an artist starts Houdini a license is checked out of the server as long as there is one available. Local licenses are designed for a single studio and global licenses are for sharing between studios in diferent locations. 

## INSTALLING LICENSES

Once you have acquired a license, you will install it by opening up the Houdini License Administrator [hkey] application. From there you can choose File > Install Licenses. You will be asked for a log in and a password that will match the ones you set up on the SideFX.com website. 

You can now use sidefx.com as the license server instead of installing locally. To use Login licensing, you need to be constantly logged in with your sidefx account. You can login using diferent computers but only one of them can be used at a time. This approach is ideal for Indie and Education users. 

Local and Global Access licenses can be installed using this method on a central server. You will then need to make that server available to anyone who needs access to the licenses. 

You can also view your licenses on the SideFX.com website by clicking on your avatar in the top right and choosing Services. You can then click on the Manage Licenses link. 

## ANNUAL UPGRADE PLAN

For visual efects studios, games studios and 3D artists who want to maximize their investment in Houdini, the Annual Upgrade Plan provides key advantages such as productionlevel technical support and access to full and dot releases containing the latest software enhancements as well as daily builds containing bug fixes. 

## SIDEFX SUPPORT

All customers including Apprentice customers can contact SideFX using our email support system to discuss installation and licensing issues. After that, only Annual Upgrade Plan and Commercial Rental Customers may contact our support team to discuss more in depth production issues. 

Our Support Specialists can be contacted directly via support@sidefx.com . Be sure to include the following information in your email: 

 Your Operating system [Windows XP, etc.] 

 Version and Build Number of Houdini 

Summary of the installation issue and a diagnostic file if you are having a licensing issue. 

To learn about support programs visit SideFX.com/support. 

## Comparison Chart

<table><tr><td></td><td colspan="2">COMMERCIAL</td><td>INDIE</td><td colspan="2">LEARNING</td></tr><tr><td>PRODUCT</td><td>HOUDINI FX</td><td>HOUDINI CORE</td><td>HOUDINI INDIE</td><td>EDUCATION</td><td>APPRENTICE</td></tr><tr><td>INTENDED USER PRICING</td><td colspan="2">Studios | Commercial Artists Visit SideFX.com</td><td>Indies | Freelancers $269 USD per year</td><td>Schools | Students $75 USD per year</td><td>Hobbyists FREE</td></tr><tr><td>Operating System</td><td colspan="5">Windows, LINUX, Mac OSX</td></tr><tr><td>Modeling</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Character</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Animation</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Solaris: Layout Tools</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Solaris: Lookdev and Lighting</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Karma/Mantra Rendering</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Terrain</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Compositing</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Volumes</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Pyro FX</td><td>√</td><td>Simple Fireball</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Fluids</td><td>√</td><td>Simple Flip</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Rigid Bodies</td><td>√</td><td>Simple Fracture</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Particles</td><td>√</td><td>-</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Vellum Cloth</td><td>√</td><td>Simple Cloth</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Wire Dynamics</td><td>√</td><td>-</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Crowds</td><td>√</td><td>-</td><td>√</td><td>√</td><td>√</td></tr><tr><td>LICENSING</td><td colspan="2">Commercial</td><td>Limited Commercial</td><td colspan="2">Non-Commercial</td></tr><tr><td>Workstation [Node-Locked]</td><td>√</td><td>√</td><td>√</td><td>-</td><td>√</td></tr><tr><td>Local/Global Access [Floating]</td><td>√</td><td>√</td><td>-</td><td>√</td><td>-</td></tr><tr><td>USER INTERFACE</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>Houdini GUI Access</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Command Line Access</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>GUI Watermark</td><td>-</td><td>-</td><td>Unobtrusive</td><td>Unobtrusive</td><td>Unobtrusive</td></tr><tr><td>Plug-in Support</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>HOUDINI ENGINE</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>Houdini Engine Plug-ins</td><td>√</td><td>√</td><td>√</td><td>√</td><td>No</td></tr><tr><td>Create Assets for Engine</td><td>√</td><td>√</td><td>√</td><td>√</td><td>For Education Licenses</td></tr><tr><td>Create Assets for Orbolt</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>RENDERING</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>Karma Tokens</td><td>5 / 10*</td><td>5 / 10*</td><td>1</td><td>10</td><td>1</td></tr><tr><td>Mantra Tokens</td><td>Unlimited</td><td>Unlimited</td><td>1</td><td>10</td><td>1</td></tr><tr><td>3rd Party Rendering</td><td>√</td><td>√</td><td>√</td><td>√</td><td>No</td></tr><tr><td>Render Watermark</td><td>-</td><td>-</td><td>-</td><td>-</td><td>√</td></tr><tr><td>Resolution</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td><td>1280x720</td></tr><tr><td>SCENE</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>.hip</td><td>√</td><td>√</td><td>.hipalc</td><td>.hipanc</td><td>.hipanc</td></tr><tr><td>.hda</td><td>√</td><td>√</td><td>.hdalc</td><td>hdanc</td><td>hdanc</td></tr><tr><td>GEOMETRY</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>USD</td><td>√</td><td>√</td><td>√</td><td>√</td><td>.usdnc</td></tr><tr><td>FBX</td><td>√</td><td>√</td><td>√</td><td>√</td><td>IMPORT</td></tr><tr><td>Alembic</td><td>√</td><td>√</td><td>√</td><td>√</td><td>IMPORT</td></tr><tr><td>.bgeo</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>IMAGES</td><td colspan="2"></td><td></td><td colspan="2"></td></tr><tr><td>.pic</td><td>√</td><td>√</td><td>.piclc</td><td>√</td><td>.picnc</td></tr><tr><td>.exr</td><td>√</td><td>√</td><td>√</td><td>√</td><td>watermarked</td></tr><tr><td>.tif</td><td>√</td><td>√</td><td>√</td><td>√</td><td>watermarked</td></tr><tr><td>.png/jpg</td><td>√</td><td>√</td><td>√</td><td>√</td><td>watermarked</td></tr></table>


* Commercial Workstation Licenses come with 5 Karma Tokens and Local and Global Access Licenses come with 10 Karma tokens 


# HOUDINI FOUNDATIONS MODEL, RENDER, ANIMATE

Welcome to Houdini. In this lesson you will start from scratch to model, render, animate, and simulate a soccer ball (also known as a football in many parts of the world). You will create a classic bouncing ball animati on using the principles of squash and stretch, apply textures and materials, add lights and cameras, and explore the use of dynamics to simulate a group of soccer balls. 

These tasks will introduce you to many dif erent parts of Houdini as you create your fi rst Houdini scene, explore the interface and discover some of its most important tools. You will learn how to work interacti vely in the Scene View and how to use the Network View to manage your nodes as you refi ne your model and build your animati on rig. You will also set up materials and textures on the Solaris Stage then you will render using Houdini’s built-in renderer Karma, and fi nally create a Rigid Body Simulati on. 

## LESSON GOAL

Model, Render, Animate and Simulate a soccer ball using Houdini’s procedural node-based workfl ow 

## WHAT YOU WILL LEARN

 How to work with the View Tools 

 How to use Shelves, Radial Menus and the Tab key 

 How to create Geometry 

 How to work with Nodes and Networks 

 How to set up Custom At ributes and a For-Each Loop 

 How to set up Materials and Texture UVs 

 How to Layout a shot and render with Karma 

 How to Set Keyframes and add Moti on FX 

 How to use Rigid Body Dynamics 

## LESSON COMPATIBILITY

Writ en for the features in Houdini 19.5+ 

The steps in this lesson can be completed using the following Houdini Products: 

Houdini Core 

Houdini FX 

Houdini Indie 

Houdini Apprenti ce 

Houdini Educati on 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ea541cdfd3e0e62523cfe2a23a6a17dabdf2f867fc97536b35f6399dfd20da61.jpg)


## PART ONE Explore the Houdini UI

To get started, it is important to learn how to work with the Houdini workspace and the three panes you will use the most. The Viewport lets you create objects interacti vely, the Parameter Pane lets you edit node properti es and the Network Editor lets you work directly with the node networks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9cc9ce6e9a83863d42b0a9230d6cdbd70db529db79d6e794a981f05a0e8be3b8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/49f85486d4fffeffaf495894abddc87f963caf50cfb343462af8e20b50b974cd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d24ed8750b338ce4cba338e1513d8753746065ff5cd95c3f523dd05c62f26c66.jpg)


## PROJECT FILES

Go to the soccerball tutorial page on SideFX.com, where you likely got this document, to download the intro_lesson directory. Put it into the Houdini Projects directory which you can fi nd in either the home directory or the documents directory. 

01 Select File > Set Project. Find the intro_lesson directory that you downloaded earlier and press Accept. This makes this project directory and its sub folders the place for all the fi les associated with this shot. 

Select File > Save As... You should be looking into the new intro_lesson directory. Set the fi le name to soccerball_01.hip (or football_01.hip if you would prefer) and click Accept to save. 

02 In the viewport, press c to bring up a radial menu. From this menu, choose Create > Geometry > Box. Your cursor now shows the outline of a box waiti ng to be placed in the scene. Press Enter to place it at the origin. 

This creates a box in the Scene view, adds a node in the Network editor and shows the object parameters in the Parameter pane. As you work through this project, you will touch on all of these interface elements. 

## 03 You can now explore the View tool in Houdini. Press the following hotkeys:

 Tumble 

 Pan 

Spacebar or Alt[Opt] - LMB click-drag 

 Dolly 

Spacebar or Alt[Opt] - MMB click-drag 

Spacebar or Alt[Opt] - RMB click-drag 

In some cases, you will want to home in to get your bearings. There are some hotkeys for that as well: 

 Home Grid 

 Home All 

Spacebar -H 

 Home Selected 

Spacebar - A 

Spacebar - G 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ce4825175e6c16d8737aea2cf4bab344ca43c3593639f4940e8d54be3d28c539.jpg)


## RADIAL MENUS

One way to access tools in Houdini is radial menus which you can access using the X, C and V hotkeys. Each of these brings up a radial menu with lots of opti ons for you to choose from. The main focus of each menu is as follows: 

Snapping 

Main (or Custom) 

View 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3a5c4151835b50b8da36904365799ec991b3a404c62d00546622767a87fc8b68.jpg)


# SELECTION HOTKEYS

If you are using the Select, Move, Rotate, Scale or Handles tools, the following hotkeys will determine your selecti on mode as well as which level you will be working at. 

Objects Object Level 1 

Points Geometry Level 

Edges Geometry Level 

Primiti ves/Faces Geometry Level 

Verti ces Geometry Level 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7ae491890db18499e7b695158ae730df4d51f1a41b884241bc4266915b2150b0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2b61c0e248ec43ada6234b8832fa8ff51a6f00b9b410585d2bb60bde59a7cec1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/56e2a87b1545e4c8b10dfcde64efaebf9c6d83e8a2a6000e678e400582c86c83.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/94cd97bb5e4b62a91fdfd6b7c48934ebc7e566043c611c8e5f88ef708352a6a6.jpg)


RMB-click to access menu 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/18b07b0fbe9cdf61c3fc291eb54eb92d81c19214e0b88843c943b7a6b68bec0e.jpg)


Select Groups or Connected Geometry 9 or Pad9 

04 With the object selected, press i to go to its geometry level. Use the Shift key to drag on handles to make it longer along z axis around the origin. 

When an object is created in Houdini, there is an Object level which is where you manage the transformati ons of the object and a Geometry level where you defi ne its shape. Pressing i brought you down into the geometry level of this object. You can also get there by double-clicking on the object node in the Network editor. Later, to get back to the Object level, you will press U. 

05 Press S to go to the Select tool then 4 to access Primiti ve selecti on. Press n to select all then press c to bring up the radial menu and choose Model > Polygons > Poly Extrude. 

In the either the Operati on Control Bar at the top of the Scene view or the Parameters pane, set Divide Into to Individual Elements and use the handle to set the Distance to around 0.4. This extrudes the faces along the normals of each primiti ve. 

You can see that there are now two nodes in the Network view. Each step you take in Houdini creates a node that you can work with to refi ne your scene. 

06 Press n to select all of the new faces and press Tab and begin typing sub… then select Subdivide from the list. The Tab key is another way to access tools in Houdini. Typing the tool name lets you focus the list making it easier to fi nd what you want without navigati ng the submenus. 

In the Parameter pane, set Depth to 2. This subdivides the geometry to create more polygons. Houdini also has a subdivision display opti on at the Object level which you can use to see subdivisions without actually adding any geometry, but in this case you do want to create more polygons. 

07 Select the dif erent nodes in the chain. The handles for each of the nodes appear as you select them but the display remains on the fi nal shape. Set the Display Flag on each of the nodes to change which node is the display node. You can also try some of the other fl ags such as Bypass or Template. Wiggle the polyextrude node out of the network then drop it back in. 

At the end, return everything to normal and set the Display fl ag on the subdivide node. This is very important. The Display fl ag determines what you will see at the object level. Always check to make sure you have the right display fl ag set! 

## PART TWO Create a Soccerball

You are now going to replace the box with a soccerball shaped platonic shape. Using Houdini’s procedural approach, you can replace the box node with a platonic solid node. From there you will adjust the other nodes to make it look like a soccerball This ability to swap out input nodes lets you prototype networks with simple geometry for added flexibility. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d9665af5a59a0205c0e46b0db2602f7d911cf96ec3b0c290bb1d5a8a606acd90.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/910ac05d5a6afcb8428d45fcf97f500dcda7d5b8c8341dcd81742bbafccd0e04.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/65443fc97897492e47b96cec262891e083f05b7d9a7b465c6caa45f77de72366.jpg)


01 In the Network editor, use the Tab key to add a Platonic Solids node to the network. Click to place it down near the top of the chain. Wire the platonic node into the polyextrude node. In the parameter pane, set Solid Type to Soccer Ball. Select and delete the box node. 

Because of Houdini’s procedural nature, it is often possible to replace an input node and have the whole network function properly. This gives you flexibility as you work and if you don’t like the results after the change then you can always wire back the original shape. 

02 Select the polyextrude node. Make sure the Handle tool is active then use the handle in the viewport to set a smaller Distance. You can also set the parameter value in the Parameter pane. This creates a beter look for the soccerball. Remember that even though you are viewing the subdivide node, selecting the polyextrude node gives you access to its handles and parameters. 

You might think that with this primitive type you are all set but it is really just a truncated icosahedron with flat faces. You need a round soccerball so you will have to put a litle more work into it. 

03 Press V in the viewport and from the Radial Menu, select Shading > Smooth Shaded. You can also use the menu in the top right of the viewport to change your shading. 

This soccerball looks like a cheap plastic ball rather than a proper leathery soccerball. You are now going to branch of and add more nodes to get a beter look. 

After analyzing it, set the shading back to Smooth Wire Shaded. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c77a3fc30b70ef198766e5bf321aa40fe797e1d0e0bb2c38b641a8fe38b26d47.jpg)


## SHADING OPTIONS

There are a number of Shading Options available from either the View radial menu or the Shading menu in the top right of the Viewport. For the shading of your objects, the lighting is determined by the Display Options on the right edge of the Viewport. You can choose from a headlight, normal lighting or high quality lighting with shadows. To quickly toggle from your shaded view to wireframe press the W key. 

Wireframe Bounding Box 

Shaded Bounding Box 

Wireframe 

Wireframe Ghost 

Hidden Line Invisible 

Hidden Line Ghost 

MatCap Shaded 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/59089b9375bf67da01cc800ec6317b720433537a3b4cc5baf5fd6b6c9ee9a3b0.jpg)


MatCap Wire Shaded 

Flat Shaded 

Flat Wire Shaded 

Smooth Shaded 

Smooth Wire Shaded 

Disable Lighting 

Headlight Only 

Normal Lighting 

High Quality Lighting 

High Quality with Shadows 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c83a1e48523a9c95ec068c80cd2f66573986c5591d3ecb54c4b75a4486c6e254.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b7bd85abf41c1540d7db1845b28796657101f5674cb1532bdf035e029670ded5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9746893feb06076feed369ef3a1f1ab516e4ebddd6e84813e634f368060e6a49.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/513f6c95658978fe95b5bba200459687ed35643978a03363b1f057bd2382cd87.jpg)


04 In the Network view, press Y and drag across the line connecti ng the subdivide node and the polyextrude node to break the connecti on. You are now going to move the subdivide in between the other two nodes so that you get a rounder soccerball. 

05 Drag the subdivide node in between the platonic solid node and the polyextrude node. You can drop it on the connecti ng wire and it will insert itself in automati cally. If not then jiggle it a lit le unti l it fi nds the connecti on. This will give more detail to the sphere before it is extruded. 

06 Use the tab key in the network editor to add a Ray node and wire it in aft er the subdivide. Now add a sphere node to the network and set its Radius to 1, 1, 1 and the Primiti ve Type to Primiti ve. Now wire the sphere into the second input on the ray node. This will project the subdivided ball onto a perfect sphere. 

This is a very powerful node in Houdini that lets you project points from one piece of geometry onto another. It is the perfect soluti on to our problem of a subdivided soccer ball that wasn’t truly round. 

07 Set the Display fl ag back on the polyextrude node. With Divide Into set to Individual Elements all the small polygons are extruded but you don’t want that. Set it to Connected Components then all the polygons are extruded. 

You need a way for this network to extrude the original patches of the soccer ball but aft er the ball has been subdivided. You can do this using the primiti ve numbers on the original geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a16809ad50fe9ac94d4a253c8b36a584511efe88feb8bdb5c4d36c299ab3e84c.jpg)


## THE RAY NODE

The ray node is a tool that projects points out to another piece of geometry. This is similar to the pinboard toy you played with as a kid. In fact, this is the node you would use to set up a pinboard in Houdini. 

GETTING HELP | To learn more about each node, you can click on the help but on in the top right of the Parameter pane to open up the node’s online documentati on. You can also hover over the tool in the shelf and press F1. In many cases, there are sample fi les that you can open in Houdini to learn what the node can do. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab822696a68c12d0e6cc90fe9d2f1a266a635661315300ac1d2cfc85f22e37c4.jpg)


## PART THREE The For-Each Node

Now you get to see the magic, as the atributes you just created in the last part are fed into a for-each loop where the original patches are extruded even though each contains many polygons. This will provide a more leathery look for the soccerball once you subdivide it once more time after the poly extrudes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/534ca169e6380bc37ead12dc2bf375d35450306fbca1a431c0816b71e3e9fd58.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4c639f6a68013f6312b2ffa91d4c546df7cacf700cbcfdddf40bfa39aac52f7b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ea72162c4734ce4157159a4bed961cc3ffb2b97d71cf83be3f5f190d7af8350f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8a0619a2423b2aa840d5db8bb1ca6568fa7d64526782abfe1bab4ef8a2f6edea.jpg)


01 Add an AtributeCreate node after the platonic node. – Set its Name to patches and its Class to Primitive. Now set the first of the Value fields to @primnum. 

This expression takes the primitive number atribute and turns it into a new atribute called patches. 

02 With the atributecreate node selected, click on the Geometry Spreadsheet tab next to the main viewport. Click on the Primitive buton and you can see the primitive numbers on the left, three color atributes which show the color of the patches and the patches atribute which matches the primitive numbers. 

Click on the ray node. This atribute will be carried forward when the shape is subdivided. You can now see there are a lot more primitives but the patches atribute only goes as high as 31 and then it goes back to 0. 

03 Go back to the Scene View tab, RMB-click on the Visualizer display buton on the Display Options bar and click on the + Plus sign next to Scene and choose Marker. In the Edit Visualizer panel, set Name and Label to Patch_Numbers, set Type to Marker, Class to Primitive and Atribute to patches. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/530a7e02b304a366b64010d3ede83f2406369c7345a266338a774f9c41299ce4.jpg)


## WORKING WITH ATTRIBUTES

Atributes can be assigned to Points, Primitives or Vertices. Some typical types of atributes include color (Cd) or UVs. You can see the atributes at any point in your chain by mousing over a node and choosing the i from the radial menu. You can also review the atribute values in the Geometry Spreadsheet panel. 

In this lesson, you will be creating a custom atribute called patches which will help you in the for-each loop. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/385aa7ec69c3752d664cc345c39aacb826030afe01fe402b75e022b82b57e892.jpg)


/obj/soccerball_geo/ ray1 Ray Sop (ray) 

1 Point Attrs P3flt (Pos) 2 Prim Attrs Cd3flt (Clr), patches flt 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d350d48fbff40db0377e43073b4a5b37fcca1e30de48f24b42066c5bd67df9d5.jpg)



at ributecreate node


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/be79288ac9913f1fddf497d18d9bea1d5f0375e6a5b5036e33447b089f9842ba.jpg)



ray node


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aa151a3439baa2b45f32e5c4b5212114d60a6f1867d013efd6b62ab51e5c87f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7734f43db851d42be72b87ac070d1009b973adbc8e7e6e67a96bd761bb0f92c0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2ff2838c0bca32a5410dbab82aaee94c1296de9ec6e2f4e2c4185e0b768f4cb2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/150f70a8ef4fa1ad6521256e9d8fe3e31e4116197d75ff3b87eeb4e25fe71160.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/56b388d5739a49914bb43128ab0545194ab877bc4fb915bc63563752b72d8a9c.jpg)


04 Now make sure the Visualizer display but on is on and you will see the patch values on the soccerball in the viewport. You can see that the prim number from the original platonic solid have been transferred to the subdivided faces. Change the display fl ag to dif erent nodes to see the relati onship. This informati on will be used to polyextrude the patches properly using a for-each loop. 

Turn OFF the Visualizer display and save your work. These steps have been a bit abstract and probably feel a bit too technical, but don’t worry the payof is coming. 

05 In the Network editor, press tab and start typing Foreach Named Primiti ve to access two nodes that you can then place into the scene. Wire the foreach_begin between the ray node and the polyextrude node and then the foreach_end aft er the polyextrude node. Select the foreach_end node and in the parameter pane leave Piece Elements set to Primiti ves and set Piece At ribute to patches. Set display on the foreach_end node. 

You should now see the original patches being extruded together based on the patches at ribute. If they are not make sure Divide to is set to Connected Components on the polyextrude node. 

06 Click the checkbox next to Single Pass to explore what is happening. Drag on the slider to watch as each of the patches is polyextruded individually. You can also set values higher than 10 to see more of the patches. 

Turn of Single Pass to see the full shape. The for-each nodes create all of the patches then return the fi nal geometry. The for-each loop is a powerful set of nodes that you will use oft en with Houdini. 

07 Add a Fuse node aft er the foreach_end node and set its Display fl ag. This connects the pieces into a single topology. The for-each nodes broke them into the dif erent patches but didn’t fuse them back together. 

Add a Subdivide node aft er the Fuse. Set the depth to 2. This will give you more detail in the viewport that you can use to evaluate your model. This adds more polygons but will not yet render as a true subdivision surface. Houdini also lets you set Subdivision display in the viewport without adding geometry but this Subdivide node is needed for later in the lesson. 

08 Play with polyextrude values to get a nice leathery soccer ball. Here you set a Distance of 0.1 and an Inset of -0.02. This gives nice rounded patches that look much bet er. 

Go to the Object level and rename the object soccerball_geo in the Parameter pane. Either select the node and press F2 or double click on the name. Click on the Render tab and turn on Render Polygons as Subdivisions (Mantra) to set up true subdivisions at render ti me. Select the Q Render Region tool, then draw a box around the soccer ball in the viewport create a preview rendering. To cancel, click on the x but on in the top right of the region. 

## PART FOUR Seting up UVs

In order to set up materials and textures, it is important to make sure that there are proper UVs set up on your object. Geometry in Houdini does not come with UVs, therefore you must create them yourself. This means adding extra nodes to the network, which in this case means adding UV Quickshade and UV Flaten nodes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f0e2d985aaab54aae98b8344d4212a4ce80dbb4c830367de8e5dbf6579cd1998.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/628dc05ec3e8c2d7f6a0aedefdb2ad3f40550fab7e2f73d6c5c3bbc501a85b57.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eca0bfb0d344aa1a2027e84dc5a6a883d47b19a79958d0a5c4415ba5c82e0005.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4bc0f6e65f98f3c9fdeab90343e9a71ada91ecaa4db014d26abc1755d5fa91e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c9967acc68f2092a4d067021d10c907b1bf3b693a3e0e4c3111548fbdea44a92.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e1d574c6bedc35fe28ebdf41c5ac69d49a0416bf77e6d7672e7267e8f3cb6991.jpg)


01 <sup>Dive</sup> <sup>into</sup> <sup>the</sup> <sup>soccerball_geo</sup> <sup>object.</sup> <sup>In</sup> <sup>the</sup> <sup>Network</sup> <sup>view.</sup><sub>press</sub> <sub>tab</sub> <sub>></sub> <sub>UV</sub> <sub>Quickshade</sub> <sub>and</sub> <sub>place</sub> <sub>the</sub> <sub>new</sub> <sub>node</sub> <sub>righ</sub> press tab > UV Quickshade and place the new node right after the foreach_end node. Set its Display Flag. 

Click on the File Selector buton next to Texture Map. Navigate into the  folder and select soccerball_color.rat. Now you can see this texture map on your geometry but everything seems stretched because the UVs were created using a projection method. 

Note: Seting up UVs to match an existing texture is not the normal order of operations. We are taking this opposite approach so that you don’t need to paint a texture yourself. 

02 In the Scene view, press n to select all then press tab > UV Flaten. In the Group field, enter the expression <sub>@patches>19</sub>. This will flaten the dark patches on the soccerball geometry using the patch boundaries to lay out the UVs. 

Using this tool brings up UV view. Click on the UV (vertex) menu in the top right and choose Background > soccerball_color.rat. Now you can see this texture in the background of the UV panel. This texture has a team insignia at the center of the image and a darker area at the top for the dark patches. 

03 RMB-click on the Handle tool and turn on the Min: handle. Use the arrow handle at the botom and pull it up until all the patches are inside the dark area at the top of the texture map. 

If you had placed this node after the fuse or subdivide then there wouldn’t have been boundaries to work with. Houdini’s ability to let you set up UVs in the middle of an existing network ofers a lot of flexibility. 

04 Add another UV Flaten node after the first uvflaten node and before the Fuse node. In the Group field, enter the expression <sub>@patches<20</sub>. This will flaten the light patches. 

RMB-click on the Handle tool and turn on the Min: handle. Use the arrow handle at the top and pull it down until all the patches are inside the light area at the botom of the texture map. 

When you finish you can RMB-click on the Handle tool and turn of the Min: handle. 

RMB-click in the Scene view and from the menu, select Texture Visualization > Of. This will remove the grid. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a0653780f74a6bb1ff3ef35d88165c7acbd85f7d6da9290bff44d2038ee7ff5c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f6d1435c08db56a06afac3bb0796589422b0e94920715d8d937ea834ba8512f1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e139dd966e80c0e99171846f550fb488c4708817cfb7dad6c4789ffe45d7e1f4.jpg)



Shift -Click


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d27d84348be6f6072ecbd5750c11275e150eb35bc8c66c395ea8428e9d08471d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d4ca613728fe3a31ee7fa79f147fe3925f9ab96d81593d7f101e66255d24499e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/feea0f2807dfe0a2026875cc44a92c06524741dc62c038f716fc05eccf3b86c1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5f44955f7bc95a45011930185a31febb62124f12ebb0ee95fd06309d46b75c3d.jpg)


05 Select the uvfl at en node and click on the Handle tool. Mouse over the geometry you can see the patches highlight. Click on the Pin Verti ces but on in the Operati on Controls bar at the top of the viewport. 

Mouse over the patch shown in this image and in the 3D view, Shift -click on the center vertex of the desired patch to select it. This adds a pin in the UV view and a handle to work with. 

06 Go to the UV view and move the pin and the patch so that it is centered on the logo. Press Y to get a rotate handle and rotate the patch unti l you line up the logo. 

By pinning verti ces on patches in the UV view, you can lock down their positi on. At fi rst there is some overlap of the neighboring patches but you can easily fi x this by repacking. 

07 Click on the Repack but on in the Operati on Controls bar to reorganize the other patches around the new one. You can conti nue moving the patch around using the pin but will need another Repack to avoid overlapping UVs. 

08 Set the quickshade node to Bypass to hide the assignment of the texture map. This node was only needed when you were seti ng up the UVs. You now see a UV grid on the soccerball. 

To hide the UV display in the perspecti ve view, got to the Display Opti ons bar and turn Of the Show UV Texture when UV’s Present but on. 

Add a Null node to the end of the chain and call it GEOMETRY_ OUT. It is a good idea to have this kind of node to defi ne the end of the network chain. Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3f338192340e84a28d6fba9bff2b6d71d10537eee4cf01724917473fa5e6efd8.jpg)


## UV FLATTEN

The UV Flat en node works in two steps. It takes individual texture pieces, defi ned by seams, and fl at ens them into 2D texture space, trying to equalize polygon size. 

This node lets you add constraints for the fl at ening algorithm. Constraints force the layout algorithm to sati sfy certain conditi ons, giving you extra control over the fi nal UV layout. You can use this node interacti vely, using the tools in the node’s state to specify constraints, or you can turn of Manual layout and use the node procedurally. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/137a2eba510afed7472d14fa12e90678839985bb25b6aa7cb5e3d36a8b995ce4.jpg)


# PART FIVE Layout: Cameras and Lights

To create a scene for rendering, you are going to bring the geometry into the Solaris or LOPS context of Houdini. This is an environment dedicated to lookdev, layout and lighting and is built on the foundation of USD (Universal Scene Description) This will allow you to render to the Karma renderer which works right in the Scene View as part of the Solaris workflow. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab5bd8b4f5168cd89ef10bc7ffec07a05aad0ea256d61d38926530ca021b3cb4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9dc57ff3552ba5ba449e17d1b495435f0035ff6ce662c6adebf9755373104d9b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/013748a442d6330ef98987ff2c2e8b5e989862c96327fc94c66fe2c69bb880bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9394b83ffea8c0ae86e29890fc4fa471fdcab4bdfdab12fec098b638ae085415.jpg)


01 <sup>In</sup> <sup>the</sup> <sup>Network</sup> <sup>View,</sup> <sup>press</sup> <sup>tab</sup> <sup>></sup> <sup>Match</sup> <sup>Size</sup> <sup>then</sup> <sup>add</sup><sub>the</sub> <sub>node</sub> <sub>between</sub> <sub>the</sub> <sub>subdivide</sub> <sub>and</sub> <sub>GEOMETRY_OUT</sub> the node between the subdivide and GEOMETRY_OUT null. Set the Display flag on the GEOMETRY_OUT node. 

Select the matchsize node and set Justify Y to Min to raise the ball up to sit on the ground. This will put it in the right position for rendering. 

## 02 Change the desktop to Solaris. Make sure you are looking at the Stage in the path bar.

In the Network view, press tab > Scene Import and click to place the node down. Next to the Force Objects field, click on the node selector buton and from the pop up window, select the soccerball geo object then click Accept Patern. 

In the Scene View, use your view tools such as spacebar-h for homing the view to get a beter look at the soccerball. 

Note: Force Objects is used instead of the Objects field because it will bring the object into LOPS even if the object’s display flag is of. 

03 In the Network view, press tab and type out Grid. Click to place down the node and rename it backdrop. Doubleclick on the backdrop node to dive down to the geometry level. 

Select the grid node and set the size to 80, 80 and the Center to 0, 0, -20. RMB-click on the grid node’s output and type Bend. Click to place the node then set its Display Flag and set: Bend to 75. In the Capture section, set Capture Origin to 0, 0, -30, Capture Direction to 0, 0, -1, and Capture Length to 5. 

RMB-click on the grid node’s output and type Subdivide. Set its Display Flag then set Depth to 2. 

04 Go back to the Stage level. Wire the backdrop node into the sceneimport node. RMB-click on the output of sceneimport and type out Camera. Press Enter to place the node then set its Display Flag. 

In the Scene View, you will see camera handles at the origin. Zoom out and look down at the scene then adjust the handles so the camera is looking at the soccerball from the left. You may want to activate the Construction plane so that you move the handles along the ground. You can also use the axis handles to control the direction and lift the camera up from the ground. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/439c619267009f5e298058bc1b96c30782a0386ee8210a53dd9542bc3dace27c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1f7a2855352f0cb6c1b91e61552583d738cc743e2badb82f0099109f11f18916.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eb4b50c2c719c467318a8b0479cbb61ffec95c91423479f3c80f2b20b60ff923.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/26bb54a9d5708f5586eb3badb144e1193cbec2d9a85f90a8f54d30f5872b8a4c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/28634717d59fe96b038a2fe42b75bf43472b8cc82cf7d726816e36f5246e6dfc.jpg)


05 In the top right of the Scene View, click on the No cam menu and choose camera1. Now you are looking through the camera and can adjust how it looks. 

This is probably not the view you are looking for therefore some view changes are needed. On the right side of the Scene View, click on the Lock camera to view buton. Now use the View tools [Spacebar-LMB/MMB/RMB] to reposition the camera. 

IMPORTANT: When you finish, toggle of the Lock Camera buton. 

06 From the LOP Lights and Camera shelf, click on the Environment Light tool then press Enter to place it at the origin. Set the Intensity to 0.5 to tone it down a bit. 

Now click on the menu just to the left of the camera menu, and set it to Karma. Now you are using the Karma renderer in the viewport. 

If you have an Nvidia graphics card and have the latest drivers installed, you can turn on the Optix Denoiser to resolve the image more quickly. Turn it on in the Display Options bar or press d and seting Enable Denoising in the Render Display Options. 

07 From the LOP Lights and Camera shelf, click on the Point Light tool then press Enter to place it at the origin. You are looking through the light. Set the camera back to camera1. 

With the node active, press Shift-F to turn on the Shadow mode. You can also click on it in the Operation Control bar. Now click on the top of the soccerball to set a pivot point then Shift-click to place a target on the ground. Ctrl-Drag to set the light distance. 

Now you can use Ctrl-Shift-drag to change the intensity of the light. You may need to set it quite high go see some impact on the look of the soccerball. 

08 In the Network view, RMB-click on the pointlights node’s output and type Light then press Enter to place the node and set its Display Flag. 

With the node active, press Shift-S to turn on the Specular mode. Now click on the right side of the soccerball to define a specular area of focus. 

Now you can use Ctrl-drag to move the light away from the soccer ball and Ctrl-Shift-drag to change the intensity of the light. 

09 In the Network view, RMB-click on the lights node’s output and type Light Mixer then press Enter to place the node and set its Display Flag. This will create a special panel in the Parameter pane which has a list of lights on the left side. 

Drag the three lights from the list to the area on the right. Click on the Star icon to Solo each light to determine its contribution then tweak Exposure to adjust the lighting. Since the intensities are so high you can click on the icon above the intensity bar and from the pop-up set a Max value that works for your shot. When you are finished be sure to turn of the Solo buton to see all the lights. 

# PART SIX Lookdev: Materials

Materials and shaders can also be created within the LOPS/Solaris context. This involves adding the materials to the Scene Graph then assigning them to the geometry. The Materials are created inside a Material Library node then assigned at the LOPS/Solaris level. To add textures to the backdrop, UVs will have to be created to position the maps properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fef7859aa535f7a1b24708c02e5d01a752ec112be224adfbb802a3b81e302ef6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8714cf49d14a26b3fcd290ad778302fa4feeac0b3c86a4ea594d42375e175ad2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e353c0a336a038abb00680b89d3aef5d30936bb9749f3de4fd90670f2a8ee655.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bfb0456f76c2004be8577c51af551ad928cf8b7c1e6d505eb2bf0267ec12c9af.jpg)


01 In the Network view, press tab > Material Library and place the node just above existing network of nodes then wire it into the backdrop node. Double click on the node to go down to the VEX Builder level. 

Press tab > Principled Shader and place the node down. Rename it soccerball_mat. Change its Base Color to white (1, 1, 1). 

Alt-drag on this node to create a second principled Shader and rename this one backdrop_mat. Change its Base Color to a dark green. 

02 Go back to the Stage level then press tab > Assign Material and place the node in between the sceneimport and the camera nodes. 

In the Parameter pane, next to Primitives, click on the arrow buton and in the viewport select the soccerball geometry. Press Enter to add its path to the Primitives field. Now click on the arrow next to Material Path and from the pop-up window, select materials > soccerball_mat and click OK. 

Click on the + buton then repeat these steps for the backdrop and the backdrop_mat. 

03 Double-click on the materiallibrary node to dive into it and select the soccerball_mat node. Click on the Textures tab and under Base Color click on Use Texture then use the buton next to Texture to call up the file window. Click on $HIP in the side list then click on the tex folder to open it and then click once on soccerball_color.rat to select it. Click Accept to assign the texture to the material. 

The $HIP reference makes sure that the reference is relative to the location of your scene file. That way if you were to move your project directories to another computer the reference will still work. 

04 Under the Textures tab and use the technique you learned in the last step to assign textures to Roughness and Reflectivity. You will find the appropriate textures in the tex folder. 

Go to the Bumps & Normals tab on the material and click the Enable buton. Click on the arrow next to Texture Path and from the tex directory choose the soccerball_normal.rat file. Set the Efect Scale to around 0.5 and see how it looks. 

# MATERIALS IN HOUDINI

Materials in Houdini live in the VEX Builder context which in this case is nested inside the Material Library node. A material is made up of VOP nodes or Material X nodes that defi ne the material qualiti es. The Principled Shader is an uber material that can be used on its own to assign texture maps and achieve a large variety of looks. You can also build your own shaders and materials for more advanced looks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7d3ac1e3051ed728ff83937a89f2c45c288fd498c9e864be92158f69a13e3c46.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9c31736d5da593d50f3f13ca761fffa028010ca26912afdd934e63e69a80591e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c26908ee144b0aa7d0bcd59631c261a6e5b65e528aa66b021f151e1b9704deaf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4cbf771e59d2372ceb6b7b4ad67a96e7b9386d3eca8755564309a4c93fd14031.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e02fb113424c7971be2e800afaee90703fb101914f1a11a00bd365fb5152298b.jpg)


05 In the Scene view, look through camera1 to see your shot. The positi on of the soccerball’s logo isn’t quite right in relati on to this camera therefore you need to rotate the ball. 

In the Scene view, select the soccerball. Press tab > transform. This adds a transform node to the end of the chain. With the Handle tool, press r to get the Rotate handle and rotate the ball see the logo properly. You may need to tumble around to get this to work. 

You can do this in the Karma or Houdini GL view. If you don’t like the edits then you can delete the node and try again. To deselect the soccerball_geo, press Ctrl and click on it in the Scene Graph. 

06 Now lets add some texture maps to the Backdrop material. Double-click on the materiallibrary node and select the backdrop_mat node. 

Set the Base Color to 1, 1, 1 because this color will be multi plied with the texture map. Now click on the Textures tab and under Base Color click Use Texture. Click the File Selector but on and use <sub>$HIP</sub> to go to the <sub>/tex</sub> directory and choose backdrop_color.rat. You can also add the backdrop_refl ect.rat texture to Refl ecti vity. 

You can see in the Scene View that UVs are not set up properly and the texture map isn’t working. 

07 Go back to the Stage level then double-click on the backdrop node to go to the geometry level. Add a UV Project node between the grid and the bend. You are puti ng the nodes here so the UVs are created before the surface is bent. 

On the uvproject node, click on the Initi alize tab and click the Initi alize but on. Go back to the Transformati on tab and set V Range to 0, -1. This will orient the UVs properly. 

IMPORTANT: Set the Display Flag back to the subdivide node. 

08 Go back to the Stage level. In the Network View, press tab > Karma to add a Karma Render Seti ngs and USD Render ROP node. Wire them into the end of the chain. Select the karmarenderseti ngs node and on the Image Output > Filters tab set Denoiser to nvidia Opti x Denoiser to turn the denoiser back on. 

Select the usdrender_rop node. Click on the Render to Mplay but on. This opens Mplay which shows the rendering as it progresses. Choose File > Save Frame As to save the image to disk. 

# PART SEVEN Rig the Soccerball

In order to create an animation of the ball bouncing, you will start by building a simple rig that will make it easier to keyframe. This will involve seting up null objects so that you can work interactively in the viewport and adding nodes to the soccerball geometry network to accommodate the ball rotation along with squash and stretch. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/55ed8ad5ddb388adfa7d2cbbe6f17f9ffbf1cdd14eb76c476a16fe53b71c25d8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3c9792b3e5c9cfee66a2524edebfa23eda587879bc4ea3ca5789aca9b6f9767d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eac8a2cf320faa3aae276d75c1d7c1be75e4957741cb2d7e0f2e76e6bb25328c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5a7b0463d1d4235ab41acc413b8e0cb0f43e98caae380619b69c747e18bf0f67.jpg)


01 <sup>Change</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>Build</sup> <sup>desktop</sup> <sup>and</sup> <sup>navigate</sup> <sup>to</sup> <sup>the</sup><sub>object</sub> <sub>level</sub> <sub>by</sub> <sub>clicking</sub> <sub>on</sub> <sub>one</sub> <sub>of</sub> <sub>the</sub> <sub>path</sub> <sub>bars</sub> <sub>and</sub> object level by clicking on one of the path bars and choosing obj. Now in the network editor, Alt-drag on soccerball_geo to make a copy of it. Rename this node socccerball_anim. 

You will use soccer_anim to build your rig. Now turn of the Display Flag on the soccer_geo node to hide it. You don’t want to make changes to the original setup because that object is being used in SHOT 1 in the Solaris context. This new soccerball will be used for an animated SHOT 2. 

02 On the Create shelf, click on the Null tool then press Enter to place it at the origin. Name it soccerball_ctrl. Go to the Misc tab and set Control Type to Circles and Orientation to ZX Plane. Set the Display Uniform Scale to 4. This creates a handle for the rig that is easy to select that won’t render later on. 

In the network editor, connect the input of the soccerball_anim object to the output of the soccerball_ctrl null to create a child/parent relationship. Moving the null will move the ball. Turn of the selection flag on the soccerball_anim so that you don’t select it by accident in the viewport while animating. You will use soccerball_ctrl instead. 

03 Select the soccerball_ctrl node. In the Parameter pane, click on the Transform tab then RMB-click on the Translate X parameter. Choose Copy Parameter. 

Dive into the soccerball_anim object. Add a Transform node between the subdivide and the matchsize nodes. RMB-click on the Rotate Z and choose Paste Relative References. This places a channel reference expression in this parameter. 

ch(“../../soccerball_ctrl/tx”) 

This will connect the movement of the control object to the rotation on this node. 

04 Click on the parameter to expand the channel. You are now going to use the ball’s circumference (2πr) to determine the ball’s rotation as it moves forward. 

Edit the expression to read: 

-ch(“../../soccerball_ctrl/tx”)*360/(2*$PI*1.1) 

First you add a negative (-) at the front. You then multiply the position of the ball by 360 degrees and divide by 2πr - π being $PI in the expression. At the object level, move the soccerball_ctrl along the X axis. The expression will rotate the ball to match the motion. Put it back at the origin when you are finished. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/30471dbdc49a36ad551b5d26402be2bfecace4781dee78e997d3bbef538eb82e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a386db821424e3d7357dc222b935cf651642b3cc6acb291f9cbdcfddfe66a4f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8e4f075d0a3650525095ad0d502f3d3be683f86467f309ef14d467ceafefc85c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f4f5f9fbc9de67691d11b384822e2cc1559afdab23c3451bcfd676df9ac8ee28.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d5767a5631023b7cdea5c80e3c11f2a1854d902ee28a2e1e70c0de8c58e0105e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/77b4a74cb7ab13a1656bc05aa7918df14afbcc7d98b7cfe2a401716bb337776e.jpg)


05 In the Viewport, create another Null object at the origin. Call it squash_ctrl. Go to the Misc tab and set Control Type to Box and the Display Uniform Scale to 0.2. 

Move the null up just above the ball. Translate Y should be about 2.5. In the Parameter pane, choose the Modify Pre-Transforms menu and select Clean Translates. This sets the Translate Y value of the null to 0 even though it is above the ground. In order for this null to drive the squash and stretch, it needs a default value of 0. 

06 Parent the squash_ctrl null to the soccerball_ctrl null. This will ensure that this secondary null moves when you animate the control null. 

RMB-click on the squash_ctrl node’s Translate Y parameter. Choose Copy Parameter. You will use this parameter to drive the squash and stretch of the ball. This will allow you to control the squash and stretch from the viewport interactively. 

07 <sup>Go</sup> <sup>into</sup> <sup>the</sup> <sup>soccerball_anim</sup> <sup>object.</sup> <sup>Add</sup> <sup>a</sup> <sup>Bend</sup> <sup>node</sup><sub>after</sub> <sub>matchsize.</sub> <sub>Turn</sub> <sub>Of</sub> <sub>the</sub> <sub>Limit</sub> <sub>Deformation</sub> <sub>to</sub> after matchsize. Turn Off the Limit Deformation to Capture Region checkbox. 

Go to a Right View then click the Set Capture Region buton. Turn on Grid Snapping and place a point at the base of the ball and another at the top. This should set Up Vector to 0, 0, 1, Capture Direction to 0, 1, 0 and Capture Length to 2.2. 

Turn on Length Scale and Preserve Volume then RMB-click on Length Scale and choose Paste Relative References. Add a +1 at the end of the expression. 

08 Go to the Object level and a perspective view. RMB-click on the Transform X and Transform Z parameters and choose Lock Parameter to lock these parameters on squash_ctrl. RMB-click on the Scale and Rotate parameters and choose Lock Parameter to lock all three channels. 

Select the soccerball_ctrl object. Lock all the channels except Translate X and Translate Y. Now when you select the controls you will only see handles for the unlocked channels. This will make it easier to work with the rig because the animator can only manipulate the chosen parameters. 

09 Now test out the rig by moving it around in X and Y and using the second handle to squash and stretch it. Once you are sure that all the parts are working, return all the values to 0 and get ready to animate. 

You may want to turn of Secure Selection in the toolbar on the left side of the Scene view. This will make it easier to select the two control nulls while in the Move tool. If not then you will need to press the S key every time you want to switch selections. 

Save your scene file before proceeding. 

## PART EIGHT Animate a Bouncing Ball

You can now take the soccer ball rig and use it to animate the ball bouncing. You will learn how to set keyframes, adjust anima ti on curves and work with ti me-space handles in the viewport. The bouncing ball is a classic animati on exercise that of ers a great opportunity to learning the basics of animati ng in Houdini. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7433af4752021f06a482b13d1de82319ad40d71e684b2dac5ed71692740e350e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9538ec06457d50d922bcdce9b6860b34d6da49a26f61dc9b2434c3a9fe955bc8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ba6dd874b3181245b21933b5eaf948d082012f8521b0acb62844ce2f9e1de898.jpg)


## THE POSE TOOL

01 At the bot om left edge of the Timeline, click on the Global Animati on Opti ons but on. Set the End to 120 and click Close. This will set the ti meline range to 120 frames. 

Make sure you are on frame 1. Click on the Pose tool on the toolbar to your left and select the soccerball_ctrl. Move the ball to around -15 in X and press K to keyframe it. Move the ti meline to frame 120. Move the ball to the around 15 in X and press K to set a second keyframe. 

Scrub through the ti meline to make sure that the ball is animati ng. It should be moving and rotati ng based on the rig design. 

02 Move the ti meline to frame 12 and press K to set an intermediate key. Repeat at frames 36 and 60. All of these keyframes are siti ng on the ground. 

Now go to frame 1 and lift the ball up in the Y directi on. You don’t need to set another key because this move simply updates the keyframe you already set at frame 1 . 

Move to frame 24 and lift up the ball in the Y directi on a lit le less than you did at frame 1. Press K to set a keyframe. Move to frame 48 and lift the ball up even less. Press K to set another keyframe. 

03 Scrub through the ti meline to see that the ball appears to fl oat whereas you want hard hits when the ball contacts the ground. Click on the Animati on Editor pane tab. 

From the Scoped parameter list, click on the Translate Y channel. Press H to home the view of the curve. Select the three keyframes where the ball contacts the ground and press the Unti e Handles but on on the Functi ons bar found just above the graph. Now click in empty space to deselect then start tweaking the tangent handles to create a sharp bounce at each point. You can also stretch out the handles at the top to slow the ball down at the peak. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/35efbb7c0f9e73383cbaf6ef40928cd46b2532646d652f3fa3e4cc0b0f376dde.jpg)


Secure Selecti on [~] 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/86b9bb56286b539342a53941d65b947f30b3507b014508807396dd5e8ad35d80.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5f6fabc718a12c55e9ffd3978f090232dabc732ecfd1405c77b175266c6ae66a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fdd3d19f2b78c6e27b36dbe5fd9c0dacd93cc394f66db695833237e993a46868.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/becf18316c0237b1995d9f1b4f656d67073df5241a11ed5473c1852bf93a4a86.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/612e6106b25c3bd073afa401173fae7868ff009588433d16ebabf7350be4240c.jpg)


04 Go back to the Scene view and preview the results. You now have a sharper hit each time the ball hits the ground. Make sure you have the Pose tool active and the soccerball_ctrl node selected. In the top bar, turn On the Motion Path handle. This shows a path outlined where the ball is bouncing. Click on each keyframe marker to tweak the bounce. RMB-click on the handle to Show tangents for more control over the curve. 

Go to the soccerball_anim object’s Misc tab, set Onion Skinning to Full Deformation. Press spacebar-d and from the Scene tab adjust Frame increment and the Frames Before and After color. 

05 To adjust the timing, you can also use the timeline. Press Shift and drag a bounding box from frame 1 to the last key in the timeline to select all the keys. Next, MMB drag on the end of the box underneath the handle to scale the timing of the bounces to speed them up. You can also select each key using MMB and then drag with MMB to time each keyframe the way you want. 

This is where you will determine the timing of the bounces. Keep exploring until you get the look that you want. Note that there may be some awkwardness in the bouncing because of the translate X values. You will fix that in the next step. 

06 Click on the Animation Editor pane tab and you will see two curves. From the Scoped Parameters list, click on Translate X for soccerball_ctrl. Now select all the keys except for the first and the last. Press Delete. Now use the curve handles to go from a high slope to a low slope. This will have the ball moving faster at the beginning and slower at the end. 

Note that if you go back to tweak the points in X on the motion path handle, you will get strange results because there are no longer intermediate keys in that direction - only use it to tweak in Y from this point on. 

07 Go back to the Scene view. RMB-click on the Motion Path handle and choose Persistent. This will keep it around as a guide as you set keyframes on the squash and stretch. 

Select the squash_ctrl and turn of its Motion Path. Go to the first bounce and move back one frame. Select the squash_ctrl handle and stretch out the ball a bit. Set a Keyframe using the K key. Now go to the bounce frame and move the handle down to create squash. Set another key. Go one frame forward and stretch the ball until it is round. Set another key. Repeat for all the bounces. 

08 When you are finished, scrub and playback the motion to preview the results. Make sure the peaks of the bounces are stretched out. Make sure the Real Time Toggle is On in the Timeline to properly evaluate the motion. 

You can now use the Animation editor to make tweaks to the squash and stretch. Make sure you keep the keyframes aligned with the bouncing of the soccer balls. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/418fce881c180c5f3c9938f1c210f00e0b5fdd66580c9b0cacc2be8208b8bb2f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b814091f05c9cb52520e029014b47d0f304caf6f0f0757e3fe127f3df9412a35.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/98c48def2bd2777ff3e3d5aff92e554b0a41bd0dd3df512952b6e3b81b34db04.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d56223cf5112174b585989a07c9ad704426d2304595cc666212e47dd12032cd2.jpg)


09 Select the soccerball_ctrl null object. RMB-click on the Translate Y and choose Moti on FX > Noise. A panel pops up with parameters that you can use to control the noise. A new subnetwork was created with the CHOP nodes that send their informati on back to the soccerball_ctrl’s Translate Y channel. 

Set the Amplitude to 5 and press Play to see how this looks. This adds dramati c up and down moti on which make it feel like there is some serious turbulence. Set the Amplitude to 1. This of ers a more subtle bump to the moti on of the ball. 

## want to focus on creati ng bumps above the ground.

Go back to the object level. Select the soccerball_ctrl null object. RMB-click on the Translate Y and choose Moti on FX > Limit. Set Minimum to 0 and Maximum to 6. Now the ball moves fl at with some bumps instead of going up and down the whole way. 

## 11 <sup>There</sup> <sup>should</sup> <sup>not</sup> <sup>be</sup> <sup>any</sup> <sup>noise</sup> <sup>while</sup> <sup>the</sup> <sup>ball</sup> <sup>is</sup><sub>bouncing.</sub> <sub>It</sub> <sub>is</sub> <sub>only</sub> <sub>needed</sub> <sub>when</sub> <sub>the</sub> <sub>ball</sub> <sub>is</sub> <sub>rol</sub> bouncing. It is only needed when the ball is rolling. You can keyframe the Amplitude to turn the noise on and of .

In the newly created moti onfx network, select the noise1 CHOP node. Go to Frame 37 where the ball stops bouncing and starts rolling. Alt-click on Amplitude to set a keyframe. Go to Frame 1 and set Amplitude to 0. Alt-click on Amplitude again to set a second keyframe. Go to the Animati on Editor and select the curve. Click on the Constant but on in the Functi ons bar. This creates a sharp cut from no amplitude to an amplitude of 1. 

## 12 When you are fi nished, close the window then RMBclick on the Moti on Path handle and turn of Persistent so that it isn’t visible when you deselect.

In the toolbar at the left side of the Scene view, click on the Render Flipbook but on. Leave the default seti ngs and click Start. Wait while the sequence is captured and then you will see the fl ipbook in an Mplay window. You can Play this back and scrub through to evaluate your moti on. 

Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/06914d901ec82032df14f0b36a6996832c40a07c5502451928540128d9db961e.jpg)


## MOTION FX

While keyframes and animati on curves are stored in the parameters of your nodes, you can also use channel operators (CHOPs) for a more procedural node-based approach to working with moti on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/102d1040b0cf33fd74b08e5a6732e09f987348344a897ad420f7444d81e5b43b.jpg)


Moti on FX can be applied to keyframed moti on which is extracted and stored in a Channel CHOP. You can then apply ef ects such as cycle, noise, smooth, limit or lag to the existi ng moti on. On the Constraints shelf, you have tools which let you have one parameter either look at, lag or jiggle behind another. 

# PART NINE Lights, Camera, Action!

To render out the animated soccer ball, you will need to go back to the Solaris environment and set up a second shot. You will begin by branching of new LOP nodes from backdrop geometry then adjust the lights and cameras to suit the bouncing soccerball animation. You will also set up motion blur for the deforming geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83dc30bbd6d48b4c7773c6fc276f7ff2196a4789f9556c23226c49de83a3bbf3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cd6c177315b05ae141b354b8838a0d4cd2bdd1b1975a0d27ab8437d1e1dd48c1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/98bb9e8e06f25b14210edb37cdd108bcc5e4a74edbc4ee1588fd1ef3a3b905eb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ff80559e835f37fcbcaa5024fd6f0f11c162371815b8aa64a4f6f15616808441.jpg)


01 Go to the Object level. Double-click on soccerball_anim to dive into it. Press n to select all the geometry then go to the Modify shelf and select Extract. This takes all the motion and bending of the ball and puts it in one network. 

You can see an objectmerge node which is extracting the ball into a new object called extract_object. RMB-click on the output and find USD Export then click to place this node. Rename this node to soccerball_anim. Click on the Export tab then set Valid Frame Range to Render Frame Range and set Output File to $HIP/geo/ soccerball_anim.usd. Click the Save to Disk buton. 

02 Go back to the Solaris desktop and point it to /stage. In the Network View, add a Null node just before the karmarendersetings node and call it SHOT_01. 

Disconnect the three light nodes (not the lightmixer) and move them above the backdrop node. This will not change how the first shot looks, but will let you share the nodes between the two shots. 

Move the backdrop, light and materiallibrary nodes to the right. 

03 Zoom in and add a Reference node to the right under the backdrop node. Connect the backdrop node to this new node and set its Display Flag. Next to File Patern, click on the File Chooser and find the soccerball_anim.usd file. Rename the node to soccerball_anim. 

Scrub in the timeline, in Houdini GL view, to see the cached animation which is part of the USD file. 

## 04 Use the Select tool and click on the new animated soccerball. In the Scene View, press tab > Transform to add a transform node to the graph.

In the Scene view, use the Transform handle to Move the Ball to the back of the backdrop in the middle. Scrub the timeline to watch the ball bounce to the right. Leave it at somewhere around frame 80. Press R to get the rotate handle. Rotate to move the ball so that it is bouncing at an angle from the backdrop. Scrub the timeline to see if you like its direction. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f79b0aa6c988adef28429ea626cfe636b5152e22789f32716a01c3394e17f025.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e842bb8224eeda37a392bcd26d474bef8bc09c340a40e26c342d0a84a4dcbe07.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ed76c107c0a4b47c5a997bc50540f54ed52a87e46ed56c50162dd610d50c0961.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6d77baac004361388e3299e4dd499734fdd45e7b94d33d6cb3284370c3470db4.jpg)


05 In the Network view, Select the assignmaterial node from the SHOT 1 network then Alt-drag to create a copy of this node. Wire the transform node into the assignmaterial node then set its Display Flag. This will assign the material to the backdrop but since the soccerball primiti ve has changed it needs to be reassigned. 

In the fi eld next to Primiti ves for the soccerball_mat , change the primiti ve name to /soccerball_anim to reassign the material to the new geometry. 

06 Tumble around unti l you see the ball animated towards the camera from the top left to the bot om right. In the LOP Lights and Cameras shelf, Alt-click on the Camera tool to place a camera from the angle you are currently looking. 

Press the Lock Camera/Light to View but on so that view changes can be used to repositi on the camera. Now Tumble, Pan and Dolly in the viewport to tweak the camera to get the framing that you want for the shot. Scrub the ti meline to make sure the camera works for the whole sequence. 

0 era. On the lightmixer node you will need to move over the lights. This will let you use the same light handles you learned about earlier to make lighti ng decisions for this shot and use the Karma display in the viewport to verify your setup. You can also use the lightmixer node to play with intensity and exposure for this shot. 

These edits are being held in the lightmixer node and changes are not being made to the original lights. The lightmixer lets you tweak existi ng lights when working in a multi -shot setup. 

08 In the Network view, Alt-drag the SHOT_01 and karmarenderseti ngs and usdrender_rop nodes. Wire the lightmixer node into this chain. Select the new karmarenderseti ngs node and make sure that Camera is set to /camera2. Set Valid Frame Range to Render Frame Range and set the Output Picture to $HIP/render/anim/soccerball_anim_$F2.exr. The $F2 adds frame numbers to the renderings with a padding of two and the /anim/ creates a directory to hold these frames. 

On the usdrender_rop node, click Render to Disk. When you fi nish, choose Render > Mplay > Load Disk Files and open up the rendered images to review the fi nal sequence. Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cf1ae07508c960ed17213ff01467e0a4952fb4b077ea5bd5be9cf09d4880b904.jpg)


## KARMA RENDERER

Karma is a physically-based HYDRA renderer built to work with USD fi les in the Solaris/LOPS context. This allows it to be used in the Viewport for interacti ve updates or to be rendered to disk using a Karma node. 

Note: Houdini 19 includes a preview for an upcoming Karma XPU render engine. This hybrid GPU/CPU renderer is Alpha with many features sti ll under development and is for testi ng purposes only. You can choose XPU in the Scene view’s Display Opti ons or in the Karma node. 

persp1 

Set View 

O Houdini GL 

Karma K 

Storm 

Render Settings 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c3a15bd305641eb4d56324e5874cc6407e3cc4f56f9f5a3393e6c58c36adf7de.jpg)


Pause Render 

Restart Render 

# PART TEN Set up a Rigid Body Simulation

While traditional animation is great for animating a single soccer ball, dynamics would be a beter option if you want to animate a bunch of soccer balls. Dynamics requires a simulation so that the solver can go frame by frame determining how each of the participating objects interact with each other. You will use packed geometry to get an eficient result for this simulation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6010e75449d061170049b4e17d2eea1231509643f4c367aa4c9ff688c8a0129e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/be44fb518e00c867428d4a18cd4fd818830569a414f61523ee3d4e052165548a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f3396424769f7b4c9e755a9cc1375a6b74b3fa41a5efe6a553dfa13afa227512.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1bbdb06dec3d9b1ecfd10b10b9434e61c8fb2a49ce57485c4b641cef019cf23a.jpg)


01 <sup>Change</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>Build</sup> <sup>desktop</sup> <sup>and</sup> <sup>navigate</sup> <sup>to</sup> <sup>the</sup><sub>object</sub> <sub>level.</sub> <sub>Hide</sub> <sub>all</sub> <sub>of</sub> <sub>the</sub> <sub>animation</sub> <sub>rig</sub> <sub>nodes</sub> <sub>and</sub> <sub>th</sub> object level. Hide all of the animation rig nodes and the extract_object node by turning of their display flags. Turn on the soccerball_geo display. 

Select the soccerball_geo node then from the Modify shelf click on the Extract tool. This creates a new object with the soccerball object merged. Jump up one level and rename extract_object to soccerball_sim. Hide the soccerball_geo object. 

Dive back in to the soccerball_sim object to work with the geometry. Add a Match Size node to center the ball around the origin. 

02 In the Network view, press tab > Box then place it to the right of the matchsize node. 

Set the following on the box node: 

 Center to 0, 8, 0 

 Rotate to 45, 45, 45 

 Primitive Type to Polygon Mesh 

 Uniform Scale to 6 

 Axis Divisions to 3, 3, 3 

This puts it in the right position for the simulation. 

03 In the Network view, add a Copy to Points node just below the other nodes. Wire the matchsize node into the first input and the box node into the second. 

Turn ON the Pack and Instance option. This will create a faster simulation because the geometry is being instanced to the points of the cube. Set the copytopoints node’s Display Flag. 

In the Network view, press tab > Mountain and place the node between the box and the copytopoint nodes. Turn Of the Noise Along Vector option then set Amplitude to 2 and Range Values to Zero Centered. This will jiggle the points on the box. 

04 Make sure you are on Frame 1. Add a RBD Bullet Solver node after the copytopoints node. Click on the Collision tab, scroll down to Ground Collision, and set Ground Type to Ground Plane to Ground Plane. Press Play to test out the simulation. The sim is cached which lets you scrub in the timeline to review the results. 

Under the Collisions tab, set Bounce to 0.8. Under the Properties tab, set Density to 10, Bounce to 1.1. At the top of the Parameter pane for this node, click the Reset Simulation buton and then press Play to resim. Scrub to evaluate. 

In Houdini, simulations are processed using the Dynamic Operators or DOPs. With the RBD Bullet Solver node in the Geometry/SOP context, you are working with a node that has a Dynamics network buried inside it. This makes it easy to set up at the geometry level with all the DOP nodes are wired up and ready to go but hidden from view. For simpler setups, working at the geometry level will give you a proper simulation. If you need more control over the diferent solvers then you would need to work directly in DOPs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a5a4136cbaa0d44eb802ca40543148ad3d575e7b7a201b697d2fb25d5fbff7dd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6a74816acf9bfdb063e7a22fda37045bf3dabaf2489bb17e9ceb0a2632519b93.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9a72be97b66509b6cbbaeefc21b342404a843b49ae73736ad9ee763779b79a74.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b03742f674057114d5fd8b0f93923f7ebea97bbff5efc19ed279fe798e8cf039.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b44704e060d0d336f5127709807856af6dc4a3e7edd1c77f826ffc62d2980476.jpg)


05 At the end of the chain, add a USD Export node, set its Display flag and rename it to soccerball_sim. 

Set Valid Frame Range to Render Frame Range and set the Output File to $HIP/geo/soccerball_sim.usd. 

Click on the Save to Disk buton and this will save the USD file into your geo directory. You will reference this cached asset into the Solaris setup as a third shot. 

06 Change your Desktop back to Solaris and set the path to /stage. Make sure you are choose Houdini GL from the persp menu. 

Alt-drag the soccerball_anim Reference node and set its Display Flag. Set File Patern to $HIP/geo/soccerball_sim.usd. 

Rename this node to soccerball_sim. 

07 In the Network view, Select the assignmaterial node from the SHOT 2 network then Alt-drag to create a copy of this node. Wire the soccerball_anim node into it the assignmaterial node then set its Display Flag. This will assign the material to the backdrop but since the soccerball primitive has changed it needs to be reassigned. 

In the field next to Primitives for the soccerball_mat , change the primitive name to /soccerball_sim to reassign the material to the new geometry. 

08 Tumble around until you see the balls animated towards the camera. In the LOP Lights and Cameras shelf, Altclick on the Camera tool to place a camera from the angle you are currently looking. 

Press the Lock Camera/Light to View buton so that view changes can be used to reposition the camera. Now Tumble, Pan and Dolly in the viewport to tweak the camera to get the framing that you want for the shot. Scrub the timeline to make sure the camera works for the whole sequence. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0bfa279757fa64749bf301ca1bd5b442d78701f57ff2793e8d72e9280e82d9cf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d2a65e00d73920a436ed0df2497dbe529091a8228ad989a9bf0942972bd3f776.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3e212bc3c4b144557a22f6de6678fb991c11de722a5e4f2d2015646e89b27177.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/278ed5d41963ed86ef1b364552077d9a64ae00c7eb399b6c0833c7fb715df9c6.jpg)


09 Add a Light Mixer node aft er the camera. On the lightmixer node you will need to move over the lights. This will let you use the same light handles you learned about earlier to make lighti ng decisions for this shot and use the Karma display in the viewport to verify your setup. You can also use the lightmixer node to play with intensity and exposure for this shot. 

These edits are being held in the lightmixer node and changes are not being made to the original lights. The lightmixer lets you tweak existi ng lights when working in a multi -shot setup. 

10 In the Network view, Alt-drag the SHOT_02 and karmarenderseti ngs and usdrender_rop nodes. Wire the new lightmixer node into this chain. Select the new karmarenderseti ngs node and make sure that Camera is set to / camera3. 

11 On the usdrender_rop node, set Valid Frame Range to Render Frame Range and set the Output Picture to $HIP/ render/sim/soccerball_sim_$F2.exr. Click Render to Disk. 

When you fi nish, choose Render > Mplay > Load Disk Files and open up the rendered images to review the fi nal sequence. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fb81f1b11a0ccd17869087b8580cf9d82cdb5ce5d114bcdea3aa3e5372c99a76.jpg)


## CONCLUSION

You have now built a scene from scratch, touching on many dif erent aspects of Houdini. You have modeled, set up textures, animated, rendered and simulated. Along the way you have learned about the dif erent Houdini contexts and how to navigate back and forth between them. 

While this lesson doesn’t result in blockbuster VFX, it introduces you to fundamental skills which you will carry with you as you dive deeper into Houdini and begin exploring its comprehensive toolset. 

There is a wealth of learning material available on the SideFX website to help you take your next steps. Best of luck on your journey! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/913ed0c4fe62945adfe86808d3a621e2a0ef60d76534afc4e4e36dba6cda9bcb.jpg)


<table><tr><td>Houdini Core</td><td>√</td></tr><tr><td>Houdini FX</td><td>√</td></tr><tr><td>Houdini Indie</td><td>√</td></tr><tr><td>Houdini Apprentice</td><td>√</td></tr><tr><td>Houdini Education</td><td>√</td></tr></table>

# HOUDINI FUNDAMENTALS NODES, NETWORKS & DIGITAL ASSETS

A great way to understand Houdini’s node-based workflow is to explore it in the context of a project. It is important to start learning how to think and work procedurally. In this lesson, you will learn how to create your own custom brickify tool using procedural nodes and networks to define its function and interface. 

Along the way you will get to use diferent aspects of Houdini’s workspace. Be sure to refer to the overviews in the introduction to remind yourself of how these UI elements work together. The lessons will then give you a chance to put your ideas into practice, which is one of the best ways to learn. 

## LESSON GOAL

 To create a custom tool that turns any given 3D shape into toy bricks. 

## WHAT YOU WILL LEARN

 How to model a plastic interlocking brick 

 How to break down a default rubber toy shape into a grid of points. 

 How to use packed primitives and instancing to speed up interaction. 

 How to use atributes to color the bricks using a texture map. 

 How to work with nodes and networks to control the flow of data 

 How to create a Digital Asset to package up and share your solution with others. 

 How to animate the bricks appearing over time. 

## LESSON COMPATIBILITY

Writen for the features in Houdini 19.5+ 

The steps in this lesson can be completed using the following Houdini Products: 

Document Version 3.0 | July 2022 © SideFX Software 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/21b8122a998d4e579b35965083a372004ae8e1004e56f1d214f8df815f85d7b1.jpg)


# PART ONE Create a Single Brick

To get started, you will build a single brick model that you will later copy onto points to create the brickified shape. You will create this shape using a combination of polygon modelling tools. Along the way you will see how each action you take creates a node in Houdini that creates a recipe of the steps taken to create the geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5bd4bd178656b510dacf49d7bd20856030b1c49ecbe2566cbe1ca982dd2a0f2d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/34e2aa040ebafb5eff432e07b8dc7395b79d7f6c9e84434e099135137dc70449.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ca845bfb12f973c785771a911f021b1898411d3b2f2e8d6eec4fa14e6cd5c7ca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e4567aa0f871683735ce34dbbfe90988ebc858d74b1e82eaf9e2caf2f945bd66.jpg)


01 Select File > New Project. Change the Project Name to brickify_lesson and press Accept. This creates a project directory with subfolders for all the files associated with this shot. Select File > Save As... You should be looking into the new brickify_ lesson directory. Set the file name to bricks_01.hip and click Accept to save. 

02 In the viewport, press c to bring up a radial menu. From this menu, choose Create > Geometry > Box. Your cursor now shows the outline of a box waiting to be placed in the scene. Press Enter to place it at the origin. In the Operation Controls bar, set Size to 0.2, 0.2, 0.2 and Axis Divisions to 3, 2, 3. 

You can see that there is a box_object in the Network view. This object level node contains the transformation information for this shape. The Operation Controls show you parameters from another box node one level down. 

03 Click on the Select tool then Press 4 to go to primitive selection mode. Select the top four faces on the box. Press c to bring up a radial menu and choose Model > Polygons > PolyExtrude. In the Network view you can see the box node feeding into a polyextrude node. 

In the Parameter pane, use the slider to set Inset to 0.04 which creates new polygons on the top surface of the box. Each node contains parameters relevant to the purpose of that node. These are geometry nodes that are otherwise known as surface operators or SOPs. 

04 Next, press the T key to call up the Move tool. This adds an edit SOP node into the network. In the viewport RMB-click in empty space to bring up a menu and select Make Circle to round out the selected polygons. 

This menu is associated with the edit node. Every node has its own interface that you can access as long as a relevant tool is active. In this case, the Move tool gives you access to the handle. In other cases the Handle tool would be used to access the interactive handles for a node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5dd0bec47a4b624ca9aa9ba49acc48db51c519533c8efc1daeb04d95217ae82f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4d9c3ed9c40f0b1de1d66a0ab611ec4156df4de7227c760345b056aa13fd74d6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fb1367074dd6e070384727f78bdaabaf8d22f3607ab4bf486ed3a2d4aa47efb2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6074ae7beade65a420b072963ee2b4f6e8ba849382665076c35e93e9ec019da6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5ecaf838157fd1c412a0522a29f70464aca2fc3219c1d96a90eed9133214a6e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9d632b3acaeab746f54362f1e29393623af3c35cc646ece415f1748cceb363fd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4a34314d5d5957fe9d2d574ad1ffb98a191e9c828a3376f99c007b299ed0cd49.jpg)


## SUBDIVISION DISPLAY

You can use Shift + and Shift - to turn subdivision display on and of on selected polygonal objects. This creates a viewport subdivide that lets you see what the shape would look like subdivided. These hotkeys set the Display As parameter which can be found at the object level on the object’s Render tab. 

Your object will not render with subdivisions unless you turn on Render Polygons As Subdivision Surfaces on the same tab. 

05 Press c to bring up a radial menu and choose Model > Polygons > PolyExtrude. In the Scene View pane, use the handle to drag up the polygons and set Distance to 0.05. 

Tumble around and press s to go into select mode then select the botom four polygons of the box. Press q to repeat the PolyExtrude tool. In the Parameter pane, use the slider to set Inset to 0.025. 

Press q to repeat that tool and set a Distance of -0.175. When you finish, tumble back to see the top of the brick. 

06 Press 3 to go to edge selection and press n to select all the Edges. In the Scene view press tab and start typing Group... Select Group and in the Parameter pane, set the Group Name to bevel_edges. 

Next, set Enable to OFF under Base Group and then set Enable to ON in the Include by Edges section. Turn on Min Edge Angle and set it to 89 and then turn on Max Edge Angle and set it to 91. 

07 Press s to go to the Select tool. Press 9 to turn on the “Select Groups” option. In the popup window, click on the bevel_edges group. 

In the viewport, press c to bring up a radial menu. From this menu, choose Model > Polygons > PolyBevel. This adds a polybevel node and automatically fills in the Group field with bevel_edges. 

Now set the Bevel Ofset to 0.006. Under Fillet, set Shape to Round and Divisions to 3. 

08 Go to the object level and in the Network view, rename the object to single_brick. With the brick selected, press Shift + to turn on subdivision surface display for this shape. Deselect the brick to see the model subdivided. If you see wire lines on your object, press v and from the radial menu, choose Shading > Smooth Shading to hide them. 

Save your work. 

## Geometrysingle_brick

Transform Render Misc 

Material 

■ Display 

Display As 

Subdivision Surface /Curves 

Render Visibility 

Render Polygons As Subdivision (Mantra) 

Shading Sampling Dicing Geometry 

Categories 

Reflection Mask* 

# PART TWO

# Copy Bricks to a Point Cloud

You are now going to create a cloud of points that match the shape of a particular piece of geometry. You are then going to instance the bricks to the 3D grid to create a brickified version. The instancing is generated by packing the brick geometry then instancing them to the points. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2596f4f12134dcf72b3177b4164f4a2a83e64b8a6e417660d90f99f2c919e6f3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/be22f79f8a0731560eaa3224dbb664fb97e02980d83dbb06dc6d8ebcb68a177f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b4554830de4bcf54b3d86dd3fda954b06686d712771d067c2f4d42027a586896.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dc342a5dc917a49b181b0f42e6641e2f4f74923f6ef0f0d99f71ab8c78c8707e.jpg)


01 In the Scene View, press tab and start typing Test... then choose Test Geometry: Rubber Toy. Press Enter to place it at the origin. 

Press i to dive into the test geometry object. Set the following:  Uniform Scale to 3 

Now add a Match Size node and set Justify Y to Min. This raises the toy so that it sits on the ground. 

02 In the Network editor, RMB-click on the output of the matchsize node and type Points... then select Points from Volumes and place it’s node in the network. Now set its Display flag to focus on the output of this new node. 

Press s to go to the select tool and press 2 to get point selection and then press n to select all the points which will highlight in yellow. You will copy the bricks to these points. 

03 Press u to go back to the Object level and shorten the name of the rubber toy to rubbertoy. In the Network view, press the shift key and click on the rubbertoy and then the single_brick. 

From the Modify shelf tab, select Combine to bring these objects together. You are taken to the geometry level and the nodes are feeding into a merge node. 

04 In the Network view, select the display_merge node and press the delete key. Now the polybevel node chain is displayed and the other chain is not. Houdini lets you choose which node you want to display which would be the node that will be visible when you go back to the object level. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/099819cdc6ea8f35e69aed214963ac02fd7088ea647ad1d20cb576afac46aa51.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0e278a41223f021d554fdef003f74dd64e098e5f122d8c5dd720c9d61e242f47.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bee42ef729f0fbb3a3e5852eb71532b6adfb88d20627cb17600988e4f30bfcf0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/161c26c5ded14ec5fbfca9549fabb407216d049f20972369b12d73fe3dac9eb3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e601754e26260d873002406288da26ff498eeb3872a72991a3768ce55f012ca4.jpg)


## PACKED INSTANCES

If you leave Pack and Instance seting OFF on the copy to points node then you will end up with a large model with over a million points and primitives. This would make it very slow to manipulate in the Viewport because instancing is not being used. If you turn it ON then the 338 points on the brick model are packed up and instanced which leaves a much more eficient point count for the copy to points node. 

05 RMB-click on the output of the polybevel nod, start typing copy... and select Copy to Points node. Click to place the node below the two chains and set its Display Flag. Turn on the Pack and Instance option. This is important because it will display the copied bricks much faster than if this option is of. At this point there is an error on the node because we haven’t connected the second input. 

06 Click on the dot under the pointsfromvolume node then connect it to the second input on the copytopoints node. The bricks appear to be overlapping. Go back to the pointsfromvolume node and set Point Separation to 0.2. Now you are copying bricks to the points of the grid. 

07 Click on the copytopoints node. Some of the bricks may appear dark grey and don’t display the proper brick. This is because of geometry culling in the viewport. You can fix this with a display seting. 

In the Scene View, press spacebar-d to bring up the Display Options. Click on the Optimize tab and either set Scene Polygon Limit to a number higher than 50 million or set Distance-based Packed Geometry Culling to OFF. Close the floating panel. Now you can see all of the bricks being copied to the points as Packed Instances. 

08 Before saving your work, let’s Organize the network. Select the nodes that make up the single brick and press Shift-O to create a network box around them. Click on the title bar of the box and enter single brick. You can then collapse the box and move it down to de cluter the network a bit. 

Save your work so far. 

Points 1,024,816 Center 0, 2.025, 0 

Primitives 1,018,752 

Vertices 4,075,008 

Min -3.1, -0.5, -2.7 

Max 3.1, 4.55, 2.7 

Polygons 1,018,752 

Size 6.2, 5.05, 5.4 

## PACK AND INSTANCE | OFF

Points 3,032 Center 0, 2.025, 0 

Primitives 3,032 Min -3.1, -0.5, -2.7 

Vertices 3,032 

Max 3.1, 4.55, 2.7 

Packed Geos 3,032 Size 6.2, 5.05, 5.4 

PACK AND INSTANCE | ON 

# PART THREE Add Color and Switch to a Teapot

You are now going to add color to the points which will then be picked up by the instanced bricks. At first this transfer of color only applies in the viewport but seting up a proper material lets you set up the point colors for rendering the bricks. You will then set up a switch between the rubber toy and a teapot to make sure that your network works with diferent shapes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e26933a79afdc11c11b7cb4536f453999ea00742173dfe243e65e32e2a2c4b2d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/72de3508dd2ab460e4b1714f420dad7956b5c3c552864cebb656bd10fb687f27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2030d05861b3ad2ab2d3759ad17cba6a871eadda04117d9b3d1f1a6c02219033.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/67d4fb65055dd9873ff41b3527fec652a4f7957cbbd107d0734263e9473315e3.jpg)


01 Add a color node between the pointsfromvolume node and the copytopoints node. This will add color to the points which will get copied to the bricks. Change the color to red to help the bricks stand out against the background. 

Click on the Render Region tool and drag a bounding box over the rubber toy. This kicks of a test Render and you can see that the bricks are not rendering as red. You need a material assigned that picks up the color. 

Click the x buton in the top right of the render region to close it. 

02 Press tab in the Network view and type Mat... Choose the Material Network tool and click to place the node down in the network. 

Go to the Material Palete and close /mat and open up /matnet. Drag a principled shader down into the matnet. Name it brick_mat. 

03 Go back to the geometry network using the back buton in the Network view. RMB-click on the output of the copytopoints node and type Material... Select material and place it’s node in the network and set its display flag. 

Click on the Operator Chooser buton on the far right of the Material parameter. From the pop-up window, navigate to and highlight brick-material. Turn on the Export Relative Path Option and click Accept. 

The material is assigned but the bricks still don’t render. 

04 Go back to the Material Palete and select the brick material. Click on the Surface tab then set the Base Color to 0.5, 0.5, 0.5 and turn ON the Use Packed Color option. 

Click on the Render Region tool and drag a bounding box over the rubber toy. The rendered bricks should now be red. 

If not then click Render in the top bar of the Scene view to make sure the changes have been applied. 

Save your work so far. Click the x buton in the top right of the render region to close it. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6c30251428a066cb84a40c8699fd18147dcf09bc75508db209d6348e925840d1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/456237af865a430a466525454321b46cf3d9dc8b9d6f942f5497f404feefa896.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1695c072f6a44ff96ae88d8950d4efc15da424d1de0d300646cede23e106a7f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/42efb8156a317440a8f7e379f51661bbd1c11e9c9a10f3edfde5cf00825ce3a1.jpg)


05 Go back to the geometry network using the back buton in the Network view. Press s to go to the select tool. In the Network view, press tab and type the word Switch then from the Sourcing folder drag it into the Network view. 

Next, drag it over the line connecting the rubbertoy node to the matchsize node. This inserts it into the network between the two nodes. 

This node will make it easier to switch between diferent incoming shapes. 

06 In the tool shelf, go to the Create menu and drag the Platonic tool down to the network view. This places a platonic node at the geometry level. Tools can be dragged into the network view as long as the node type makes sense for your current network level. 

Set the platonic node’s Solid Type to Utah Teapot. Set Radius to 4.2. The volume from points node will update the points to match the new volume to generate a diferent configuration of bricks. 

07 Connect the output of the platonic node to the input of the switch node. Now you can select the switch node and change its Select Input to 1. The platonic shape has been cubified using the same setup as the rubber toy. 

This is one of the big benefits of a procedural system. Later you will package up this network into a custom tool called a digital asset. As a digital asset, it will be easier to share the network with others and to manage the tool as it gets deployed in a studio environment where changes and updates are inevitable as the tool evolves. 

08 Use the switch node and set the Select Input to 0 to go back to the rubbertoy. You can now go back and forth between these two shapes and even add more shapes to see them brickified. 

Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dd64b06f855df013aa2fc64c9c023d8fe116d1a01fea8780d9cf8d4767813ee3.jpg)


## SWITCH NODE

The Switch node is a great tool for providing options within a node network. This node lets you quickly explore multiple options without the need to wire and unwire diferent chains. 

This node is also very useful when you wrap up your network into a Digital Asset because you can promote the switch to the asset as either a menu or a slider for quick access to diferent options. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/37af9090396e1e6eac9a6ef82c0a0987a263ada3db0bd6432db03aa8e4c6ac6f.jpg)


# PART FOUR Color the Points using a Texture

Earlier you added a color atribute to the points which afects the coloring of the bricks instances. Instead of using a single color, you are now going to use a texture map to create a more interesting look for the bricks. This will involve some special nodes to turn the texture into point colors. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8ef81c5ebdf49f38578c1544e933d8d53ee98f2dd7329230c9bcb7572154a4f6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ac7de65c4d3ec57152934882c9e1492363b3020f4d178b5072eff8e50523494b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7d27c8702585decc22f1a17e3e20b11551f9d276bf13364ae9d4490dd8b3172d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f24056ec52badbe10ff0fe6e2c89d0b41657a0795b8e456d51c83651f5ab4382.jpg)


01 Turn on the Display Flag on the testgeometry_rubbertoy. Select the rubbertoy node and in the Parameter pane turn Of the Add Shader parameter. 

To hide the UV display in the perspective view, go to the Display Options bar and turn Of the Show UV Texture when UV’s Present buton. 

You will bring back the color on the bricks using a diferent method that involves pulling the color from a Texture Map on disk. 

02 From the Asset menu, choose Edit Asset Properties > Rubber Toy. In the Properties window, click on the Extra Files tab and select toylowres.jpg. 

Click the Save as File buton and save it into the tex folder. The texture was stored in the digital asset so that it could be shared along with the asset. You will use the texture on disk to add color to the bricks. 

03 In the Network view, press tab and start typing Atribute... Select the Atribute VOP node and place it into the network beside the pointsfromvolume node. 

Feed the output of the matchsize node into the first input of the atributevop node. Set the Display Flag on this new node. 

In the Parameter pane, set Run Over to vertices. 

04 Double-click on the atributevop node to dive down and use the tab key to add a Texture VOP. Feed it into the Cd input of the geometryvopoutput node. 

Add a UV coordinate node and feed it into the UV input on the texture node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e595503d0e04628fb147cf4e80a457da0d1b7ac8c79dbb209f73503e7865c3e5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4084d8881a664fa8fb676a1ef02ff27f2c608309a07c753d3aa7413ec6fff2ee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/930254966fe48613d257f682880e82aad1a080544fc9ab77419402e042e77988.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d3ec47e3cc1917ee752170dfd5768aab298c99789f8064dd55782a41ce4305b0.jpg)


05 Select the texture node. Click on the Gear icon on the far right of the Texture Map parameter and from the menu, select Promote Parameter. This will add this parameter to the upper level of this node. 

Click on the lit le knob that appears next to map. In the parameter pane, change the Label to Texture Map. 

06 Press u to go up one level. You can see the Texture Map parameter. Leave it set to the default Mandril.pic texture for now. You will add the toylowres texture map at the end. 

Add an At ribute Promote to the end of this chain. Set Original Name to Cd and Original Class to vertex. Leave New class set to Point. 

## Add an At ribute Transfer node. Wire the

pointsfromvolume into the fi rst input and at ribpromote into the second. In the At ributes tab click on arrow on the right side of the Points fi eld and choose Cd. 

Add a switch node aft er the color node and wire the at ribtransfer node into the switch. Rename this node texture_switch. 

Set the Switch to 1. Set the Display Flag on the copytopoints node. Now you can see the colors from the texture map being transferred to the copied points but the bricks are rotated. Turn of Transform Using Target Point Orientati on to straighten up the bricks. 

## 08 Set the Display Flag on the material node.

Select the at ribvop node and click on the File but on on the far right of the Texture Map parameter and navigate to the toylowres.jpg texture and click Accept. You can see that the texture map colors are now being assigned to the verti ces. 

Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d98a1d00be2319bcf80f4ac7bd1a2a6f2c8fbe64f4552e9bd06fe204cd5a3fe8.jpg)


## ATTRIBUTE TRANSFER

When you want to get at ributes from one piece of geometry to another, you can use At ribute Transfer which uses a Distance Threshold along with other parameters to get the at ributes copied over. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/159eadaf5833cf40ed62c5a9193aad7c85db72519c965059c06da1f12d66f6b0.jpg)


# PART FIVE Create a Brickify Digital Asset

Now that the brickify recipe is working and the nodes are wired together properly, you are going to wrap up some of the nodes to create a single Houdini Digital Asset [HDA] node. Now you can share the network with parameters from inside the asset promoted to the top level to create an interface that can generate unique results each ti me the asset is used. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/850e892a715e9e4134af49cc1d8c2b1617fc309e0ff23272d878445f9dd8507b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c0b81da372c28dded0768d910bbf4190f68fa378377ab9443ce96c893f7c682a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9ffe273bee56da4e4a1a3ed5d0b7e57084263aca094788ed624610923c95df58.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1f04565c5dc3eae40869a5d1a2436541fbf3f49ccf47ed3d22f4aac20e896928.jpg)


01 <sup>In</sup> <sup>the</sup> <sup>Network</sup> <sup>view,</sup> <sup>drag</sup> <sup>the</sup> <sup>platonic</sup> <sup>node</sup> <sup>of</sup> <sup>to</sup> <sup>the</sup><sub>side.</sub> <sub>Select</sub> <sub>all</sub> <sub>the</sub> <sub>other</sub> <sub>nodes</sub> <sub>in</sub> <sub>the</sub> <sub>network</sub> <sub>and</sub> <sub>fro</sub> side. Select all the other nodes in the network and from the Assets menu, select New Digital Asset From Selecti on.... This will collapse them into a single node. 

Set the Operator Name to brickify which in turn changes the Operator Label to Brickify. Click on the but on on the far right of Save to Library. Select $HIP in the Locati on sidebar and then double click on the HDA directory. Press Accept then click Accept again in the Create New Digital Asset dialog. 

02 This brings up the Type Properti es window and make sure the Basic tab is visible. Set Minimum Input to 0 so that you don’t “require” an input for the asset to work. The Maximum Inputs parameter is set to 1 which defi nes how many inputs nodes you will allow. 

This is the input that is currently connected to the platonic node. When you use this digital asset later, you will use this input to point it to a dif erent shape. 

Press Apply. DON’T press Accept because it will close the window. 

03 In the Network view, rename the new asset node brickify_asset and double-click to dive into it. Click on the switch node that is switching between the testgeometry_rubbertoy and the Subnetwork Input node. The input node is bringing in the platonic teapot shape from the level above. 

In the Type Properti es window, click on the Parameters tab. Click on the Select Input parameter name and LMB-drag it to the Existi ng Parameters list in the Type Properti es window. Drop it on the root to add it to the UI. Click Apply which adds the parameter but doesn’t close the Type Properti es window. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4e244711ff7d22f34e662f43c9b4965bdca1a96a7caee08b77258a70bccdf0e5.jpg)


## WHAT IS AN .HDA FILE?

When you saved your asset, it creates a .hda fi le on disk. HDA stands for Houdini Digital Asset and the asset defi niti on is stored in this fi le then referenced into your scene. This fi le contains informati on about the nodes, the promoted parameters, UI elements and more. This fi le can be referenced by multi ple people into dif erent shots for a shared experience. 

The assets being referenced into your scene can be managed by going to the Assets menu, selecti ng Asset Manager... and opening Current HIP File . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/727077396779f4d3a6f5a75d8109898160ef56071a4b29f68e5e3e0bf161ffd8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/281a48c53a0026f6591514037a9cba09677a95584d2b0c27516da96a83ca394a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/848ba253f5a3aa5dd03dd11d4a84ae3345250e500810bbbfd6681accfacd1d06.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9f924404dc7f816ed08fe71bd81d0c42dedbe698c0a51a49f9bd5adc9d556cde.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/15793e31a32f99849ea22189a70530e7fb7019354deabcfca6bb8fbc51f9a73f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dda3a80c39efcfb62efc661c2973f82340b3e58c795c96daf6de1b6011d1ef88.jpg)


04 RMB-click on brickify_asset in the Network View’s path bar and choose Parameter and Channels > Parameters. Now you have a floating Parameter window with the two brickify asset parameters. These are the parameters that will be available to anyone who uses this asset. Let’s add some more. 

The brickify node has a new parameter. Change its value from 0 to 1 and back to see how it afects your scene. The problem is the name isn’t very appropriate and a menu would work much beter than a slider in this case, so you are going to refine the UI using the Type Properties. 

05 In the parameter list, click on the Select Input parameter. To the left are options for refining how people see it. Change its Name to shape and its Label to Shape. 

Now click on the Menu tab and turn on Use Menu. Now under menu items, type 0 under Token and Rubber Toy under Label then press enter. Next type 1 under Token and Custom Shape under Label. Press Apply. 

Now in the floating parameter pane, you see a Shape parameter with a menu. Try it out to see how it works. 

06 Select the second switch node that sits just under the color and atributetransfer nodes and promote the Select Input parameter to the parameter list. Change its Name to look and its Label to Look. 

Now click on the Menu tab and turn on Use Menu. Now under menu items, type 0 under Token and Color under Label then press enter. Next type 1 under Token and Texture Map under Label. Press Apply. 

07 Now select the color node in the network and promote the Color parameter to the parameter list. This brings over the color widget and the color wheel as well as the RGB fields. 

Press Apply in the Type Properties window to see what this parameter looks like in the brickify_asset parameter interface. 

Note: If you press Accept by mistake the new parameter is saved to the asset but you will need to use the Asset menu and choose Open Edit Asset Properties... > brickify to reopen it. 

## 08 Now select the atributevop node and promote the Texture Map parameter to the parameter list.

In the Parameter description section, click on the Channels tab and change the default value to Mandril.pic. This is a default texture map that doesn’t require a path to load and is a more reliable default. Later you will reload the toylowres.jpg texture map. 

Press Apply in the Type Properties window and you will see this parameter in the brickify_asset parameter interface and the Mandril texture map is now coloring the bricks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5de18df6f83111079fa30a2160c92cb1201dccdd586087c8e7419381460c1acb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/afebf14ba2bef246cc5bc6afb9b640727f4d00d0a28649e4bd466c5289ccdac1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1b8943fe16ad7d6d0e648a8e9625d9d981ce4f1c255d5e802f01833972967317.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c25cbb74879cb577b162ebe6bfa565698ce4ce1e2148dadc0d5d9f0bf15628b.jpg)


09 To make it clear which parameters are associated with which shape, you can disable and enable them based on the menu choice. Click on the Color parameter and in the Disable When field, enter <sub>{</sub> <sub>look</sub> <sub>!=</sub> <sub>0</sub> <sub>}.</sub> 

This tells this parameter to disable whenever Color has not been chosen in the Look menu. Next, click on Texture Map and in the Disable When field enter <sub>{</sub> <sub>look</sub> <sub>!=</sub> <sub>1</sub> <sub>}.</sub> 

Press Apply and test the results using the Shape menu. You can see the parameters disabling when they are not needed. You could also hide them with the Hide When option but disabling is fine for now. 

10 The brickify_asset texture map parameter now defaults to Mandril.pic which is a more versatile default because it is a texture map that will always be available. To go back to the toy map, you would need to click on the file selector next to Texture Map and again click on $HIP then dive into the tex directory and select the toylowres.jpg file. 

The asset is now using the Mandril.pic because it is the default. 

## close the Type Properties panel.

In the Network view, press u to go back up one level. With the brickify_asset node selected, choose Assets > Lock Asset > Brickify from the main menu. Press Save Changes if prompted. 

If you double-click on the brickify_asset node to dive down, you can see that the network is greyed out and these nodes are protected. You can only manipulate this asset using its parameters. You will have to unlock the asset to make changes to its inner workings. 

## 12 Go to the Object level. Now Save your scene file to preserve the work you have done so far.

You now have the scene file and the .hda file which is being referenced into your scene to create the asset. You can use this library to create other instances of the asset in this scene or to add the asset to another scene. 

In the next section, you will test out your asset and find out if it is working properly. It is always good to have one working asset and one for testing to make sure it is doing what you want it to do. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/41a4f5f3272c08a1cece94ead4830ec77ef18a34cd9f174152bef77a767bda9b.jpg)


## LOCKING AND UNLOCKING ASSETS

You can lock and unlock selected assets using the Assets menu. When the asset is locked, it references the HDA file to determine how the asset behaves. If the asset is unlocked the active definition is in your scene file. When you lock it you will be prompted to save if there are changes. 

Assets 

New Digital Asset From Selection... 

Unlock Asset 

Lock Asset 

Save Asset 

# PART SIX Test the Digital Asset

A Digital Asset can be instantiated more than once in a single scene file. You are going to use this asset on a diferent piece of geometry to test how it works. It is always good to have a test version available so that changes set to the first asset can be quickly verified. The asset can also be used in other scene files once you have it working properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/31c88515ffde23e583994551768442128dc1e77fda5e7809972c3f9867047a06.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/958769c9cc9c9548a93dd5bbe9b86bf522df6c85d4480e3e5853bd9f54486c20.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b44e4fb85ca2491c88f5ed56215d52f5bb08e700dfc6eb36eab0e2b12d85f7fa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b1eebdf2f3f84a3fc41d9006b7f6208cfc88a0892ed582f51f7c8061cba352cb.jpg)


01 Use the tab key to get the Squab Test Geometry. Press Enter to place it at the origin then use the handle to move it to the side away from the rubber toy. 

Double-click on the new object node to dive down to the geometry level. Select the node and set Scale to 3 and Translate Y to 1.5. This will make the Squab a bit bigger than the rubber toy. 

02 RMB-click on the output of the test geometry node and start typing brickify... then select the brickify asset from the menu. This places the asset into this new network. 

Set its display flag and you will see another Rubber Toy colored Red. This is because these are the defaults for this asset. 

03 On the brickify asset node, set the Shape parameter to Custom Shape and how the squab is being brickified. The new shape is running through the node network inside the asset to create a unique result. The shape will be lifted above the ground some more because of the Match Size node inside the asset. 

This is how digital assets become tools that you can put into your pipeline to package up multiple actions into a single node. This is an approach that speeds up your workflow and helps you achieve more consistent results. 

04 Select the testgeometry_squab node. From the Asset menu, choose Edit Asset Properties > Squab. In the Properties window, click on the Extra Files tab and select squab_ difuse.jpg. Click the Save as File buton and save it into the tex folder. The texture was stored in the digital asset so that it could be shared along with the asset. 

Now use this texture on disk to add color to the bricks using the brickify node’s Texture Map parameter. 

When you are finished, go to the object level and name this object squab and the other one rubbertoy. Save your work. 

# PART SEVEN Animating the Bricks

It is possible to continue adding features to the asset and you will create an automating build-up animation for the bricks. This will involve adding more nodes to our network to make sure the asset has this new functionality. Once the results are saved into the .hda file, the features will be available for use by anyone using this asset in their work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/44971815f6ba8680391d122914fd5b03fd985db1829eeb14702559df31a0d26b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5c601d7ae924893fbb877df8ba9ba03ae500503b28596ae8d8f1ff12bffe6105.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ae9337a82093c027835911c7d65b0b3573f275a7760e2c9ceb40987d3260512b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2346014c732825304151e1abc9c0e1de66fd1acf27f92b1d1b215fe23933ec6.jpg)


01 Hide the Squab object and dive into the rubbertoy object. Select brickify_asset and choose Assets > Unlock Asset > Brickify. Double-click on brickify_asset node then RMB-click on the output of texture_switch and select Group by Range. Place the node and set its Display flag then set the following parameters: 

 Group Name to hide_points 

 Group Type to Points 

 Range Type to Start and Length 

 Length to ($F-1)*20 

 Under Range Filter, leave Select to 1 and Of to 1 

02 RMB-click on the output of the grouprange node and select Polygon > Blast. Place this node down then using the arrow next to Group, select the hide_points group. Now turn on Delete Non Selected to delete points outside the group. Set the Display flag on the blast node. 

Press play to watch as the points grow with every frame. Now set the Display flag back to the material node at the end of the chain and watch the bricks grow over time. 

03 Right now the bricks are coming in from one side instead of from the ground. This is because the points are appearing based on their point numbers. To control this, you need to reorder the points to create the look you want. 

RMB-click on the output of the texture_switch node and type Sort... then select the Sort tool. Place this node down and change Point Sort to Along Vector. With this set to 0, 1, 0, the points start at the botom and go up. 

Playback to see this result. Test out diferent vectors to see how it afects the animation. 

04 To let you choose whether you want to animate the brickify efect, you can add another switch node. In the Network view, Press tab and start typing Switch... Choose Switch and place the node down. Rename it animation_switch. 

Click on the output of the texture_switch node and feed it into the input of the switch node. Repeat for the blast node. This makes the original shape the first option and the animated efect the second option. Changing Select Input to 1 will reveal the animated bricks but for now keep it at 0. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a50d4520afe7a11ac2eb6d87e543d0a6443d04e77ea5ab844ede0214eafb2f95.jpg)


## Interactive Extra Files Save

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/51d0e94f4c275d61942fd4fdf2f1c4c0a7f57448ddbc8502f28b4254a7a31891.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/989d2160cd53c77586765665883e2d79ec9b4caf499f18fd30f986dccac4ca90.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cf691d2f6943fcf280e1b7832be30db22960ef1a24ed2a7c9151b43804a1e0d6.jpg)


05 From the Assets menu, select Edit Asset Properties > Brickify. Go to the Parameters tab and drag a separator from the Create Parameters section to the botom of the list. 

Next, drag the animation_switch node’s Select Input from the Parameter pane to just under the new separator. Set its Name to animate_bricks and its Label to Animate Bricks. Next, change its Type to Toggle which limits to you an on[0]/of[1] seting. 

In the Parameter Description section, click on the Channels tab and set the default value to 0 [of]. 

Click Apply to save changes. 

06 From the Create Parameters section in Type Properties, drag an Integer parameter under the animate_bricks parameter. Set its Name to build_speed and its Label to Build Speed. 

Turn on the Range option then set the first value to 1 and the second value to 20. Click on the lock next to 1 to make sure the number never gets smaller than 1. 

In the Parameter Description section, click on the Channels tab and set the default value to 1. 

Press Accept to save and close the window. 

07 This parameter isn’t atached to anything yet but you will now use it to drive the grouprange node’s Length expression. Select the new grouprange node and change the Length expression to: <sub>($F-1)*ch(“../build_speed”)</sub> 

At the end of the network there is an output node. This will ensure that you get the right output for your asset even if the Display flag is on another node in the network. 

With the brickify_asset node selected, choose Assets > Save Asset > Brickify from the main menu. This lets you save this expression to the .hda file without re-opening the Type Properties window. 

08 With the brickify_asset node selected, choose Assets > Lock Asset > Brickify from the main menu. You now have the brickify efect wrapped up into a custom tool which can be used on diferent shots by diferent artists. 

Go to the Squab network where the new features are available on the brickify node. Turn on the Animate Bricks toggle and set the Build Speed which might need to be set to around 30 because of the large number of bricks in this shape. 

Playback to see the results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/03da311f43caf6671617e8a7d1eb87fa06a7c3b3dce3c16c638876a89764997a.jpg)


## CONCLUSION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6eedda2f13ed3d694ebbe9bb754c1315e504fe16e58fd77e60f35ecca2e7f538.jpg)


## PART EIGHT

# Loading HDAs into other Applicati ons

Once you have a Houdini Digital Asset [HDA] saved on disk, it is possible to load that asset into a host applicati on using the Houdini Engine plug-ins. These let you share assets with colleagues who can load them directly into 3D apps such as Autodesk Maya or 3DS Max or into game editors such as Unity or Unreal Engine 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1b8a014b9d2586978b3f691a2705738c3dfe47284866b434f90e55390ea9f76d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5e30b9c683245d05d6eb1521ecfd6bbdf816a113184dd218e95958e7e491c260.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c93069ac52a7c953753374e730f5d0bbc2ab330ebb6a412add1839caf1cb3f1f.jpg)


01 To use the Houdini Engine in a host applicati on, you need to fi rst install the plug-ins using the Houdini installer or Launcher. This will make the plug-ins available but you may need to take further steps to make the Houdini Engine available within your session. 

Visit the following page for details: SideFX.com/engine 

Click on the Engine Plug-ins tab and then click on the desired plug-in for more informati on. Once installed, you will fi nd a Houdini Engine menu in the host applicati on. You can use this menu to load assets. 

02 Once you have the plug-in installed, you can load the asset using the Houdini Engine menu. This will bring the brickify asset into the viewport while the asset parameters become available for manipulati on. 

You can also turn on animati on for Maya or 3ds Max and play it the sequence using the ti meline. 

03 In Unreal, you can use the Import but on to bring digital assets into your scene. You can also set Shape to Custom Shape and connect the asset to geometry within the host applicati on and the brickifi cati on will be applied to that object. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4c999804f3c6178c9e5e5f3e21fc57acaecc44ba76d316e8cddb5f6b26d619d0.jpg)


## WHAT HAPPENED TO THE BRICK COLORS?

You may noti ce that none of the brickifi ed shapes are showing the brick colors within the various host applicati ons. This is because the plug-ins don’t always process informati on the same way as Houdini would. The point colors are sti ll part of the asset but the host applicati on is not receiving this informati on. 

And while the animati on works in Maya and 3ds Max, it would not make sense in Unity and Unreal Engine because Houdini assets can not become part of the runti me experience of a game therefore the built-in animati on would be ignored. It is important to tailor your assets for the capabiliti es of the host applicati on. 

## HOUDINI FOUNDATIONS SMASHING WINE GLASS

In this lesson, you will smash a wine glass then slow down ti me to hold onto the big splash. This ef ect involves both an RBD simulati on for the shat ered glass and a fl uid simulati on for the wine. You will learn how to set up the dynamic network and output the simulati ons. Visual ef ect shots oft en involve a combinati on of dif erent kinds of dynamic solvers and Houdini’s dynamic network is designed to achieve a unifi ed result with these dif erent solvers. 

You will also use a reti me node to slow down the simulati on when it is at its most explosive then reverse ti me to return to the starti ng point. You will then move the simulati ons into Solaris/LOPS, set up lights and a camera, then render the shot using the Karma renderer. 

## LESSON GOAL

To simulate a bullet smashing through a wine glass causing the glass to break and the liquid to splash. 

## WHAT YOU WILL LEARN

 How to model the Wine Glass, Bullet and Liquid geometry 

 How to pre-fracture the glass geometry using Booleans 

 How to run a Rigid Body Simulati on of the bullet smashing the glass 

 How to run a FLIP Fluid Simulati on of the liquid splashing 

 How to reti me the simulati on to slow it down then go back in ti me 

 How to export the results as USD for use in Solaris/LOPS 

 How to set up lights and materials in Solaris/LOPS 

 How to render the fi nal shot with Karma 

## LESSON COMPATIBILITY

Writ en for the features in Houdini 19.5+ The steps in this lesson can be completed using the following Houdini Products: 

<table><tr><td>Houdini Core</td><td>✗</td></tr><tr><td>Houdini FX</td><td>√</td></tr><tr><td>Houdini Indie</td><td>√</td></tr><tr><td>Houdini Apprentice</td><td>√</td></tr><tr><td>Houdini Education</td><td>√</td></tr></table>

Document Version 2 | Sept 2022 © SideFX Soft ware 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/676b29ac9e5292db58324250fbf4c6242d892dffd0314588a6f5b592fded28ab.jpg)


# PART ONE Model the Wine Glass

To start, you will draw a polygonal curve then revolve it to create the wine glass. Creasing will be used to sharpen some edges and then you will subdivide to create denser geometry for fracturing. You will then extract geometry from the wine glass to create a shape that you will use to simulate the fluid. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/81f97dcf546c87c8749aec62d4df090f9336a47817233773257db0d76d8010ca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/73da84796971093a7951728a4aafb180a66b4e07cc3b2d678a25966769968f22.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f465f483a97ebcbd815f65507393e97c44dc935d4d4f840220890f51f43f3d12.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/affd5b6d9043ff8c526c0245a04b1856df6a8d9af4692e626fbc6c74ccf12204.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c94a7f810902988539a1ad551d6452cfd32595d0ba2bc09294273a7ae5dd2521.jpg)


# PROJECT FILES

Go to the fluids tutorial page on SideFX.com, where you got this document and download the fluids_lesson_start directory. Rename it fluids_lesson then put it into the Houdini Projects directory. 

01 Select File > Set Project. Find the fluids_lesson directory (see instructions above) and press Accept. This makes the project directory and its sub folders the focus for all the files associated with this shot. 

Select File > Save As... You should be looking into the new fluids_lesson directory. Set the file name to wineglass_01.hip and click Accept to save. Now you will be able to access the reference images in the Tex folder. 

02 In the Scene view, Press v to bring up a radial menu and choose Viewport Layout > Four Views Move your cursor over the Front panel and press spacebar-b to expand it. 

Hit D with the mouse in the viewport. Click on the Background tab and on the Front tab , use the file picker to navigate to $HIP then tex>wineglass_profile.jpg. Set the following: 

 Make sure Auto-Place is turned OFF 

 Image Ofset to 0, 3 

 Image Scale to 5, 5 

Now if you dolly or pan the view, the background moves with it. 

03 On the Polygon shelf, click on the Curve Polygon tool. This creates a Curve node with the Primitive Type set to Polygon. Press x and choose Grid to turn on grid snapping then click on point A and then to the second point which also sits on a grid point. Turn Grid snapping to OFF then keep tracing the image. 

Turn Grid snapping back ON for the final four points at the base of the glass to make sure they are aligned. When you finish at point B, press Enter to complete the curve. Turn Grid snapping to OFF. 

You can then click on the Edit Mode buton in the Operation Controls bar to move any points that missed their mark. 

04 <sup>Press</sup> <sup>Spacebar-B</sup> <sup>to</sup> <sup>go</sup> <sup>back</sup> <sup>to</sup> <sup>a</sup> <sup>four</sup> <sup>view</sup> <sup>layout</sup> <sup>then</sup> mouse over the perspective view and press spacebar-b again to expand it. Now you can see the curve in 3D. 

Press s to get the Select tool and press n to select all the primitives on the curve. Press c and choose Model > Curves > Revolve. This will turn it into the wine glass model. 

Press 3 to go to edge selection then double click on the top edge of the glass then press Shift and double click on the second top edge and the two edges of the base. Press tab > Crease then set Crease to 0.75. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/58178d3f72a0612c08f2ac673cae73e9a030425d0359e80f58989ac89780c901.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8d5e86a1cc5a92bdc2d65b506c1c7e0de8f3fbe6fc7e0ea3a9b4e05574081d7a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c652d7a550e7369471813f77734b0cf238c31424e7e3d1896ccdc82e86d896e8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3bd7d6c38ab5b6126230973bd467dbd698e72e1cf05cdfe6d4ca5fef705b4388.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/abf0f532f115d7a38920b2f518d0d07719c0bbf47dcfcefea76a68e9aae5d969.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cda479e7c666226cc9b0beb8a659f13409d11914066959e5f016b6d6baa309a2.jpg)


05 Press 4 to switch to primitive selection then press n to select all. Now press tab > Subdivide. Set Depth to 2. 

This will subdivide the model with the creased edges set up to be sharper than the other areas of the model. A higher Crease weight could make these edges completely sharp but for now a softer look works beter. 

In the Network editor, add a null node to the end of the chain and set its display flag. Rename this node to GLASS_OUT. 

Go back up to the object level and rename the object to wine_glass. 

06 With the wine_glass node selected, press n to select all the primitives then go to the Modify shelf and click on the Extract tool. This will create an objectmerge of the wine glass geometry and place it into a new object. 

From the Front view, select the faces at the top of the wine glass and then press delete. This adds a Blast node into the network that removes the faces. 

Note: You can still see a ghosted version of the original wine glass because the Scene View is set to Ghost Other Objects. This seting is useful to add context to your work. 

07 Now go back to a Perspective view and double-click on the base of the wine glass and press delete. This adds a second blast node. Now you are left with interior faces where you want the liquid to be. The faces of the wine geometry will appear dark on the outside. This means that they are the back sides of the primitives. 

Press n to select all the primitives. Press tab > reverse to reverse the normals so that they are facing out. The darker side of each primitive will now be on the inside of the shape. 

08 Press 3 to change to edge selection then double-click on the edge of the shape to select the open edge. Press tab and start typing polyfill. With Polyfill highlighted, press Enter. 

Set the following: 

 Fill mode to Quadrilateral Grid 

 Tangent Strength to 0. 

This creates a closed shape that will become the source for the FLIP Fluid later in the lesson. 

09 Press 4 to change to primitive selection then press n select all of the primitives. Press c and choose Model > Polygons > PolyExtrude. Set Distance to 0.01 to create an overlap with the wineglass to help the fluid render properly. 

In the Network editor, add a null node to the end of the chain and set its display flag. Rename this node to FLUID_OUT. 

Go up to the object level, rename this object to wine. 

# PART TWO Model the Bullet

To create the bullet geometry, you will start with a primitive sphere and slice it in half. Next you will polyextrude the open end then use polyfill to close the shape using quad topology. You will then subdivide to define the final shape. This object will be moving very quickly therefore lots of detail isn’t required. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/704fd07bf6e87671b018c4c129e41acdf14e9315415255a9d25c22a50c9ce7a3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3831db0a90eb6737bac2b74a7fe78d4a2ad8cffb13e5569d3e9f993d79d2ab7f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3efd7cb137d157f09dfd12ee5a0bb9d46c2c8ea0daff5499bafd8d76670661d6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9381f1405a617fbfeb3db9a7deb90308d96f9c5df346e37625f37b16e4490c6d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/428a7371c6c25b8d2ee346556505a139fd190930f6f714f79b7e2b9fb2e8ab50.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f1052632064e5369865a0dd29f9bbef672bcf574ed569e86e3895fb2b24241ef.jpg)


01 Go to the object level and in the Network view, turn of the Display Flags for the wine and wine_glass objects. In the Scene View, press c and choose Create > Geometry > Sphere. Press Enter to place it at the origin then dive inside and set the following: 

 Orientation to X axis 

 Radius to 0.2, 0.125, 0.125 

 Columns to 12 

Press tab > clip in the Scene view then press n to select all the primitives and press Enter and set the Direction to 1, 0, 0. 

02 <sup>Click</sup> <sup>on</sup> <sup>the</sup> <sup>Select</sup> <sup>tool</sup> <sup>then</sup> <sup>press</sup> <sup>3</sup> <sup>to</sup> <sup>turn</sup> <sup>on</sup> <sup>edge</sup> selection and double click on the open end of the sphere. Press c and choose Model > Polygons > PolyExtrude. 

In the Extrusion tab, set the following: 

 Transform Extruded Front to ON 

 Translate Z to 0.04 

 Scale to 0.7, 0.7, 0.7 

This adds a litle extra geometry before you remove the triangles at the front of the bullet then close the shape. 

03 Tumble around and press s to get the select tool and 4 to get face/primitive selection. Select one of the triangles at the tip of the bullet then press and hold the a key and then middle click two triangles over to select all the triangular faces. Press the Delete key to remove them. This adds a blast node to the network. 

In the Network View, press tab > polyfill and place the node after the blast. Set Fill mode to Quadrilateral Grid and Corner Ofset to 1 then turn on its display flag. This will close both ends of the bullet with good quad topology. 

## 04 Now add a Subdivide node at the end, set Depth to 2 and then set its display flag.

In the Network editor, add a null node to the end of the chain and set its display flag. Rename this node to BULLET_OUT. 

Go back to the object level and rename this object bullet. Turn on the display flag for the wine_glass. Translate the bullet to about -20 in X and 5 in Y. You may want to go back to the Front orthographic view to make sure it is aimed at the desired impact point on the wine glass. 

Save your work. 

# PART THREE Fracture the Wine Glass

To define the cracks in the wine glass, you will create natural looking lines using the draw curve tool then extrude them into sheets of geometry. You will then agitate the surfaces using the mountain tool. This chaotic looking shape can then be merged into the wine glass object where you will set up a boolean operation that uses the sheets to shater the glass. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/597402a9f52899e929e547c2337ca6d543748b668a9606311eb422b189e6436e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a6c4a43ce9166b2b58ca84cff1ba367ac55e077a2453d84acd2f8d654e03ab67.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f780b521910d8ea423ac661214b3ad3771642c715a23c9726a5b78e2f00ee631.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/56fc57f964c610b411f88ad56f57309de0ed3d2f825dd504c357305cabd301cd.jpg)


01 In the Scene View, go to the object level then press c and choose Create > Geometry > Grid. Press Enter to place it at the origin then i to dive inside and set the following: 

 Orientation to YZ Plane 

 Center Y to 4 

 Size X to 5 

 Size Y to 8 

 Rows to 16 

This will create a drawing surface for the Draw Curve tool that matches the shape of your wine glass. 

02 Go to a Right view and press v > Shading > Wireframe to go into wireframe mode. You can see the bullet siting behind the grid and the wine glass. Press n to select the whole grid then go to the Create shelf and click on the Draw Curve tool. 

Draw curves over the wine glass that converge where the bullet hits the glass. Also add some curves across the stem of the glass since that will shater as well. If at any point you draw a curve you don’t like, press Ctrl-Z to undo it. 

03 Go to the Select tool then Press n to Select all the curves then press c and choose Model > Polygons > PolyExtrude. Set Divisions to 4. 

In the Extrusion tab, set the following: 

 Transform Extruded Front to ON 

 Transform Space to Global 

 Translate X to -4.5 

Next, click away then select all the geometry and press tab > Transform. Set Translate X to 2.25 to center this geometry around the origin. 

04 Press s to bring up select tool, then press 4 to go to primitive selection. Double click on one of the sheets to select the whole thing. Press tab > Duplicate to create a copy. Use the Rotate [r] handle to reorient the duplicated sheet to be almost orthogonal to the others, making sure it cuts through the cup but avoids the stem. This will break the cup in the other direction to create more realistic slivers of glass. 

Repeat with another sheet to create another surface for cuting at a diferent angle. 

The Boolean node is oft en used to create traditi onal booleans such as Union, Intersect and Subtract. While these work well with closed shapes, you can use the Shat er opti on to slice up the geometry with sheets. Houdini has a Voronoi Shat er tool that can also be used but it will not give you the jagged look you need for broken glass. There is also an RBD Material Fracture node that can create glass-like fractures. These work best with fl at surfaces which is why it wasn’t used in this lesson for the wine glass. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b99922ff4818ff422f0feffd2c7198b5d46d579b781069826ff7258023d86672.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dfe810ad45dfbe16ae94d2f7666309340f147f8c7a77749de0593b95f45dfb46.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2d2174157a8f0f2227ad2a38acbd22edfd2070b4e6c8c2803275e2ae8f163bd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/10044a29a2d1abbbcf1a782e352a4f343bd4eef5cbcb4f09739bd0a8bb3d806f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7a5ed29237eaacc05ca8447225b5943b86bff9d6af891a77150ed392d87ab272.jpg)


05 Select all the geometry and then press tab > Mountain to add some noise to the points on the dif erent sheets. Set Amplitude to 0.75. This will create more interesti ng cracks in the glass. 

In the Network view, add a Null node to the end of the chain and rename it FRACTURE_OUT. Set the display fl ag on this node. 

Go to the object level and name this node to fracture_geo then turn OFF its display fl ag to hide it. 

06 Next dive into the wine_glass object. In the Network view, press tab > object merge and place the node down. Click on the node selector next to Object 1 and navigate to fracture_geo > FRACTURE_OUT and select that node. Make sure that Transform is set to Into Specifi ed Object . 

This brings the agitated sheets into the wine glass geometry network where you can use it to boolean shat er the glass. 

07 In the Network view, press tab > boolean and click to place down the new node. Wire the subdivide node (not GLASS_OUT) into the fi rst input and the object_merge into the second. Set its Display fl ag then set the following: 

 Set B: Treat As to Surface 

 Operati on to Shat er (Pieces of A) 

To visualize the cracks, add an exploded view node at the end of the chain. If you want to change how things work then you can go back to the fracture_geo object and edit the sheets. Those edits will update procedurally. 

08 In the Network view, add a Null node that bypasses the exploded_view node and rename it GLASSFRACTURE_ OUT. Set the display fl ag on this node. 

You now have two output nodes for this network. GLASS_OUT gives you the wine glass in its original form and GLASSFRACTURE_ OUT gives you the shat ered glass. You will use them both down the line to complete the shot. 

Save your work. 

# PART FOUR Set up the RBD Simulati on

You are now going to create a rigid body simulati on using shelf tools. This will add a DOP (Dynamic Operator) network that brings together geometry, forces and a solver node. In the wine glass geometry network, nodes will be added to prepare the geometry for simulati on. You will use convex proxies so the Bullet RBD solver can handle the odd-shaped pieces of glass. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8c650896a85acb667ab137585caadc5f03e18898e9e63b296a70343d85b9a5f0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bdda8c6fae5f8e4a2a979d393f436398d52ea5d1c43d92797c76562a27168a16.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/60a3119288efeb1c95cb9f56aafefc894b94e6f0de2577a762090a0c452eccf7.jpg)


01 <sup>Go</sup> <sup>up</sup> <sup>the</sup> <sup>object</sup> <sup>level,</sup> <sup>select</sup> <sup>the</sup> <sup>wine_glass</sup> <sup>object</sup> <sup>then</sup><sub>from</sub> <sub>the</sub> <sub>Rigid</sub> <sub>Bodies</sub> <sub>shelf,</sub> <sub>click</sub> <sub>on</sub> <sub>the</sub> <sub>RBD</sub> <sub>Convex</sub> from the Rigid Bodies shelf, click on the RBD Convex Proxy tool. This will set up the initi al dynamics network for you. It is called AutoDopNetwork. Press v > Shading > Smooth Wire Shaded. 

This tool is used to break down the parts of the wine glass into convex shapes that can be used to create complex collisions. These will appear rougher than the source geometry but aft er the simulati on, you can go back to visualizing the cleaner topology. 

02 Go to the Collisions tab and click on the Ground Plane shelf tool. This will create an infi nite ground plane for your geometry to collide with. 

You can turn Of the Display fl ag on the groundplane_object to hide it from the scene view. It will sti ll functi on as a colliding surface in the simulati on. 

03 Dive into the AutoDopNetwork node. Select the wine_ glass node and in the Physical tab set Density to 2000, which is approximately the density of glass. 

Press Play in the playbar to see what happens. The glass falls and hits the ground. Right now gravity is the only force acti ng on the pieces. 

You could set up a glue network to hold the pieces together unti l impact but the bullet will be so fast that connecti ng the parts is not necessary. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/82a67bc4a500cf762f4f03328b497ac43596c1082a7362266ef05cba5b145cf5.jpg)


## CONVEX DECOMPOSITION

For RBD simulati ons, Houdini uses the Bullet solver which prefers convex shapes in order to maintain fast simulati on speeds. Convex Decompositi on lets you take shapes that are concave and break them down into convex shapes that are connected together. These are then simulated as one composite piece by the Bullet solver. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dfd771a88f186431f6a7142a7726218850a4ff11371e1a430991a68b603b0500.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5c4d33db31d110da14d88ec26cd559bfe3dad433d62692cb6fd9b8282f67b494.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2f6ca76fb673b5100259de52492f33add08e7b42519cec395df79958d2443ce0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/67e69d05d207e8d55227f98f68d985e0b9031cc7f30e1d85f0295d48bb50dacc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9c1f52913bb52304ea010477cc444657281fefd93ccf1f159c35dacc2ad2c1e2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/16f0787c3d79f7ff2464cbf77c6ad42e47ea0265c4ffd14f6c3570fb104123b6.jpg)


04 Go up to object level and dive into the wine_glass object. A number of nodes have been added to create the proxy geometry and this chain ends with the dopimport node which is currently displayed. 

On the convexdecomposition node, you can change Max Concavity to 0.05 to adjust your collision geometry. 

Press Play to watch it simulate. 

05 Go up to object level and select the bullet object and then go to the Rigid Bodies shelf and click on the RBD Objects tool. This will create a packed rbd object from the bullet and add it to the dynamics network. 

Navigate into AutoDopNetwork and select the bullet node. 

 In the Initial state tab, set Velocity to 400, 0, 0. 

 In the Physical tab set Density to 20000 

This is the density of lead and should work well for the bullet. 

06 Before you simulate, you want to make sure that the base of the glass stays on the ground. Navigate into the wine_ glass object and in the display bar, turn on primitive numbers. You can see that in this case the base packed primitive is 171 - yours will probably be diferent. 

Add an Atribute Create node between the create_packed_primitive and proxy_geo nodes. Set the following: 

 Group to !171 (or whatever number your base is) 

 Name to active 

 Value to 1, 0, 0, 0 

07 Next, set the display flag on the transform_hires node and open up Global Animation Options and set End to 50. 

Now play back the sim. You can now see the source geometry being animated to match the proxies but the collision is as dramatic as it could be. 

08 The Bullet sim defaults to 10 substeps on the solver. This isn’t enough to resolve collisions for the speed the of the bullet. Go up to the object level and on the AutoDopNet node set Substeps to 5. This will add substeps on top of the solver seting. This may take longer to simulate but will increase accuracy and generally make the simulation more active. 

Play the simulation again to see that the collisions are looking much beter. Go back and tweak setings if you want too change things. You can even go back and reposition some of the cracks. 

Save your work. 

## PART FIVE

## Add Fluids to the Simulation

Now that the bullet is smashing the glass, it is time to convert the wine object into a fluid that will become part of the integrated simulation. This means that the RBD and Fluid simulations take place in the same DOP network and will work as one system. At first, the fluid will be represented by particles that can then be surfaced to visualize the fluid. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/18cc6689fc0c8bbab1b4de7bdf2fb235efb498a35703c79a8e3d8b0f03a70e7e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/429a2bebbd32938672366d6ae55c2b2a9dc2ebecc9eccb6a7b15496765989632.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dc793830fcdea70a5cd63ec8e265ca2e8d4b97535e2086c792b66d841a42b5d5.jpg)


01 <sup>Go</sup> <sup>to</sup> <sup>frame</sup> <sup>1.</sup> <sup>Select</sup> <sup>the</sup> <sup>wine</sup> <sup>object</sup> <sup>in</sup> <sup>the</sup> <sup>Network</sup><sub>view</sub> <sub>and</sub> <sub>from</sub> <sub>the</sub>  <sub>shelf,</sub> <sub>click</sub> <sub>on</sub> <sub>the</sub> Particle Fluids FLIP Fluid from Object tool. 

This turns the fluid into a volume of fluid particles. In AutoDopNet, select the flipfluidobject node and set Particle Separation to 0.05. This creates more particles which in turn adds more detail to the simulation. 

02 Select the flipsolver1 node and click on the Particle Motion tab, under Behavior set: 

 Add ID Atribute to ON 

Under Reseeding set: 

 Reseed Particles to OFF 

In Volume Motion, set: 

 Velocity Transfer to (APIC) Swirly 

Under Surface Tension, set: 

 Enable Surface Tension to ON 

 Surface Tension to 500 

03 Press Play to run the simulation. With extra substeps it will take a litle longer but will give you more accurate results. Simulate to just past frame 10 and press Escape to stop the sim. Go to frame 10 to preview the fluid so far. 

To see it as a surface, go up to the object level and go into the wine fluid object. Set the display flag on the Render null node to see the surfaced fluid. This will take longer to cook but will show you what the surface is going to look like at each frame. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/469efb27e1b70ec70a0b297d6ad8442c4940b9cb9472253c90147b3f565ddf59.jpg)


## DISPLAY AND RENDER FLAGS

When the wine_fluid geometry network is first created, the Display flag is on the dopimport node which shows particles while the Render flag is on the null node which flows from a particle surface node. This set up is meant to give you fast performance in the viewport and if you render then you see the final surface. In this lesson, you will be caching out the surface therefore these nodes will not be used to render. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ee4ec0b628fcec4e5fbb35a22e24918339fef78224d3ceab107f48a9bbae95cb.jpg)


# Cache and Retime the Simulations

For this shot, you only need to compute 10 frames of the simulation. You will save this to disk then use a retime node to create a longer shot where the fluid slows down then reverses in time. The retimed fluid particles will then be surfaced and output as a 50 frame sequence which will define the final shot for rendering. The wine glass and bullet will then be retimed to match. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9e2404ea42e970480e1ad37f818592fa10df094aad99153f22b128adf4038ae1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7867229d7767fb9dccba4194a7e8db2c6da516a32d88ba04ed30ac9c66d6858e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/910bf9c2b552bbdc9f26598c8b5dd2d8b97a9e67654c8a0daf25ca6b1be3bf35.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/544f9d426fa05cae9e1f4c097ee7fc44c9f7cce60b2e667d63074308a308b7aa.jpg)


01 At the object level, delete the wine_fluid_interior node that the shelf tool created. Dive into the wine_fluid object. Delete all the nodes except the import_wine, compressedcache node and the particlefluidsurface nodes. 

On compressed_cache, set the following: 

 Base Name to wine_fluid 

 Base Folder to $HIP/geo/fluid/ 

 Turn Of the Version check box 

 End to 10 (RMB-click > Delete Channels first) 

Hit Save to Disk. 

02 When it finishes, stay at the geometry level. From the Visibility menu in the top right of the Scene view, select Hide Other Objects. 

Set Load from Disk to On and Scrub through the geo sequence. It will only play for 10 frames. You are now going to retime the sequence to stretch it out over 50 frames and slow down the efect. 

03 Add a Retime node after the compressed_cache node and set its Display flag. Set the following: 

 Evaluation Mode to By Frame. 

 Turn ON the Scale Velocities option 

RMB-click on the Frame field and choose Delete channels. 

 At frame 1: set Frame to 1 and Alt-click to keyframe 

 At frame 5: set Frame to 1 and keyframe 

 At frame 10: set Frame to 7 and keyframe 

 At frame 40: set Frame to 10 and keyframe 

 At frame 45: set Frame to 1 and keyframe 

04 Click on the Animation Editor pane to see the animation curve you just created. Press h over the graph to home the view and then RMB-click-drag to zoom out a bit. 

Click and drag on the curve handles to get a shape similar to what you see here. If you need to break tangents on a curve, select the key and press T to untie the tangents. Then select and drag on each end individually. The goal here is to have the liquid splash out quickly then slow down until is freezes for a short time then speed out into a fast reconstruction back to its original shape. 

The most interesting part of the smashing wine glass is the first 10 seconds. To emphasize this part of the simulation, you are going to save out the fluid particles for the 10 frames then uses the retime node to stretch out the sequence in a sort of “bullet-time” efect that snaps back to the original wine glass by reversing time. Once you have this set up for the fluid, you can surface the points and save out a longer sequence. The same retime node can then be copied and pasted to be used on the smashing glass and the bullet. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e41801bc2c0960771544fe8356ef70a66f7ec0f56aceffe593ba7427ffcc5e43.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c1e9d231a8abbe5f0de75f23488127b8652619eb2c921c13fa8f38ba56821e36.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ef9bb9495f74b2ef6c16bddc93e6019d21ea21a81001d3ea4fab4d073a571b2b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ec75029d3313e38a6c30b7cde627e27fc739fa62dbee0087aa24a1063e036c08.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/424b24ca850387e455b8f0c6b32711b5b54988f47293ac9a85d0cb6fe724e8be.jpg)


05 Make sure that the retime node is wired into the particlefluidsurface node then set it’s display flag. This will give you your final fluid based on the retiming. Select the particlefluidsurface node and keep: 

 Method set to Average Position 

 Set Union Compressed Fluid Surface to Of. 

In the Filtering tab turn: 

 Dilate to ON and set it to 2. 

 Smooth to ON and set it to Laplacian Flow 

06 Add a USD Export node to the end of the chain. Rename it wine_surface. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/wine_surface.usd Hit Save to Disk. 

07 Select the retime node and press Ctrl-c to copy it. You will paste this in another network to retime the shatering wine glass. This will ensure that the keyframes match in both of the networks. 

Save your work. 

## 08 Go to frame 1 and navigate into the wine_glass network. Beneath the transform_hires node, wire in a File Cache node and set the following:

 Base Name to glass_pieces 

 Base Folder to $HIP/geo/ 

 Turn Of the Version check box 

 End to 10 (RMB-click > Delete Channels first) 

Hit Save to Disk. Set Load from Disk to On and Scrub through frames 1 to 10 to make sure that it looks correct. 

## USD and SOLARIS

To support the look dev stage of this project, you are caching out the fluid, the wine glass and the bullet to USD. By doing this, you can focus on rendering without worrying about simulations being recalculated. Here you will display the caches in the same scene file as the simulations but another option would be to start a new scene file and import the caches into that file. This would let you focus on lighting and rendering your shot but would make it harder to go back and tweak the sim. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/24e5faef695fbc56c770bb03a52686c6154d99bb1fa91d98222146bd34bfb512.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ee8c05aaa8d4a34e76453c3819d4244e5fb5c16e1868c66dda8e33014a1c93bd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f6a3b47bbad5c2180d92f545648c15bb6f6227a7ece423fd425d7325600e2eff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/51aec6c8caa318d470ce9f90240c630ca2972732b0debf8f3118f7f9f4f88009.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/68d08a1e65d87d55323d0c073c811f330ef1e51d0d656cc5b56f57e39291aae7.jpg)


Press Ctrl-v to paste in the retime node and place it after the filecache node and set its Display flag. Now you have the same timing on the glass that you have on the fluid. You can scrub through the timeline to watch the timing of the pieces. 

After the retime node, add an Atribute Delete. From the arrow next to Primitive Atributes, select name to remove this atribute from the geometry. 

## 10 Add a switch node into the network. Feed the GLASS_ OUT into it first and atribdelete node into it second.

Set Select Input to $F>5 && $F<45. Scrub in the timeline to see how this works. This expression makes the switch from the unbroken glass to the broken glass at frame 5 and then back at frame 45. 

You are puting these shapes together so that the glass is unbroken before and after impact in the wineglass USD file. 

11 Add a USD Export node to the end of the chain. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/wineglass.usd 

Hit Save to Disk. 

## 12 Go to frame 1 and select the bullet object. From the Modify menu, select Extract. This gives us the world space position of the geometry. Dive into extract_object and, Paste the retime node beneath the object_merge node then connect them.

Add a USD Export node to the end of the chain. Rename it bullet. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/bullet.usd 

Hit Save to Disk. 

## PART SEVEN Set up and Render the Shot

To render the shot, you will reference the USD fi les into the Solaris Stage then add a backdrop. Solaris is the context of Houdini that uses LOP nodes to set up the USD Scene Graph. Next, you will add and positi on a camera and then an environment light. The Karma renderer will then be invoked in the viewport to create a preview render of the shot. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/09ee232d6f9a386049c4c5ee52b7c1c737f49fd835cb8744760f972e7a32d2d3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f3e1d1821bd195c1dea88aa94ed49bf545d5e1d85a268fd766b88d3cc8618739.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e309f19cd2f66d27567e2cb2f127c00f80c88755b605d653fba86315c681894c.jpg)


01 Change the desktop to Solaris. Choose Stage from the path bar. 

In the Network View press tab > Reference then click to add a Reference node. Next to Reference File, click on the File Chooser and fi nd the wineglass.usd fi le. Rename the node to wineglass. Set the Primiti ve Path to /geo/$OS - this will use the node name and place it into a group called geo. 

In the Scene View, use your view tools such as spacebar-h for homing the view to get a bet er look at the wine glass. 

02 Alt-drag on this node to make a copy and again to make a second copy. For the fi rst copy, click on the File Chooser and fi nd the wine_surface.usd fi le. Rename the node to wine. 

Repeat to make another copy, fi nd the bullet.usd fi le. Rename the node to bullet. 

Add a Merge node to the network and wire all three reference nodes into it. Set its display fl ag then scrub to see the results. 

In the Scene Graph, you can see a geo entry and underneath that you will fi nd the three referenced USD fi les. 

03 In the Network view, press tab and type out Grid. Click to place down the node, rename it backdrop and wire it into the merge node. Set Import Path Prefi x to /geo/$OS. Doubleclick on the backdrop node to dive down to the geometry level. 

Select the Grid node and set the Size to 200, 200 and Rows and Columns to 20. RMB-click on the grid node’s output and type Bend. Click to place a bend node and set its Display Flag then set: Bend to 75, Capture Origin to -40, 0, 0, Capture Directi on to -1, 0, 0, and Capture Length to 20. RMB-click on the grid node’s output and type Subdivide. Set its Display Flag then set Depth to 2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7054e93a70c6c3d209541ff600fb9f5ba3f7d281ca8fb29ee66dde43514187d2.jpg)


## CACHING OUT SIMULATIONS

To support the look dev stage of this project, you cached out the fl uid, the wine glass and the bullet to geometry (USD) sequences. By doing this, you can focus on rendering without worrying about simulati ons being recalculated. 

This is a typical workfl ow when working on VFX shots that can consume LOTS OF HARD DRIVE SPACE. You should be aware of this before sending of huge simula ti ons with lots of parti cles - make sure you have somewhere to store the various intermediate stages. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/74f77905750f31504e899bb3e8cb5e01deb37919f52c446366ea6c439a9202a2.jpg)


You are now going to render the sequence using Houdini’s renderer Karma. At fi rst this will render using seti ngs you can fi nd in the Display opti ons. Press d in the Scene View to bring it up. You can turn on the denoiser here, set Pixel Samples and the Image Resoluti on. Later when you set up a Karma LOP, there will be render seti ngs on that node which will be used to create the fi nal output. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b2a39b566eb4cb91e9ae6db6a39d6691abe61b1119824e2ce3dfbfd21e2c974e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e976caf9744091a5d356e6cdc9403734b481b45a3bca440f645a4e0ce588b1bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8787144ca07c940a90c2af75e716c3639e82dcadd0270cd5bb7e98a017b8ce3b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/00891837d69bfb2b4e8af5c587f71858668163590d969a205a9483a3115380ec.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/56fc575fb35679abacce7c62a806ba4b4755841a1ab64c1b16c2d23dfc270972.jpg)


04 Use your view tools to look at the wineglass from the front. From the LOP Lights and Camera shelf, Ctrl-click on the Camera tool. This adds a camera node into the network and you are now looking through the camera in the viewport. 

Press the Lock Camera/Light to View but on so that view changes can be used to repositi on the camera. Now Tumble, Pan and Dolly in the viewport to repositi on the camera so the wineglass is on the left and the splash moves to the right. Scrub the ti meline to make sure the camera works for the whole sequence. 

05 From the LOP Lights and Camera shelf, Ctrl-click on the Environment Light tool. This adds a domelight node to the end of the chain. 

Select the domelight node and from the Base Properti es tab, click on the File Chooser but on next to Texture. Click on the $HFS/ houdini/pic/hdri listi ng in the sidebar then select the HDRIHaven_ skylit_garage_2k.rat fi le. Click Accept. 

On the Display Opti ons bar. Click on the High Quality Lighti ng with Shadows but on. 

06 From the Persp menu, choose Karma to render with Karma in the viewport. You can move to dif erent frames in the ti meline and the viewport will update quickly. 

Karma is designed to work with USD which is why everything in the LOP context is converted to the USD scene graph. You can only use the Karma renderer from this part of Houdini. 

07 To get a cleaner image when you render, you can turn on Denoiser if you have an Nvidia graphics card and you have installed the latest drivers. You can turn it on in the Display Opti ons bar. 

## PART EIGHT

# Assign Materials and Render a Sequence

Now you can add materials to the wineglass, wine and bullet. These materials will become part of the USD Scene Graph and will get assigned to the geometry using a LOP node. You can then use a Karma LOP to prepare your render setings including the use of the Nvidia Optix Denoiser. After you render, you can load the sequence into Mplay to review the results. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e1477dd4a7083851dc431398af782c23951e515a75e962fd6faab75ce7d30959.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/795402e6fdeac197e2c1004d5a743085d2edac7afdfdf0a013894187c846693a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5abf0e34f15d1b36c26502449da29eea388a5ef97cbb0c212e033078e3e64911.jpg)


## 01 In the Network view, press tab > Material Library. Wire it into the end of the chain then set its Display Flag.

Go to the Material Palete pane. Click on the arrow next to /stage/ materiallibrary to open up this area. Scroll through the material gallery on the left of the palete and drag two Glass materials into the materiallibrary working area for the wineglass and wine. 

Now find a copper material and drag it into the materiallibrary working area. You will use this for the bullet. 

Set Inside IOR to 1.3443 which is an IOR for wine. Next, set Reflectivity to 0.2 to reduce how much the surroundings are reflected. 

Set Transmission Color to 0.2, 0, 0 which will create a reddish wine look. Next set At Distance to 0.3. 

## 03 Go back to the Stage level. After the Material Library node, add an Assign Materials node.

From the Scene Graph, drag the wineglass to the Primitives field then click on the arrow next to Material Path and choose the glass material for this primitive. 

Now click the Plus Sign next to the check box twice to add two new entries. Use the same method to assign the wine material to the wine primitive and the copper material to the bullet primitive. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/36da9fa48d65652de063819b1f98e9871bfb8c56caaefa8629c9c307d8fb3b9b.jpg)


## SCENE GRAPH

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7f47c1fe6b9fdba7b83341bc961748b29556b4ad9491c26221145a37f7f17269.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8a66dcf9c119798cd50afd7813c7924402a81213af87e876c8dbad951551ea69.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1384ece46ffd449ebc2aaa731492be489d51b9eadad4ee2044e0ebc0a3979685.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9cf258466c8949fb738a9626995e0cb24a4ed31326deb1d111bdd773b3f88b39.jpg)


04 In the Network View, press tab > Karma to add a Karma Render Seti ngs and USD Render ROP node. Wire them into the end of the chain. Select the karmarenderseti ngs node and on the Image Output > Filters tab set Denoiser to nvidia Opti x Denoiser to turn the denoiser back on. 

Select the usdrender_rop node. Set Valid Frame Range to Render Frame Range and set the Output Picture to $HIP/render/ wineglass_$F4.exr. The $F in the name is needed to add frame numbers to the renderings and the 4 is the padding of the frame number. 

05 The denoiser from the viewport will not af ect the output from this node therefore you much choose it explicitly. Select the karmarenderseti ngs node and on the Image Output > Filters tab set Denoiser to nvidia Opti x Denoiser to turn the denoiser back on. 

The nVidia Opti x Denoiser will match the one used in the viewport. There is also an Intel OIDN denoiser which is only available when rendering to disk. 

Save your work. Select the usdrender_rop node and click on Render to Disk. 

06 When you fi nish, choose Render > Mplay > Load Disk Files and open up the rendered images to review the fi nal sequence. 

Later you can branch of another Karma node to up the resoluti on and render seti ngs for your fi nal rendering. You can go back to Convergence Mode set to Variance, up the sample count and turn of the denoiser. It is always good to complete test renderings at a lower resoluti on fi rst to make sure that everything is working the way you expect it to. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/52ed07fea4695cde9fbaf8c0f8cfcacd2a5029774bf0b038d650ebe74c0416c7.jpg)


## CONCLUSION

You have now created a complete VFX shot using the Bullet RBD and FLIP Fluid solvers to smash a wine glass. You used the reti me node to slow down then reverse ti me so that the wine glass fi nished in the same positi on as it started then you cached out the results to USD fi les. 

These were then used to set up and light your shot using the Solaris/LOPS context. Materials were created and assigned to the primiti ves get the right look for your shot. 

This project shows how you can use Houdini’s dynamic nodes and networks to integrate dif erent kinds of ef ects while using geometry nodes to set up and output the simulati ons. 

Now that you have an understanding of the nodes and networks used to create VFX shots. This will assist you as you dig deeper into Houdini to achieve your own ef ects. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/58f4b3194fffc56c9a9639730fe7ef1473b63f6a5846f227210262e8469b1d6d.jpg)


## HOUDINI FOUNDATIONS DESTRUCTION FX

One of the things that makes visual ef ects fun is that you get to blow things up without causing any real damage. In this lesson, you will light a fuse using parti cle sparks then explode a cartoon bomb using rigid body dynamics for the shell of the bomb and Pyro FX for the fi re and smoke. This lesson will teach you how to set up dynamic simulati ons using a variety of shelf tools and network nodes. 

To give you a complete understanding of the shot being developed, you will build all the elements from scratch, then simulate the ef ects. This will help you understand how the simulati on nodes work within the wider context of a Houdini scene. In the end, you will render out the shot using the Karma renderer. 

## ACES | OPENCOLORIO SETUP

For more accurate color display when working with Pyro FX, you should use the Academy Color Encoding System (ACES). To use it, bring up the Correcti on Toolbar from the 

Display - sRGB Output - SDR Video LUT and Gamma 96 OpenColorlO 

viewport (persp) menu in the scene view. From the arrow but on on the right, choose OpenColorIO. This will give you a Display of sRGB and an output of SDR Video - ACES 1.0. This seti ng only works for your current session and will need to be turned back on each ti me you open Houdini. 

## LESSON GOAL

Model then blow up a bomb using parti cle sparks, rigid body dynamics and Pyro FX. 

## WHAT YOU WILL LEARN

 How to model the bomb and animate the fuse 

 How to animate a camera to set up the shot 

 How to set up a parti cle soot trail and sparks for the fuse 

 How to shat er then explode the bomb geometry 

 How to set up a Pyro FX simulati on for the explosion 

 How to set up materials and textures 

 How to render the ef ects with Karma in the Solaris context 

## LESSON COMPATIBILITY

Writ en for the features in Houdini 19.5+ 

The steps in this lesson can be completed using the following Houdini Products: 

<table><tr><td>Houdini Core</td><td>✕</td></tr><tr><td>Houdini FX</td><td>✕</td></tr><tr><td>Houdini Indie</td><td>✕</td></tr><tr><td>Houdini Apprentice</td><td>✕</td></tr><tr><td>Houdini Education</td><td>✕</td></tr></table>

Document Version 1.0 | July 2022 © SideFX Soft ware 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/24c940c62e0a1adc8aad614dfa154079e3cd89c796fab9fb856c83a727521cfa.jpg)


# PART ONE Model the Bomb

To create the bomb geometry, start with a primitive sphere and modify it to define the opening at the top. This will involve a few poly extrudes and bevels to define the geometry you will need for the final shape. Later in the lesson, you will fracture the bomb. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a2ec321244b55e06abdde02f80c465db068ce40ca9fe312ea475701826b60e47.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/25f56315563ff7920473c76b699e2a11efb09e3c4568f59fe9e81a2afb834c47.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/94a6083fbd24d23c0e9734087aabd331cda1caf415f514f00f6d74e20b84d4bc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2d79c5b3c4d6b6192b83024edc7cc38b1a3ce0f5368ea43111f99d4703133df6.jpg)


01 Select File > New Project. Change the Project Name to destruction_lesson and press Accept. This creates a project directory with sub directories for all the files associated with this shot. 

Select File > Save As... You should be looking into the new destruction_lesson directory. Set the file name to destruction_01.hip and click Accept to save. 

02 In the viewport, press c to bring up a radial menu. From this menu, choose Create > Geometry > Sphere. In the viewport, press Enter to place it at the origin. In the Operation Control bar at the top, set Radius to 0.3, 0.3, 0.3. 

Press s to get the select tool then 3 to invoke edge selection. Press Spacebar 2 to go to a Top view. Box select the edges at the top and botom of the circle and press delete. This dissolves the edges and leaves two circular polygons in their place Press Spacebar 1 to go back to a perspective view. 

03 Press s to get the select tool then 4 to switch to primitive (face) selection. Select the circular polygon at the top of the sphere. 

Press c to bring up the radial menu and select Model > Polygons > Polyextrude. Move the handle up by a Distance of about 0.075. Set Output Front to Of. 

04 Select the circular polygon at the botom of the sphere and press Delete. This will add a blast node to the network. Press s to go to the Select tool and 3 to change to edge selection. Double click on the edge of the hole you just created to select all the edges. 

Press tab > Polyfill. In the Parameter pane, set Fill Mode to Quadrilateral Grid and Smooth to 270. This creates a cleaner topology for the botom of the sphere that doesn’t go to a single point. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3eaf1d915f309a1f74fb09cfe7499163e407d98fb085c6b911fee82ad6856f9f.jpg)


## SURFACE NORMALS

Every primiti ve has a normal directi on where one side is the inside and one is the outside. When you polyextrude the bomb geometry it will be inside out at fi rst. This is indicated with the blue color on the faces. You can then use a Reverse node to redirect the normals. You can see the normals on the surface using the Display Primiti ve Normals but on found in the Display Opti ons bar on the right side of the Scene view pane. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/98de0a8e3301741ad123f6e9a4b9e335e7323ff285a4c1c22f2c81826d98c935.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c8a0d2a351180bd1e7e1a965d53042af70e429f4a326a3f3f76c660b3cc2e632.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1cafc8a9ec94cf0b791085742c054f6363079c7e67c88fed27b7db8967d35fdb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3e7213d298e01827d0367487602397fa9a8a618ab5efa182919b53cb8f5b61df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b7099088f55ac7a8abc0f102992240fa4cf1e85a3745894ecb3013d61c626d85.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eeb812babeea0da3abcf91c2375c1c895c63a48e2103146445c0557cf10b78c2.jpg)


05 Press n to select all Faces and again get the Polyextrude tool. Extrude to a Distance value of around -0.04. In the Parameter pane in the Extrusion tab, turn on Output Back. Press n to select all Faces and again press tab and start typing Reverse. This node reverses all the polygon normals. Now they are pointi ng in the right directi on. 

06 Press s to go to the Select tool and 3 to change to edge selecti on. Double click on the edge at the top of the bomb and then press Shift and double click to select the inner circle at the top. 

Press c to use the radial menu to go to Model > Polygons > Polybevel. Set Distance to 0.005. Set the Shape to Round and Divisions to 3. 

07 Press s to go to the Select tool. Double click on the edge where the circular part of the bomb meets the extruded secti on at the top. 

Press q to repeat the last tool which was Polybevel and set Distance to 0.01, Shape to Round and Divisions to 3. 

## 08 In the Network view, press tab > Transform and add it to the end of the network. Set Translate Y to 0.3 and Rotate X to around 27 degrees.

Add a Null node. Wire the end of the polybevel to the null then set the display fl ag on the null node to display it. Double click on its name and change it to BOMB_OUT. 

Go to the Object level and rename the object to bomb_geo since it holds the bomb’s geometry. 

## PART TWO Model the Fuse

To create the Fuse, start with a Bezier curve that emerges from the top of the bomb. You can then snake the curve on the ground to create a longer fuse. Reverse the curve direction to get ready for animating the fuse then add a Polywire node to give the fuse thickness. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/65a7750e8b6abaee343b6561cee0c1269845bf5bee68533b9c1b1ea3869cee34.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a3fa7f207c63a4bd03d391f1c1306c26c5adc109300a68d1fdc3a8b245a6a2fe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e0cc4b353f2dd4d305f85b594482139318b674065075e709e22325a075aba4aa.jpg)


over the Right view and press spacebar-b to expand it. 

Press c to bring up the radial menu and choose Create > Geometry > Curve. Click drag up to create the first point and tangent handle for the curve. Next add a point and drag down to quickly draw the curve pointing down. 

02 <sup>Press</sup> <sup>x</sup> <sup>and</sup> <sup>choose</sup> <sup>Grid</sup> <sup>to</sup> <sup>turn</sup> <sup>on</sup> <sup>grid</sup> <sup>snapping.</sup> <sup>Click</sup><sub>and</sub> <sub>drag</sub> <sub>on</sub> <sub>the</sub> <sub>ground</sub> <sub>to</sub> <sub>create</sub> <sub>a</sub> <sub>third</sub> <sub>point</sub> <sub>with</sub> <sub>its</sub> and drag on the ground to create a third point with its tangent handle aligned along the ground. 

03 Press spacebar-b to go back to 4 views then mouse overthe perspective view and press spacebar-b again expandthe view.一

Turn of Grid Snapping then turn on the Construction Plane using the second buton at the top of the Display Options bar. This will make sure that any edits you make stay on the ground. 

Draw three new points with their tangents dragged out to define the curve’s shape. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0b98d95b68726ce8faae93e42db7d96eed0e9b6b3bbdf0ea80993caa25a95f62.jpg)


MMB-click to complete the curve. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a3c2eaf611b7d60ac3d5a3eba8e76e49e3d786f5eac6312cd0a9f54dd026651.jpg)


## TOOL HINTS

The curve tool comes with tool hints that display in the Scene view as you work. These provide diferent shortkey options for this tool and help you get familiar with how it works. 

You can collapse it using Shift + F1 and only the tool name will display. There are a growing number of tools that use tool hints and you will see more of them in future versions of Houdini. 

Press Shift + F1 to hide hints 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/30e3e36d4c0b1b30ab649a01525dcff99ce9ffcd4f856aa8ac87515fc79e243d.jpg)


Curve Type 

Drag entire curve 

Insert a point (on curve) 

Change radius relatively (radius widgets) 

Tangents 

1 - 3 Set selected point type 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1d197bba816471fa3e007fbaf1bd790ae2ea971d5b9de60196bf5e058e830cbc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b1edf20048bec9029358538e1f76a5d862f1045baa7cd74aa2b0e863526b0d78.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dcb78816b99948ee94dc49168ff3a481fdfa82cc5715cac0ca7bf37cb2eb67fc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eb470a76e788648938a89aadfbec28263e188fe232760749009b9d8490b95fe8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/73cf84731db76830f80af04446f70c28132b5e2801d4d5a508a219724e0388cd.jpg)


04 In the Operation Control bar, change the curve Mode to Select/Edit. Now you can click on the edit points on the curve and make changes to refine the shape of the curve. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e7f543e14c55b08455ba97c5c41536bc0bb5121e03b7cfe16cf46743461aaf02.jpg)


Select and edit the points on the ground to get the desired look for the curve. Tumble around to make sure that your curve stays above the ground plane. 

05 In the Scene View, press tab > Reverse. Press n to select the whole curve and press Enter. Since the curve was drawn from the bomb out, it will not animate in the direction you need. This will put the start of the curve where the fuse begins. 

06 Turn on the Display Points option in the Display Options bar. Add a Resample node. On the resample node, set the Maximum Segment Length to 0.025 to add more detail. The resample node evens out the points. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/56991ff6f5b99bc4cd529a362cfe069b171c6132d286f8c93ed9da0fa6cf34c5.jpg)


## 07 Add a Polywire node to add thickness to the wire. Set the Wire Radius to 0.0075 and the Divisions to 8.

Between the reverse and polywire nodes, add a Transform node. Go to the polywire node and RMB-click on the Wire Radius parameter and choose Copy Parameter. Now go back to the transform node and RMB-click on Translate Y and choose Paste Relative References. 

This will lift the whole fuse up so that it is not halfway under the ground grid. 

08 Add a Blast node Set Group to 0. This deletes the end of the fuse geometry. Next add a Normal node to the end of the chain. 

After the normal node, add a Null node and name it FUSE_OUT. This gives you a node representing the whole fuse geometry. Go back up to the object level and rename this object to fuse_geo. 

## PART THREE Animate the Fuse

Animate the fuse using a Carve node that lets you control the length of the curve over time. Add a round cap to the fuse that will be used to emit soot and sparks. You need to set up tangents on the curve to ensure that the cap follows along properly. Next add some NULL objects to make it easier to export the cap for use in emiting particles. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c9ab23bd5ba77b66bc427d47152242c6f64d02d30b1a6218d48525b80bcbe9e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c798f6319d5c3ad3b92061dd1dd6052db6f29447ea1700175da8ec894ce7708.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bf025a4c06c52f46da561537e53fd934279a2b3028bbc835f4c86695daaca52e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1571b1b1cd0f524a219db5fd156656b420505bf6c15c8e6474270761d0fb3402.jpg)


01 <sup>Dive</sup> <sup>back</sup> <sup>into</sup> <sup>the</sup> <sup>fuse_geo</sup> <sup>object.</sup> <sup>Between</sup> <sup>the</sup><sub>transform</sub> <sub>node</sub> <sub>and</sub> <sub>the</sub> <sub>Polywire</sub> <sub>node</sub> <sub>add</sub> <sub>a</sub> <sub>Car</sub> transform node and the Polywire node add a Carve node. Drag on the First U slide to see how this afects the curve. 

Set First U to 0. Alt click on First U to set a keyframe at frame 1. The parameter box will change color to indicate that it has been keyframed and that there is a key at the current frame. 

02 Go to frame 180. Set First U to 0.999. This will set a keyframe. You can see that the fuse will. Go to frame 200. Set First U to 1.0. This will set another keyframe. 

In the botom left of the Playbar, toggle realtime playback on so that it doesn’t play back too fast and press Play. 

The fuse now animates into the bomb geometry where you will set up the explosion. 

03 Click on the Animation Editor Pane tab. Select the animation curve and click on the Straight buton at the top of the panel. This will straighten the curve and the fuse will animate evenly from start to finish instead of speeding up then slowing down at the end. 

Go back to the Scene View pane tab and playback the animation to see how this change afects the motion. 

Save your work. 

04 In the Network View, add a Sphere node and set its Display Flag. Set the following: 

 Radius to 1, 1, 1 

 Center Y to 0.0075 

 Uniform Scale to 0.0075 

Press Spacebar-F to focus on it. 

 Orientation to Z Axis 

 Rows to 9 and Columns to 8 

In the Scene view, press n to select all then tab>Clip node and set its Direction to 0, 0, -1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b7c154563fb9830e69bfb55dea9b4e1f91c44cb8c0d97d8ad0661f78f983eb8d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c85c290d58ae5971f2237b45683da139c2f9d2a536e9c9d0ded7afbc8b3e0ebf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/88018f62f83ffa4f0707bbc156723cfe98828a698cf5faa0bc7451ee9ba16c95.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/27c9e3c5f7aac4ef4c2e6c92bb3b5a79ef6ffd3d73674e24dd5c8c970f5d81af.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/24ca385ba3a6358c41df4ada82e8404d976d405d8cfcbb7d1bb508228ea05ed1.jpg)


05 Tumble around and press s to get the select tool and 4 to get face/primitive selection. Select one of the triangles at the tip of the sphere then press and hold the a key and then middle click two triangles over to select all the triangular faces. Press the Delete key to remove them. This adds a blast node to the network. 

Press 3 to go bring up edge selection then double click on the edge of the area you just blasted. Press tab > polyfill which places the node after the blast. Set Fill mode to Quadrilateral Grid then turn on its Display flag. Set Smooth to 100 and Tangent Strength to 0. This will create quad topology at the tip of the sphere. 

06 Add a Copy to Points node into the network. Feed the polyfill node from the sphere into the first input and the carve node into the second input. Set Target Points to 0. 

Add a Merge node. Feed the blast node and the copytopoints node into it then wire it into the normal node. 

The cap it positioned properly at the end of the curve but it isn't oriented correctly. You need to add normals to the curve to allow for proper alignment. 

07 Add a Orientation Along Curve node between the reverse and the carve nodes. Under Output Atributes turn of the Y Axis option. Leave Tangent (Z axis) set to N. This adds normals to the curve that will align the end cap as it moves along the fuse. 

08 Add a Color node after the polyfill node and set the Color to yellow. Add another Color node after the fuse’s blast node and set its Color to Dark Gray. These colors will be helpful for visualizing the fuse as you work and can also be used to afect the materials being assigned later. 

09 Branch of a Null node after the copytopoints node and place it to the side. Name the null node CAP_OUT. You will use this later to extract the cap into another network that you will reference to emit particles. Set its Display Flag to see only the half sphere. You can scrub the Playbar to see it move with the carve. 

When you are finished, set the Display Flag back to the FUSE_OUT null. 

# PART FOUR Create an Animated Camera

As you develop this shot further, it would be helpful to have a camera set up to frame the final shot. This camera rig will be built by constraining a null object to a curve then using an aim constraint to point the camera to the null object. This will give you a camera that follows the end of the fuse to make it easier to evaluate the particles as they are being emited. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0189d90b9869d98e6ec48a89f120f050f066f8470ae7053679104c0dde2e7fc5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0d5968e90955e6d0327c09c56ba189da6095c7401bc7e3a03f56f8b37557d746.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b6fff126e0c4e2d84e7ee2c17d4caaf5609d7447d5b23a911af891adcd20f0cf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83a6bc4c3e319ca24e865edfb0a62ea50fa5c632b19c2654ca14f9e9231fb240.jpg)


01 <sup>Dolly</sup> <sup>out</sup> <sup>to</sup> <sup>see</sup> <sup>the</sup> <sup>whole</sup> <sup>scene</sup> <sup>from</sup> <sup>above.</sup> <sup>Make</sup><sub>sure</sub> <sub>the</sub> <sub>construction</sub> <sub>plane</sub> <sub>is</sub> <sub>on.</sub> <sub>Press</sub> <sub>c</sub> <sub>to</sub> <sub>bring</sub> <sub>up</sub> sure the construction plane is on. Press c to bring up the radial menu and choose Create > Geometry > Curve. Click-drag a point near the start of the fuse and drag forward to extend the tangent. 

Next, click-drag a second point behind the bomb and drag to pull out the tangent to create an s shaped curve. MMB-click to finish and use Select/Edit mode if you want to tweak the shape. 

02 On the Curve node, turn on the Z Axis option and set it to N. This will create normals that will assist with animation along the curve. 

03 Add a Null object at the origin. Rename this node camera_lookat_null. From the Constraints shelf, click on the Follow Path tool. This accepts the null as the starting object. Select the curve as the path object then press Enter. Press Enter twice more since you don’t need a look-at object or a look-up object. 

Now if you scrub in the timeline, you can see that the null object is moving along the Path from the first frame to the end frame at an even pace. 

04 A constraint network was added to the null object and a path node is created. Go to frame 1. With the Path node selected, RMB click on the Position parameter and choose Delete Channels to remove the expression that is animating the null along the path. Set Position to 0. Alt click on Position to set a keyframe. 

Go to frame 195 and set Position to 1. Alt-click on Position to set a second keyframe. 

Click on the Animation Editor tab and press h to see the whole curve. Select it and press the Straight buton to make it linear. Grab the tangent on the second point and adjust to smooth out the end. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/415417f7b46a4f1127934a680167492cd3ecaef401ff414e1665de00683d526c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f62afd7736e9e75742db7bb03f7f887d485c9adc51bf63f880a8506cedca6f27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c20b1d295de63b9a60800a19e03f4aec5779f905523e838a19c6270677c2499c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2e54195d7bc1b4ac2a0275bdaab72783400883cf9fe9d34a5b2afcf02a440ad5.jpg)


05 In the Network view, press tab > Camera and press Enter then click to place it at the origin. Now use the Move tool to move it in front of the fuse and a bit to the right. Next move it up along the Y axis to raise it from the ground by about 0.75 units. 

06 From the Constraint shelf, click on the Look At tool. This will use the selected Camera as the look at object. Select the null object as the look at object and press Enter. Press Enter again to not assign anything as the look up object. 

Now the camera is looking at the Null object. From the Camera menu, select cam1 to look through this camera. 

07 Go to Frame 1. Select the camera and make sure the Handle tool is active. This brings up a camera handle which you can use to reposition the camera to have a beter view of the fuse's starting point. 

Go to Frame 195. Use the same handles to reposition the camera to make sure the bomb in nicely positioned in the frame. 

You may need to scrub back and forth to tweak the camera to work properly throughout the sequence. Make sure you can see the fuse throughout the whole sequence. 

08 Go to the object level and select the curve, camera lookat_null object and cam1 node and align them then put them into a network box. Double click on the box’s title bar and name the box Camera Rig. Turn of the display of all the parts so that you don’t see them in the scene view as you work. You can collapse this box if you want or keep it open if you want to work with it further. 

Save your scene. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bb2a1b730e44615e4f5ae16c8a4794cf13351c65dc829b97b15e4cb1575596b6.jpg)


## CONSTRAINTS

To get the null object to follow the path and then to get the camera to look at the path, you used animation constraints found on the Constraints shelf. The are accomplished using a special node type called Channel Operators or CHOPS. You can find these nodes inside the null and camera nodes. You can use these to control how the constraints work. 

Another way to work with CHOP nodes is to use the Motion FX menu that you find when you RMB-click on any parameter. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4b63eebd3a9298a3bfc3bc9d407fc7948e13d18b2623441ed6afcda55cce72dd.jpg)


# PART FIVE Create a Soot Trail

To create a soot trail, use the end cap to emit a trail of particles. Learn how to emit these points properly and how to add forces such as gravity to control the motion of the particles. Learn how to set up collisions where the particles either stick to the ground or slide of the bomb surface. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ddea7e009f0ecbe337ed621be28a75b7645d623aed5793f5e0584915e29b7348.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/00e7c9cd7aaeeaae214e041505c39cfd596b1e87f13627dea3a38552ae48f027.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/62300dacb06dba99afde4f78261f77a45eb179a4233b3a8a15c672e79ec0a3e4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83a119ffc6fa2dfafadc95cfce136b4d4c57ff63bf973f5fac10ff1836a82d75.jpg)


01 Dive back into the fuse_geo object node. With the display flag on CAP_OUT, go to the Modify shelf and use the Extract tool. Press n to select all the faces then press Enter to create a new object with the Cap being imported using an Object Merge node. Go up to the object level and name this object soot_ trail. 

Go back to the fuse_geo object and set the display flag to FUSE_ OUT. Now you will see the combined fuse geometry when you render and the new object will be used to generate particles. 

02 Dive into the soot_trail node and add a POP network node to the end of the chain. Dive in and on the Source First Input node, set Const Birth Rate to 1000. Press Play. You can see particles being emited but they aren’t doing anything. 

Go back up one level and on the Simulation tab, set Substeps to 3. Press Play. You can see particles being emited more evenly. 

03 Alt-drag on the object_merge node to make a second copy. Set Object 1 to the fuse_geo>resample node. You are going to use this curve to transfer velocity onto the cap. 

Now add a Orient Along Curve node and under Output Atributes turn on Tangent (Z Axis) and set it to v. 

Add an Atribute Transfer node between the original object_merge and the popnet node. Turn of the Primitives checkbox and set Points to v. 

04 Place an Atribute Adjust Vector node in between the atributetransfer and the popnet. Under Adjustment value set the following: 

 Adjustment for to Direction Only 

 Adjust with to Noise 

 Range Values to Zero Centered 

 Amplitude to 0.5 

Under Noise Patern set Element Size to 0.025 and under Post Process, turn on Enable Post-Process. Press Play to test. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a57b88635be039253f4cd0639dabb0765a93d12f9dda6cc5e040c0733065187.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6cdfc344fda8b8ac9111b2b5aa684f33d13d356ae03a515633341aee38e9c34a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5e477aedc1a31d4ce0d3c71ae12d32de674a789dfac8edfc3604e087cb3b0bd4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/69a00aa6fea64d2641ff22f0b5625ea14fde2dc9ccbecc7f1a8bc24866931400.jpg)


05 Dive back into the popnet and add a Gravity Force node under the popsolver. Now if you play the simulati on the parti cles fall below the ground. 

06 Go back up to the Object level and create a grid. Set size to 30, 30 and Rows and Columns to 31, 31. 

Rename this to ground. Go back into the popnet and add a Pop Collision Detect node aft er the source_fi rst_input node. Set the SOP Path to the <sub>obj/ground/grid1</sub>. On the Behavior tab, set Response to Sti ck. Keep Color Hits set to Red. 

Add another Pop Collision Detect node. Set the SOP to the bomb_ geo geometry object. Set Response to Slide. Change Color Hits to Green. Press Play. 

07 Right now the parti cles will be emit ed throughout the whole sequence. You need them to stop them just as the bomb explodes. Add a POP Kill node aft er the wire_pops_into_here merge node. Go to frame 1. Set Acti vati on to $F>199. This will kill the parti cles at frame 200. 

Now under the Rule tab, turn on Enable. Press Play to test. 

08 Jump back up to the geometry context and wire the popnet into an at ribute create node. Set Name to pscale and Value to 0.001. 

Add a Color SOP and set the Color to dark grey. 

Add a null to the end of the chain and name it SOOT_OUT. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ccf6350e6f064317cf05a1abb7735227fb74ce8f9f7f38cd670a7868d0fd030d.jpg)


## PARTICLE FX

The soot trail is created using parti cle dynamics. Parti cles are points that you can af ect using forces such as wind or gravity. Starti ng with the end of the fuse, you give birth to points that are then simulated using a number of dif erent techniques. 

Parti cles are simulated using the Dynamics or DOPS secti on of Houdini then brought back into SOPS where you can work with them as geometry. In the next secti on, you will use parti cles to create sparks at the end of the fuse. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/77d60022c2e6346cdb977b808b4610af7ebcf597640c1b3680a1bf1a6c477c3d.jpg)


## PART SIX Create Parti cle Sparks

To create sparks, start by copying the soot parti cle object and make changes to the new object to generate sparks. These parti cles will have shorter lifespan and will be more acti ve. The Spark Trail node will give you the look you need to add sparks to the shot. You can adjust parameters on this node to get the look you need. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/014037dacbd28beaa42e7764a20335bb1ed586d1fb41d5a9016053963b968dab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2689891ffa28482d2629698719f0388ef7e90f5fc92e43f5221718cab6056e48.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c328f33e92187e378c0e14492ad9e17c462edf2d1dab358283fcec9d88b7a183.jpg)


01 <sup>Go</sup> <sup>to</sup> <sup>frame</sup> <sup>1</sup> <sup>then</sup> <sup>navigate</sup> <sup>to</sup> <sup>the</sup> <sup>Object</sup> <sup>level.</sup> <sup>Hide</sup> <sup>the</sup><sub>Ground</sub> <sub>object.</sub> <sub>Alt-drag</sub> <sub>on</sub> <sub>the</sub> <sub>soot_trail object</sub> <sub>to</sub> <sub>make</sub> Ground object. Alt-drag on the soot_trail object to make a copy. Name the copy sparks. 

This new object already has a popnet and can be modifi ed to generate the spark parti cle simulati on. In Houdini, it is oft en a good idea to re-use a network you already have as opposed to building everything from scratch. 

02 Dive into the sparks object. You will make a few changes to get the network set up to create sparks. 

Delete the at tributecreate and color nodes. These are not needed for this parti cle network. Rename the null node to SPARKS_OUT. 

On the at ributeadjustvector node change Amplitude to 1.75. 

Add a new At ribute Adjust Vector node above this one. Turn on Enable Pre-Process and set Constant Value to 0, 1, 0. Now the parti cles will rise up before dropping down. Press Play. 

03 Got Frame 1. Add an At ribute Adjust Float node just before the popnet node. Set the following: 

 At ribute Name to life 

 Unit Seti ngs to Durati on 

 Pat ern Type to Random. 

 Min Value to 2 and Max Value to 4 

 Under Random, set Seed to $F 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eba9c8a1cadb81c01da17b2952f269efe596aa121d804f8e136765c9a2e8db08.jpg)


## SPARKS | PARTICLE TRAIL

The Parti cle Trail SOP takes an animated parti cle system and generates moti on trails from its parti cles. These trails can be used for various ef ects such as sparks, fi reworks, and rain. 

This node also allows you to control the look of the trails. This enables you to fi ne-tune their look in the SOP context, without the need to render the points with large amount of moti on blur. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/da3aa09748dd79c8cf636d38904f002c6171017b1fd948139a2b285c37c027c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/afffb1008720daacc10b31e1314e9feafca8c9b6509b17e5487427ee622e1073.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/89b2f777eb04cda54872c9da4375d64f3c2cf6487f321a37900b895d77a18de4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cb5cc561bfb3e0556cfa71d6f4e4810bb5bcd25cac836d544f248a2f6859291f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e16d8988efa42eba041bb56d50e9e4b528a9bdfcd600cdf62ce4b7c44fda83ad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/60c8658ab573086fb2ea1f2496a253de1a31323bfef8191223b476e711c2ef24.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6f7eb062e6e94283f773c2f6ccf94a253b960eabae0b70614d68b72ab0e7f0bb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/59f326faaa6b23bbac00a6ae3a2b7fb93b76c299ac10c3a0674bd56f158fc1ce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1efc1be37360b92abcdc472fef480a524c46aede74893389d1845a061d00b1ef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ad261ab75a1317eece73f345f532ecce7ad88ecdbd84e5c8d0669adac28aa784.jpg)


04 Dive into the popnet and delete the two collisiondetect nodes. You will not need to worry about collisions at this point. You will add other nodes back later when needed. Press Play to see the parti cles being emit ed. 

## 05 Go back up to the Geometry level. Go to frame 1. In the Network view, press tah > Snark Trail. After

In the Network view, press tab > Spark Trail. Aft er a short delay, this will put down two nodes - a ti meblend and a sparktrail node. Wire the popnet into the ti meblend node and the sparktrail into the SPARKS_OUT null. 

Press Play. You will see sparks but they will be lagging behind by the end of the fuse. 

06 Add a Time Shift node aft er the object_merge which brings in the cap and the at ributetransfer node. Click on the Frame parameter name to see the expression being used. Change it to <sub>$FF</sub> <sub>+</sub> <sub>1</sub> 

This will move the cap forward a frame but at the same ti me align the sparks with the end of the fuse. Press Play to test. 

07 Go to frame 1. Select the sparktrail node. Click on the Split tab and turn on the Enable Split checkbox. Set Percent to Split to 40. 

Under Shape, set Splits per Point to 4. Press Play to test. 

## 08 Go to frame 1. Jump up to the Object level. Set the camera to cam1 and press the Flipbe

Set the camera to cam1 and press the Flipbook but on on the bot om of the toolbar. Click Start on the window that pops up. This will create an animated sequence of the scene view that you can use to evaluate the moti on of your parti cles. 

Make sure the Realti me toggle is on and playback the fl ipbook to see how the shot is progressing. 

# PART SEVEN Blow up the Bomb

For the bomb geometry, a rigid body dynamics simulation will be needed. Start by fracturing the geometry then adding atributes that will create an explosion. You can then control the speed of the moving parts to art direct the look. Once the simulation is ready, you will cache out the geometry to work more eficiently as you move on to the PyroFX stage. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1d3c472e680e9ae77461cc8c59c3e085c365f9ff8024d7172bdc79940c8be707.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c0b83deae1404f3c78836dd866c54109bd9616f6d04b361fc3535c0f949ea6ad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/91cf5917850059ef8b29ad0beebd772b2443928cdd2a03a17a9c615d5a93c14c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/338c48891225d5f4c9ad23055322af13ee486cbf350178f57047fb99fad8b9ae.jpg)


01 Hide the fuse_geo, soot_trail, and sparks objects. Press Spacebar-G to focus on the bomb geometry. Go to Frame 1 in the Playbar. Press Spacebar G to focus on the bomb. 

Select the bomb_geo object and from the Simple FX shelf, select Simple Fracture. When asked to Select Collision Object just press Enter with nothing selected. It will then take a short time to set up this network. This object merges out the bomb geometry and sets up nodes for fracturing and simulating. 

02 On the fracture_solver node, set Start Frame to 200. Now set the start frame in the Playbar to 200. Click the First Frame buton to go to frame 200. You will only need to simulate the explosion from frame 200 to 240. 

On the fracture_solver node go to the Collision tab in the Ground Collision section, set Ground Type to Ground Plane. Click on the Advanced tab then in the Constraints >Glue section, remove the word Glue from the Data Name field. 

Press Play to watch the bomb fall apart. Now you want to add a starting velocity to explode the parts. 

03 Go to Frame 200. Add an Atribute Adjust Vector node and place it to the right of the other nodes. Wire the third output of the rbd_configure node into the atributeadjustvector node then wire the atributeadjustvector node into the third input of the fracture_solver node. 

Set the following on this node: 

 Turn on Enable Pre-Process 

 Turn on Overwrite Initial Value 

 Initial Vector to 0, 1, 0 

## 04

Under Adjustment Value, set the following: 

 Adjustment for to Direction Only 

 Operation to Spread 

 Adjust with to Noise 

 Spread Angle Min to 15 

 Spread Angle Max to 120 

Under Noise Patern set Element Size to 0.5. 

Under Post-Process turn on Post Process then turn on Length Scale and set it to 20. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cb8bc8921dfae7d954b3144cead4c1cb5aa4cb99f9421fe7f8fd705df11faf70.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/495ed4f11ecc7fe752624d31b6a4b025e2c9f19075df8a98d3cf57407114a6ac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6c933a17d5e8da5b6c4588f2e12c36f693d1a882cffddcfe9cb72572428724ef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b6cf73e3d04e8a40fc3bb2f5e45a235efef11199dcb2b709cfbe00f1032ce310.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0baf1a306fb54b5220459c1723886a9281136017e1ca682d35ffed48bd36d0a5.jpg)


05 Press Play. Now you have the bomb exploding. Seting velocity atributes on the geometry feeds into the simulation which uses the initial velocity of the pieces to propel them forward. 

The manipulation of atributes plays a bit role in many visual efects setups in Houdini. 

06 Select the rbdconfigure node. Open up the Speed Limit section and turn on the Speed Max and Spin Max parameters. Set Speed Max to 2 and Spin Max to 30. Press Play. The simulation slows down a lot from its original speeds. 

Now set Speed Max to 10 and Spin Max to 60. Press Play. 

07 Select the rbdmaterialfracture node and under Cell Points set Scater Points to 25. Press Play. Now you have a lot more pieces. 

Go back to the atributeadjustvector node and set Length Scale to 50 and Initial Vector to 0, 5, 0. Press Play. 

08 Go to frame 200. On the fracture_io node, set Base Name to exploding_bomb and Base Folder to $HIP/geo/ bomb. Click Save to Disk which will then turn on Load From Disk. Press Play to preview the cached geometry. 

## 09 OUT.

## Add a Null node and wire the first output of the fracture_ io node into it. Rename this node EXPLODING_BOMB_

# PART EIGHT Create the PyroFX Explosion

As the bomb explodes there needs to be an accompanying fireball. You will start with a Simple Fireball that works on the GPU then make changes to create a look that works for the shot. You can also incorporate the parts of the exploding bomb to push and influence the PyroFX volume in interesting ways. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d9ae36ce40c13f293d5dcbb546851184175ab29bbadf44d45e1d7965f5f9b1f2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e829bafec655ae3da175376570d17c0c8a98ba55539ac3fd7b7342cc45088cca.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d993b10278a011a97a04522ea431bbf4415f0fc52e33dde01f9896989307c6d4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/21fff66f0a6f43c742fa3360a997c84d8fb204d46625342c8378444db038c59f.jpg)


01 Go to the Object level. From the Simple FX shelf, click on Simple Fireball. In the Scene view, press Enter to place it at the origin. This creates several nodes inside a fireball object. 

Set the Display Flag on the pyroburstsource node and on the Burst Animation tab, set Start Frame to 200. Go to frame 200. This node represents the initial blast of the explosion. 

From the Quick Setup menu, choose Single Input Point. This adds a single point. Use the transform handle to raise it up to around 0.3 which is the middle of the bomb geometry. 

02 On the pyrosolver_fireball node, change Start Frame to 200. Set Simulation Type to Minimal OpenCL to simulate using your GPU. 

Under the Sourcing tab, open the Limit Source Range option and set the Frame Range to 200, 240. Turn of Cycle Length. 

Set the Display Flag on the RENDER_Simple_Fireball null node. Zoom out to see more of the scene then press Play to test the simulation. The Fireball is very big. Zoom out to see the whole explosion. 

03 Go to frame 200. On the pyroburstsource node go to the Burst Shape tab and set Initial Size to 0.35 and Spread Angle to 180. 

Now go to the fireball Pyro Solver node and click on the Bound tab and set Size to 15, 12, 12 and Center to 0, 4, 0. This will make a smaller box which will fit beter on the GPU. On the Setup tab, set the Voxel Size to 0.035 - this will add more detail to this smaller simulation. 

Press Play to test the simulation. Now the explosion fits beter in this scene. 

04 The next step is to integrate the Pyro FX with the exploding bomb. Add a File node and load the $HIP/geo/ bomb/exploding_bomb.$F.bgeo.sc geometry sequence from disk. Wire this node into the second input of the fireball Pyro Solver node. 

Press Play to test the simulation. The collision geometry isn’t having an efect because it hasn’t been prepared properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7384e9810ee14d5a22631131bb702207acc6da2d27cc0ae91418e75adc2420a2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab7db2b1db82f668db4370c47e891b39f3e338d92ee31379792c06bf4e66daff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6f53d27724782ee4c67cb35ca36173852236b6ccbefeaa8e7e39b034936b5639.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/08fd557aadedc5941345d5ee35963f19681e13d7be5a27aae0b3f03840c54140.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/15ad2b9d34ce39e09f52ccb29c5650ec4620d5e1cfcf107a6a91e1c0372e989f.jpg)


05 Go to frame 200. Select the fireball node. From the Quick Setings menu in the top right, choose Setup SDF Collision. This adds a vdbfrompolygons node. This node gets it’s Voxel Size from the Pyro Solver node. 

Add an RBD Unpack node between the file and vdbfrompolygons nodes. 

Add an Unpack node between the rbdunpack and vdbfrompolygons nodes. On the unpack node, set Transfer Velocity to v. Set the Display Flag on vdbfrompolygons then press Play to see the collision geometry. 

06 Between unpack and vdbfrompolygons, add a Peak node to make pieces bigger. Set Distance to 0.1. Between the peak node and the vdbfrompolygons node, add a Atribute Adjust Vector node. Turn of Adjust Value and turn on Enable Post Process then turn on Length Scale and set it to 2. 

Set the Display flag back to the fireball node. From the Collision tab, open the Limit Collision Range section and set Range Type to Frame Range and Frame Range to 200, 240. Turn of Cycle Length. Press Play to test the simulation. The exploding bomb is now colliding with and influencing the Pyro FX simulation. 

## 07 Between the fireball Pyro Solver node and the pyrolook node, insert a Pyro Post Process node. Turn on the

Convert to VDB and the Convert to 16bit Float checkboxes. Next turn on the Cull Volume and Resample Volumes options and leave them both set to vel. 

This node will make your volume more eficient and save you disk space when you cache your volume. 

08 On the fireball Pyro Solver node click on Quick Setups and choose Cache Simulation. Move the node to the side then wire the pyropostprocess node into the sim_fireball cache node then wire the cache node into the pyrolook node. Set Base Folder to $HIP/geo/pyrosim/ then click Save to Disk. 

Now with the Load from Disk option set to on, you can scrub in the Playbar to see the PyroFX explosion. 

09 Set the Display Flag on the pyrolook node. This is the Pyro Bake Volume node that can be used to visualize the simulation in the Scene View. It is designed to provide a similar interface to the Pyro Shader you will use later when rendering. 

Under the Smoke tab, darken the Smoke Color then under the Scater tab set Intensity Scale to 2500. Make other adjustments to get a look that you like for your simulation. 

# PART NINE Export the Geometry to USD

To set up the shot for rendering, you need to export the geometry to USD files that can be referenced into the Solaris context. While you could import the geometry directly, having it cached out as USD will allow you to lock down your sequences then focus on lighting and rendering in Solaris. For some of these objects, you will add UVs before exporting to prep for texturing. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6af26efdc8b2e803db937a22c435f54f9fb0ae71c484e394fcbc1826219f8879.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4795a666087161a787b353ed07953018351db115ef376296a9f99c8215381ec9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/22379f63c95ba1c22d886b20b416156c01e18670539a83424e9cd8556c65d87d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e43d3517512a60ba4369eea10d7f16eafe1d36647de4c7b1f6858b0ee9b6b446.jpg)


01 <sup>Go</sup> <sup>to</sup> <sup>the</sup> <sup>Object</sup> <sup>level</sup> <sup>and</sup> <sup>hide</sup> <sup>the</sup> <sup>fireball</sup> <sup>object.</sup><sub>Double</sub> <sub>click</sub> <sub>on</sub> <sub>the</sub> <sub>bomb_geo</sub> <sub>and</sub> <sub>set</sub> <sub>the</sub> Display Flag on the second polybevel node. This shows you the bomb geometry before it was rotated into place. 

Set the Display to Hide Other Objects to stay focused on the contents of this network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2de1bbe6da4d7e837d925178a6483fc5147dcd981c15911e243a72c22f21fd4b.jpg)


02 Go to the Select tool then press 3 to select Edges. Press w to go into wireframe mode and then press Shift and double click to select part of the loop at the botom. Press Shift and double click to select all four parts. Repeat for the inner loop. 

Now go to the loop on the top of the inner sphere and press Shift and double click to select. Now pick the latitudinal line that aligns with the X axis and press Shift and double click to select. 

In the Scene View, press tab > Group. Change the Group Name to uv_edges. 

03 In the Scene View press tab > UV Flaten which adds a uvflaten node after the group node. Set Seams to uv_edges and under Layout Constraints, turn of Enable Manual Layout. This provides a good looking UV layout that will be perfect for texturing the bomb. 

Set the Display Flag on the BOMB_OUT null node. 

04 Add a USD Export node to the end of the chain. Rename it static_bomb. Set the following 

 Valid Frame Range to Render Current Frame 

 Output File to $HIP/usd/static_bomb.usd 

Press Save to Disk. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7cf82f45207935c8b44d6420b0ee950395aab740c0e708fc298b18f3480210dd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4da781024853b2875afd1940a29a7fdb6c8a2f21edcacca8fcbcd6ad2a42518b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3c59c5fb814c0cc72063b993ac4c6eee65a9f9677be6ef405513d229cb0bb867.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e98253550f9a034ce5a8dad1c0f3cbaffa7a5c41aee813eab52c6ec2306f202e.jpg)


05 Go back to the Object level then double-click on the bomb_geo_fracture network. Select the fracture_io node and press Save to Disk to cache out the geometry with the new UVs. You won't see them yet because the geometry is packed. 

After the fracture_io node and before the EXPLODING_BOMB_OUT node, add an Unpack node then an Atribute Delete node. On the atributedelete node, enter name next to Primitive Atributes. Turn of the Point Atributes section. 

This ensures that the sequence comes into Solaris as a single mesh. The name atribute would break the sequence into individual parts. 

06 After the atributedelete node, add a Normal node. This will help the bomb geometry display properly in Solaris. 

Add a USD Export node to the end of the chain. Rename it exploding_bomb. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/exploding_bomb.usd 

Press Save to Disk. 

07 Go back to the Object level then double-click on the ground network. After the grid node, add a UV Project node and set its Display Flag. Go to the Initialize tab and press the Initialize buton. On the Transformation tab, change Scale X to -1, Scale Y to 1 and Rotate Y to -90. 

This will allow the texture to repeat on the ground surface rather than create one large texture, 

08 Add a USD Export node to the end of the chain. Rename it ground. Set the following 

 Leave Valid Frame Range set to Render Current Frame 

 Output File to $HIP/usd/ground.usd 

Hit Save to Disk. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cf6398b6cd1603c29ffad711c136ed73275056cce15a6614d8e0598d05feebfe.jpg)


## USD and SOLARIS

To support the look development stage of this project, layout, lookdev and lighting workflows are set up in the Solaris context. This is represented by LOP networks. The USD caches you are creating here will go into the Solaris context. 

You will reference the USD caches into the LOP network using this scene file but in a larger pipeline another option would be to start a new scene file and import the USD files in a fresh scene. This would let you focus on lighting and rendering your shot but would make it harder to go back and tweak the geometry and simulations. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6f14e379e586dc394f6d7633e8d9a255e0e54ad354398c9cf609e76c31ff8fe2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/087d715ecdb1fece8ccf91eb46147578e34180526313be994dd72e9b7b0741f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a4790f4a1b0539139b86ad1497ac284e4c66e9d271b38fccb65368a76715905e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f4a80590d7a0074848fe087f7b69e93130d30eccffc6c7f5edf0d8e2c8ae27f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/352500aa52546cd75dadb751686af3be5a16d4c9f7dc32d3d33f4f0511a6b0b0.jpg)


## Scene Import

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/602eb9ec88169978b8b582af9e37b0494229c28bdef57e0fcce2dbb796500e58.jpg)


09 Go back to the Object level then double-click on the fuse network. Add a USD Export node to the end of the chain. Rename it fuse. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/fuse.usd 

Hit Save to Disk. 

10 Go back to the Object level then double-click on the soot network. Add a USD Export node to the end of the chain. Rename it soot_trail. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/soot_trail.usd 

Hit Save to Disk. 

11 <sup>Go</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>Object</sup> <sup>level</sup> <sup>then</sup> <sup>double-click</sup> <sup>on</sup> <sup>the</sup><sub>sparks</sub> <sub>network.</sub> sparks network. 

Add an At ribute Create node to the end of the chain. Set the Name to width and the Value to 0.0005. This will determine the look of the sparks when they are rendered. 

Add a USD Export node to the end of the chain. Rename it sparks. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/sparks.usd 

Hit Save to Disk. 

12 Go back to the Object level then double-click on the fi reball network. From the sim_fi reball node, branch of a USD Export node. Be sure to bypass the pyrolook node. Rename it pyro_fi reball. Set the following 

 Valid Frame Range to Render Frame Range 

 Output File to $HIP/usd/pyro_fi reball.usd 

Hit Save to Disk. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/493f96d2ddff0b308d49c0df38d2e17d69db8cd91230badcd1897fea0116eb11.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4f6fad9c4ed937b122daa4f23ddf46b09f52786a6895f289db7d9366bbecc1be.jpg)


# PART TEN Set up the Shot in Solaris

Learn how to reference all of the USD files into Solaris then import the camera from the object level. Apply materials to all the elements and start rendering with Karma to evaluate the results. Learn how to add a key light and prepare render setings to explore the final look of the shot. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/20444e5546e820444ccc03093122db8b23b6c22e6ad0400b0a501cf6aeb45aab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1cd0a7f5ccae63eae1e5d6a2da2d6e9790546b709a338bcf1ffa7e90caf4473a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/512e1d4f8cc1bc83aa2ea222aae50c37de2e662b4242016a0df644147dade705.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b70b8a7fe74063b8cdc564264d1e1c05031ef2e1cf42971ffd42be5fc4aa4c37.jpg)


01 <sup>Go</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>Object</sup> <sup>level.</sup> <sup>Press</sup> <sup>tab</sup> <sup>></sup> <sup>LOP</sup> <sup>Network</sup> <sup>to</sup><sub>create</sub> <sub>a</sub> <sub>subnetwork</sub> <sub>to</sub> <sub>use</sub> <sub>to</sub> <sub>set</sub> <sub>up</sub> <sub>your</sub> <sub>shot.</sub> <sub>Name</sub> <sub>it</sub> create a subnetwork to use to set up your shot. Name it destruction_stage. Double click on the node to dive into it. 

Change the desktop to Solaris. Make sure you see obj > destruction_ stage in the Scene view’s path bar. Press D over the scene view and go to the Background tab and set Color Scheme to Dark. 

In the Network View press tab > Reference then click to add a reference node. Next to Reference Patern, click on the File Chooser and find the static_bomb.usd file. Rename the node to static_bomb. Set the Primitive Path to /geo/$OS. 

02 Alt-drag on this node to make three copies. Name them exploding_bomb, ground and fuse then point the File Chooser parameter to these USD files. 

Feed these into a Merge node and set its Display Flag. After the static_bomb node, add a Prune LOP. Set the Prune parameter to $F >200. After the expoding_bomb node, add another Prune LOP. Set the Prune parameter to $F <199. Now when you scrub in the Playbar, the bomb will switch between the static and exploding bomb at frame 200. 

03 Press tab > Scene Import (Cameras). Place down this node and wire it into the merge node. Set the Destination Path to /cam/. This adds any camera found at the object level into the Solaris context. 

Go to the camera menu choose cam1 to look through this animated camera. Make sure you have the merge node selected. Scrub in the Playbar to see the fuse and the exploding bomb animate and then explode through the lens of the camera you set up at the object level. If you were to make changes to that camera it would be reflected here in Solaris. 

04 In the Network View press tab > Reference then click to add a reference node. Next to Reference Patern, click on the File Chooser and find the sparks.usd file. Rename the node to sparks. Set the Primitive Path to /fx/$OS. 

Alt -drag on this node to make a copy. Name it soot then point the File Chooser and find the soot_trail.usd file. Add a Merge node to bring these files together then feed them into the main Merge node and set it's Display Flag. If you scrub in time, you will see the sparks and the soot persist after they were killed. The USD file holds onto the particles right until frame 240. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6ec737295cd6e39fe247148b0872d2942373856d94e56a8d19138b698ae02d57.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/edd881b7a70f43d975d4eefa0ea33445351c6d51deaf512b3abce8ba7b5f4d7e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6eb2b1a0c7424d587f685638404c1dc943e5caf00169cc032d1441b24fe61032.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3118570d5e3d996030b908c5f241941baa96d3002c2c726c9f4d5e8814f0bf93.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3c4f958a038260389853f4b1a05eb0b78486d02230a4f037d16fd156da49c7d3.jpg)


05 After the efects merge node, add a Prune LOP. Set its Display Flag. Set the Prune parameter to $F >199. Now the soot and sparks disappear at this point. 

06 Add a Material Library node after the merge node. Go to the Material Palete and drag a Principled Shader and a Concrete Shader into /stage/materiallibrary. 

Go to the Network view and rename the principled shader to bomb_mat. Alt drag to make three copies of the principled shader and call them fuse_mat, sparks_mat and soot_mat. 

## 07 Go back up one level and add an Assign Material node to the end of the chain. From the Scene Graph, drag static_bomb and exploding_bomb to the Primitives field.

Now click on the arrow next to Material Path and select the bomb_ mat. Press the plus sign to add more sections and repeat these steps to assign materials to the fuse, sparks and soot. 

Assign the concrete Material to the ground. 

08 Go to around frame 180. Click on the Light tool in the LOP Lights and Cameras shelf. This adds a light to your shot and has you looking through it. 

Go to the Base Properties tab and set Intensity to 50. 

In the Scene View, click on the Shadow buton and click on the surface of the bomb then Shift click behind it to create a shadow. 

## 09 In the Scene view, select Karma from the Persp menu. Turn of the Reference Plane.

Go back into the Material Palete and select the concrete shader. In the Texture section, set Efect Scale to 0.01. 

Turn on the Denoiser in the side bar. This will use your graphics card (nVidia cards only) to more quickly resolve the noise in your rendering. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/74771533b856c587d6001edafa7235bd8633e5b110bf3a1aeff3fc896f753108.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/79f521ffd02e550d7e38f6a49b7b00ea6cab37c23f86fafdf076fce0d6f6fc14.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3be6d786be866c3f7199d93a24434f4aba416f2acc92e82a4703e98c6ed2753c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4a4134d42f124eb180bdf06d510bebf3ef1fc07dcb8e2acd616c09585766c3b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f8d5c732f8e58381887fb177917f82b2b53d631a15f7d49a7b4ff2cff78a87b1.jpg)


## 10 Select the bomb_mat shader. Under Surface, set the following:

 Base Color to Black [0, 0, 0] 

 Roughness to 0.7 

Under Displacement, turn on Enable Noise Displacement and set the following: 

 Noise Type to Alligator Noise 

 Frequency to 30, 30, 30 

 Amplitude to 0.01 

 Roughness to 0.8 

## 11 <sup>For</sup> <sup>the</sup> <sup>fuse_mat</sup> <sup>and</sup> <sup>soot_mat</sup> <sup>shaders,</sup> <sup>set</sup> <sup>the</sup> <sup>Base</sup><sub>Color</sub> <sub>to</sub> <sub>a</sub> <sub>Dark</sub> <sub>Grey.</sub> Color to a Dark Grey.

On the fuse_mat shader turn of Use Point Color to allow the Base Color to control the look. 

## 12 Select the sparks_mat shader and under Emission set the following:

 Emission Color to 1, 1, 1 [white] 

 Emission Intensity to 10 

 Turn on Use Point Color 

This will make the sparks shine brighter and even create a bit of illumination on the ground surface. 

## 13 Go back to the Stage level. In the Network View, press tab > Karma to add a Karma Render Setings and USD Render ROP node. Wire them into the end of the chain. Select the karmarendersetings node and set Primary Samples to 32. On the Image Output > Filters tab set Denoiser to nvidia Optix Denoiser to turn the denoiser back on.

On the Advanced tab, go to the Sampling section and set Convergence Mode to Path Traced. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/66f1600782f311d3e15a004087a93d8d35aa226e9f77428f37ed432c801ec1db.jpg)


## RENDER SETTINGS

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/96b3af0c89c7d50bd576513895b514d7959494bcb35df61d0191bc3e8883a615.jpg)


# PART ELEVEN Render the PyroFX

To complete the shot, add the fireball USD file then assign the proper material. Next, you will set up another camera to create a wide angle shot of the explosion and then render out the two sequences to achieve the final sequence. You can then preview the results using the Mplay image viewer. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ee970112169ec27f8c172a50baa264a429d16d2b44417429f1a277579b15eb6a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/03c0cef6fb6e2cfa1d93afe13d1111cf78d25d2b12a48e555233f2c72ea74b44.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/572174b2b46d64d284f60ce22902e3324d7f443707ab6891cfc9023652be6ee8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dcc1e5cea7b6e691b090f200babc5decb84c0dd93ad8b4a8141ac18471017552.jpg)


01 Set the Persp view menu back to Houdini GL. In the Network View press tab > Reference then click to add a reference node. Next to Reference File, click on the File Chooser and find the pyrofx_fireball.usd file. Rename the node to fireball. Set the Primitive Path to /fx/$OS. 

Feed this node into the original merge node. Alt click on the connecting wire to add a dot and move the dot to the lower right. With the Display Flag on the Karma node, scrub to around frame 204 to see the explosion. 

02 Navigate back to the Object level then into the fireball object. Select the pyrosolver_fireball node. From the Quick Setups menu, select Create Render Stage. This adds lopnet_ fireball into this network. You can dive into it to see the suggested setup. You could use this to render the fireball on its own but you need it as part of our existing LOP network. 

Select the rendergeometrysetings node and press Cmd-C to copy it. 

03 Navigate back to the destruction_stage LOP network and press Cmd-V to paste it into the network. Wire it just under the fireball reference node. 

This node does two things. First it sets up velocity motion blur on the fireball then it uses the volume to help light the shot. 

04 Select the materiallibrary node and click the plus sign next to Number of Materials. Click on the Operator chooser buton next to Material VOP on the new listing and navigate into the fireball object then into the lopnet_fireball then into the matnet to select the Pyro_Shader. Click Accept. 

Even though this material is in a diferent LOP network, it can be referenced from its location to this materiallibrary node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3230aee39c52efc648952af55d884cfe225a994b0a6522c0a7f543a466c7a91e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b63c519c574823ace225443738cf0af9519969c52a54676339e70e8ca96b22d2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2c624ac7d5c5d72eea046ff98b6e83cbddda13a1bbbda2edef95764dbb17edfc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0c43629cf16d37f3af81963127b864c5f7c6a3c4c47cccbdfe82b45b5944a589.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4fcc545a5a396da08eff040dbbb5e0067b711f1b694d20795f5e35e9e7ba076d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b71738c28d7a7dcee82a8f85c84ad258d863fe16ce887cf10db9326854d0da47.jpg)


## 05 On the assignmaterial node, add another material listing and from the Scene Graph drag /fx/fireball to the Primitives section then click on the Material Path arrow and choose Pyro_Shader.

Set the Persp view menu back to Karma. 

06 Add Prune node to the network and wire it just under the rendergeometrysetings node. Under Pruning Options, set Prune to $F<201. 

The fireball at frame 200 was poking through the bomb geometry and this will delay the explosion for one extra frame. 

## 07 On the Karma node, set Valid Frame Range to Render Frame Range. RMB-click on the End value which shows 240 and select Delete Channels. Change the End value to 210.

You will use the animated camera for the first 210 frames then cut to a diferent camera for the last 30. 

08 Set the Persp view menu back to Houdini GL. In the Network view, Alt-drag on the karmarendersetings and usdrender_rop nodes to the right. Set its Display Flag. 

09 Tumble in the Scene view to get a new camera angle that is looking down on the explosion from above. Press the Ctrl key and click on the Camera tool in the LOP Lights and Cameras shelf. 

Set its Primitive Path to /cam/$OS and its name to cam2. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/18d90be12cb4ccc3c8856a13c9a38451fa03eea6fc02f1c9850f15f33af7e6c2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fc7840a02e0c814d3083bff560235cd0a7a04d4fb499866d5a796e378c40d986.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/66d94f79ea962d912d505f356dd90b8026fec7091f9977d471513a168662e842.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/dbd1b5d5ae1dd9b6f93a644a34f6a6ece55fc66e7bb294e30bb99998c359e8c9.jpg)


## CONCLUSION

You have now built a destructi on shot using parti cles, rigid body dynamics and Pyro FX. You built the complete project from scratch and have experienced many of the tools and techniques that Houdini arti sts use on a daily basis. You have also had a chance to bring your work into Solaris where you used USD to set up the scene graph for rendering to Karma. Now you can take these skills and begin exploring your own Destructi on FX shots. 

10 Lock the Camera to View and tweak the viewpoint to get the shot you are looking for. Check it at various points between frame 210 and 240. Turn the Lock the Camera to View opti on of when you are ready. 

11 Move the cam2 node up above the karmarenderseti ngs2 node. On the usdrender_rop2 node, change the Start and End to 211 and 240 then change the camera to point to /cameras/ cam2. 

Select the fi rst karmarenderseti ngs node and make sure that its camera is set to /cam/cam1. Otherwise the node will not render since the default camera1 isn't in our scene. 

Select both usdrender_rop nodes, and change the Output picture to: $HIP/render/bomb/destructi on_fx_$F2.exr 

## 12 Select the usdrender_rop1 node. Click on the Render to Disk but on. Repeat for usdrender_rop2.

Go to the Render menu and select MPlay > Load Desk Files. Go to the render/bomb directory and select the image sequence then click Load. This will play the images as a single animati on. 

# HOUDINI FOUNDATIONS TERRAIN GENERATION

Houdini includes a dedicated toolset for generati ng and shaping terrains. These tools represent terrain using 2D volumes, called heightfi elds, where each voxel contains the height of the terrain at a parti cular grid point. The Houdini viewport lets you visualize 2D heightfi elds as 3D surfaces. You can also set up mask fi elds that can be used to focus your edits to specifi c parts of the terrain. In this lesson, you will build up terrains using pat erns, noise and erosion then export the results for use in a game engine. 

## LESSON GOAL

Create a landscape using the Heightfi eld tools in Houdini and bring it into Unreal Engine or Unity. 

## WHAT YOU WILL LEARN

 How to create a Terrain using heightfi elds 

 Add pat erns, noise and distorti ons 

Create Masks using terrain features 

 How to create Scat er Points on heightfi eld 

 How to set up Instancing using Terrain Scat ering 

 Export the Terrain as a Digital Asset [HDA] 

 Import the HDA into Unreal Engine 

## LESSON COMPATIBILITY

Writ en for the features in Houdini 19.5+ The steps in this lesson can be completed using the following Houdini Products: 

<table><tr><td>Houdini Core</td><td>√</td></tr><tr><td>Houdini FX</td><td>√</td></tr><tr><td>Houdini Indie</td><td>√</td></tr><tr><td>Houdini Apprentice</td><td>√</td></tr><tr><td>Houdini Education</td><td>√</td></tr></table>

Document Version 2.0 | July 2022 © SideFX Soft ware 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/77b1e93d24e6b2a213492ad491ed4d8ae3a4a3dbbe4a789ce5ed01ae5cd57036.jpg)


# PART ONE

# Shape the Terrain using Heightfields

To create terrains in Houdini, you will work with heightfields. You will start with a blank heightfield then add some noise and distortion to define the basic look of the landscape. As you work, you can tweak parameter values on the nodes while layering in details. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a7d579a325c84992d2ae27d3f2775236ba35f0cf6e76fd4c3b4181abd0909420.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e98d7c8ff5f92502f3e9d98892d0c4c89bbd9cd5316b7661622b5bb7c04785dc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6738d4c4512f9156ed1ab110ced00a97dd27bb97c1f0c79cdadea582a01a3e62.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9c481e898cbe49aa859a895750e1731a4449545ab2514acda002cfd0a0738f3c.jpg)


01 Go to the Desktop selector and choose Terrain. This will give you shelf tools and radial menus focused on terrain. Turn of the Reference Plane using the buton at the top of the Display options then press d in the viewport and from the Background tab set Color Scheme to Dark. 

Select File > New Project. Set the Project Name to terrain_lesson and press Accept. Select File > Save As... You should be looking into the new terrain_lesson directory. If not then click on $JOB in the sidebar and you will be looking at the directory. Set the file name to terrain_01.hip and click Accept to save. 

02 From the Terrain Tools shelf, click on the HeightField tool. Press Enter to place it at the origin. Press Spacebar H to show the whole heightfield. 

This defines a 1000 x 1000 grid with a grid spacing of 2. 

03 Use the main radial menu (hotkey c) to select Deform > Noise. Set the following: 

 Noise Type to Worley Cellular F1 

 Amplitude to 360 

 Ofset to 20, 0, 300 

This kind of noise gives you a good starting point for your terrain. Use the main radial menu to choose Deform > Blur to access the Heightfield Blur tool. Set the Radius to 20. This softens the edges to make them feel worn by time. 

04 Use the radial menu to choose Deform > Distort. Set the following: 

 Amplitude to 40 

 Element Size to 220 

This node moves the existing values around by advecting them through a noise field. You can use the parameter values proposed here or explore on your own to get a look that you like beter. 

Houdini’s procedural approach would even allow you to come back later and change the parameter values to see how diferent setings afect the outcome. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b9443f7571cb7b7d832fe5bf97b7ee0f3570afd2a2be3a6421347af317223856.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bc0178fd4bcfbcaa371280f1737cf1b95f60ed82a92a72d9aa6181e8c783e023.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b743b3154e188e6a42b29ce5e814a47bad24f586bbf1ce23b507a9758ba9cb48.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c62315a2df1378425b9131cb293669de19aa659988e9f8e81acfa27a9ce2e62c.jpg)


## 05 Use the radial menu to choose Deform > Noise. Set the following:

 Amplitude to 10 

 Element Size to 20. 

Select the last four nodes in the Network view then click on the Network box icon to add a Network box. Adjust its edges to shape the box then click in the top bar and name it Shape the Terrain. Network boxes make it easier to read the network especially if you share your file with other artists. 

06 Use the radial menu to choose Mask > Mask by Feature. Set the following: 

 Min Slope Angle to 35 

 Max Slope Angle to around 60 

This lets you focus on areas on the side of the mountain. 

If you were to go back and change the shape of the terrain feeding into this node then the mask would update accordingly. 

## 07 From the radial menu, choose the Erode > Slump. Set Spread Iterations to 75.

The heightfield_slump node creates a type of erosion that moves unstable piles of rubble into a more stable configuration. It afects the Mask layer and also outputs to the Flow and Flow Direction layers. 

If you MMB-click on the node, you can see which layers are being created. You can MMB-click on an earlier node in the chain for comparison. 

08 From the Terrain Tools shelf, choose the Heightfield Remap tool. Set Layer to Remap to Flow then click on the Compute Range buton. Set Output Max to 1 to normalize these values. Use the radial menu to choose Mask > Clear Mask. This clears the mask layer so that you can use it to create more layers in your setup. 

Select the last four nodes in the Network view then click on the Network box icon to add a Network box. Adjust its edges to shape the box then click in the top bar and name it Create Flow Mask. Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9e30892eec8d6143ad3159cc16c851b24e0da889b41c6b24aca101e35eeecabd.jpg)


## HEIGHT LAYERS

• height 

[500, 500,1] 

# PART TWO

# Add and Visualize Mask Layers

You can set up layers on your terrain by first populating the mask then copying that information to a particular layer. You can do this more than once to add more layers. These layers can be used later to visualize key aspects of the terrain. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3de87059fac58457609645691cde978f293b4ab4a6b3b90a1abe898ed6143abf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8244b80099607c90833042b919f1678755e3b1c17ebc4b4c3c6c54f7911982c6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3ebb471e621655b2c5fa4d70f1c36470c73d90620dfb2657b54849f8d0ddbc78.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/84c685174cf6e5a92f437e59501b1c27a257c2f6b1ed3d3b55121cc8fff03f64.jpg)


01 From the radial menu, choose Mask > Mask by Feature. Under Mask by Slope, set the following: 

 Min Slope Angle to 0 

 Max Slope Angle to around 45. 

Turn on Mask By Direction then set: 

 Goal Angle to around 136 

 Angle Spread to 180. 

These setings cover a larger area of the terrain including the valleys. 

02 From the radial menu, choose Layer > Copy Layer. Leave the Source set to Mask and set the Destination to slope. By copying the mask to a new layer, it leaves you free to clear the mask and use it for other tasks. 

From the radial menu, choose Mask > Clear Mask. This again clears the mask layer so that you can use it to create more layers in your setup. Add a network box to organize your nodes and call the box Create Slope Mask. 

03 Use the main radial menu to select Mask > Mask by Feature. Under Mask by Slope, set the following: 

 Min Slope Angle to 0 

 Max Slope Angle to around 70. 

Turn on Mask By Curvature and set: 

 Max Curvature to 0.5. 

Next move the Curvature Ramp points in towards the center to find the peaks of the terrain. This gives you a very detailed mask that you can use to find the peaks of all the key features in the landscape. 

04 From the radial menu, choose Layer > Copy Layer. Leave the Source set to Mask and set the Destination to peaks. Afterwords, choose Mask > Clear Mask. This again clears the mask layer. 

You now have three layers that have all been derived from masks. Add a network box to organize your nodes and call the box Create Peak Mask. 

You will use these in the next step to visualize the terrain. 

# VISUALIZING HEIGHTFIELDS

To visualize your heightfields, you start with a ramp that is assigned to the overall height of the terrain. You start by Computing the Range that the ramp will apply to then you can adjust the colors in the ramp itself to visualize your landscape. 

You can then add colors to the various layers that will sit on top of the ramp. This lets you create a richer look for your scene. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2075cae9407aa4da60676883cff7e2e2824cbcf5977a9414b4b6bb211d27c38.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f494a687cdb82bf6b14aa73277224aa1ac01cca97e63e45c937e36efb2c0e5e4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0cc219046a08d1624426c42283699a86ae9b242063810850389ae47c3be6d1fb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/df53b53cfe93f8539775d238c91954a8676ceb4e86bd8fa1add8b35a272ca713.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/db1d2955601de46f081d06c36f51c65ca6dae1462ae3fdb05f7eda18069a1bbd.jpg)


05 From the radial menu, choose Visualize > Heightfield Visualize. Click on the Compute Range buton to align the visualization with the current heightfield range. 

This sets the ramp visualizer to go from the base of the terrain to its peaks. You can see how the ramp looks in the 3D view where the mountain tops are highlighted in white. 

06 Under the ramp widget, set the following: Layer 1 to peaks 

 Layer 2 to slope 

 Layer 3 to flow 

The default colors are now visible in the 3D view using the three layers you built up using masks. You will now use these to define the look of the terrain. 

07 Set all three of these layers to white. [1, 1, 1] This gives a snowy look to the landscape. You can use these layers for any number of diferent features, but for this mountain, snow is the look that you want to emphasize. 

## 08 In the Height Ramp, select and remove all the markers except two. Set the one on the right to black and the one on the left to dark grey. This creates a darker look under the snowy layers which helps the dark areas pop out visually.

Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/983802d60dca3fff0c6e6ddd48b887773421a31054a803e0006051ec99d4f1b9.jpg)


# PART THREE

# Remap and Erode the Terrain

Right now some of the heightmap is below 0 and some is above. You are going to use a Remap node to change the range and then use the ramp on that node to add a ridge around the moun tain. You will then erode the landscape to add new layers to the terrain. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8c48d767e353e5ae6b40865508ac7d7052de6c6d048c07ae8f6bd3f36d7714b4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d13ade02f53e7143676132b88459aa49a27b09169ea515134d8fba9a5bc330b9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8f1588576264bf1bd6728faf6fa8b8a1b330113a2127e9c15f3f594ec84364dd.jpg)


01 Find the Heightfield Noise node at the end of the Shape by Terrain Network box. Turn on its Display Flag and click to select his node. 

From the Terrain Tools shelf, click on the Heightfield Remap tool. Click on the Compute Range buton. To reframe the heights, set the following: 

 Output Min to 0 

 Output Max to 300 

02 Using the Remap ramp, add points in the middle then add and adjust the following points: 

 Point 2 has a Position of 0.25 and a Value of 0.25 

 Point 3 has a Position of 0.4 and a Value of 0.27. 

This creates a ridge running along the base of the mountain. 

03 Choose Erode > Erode. Click on the Visualization tab and click the Compute Range buton. Press Play to watch the terrain erode. Stop around frame 15. 

04 Set the Display flag back to Heightfield Visualization node at the end of the chain. Set Layer 3 to water which is a layer that is coming from the erode node and change its color to a blue. This will bring out some of these areas in the visualization. 

# PART FOUR

# Scater points on the Terrain

To add trees and rocks, you will mask out the new plateau area then set up a special terrain scater that will use this mask. These scatered points will then be used to copy instanced cones designed to represent trees. These will be replaced later in Unreal. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cf283142b66e90a67f954b996e1d3c7194baef47a20aaba22f8c09112375f58d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5f8d29490f91259b039d665e7501e8189670aae8b68b5a173b510a79568ab2ef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0372772428032f1986584a0f0147488d97e453ae4347625c68a1e9a797116873.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a248460f1f1e9c47b2bbfe8bc3a015dffb9a93aa0b99ed9c7078be4e06118d50.jpg)


01 Use the radial menu to choose Mask > Mask by Feature. Set the following: 

 Min Slope Angle to 0 

 Max Slope Angle to 50 

Turn on Mask by Height and set the following: 

 Min Height to 70 

 Max Height to 85 

This should highlight the plateau created with the remap node. If not then tweak these values until you isolate this area in the Mask. 

## 02 In the Network editor RMB-click on the output of the maskbyfeature node and start typing scater…

Place the Heightfield Scater down and set turn on its Display flag. Now wire the output of the maskbyfeature node into the second input of the scater node to restrict the points to the area defined by the incoming mask. 

Set Coverage to 0.05. Turn of the Keep Incoming Terrain option. 

03 In the Network Editor, press tab and begin to type Copy to Points and click to add this node. Click the Pack and Instance check box to turn it on. Wire Heightfield Scater into the second input of Copy then set its display node. 

In the Network Editor, add a tube node down then feed it into the first input of the copytopoints node. Set the following: 

 Radius to 0, 2 and Radius Scale to 1 

 Height to 10 and Center to 0, 5, 0. 

Add a color node after the tube to make the trees green. Add a Merge node and feed Heightfield Visualize and copytopoints into it. 

04 Go back to the heightfield_scater node and turn of the Match Normals with Terrain and Match Direction with Slope. This will ensure that all the trees are pointing up. 

Now change Random Up to 10 to create some variation in their direction and set Randomize Yaw to 20. You cannot see the efect of this but if you replace the tree later you will see random rotation. 

The Scale of the trees is controlled by Variability. Change the Range to 1, 2 to create random scales these two values. 

## PART FIVE

## Open the Terrain in Unreal

To bring the landscape into game engines such as Unreal Engine or Unity, start by creating a Houdini Digital Asset. Once you have the Houdini Engine plug-in set up properly, then this asset can be loaded into the game editor with the copied tree stand-ins importing as instanced objects. When you import the terrain into Unreal Engine, the heightfields will be recognized as a landscape. You can also import the asset into Unity using the Houdini Engine plug-in. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5a2bf0a0f32665a9e12a38f61a4ebcdad9e2b0f0651077a1328005b29681f259.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c49f844d775c6617be62530c82b8812e0e56e27c32a3d833c7da02532451db98.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1dc5c7d6623ed64f1f1d83d2f6fe030e383786605cedfe2bfc738dcdbd65ca2c.jpg)


01 <sup>Select</sup> <sup>all</sup> <sup>the</sup> <sup>nodes</sup> <sup>in</sup> <sup>the</sup> <sup>Network</sup> <sup>editor.</sup> <sup>Click</sup> <sup>on</sup> <sup>the</sup><sub>Create</sub> <sub>Subnet</sub> <sub>from</sub> <sub>Selected</sub> <sub>Buton.</sub> <sub>RMB-click</sub> <sub>on</sub> <sub>th</sub> Create Subnet from Selected Button. RMB-click on the new subnet and choose Digital Asset> Create New. 

Set the Type Name to terrain and turn of Branch and Version. Set Library Path to HIP File Directory and Library Filename to Node Name. 

Click Create. The Edit Type Properties window opens up. Click Accept to close this window. 

02 Open Unreal Engine and from the main panel click on the New Project tab and choose the Third Person template. Click Create Project. When it opens, delete the default geometry so that it doesn’t get in the way of your terrain. 

From the Content Browser, click Import to Game and find the terrain.hda asset file. Drag the asset from the Content Browser to the 3D workspace. Set the ThirdPersonCharacter up to a Translate Z of around 10,000 then press Play and walk around the terrain. 

03 Go to the Houdini Instanced Inputs section and expand terrain1_1. This is the cone instance which you can replace with content from within Unreal. 

In the Content Browser, open StarterContent > Props. Drag the SM_Bush prop over to the Houdini Instanced Input. Set the Scale Ofset to 5, 5, 5. The geometry is instanced to the points then randomly scaled and rotated just like the cones. 

In the outliner, select the Landscape node under terrain. Beside Landscape material, click on the menu and find a grass material. Press Play to explore the Terrain. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7b717c33fd9ed66e49192785c78421513ce5036c1116afaa967d045e4e1fc4d4.jpg)


## CONCLUSION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c75e0cf81f80bf76e318a4bc52f726cfe1e6be8bf8188f66b4e3ea0e0b81fce3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aeac6ae1556c9673e5b9d6df5eee94330e31d91d6e7b84dbc81c0f2f97505003.jpg)


## CHARACTER FOUNDATIONS KINEFX RIGGING | FUR DUDE

In this lesson, you will rig, animate and add fur to a two legged character named Fur Dude. Starti ng with existi ng geometry, you will draw the skeleton, capture the geometry then build rig controls for an animati on rig. You will then keyframe a walk cycle and add fur to the surface of the creature. 

This lesson uses KineFX, Houdini’s new SOP-based procedural rigging tools. While these tools are used primarily for retargeti ng workfl ows they also include tools for rigging characters and creatures. These tools are sti ll evolving and this lesson of ers a taste of what will be currently possible. In future releases, you will see the KineFX and animati on workfl ows expanded and refi ned. 

## LESSON GOAL

To rig, animate and add fur to the fur dude creature. 

## WHAT YOU WILL LEARN

 How to build a skeleton using KineFX joints 

 How to capture deforming and rigid geometry to the skeleton 

 How to wrap up the capture rig into a digital asset 

 How to add controls and build an animati on rig 

 How to animate a walk cycle 

 How to add fur to the creature 

 How to render using Solaris and Karma. 

## LESSON COMPATIBILITY

Writ en for the features in Houdini 19.5+ 

The steps in this lesson can be completed using the following Houdini Products: 

<table><tr><td>Houdini Core</td><td>√</td></tr><tr><td>Houdini FX</td><td>√</td></tr><tr><td>Houdini Indie</td><td>√</td></tr><tr><td>Houdini Apprentice</td><td>√</td></tr><tr><td>Houdini Education</td><td>√</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6f924553f58b3106b6ea424f4ad1a746147a197d40d44bd324178a1f65dc0461.jpg)


# PART ONE Draw the Skeleton

Start by opening the scene file and reviewing the Fur dude geometry then place joints using the Skeleton tool. This tool will let you create, name and adjust joints to line up with the character you want to animate. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b8eb200c2eae180927974eb039143d96b8242592e66b632c63951173ece2f534.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/27ad84f6d509c7142b0161799ab083263f43807b7759c6749b06fefbf0cc0e05.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/20288f828e32034a79811c81415494486896a384277120e94089ae99bccc5cd5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1fcafffa9d2645a09b5b9d3ee154df13d5d737398eaeec545bc969fd1c66c7bb.jpg)


# PROJECT FILES

Go to the Fur Dude tutorial page on SideFX.com where you got this document and download the furdude_lesson_start directory. Rename it furdude_lesson then put it into the Houdini Projects directory. 

01 Select File > Set Project. Find the furdude_lesson directory that you downloaded earlier and press Accept. This makes this project directory and its sub folders the place for all the files associated with this shot. 

Select File > Open. You should be looking into the new furdude_lesson directory. Open the file name to furdude_start.hip. Select File Save As... and rename the file furdude_01.hip. Click Accept to save. This way you can go back to the start file later if you want to redo the lesson. 

02 The scene opens with a single object called fur_dude_rig. You are going to capture this geometry to bones created using the KineFX toolset. 

Double-click on the node to dive down to the geometry level. Here you can see the File node which is importing the fur_dude_geo.bgeo file from disk. 

This geometry has some information stored with it such as primitive colors and groups. To see this you can MMB-click on the node to see Atributes and Groups listed. You will use the groups later on to help capture the geometry. 

03 Move your cursor over the Scene View and press spacebar-b to go to a four view layout. From the icon in the top right, turn on Link Ortho Views. Now you can pan and zoom in the top, front and right views and they are all synced up. Move your cursor over the Right view and press Spacebar-b again. This is a good view for drawing joints. 

04 In the Network view, press tab > Skeleton and place the new node next to the File node. Set it’s Display Flag. Set the file node’s template flag so that as you are working with the skeleton node the geometry is visible as a grey wireframe. 

Make sure the Handle tool is selected. In the top bar, set Joint Placement to Freehand. This will draw on the construction plane without taking the geometry into account. Click to place your first joint just above the leg and then place six more joints as shown in this picture. 

MMB-click to stop drawing joints. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fcfec6c89310688aa4c1e4023c2507c13ce5567aa938dabe00387d1ed71820c4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b421e6d9955dbe1c20b33fe0a0b7f792d4a1eb52f55d74012df1bb53ab921b07.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/eb7bb58d5cb058874b074ac1c399a5af0d04b04d59ac55d553271e233334cd98.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fc82b986e5132f5b2b537ea8cb8a19b00d86f5fee8606a415133783f8e430be7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/641574ce736c8a9a848ae99a70df2c8bae94a55590fe29b7a498d3ff8f9adbf8.jpg)


05 In the top bar, set Mode to Modify. Now you can edit the joints instead of drawing them. Click on the fi rst joint and in the top bar set its Name it COG. 

In the Parameter pane, click on the + sign in the tab area. From this choose New Pane Tab Type > Animati on > Rig Tree. This brings up a pane that shows your skeleton joints. You can double click on the second joint and name it spine1. Now either use the Scene View or the Rig Tree to name the rest of the joints as shown. 

06 In the top bar, set Mode back to Create. By default it will try to draw from the end of any selected joint. MMB-click to stop this drawing acti on. Now click on the COG joint in the Right view then draw a pelvis joint just below it. 

In the Scene View, press spacebar-b to go back to a four view In the Front view, draw a hip joint on the left side of the character. 

07 Now go back to the Right view and draw the fi nal four joints for the leg as shown here. 

Go back to Modify mode then rename the joints using either the Rig Tree or by selecti ng and naming the joints in the top bar. Aft er the pelvis, all the other joints will have a “l_” prefi x since these joints will be used for the left leg. 

08 In the Scene View, press tab > Skeleton Mirror. This creates a mirror copy of all the joints. Go to the Parameter pane and click on the arrow next to Group. Select only the leg joints and press enter. Now only the leg is being mirrored. Under naming, set Find Tokens to l_ and Replace Tokens with r_. Now you have the right leg joint properly named. Select File > Save to save your work so far. Select File > Save to save your work so far. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b299596acc73299173ce18ee13f66a3b7fc4f6a0e38c35086ca91df258172d32.jpg)


## KINEFX VS OBJECT LEVEL RIGGING

The KineFX tools in Houdini of er a joint-based workfl ow that takes place at the geometry [SOP] level. Houdini’s other character workfl ow is bone-based and in this case you work primarily at the object [OBJ] level. 

In the KineFX workfl ow, joints are basically just points on a curve and this opens up lots of opportuniti es to use sop-level tools to manipulate rigs. Here you are going to learn about tools designed specifi cally for rigging characters and creatures. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7faeda61ddce0b0d50ef2905e67932b785f0a3d6c37f36ccfb3270f3e7601706.jpg)


# PART TWO Capture the Geometry

Rigging a character involves capturing geometry to the skeleton joints in such a way that rotating the joints deforms and bends the geometry. Houdini uses a biharmonic capture method that gives great results with your first capture so that you can start testing out your rig right away. Later you will paint capture weight s to refine the results to work with your character. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4c53a9bef43cfd12dbfa50e713c66139eae957f74026d5d8496e6333525deeed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a5a2b99979c992defcb0654c26b08e46326a3e5649a07387d931d8e0f507d30.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/712606908e33a44a9d5371ef3d248b2f96ca275277746b10d51178e57f512969.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b8ca616fe8d864cae49e389a1e42671c59c78b01d80ee0cd38d43139427ce506.jpg)


spacebar-b. Make your Network View a bit bigger so you have room to work. 

In the Network view, press tab > Joint Capture Biharmonic and place this node down under the skeleton nodes. Wire fur_ dude_geo into the jointcapturebiharmonic node’s first input. Wire skeletonmirror into the jointcapturebiharmonic node’s second and third input and then set its Display flag. 

You can now see capture weights on the geometry. You will refine and paint these later to set up the deformation of the geometry. 

02 In the Network view, press tab > Bone Deform. Wire the three outputs of jointcapturebiharmonic into the three inputs. Set the Display flag on bonedeform. 

In this lesson, you are capturing teeth, claws and the eye which you probably don’t want to deform. You will split these out later to capture them using a diferent method. 

03 Next press tab > Rig Pose and place down the node. Move it over the third line connecting jointcapturebiharmonic and the third input on bonedeform to add it into the chain. This is where animation goes on the rig and the rigpose will be used to rotate joints and can also be used to set keyframes. 

04 Select the rigpose node and make sure the Handle tool is active in the Scene View. Select and rotate various joints to test out the deformation. You can reset this later so feel free to explore. 

## PART THREE Add More Bones

It would be nice to have more bones in the mouth area. The procedural networks in Houdini let you to go back and add the joints and all the other nodes including the biharmonic capture will update to reflect the changes. This gives you flexibility when first seting up your creature’s rig. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/07bfeca5586b7a7bc71ec34c97b32eff5cccbbd68465017e815c1daa73f2db38.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f51621b3ed4e1e8a84b6b68b420c82c4b014140d19950a8b45915f02c973915b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1acba5f753bd6ffe952d45c51aa662974b6abc26a430f8c2b94dad90405039c4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/603c721503dc11e0f71d574c9d0c6c697c8ce1a8249dc529973ee7922438e662.jpg)


01 In the Network view, set the Display flag on the skeleton node and the Template flag on the original File node. Go to the Right view in the Scene View using spacebar-b twice. 

Set the Display Flag on the Skeleton node. Select the skeleton node and turn on the Handle tool. Set Mode to Create. This will allow us to add more joints to the skeleton. With KineFX, you can add bones and the procedural nature of the other nodes in our network will allow these changes to be accepted. 

02 Click on the neck1 joint to start drawing then click two joints at the jaw and lower mouth. When you have these joints in place MMB-click to stop drawing and change Mode back to Modify. Now either click on the joints and rename them jaw and lower_mouth or rename them using the Rig Tree view. 

03 You can edit the joint positions in Modify mode. Turn On the Tweak checkbox in the top bar and now you can click drag on joints to move them. As you move a joint, all of its children will also move and you may have to adjust them back into place. To avoid this, you can turn on Child Compensate. 

If you RMB-click on a joint, you will see options for spliting, unparenting, copying and pasting joints. You won’t need to do those things for this skeleton but it is good to know they are there. You can even mirror joints here but you are using a diferent node for that in this network. 

04 Set the Display flag on the bonedeform node and turn of the Template flag on the file node. The geometry will be reconfigured then captured using the new bones. Select the rigpose node and select the Handle tool. 

Click on the new jaw joint and rotate it down. This works but it manipulates both the lower lip and upper lip. It would be beter if it only afected the lower lip. To fix this you will paint the capture weights in a later section of the tutorial. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2080f3121763c8d96751cf59caedc974ea9224db7248946209370acc6038edaf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/af4e7dcc16311a6c35b138737e6edac047b3cf0a955d975a323d4d97dbb46ebe.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/44aba5149315645ad8b8688d81b0f6fd45a1d8f4597be496d04c4fd120f32b9a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9a45054a04868cd4ce1fef1e5210c4ac21bfea0fe1ad2078bb3da8a23a48bfd7.jpg)


## 05 Set the Display fl ag back to the skeleton node and the Template fl ag on the original File node.

Select the skeleton node and turn on the Handle tool. Set Mode to Modify. Click on the head joint and using Tweak Mode, lower it unti l it aligns with the eyeball. 

Set Mode to Create. Click on the head joint and then click a new joint right in the center of the eyeball. Switch to Modify mode and Name this joint eyeball. 

06 Set Mode to Create. Click on the head joint and then click a new joint above the eyeball joint. MMB-click to deselect then again click on the head joint and then click a new joint below the eyeball joint. 

Switch to Modify mode and Name these joints upper_lid and lower lid. You will use these joints to rotate the eyelids during animati on but they need to also be at the center of the eye. 

07 Turn of the Template fl ag on the geometry. Select the upper_lid joint and use Tweak Mode to drag it down on top of the eyeball joint. Repeat with the lower_lid to overlap the eyeball joint. 

You now have all three joints in the same spot. Later you will at ach geometry to each of them individually and then you will be able to animate them independently. 

## 08 Set the Display fl ag on the bonedeform node. The geometry will be reconfi gured then captured using all the new bones.

You are not able to pose the new joints yet because the geometry hasn’t be at ached to them in a rigid manner yet. That will come a couple steps down the line aft er you paint capture weights on the body and the tongue. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0e24074b3d4a387f7f0e0965a988ed8dfdfdc1568cea5926aed4fd22c7550bb4.jpg)


## JOINT ORIENTATION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fe58312838c750084b0dd076f320ec923c679bc032539d4e06511e205fd90d22.jpg)


# PART FOUR Joint Orientati ons

When you animate the character, the orientati on of the joints plays a signifi cant role in how you manipulate the rig. At this point, you will orient some of the joints by hand and then use a Re-orient joints node to point all the other joints down the -z axis. Someti mes when you evaluate your rig at a later stage, you may need to come back and tweak the orientati ons. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1b3dcc343d6b21a305cad24b186614160eecc94eeddb172618061e23142a5989.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7e3007d0988ae57c8e4b28f3dbdb51b798f0d604a4331bff6c9d06b6259389b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ba377c3a4265763c494ad545cde2e260c8a2c23ada2a6dd44546c7f83f966932.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e11e68c338c1db8cadc3a927801fbbd8065ac77fd19cabbc3268a3fb2aadcf84.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/97a8df39e9bf4c5c6b233fed0392fd4a4678dff568eddb7b8be7814919c347ee.jpg)


01 Go back and set the Display fl ag on the skeleton node. In the Scene View , RMB-click and select Display Joint Axes to see the joint orientati ons. Select the COG joint and RMB-click and select Show Handle. Now if you rotate the joint the whole rig goes with it. Press Ctrl-Z to undo. 

Click on the Child Compensate checkbox and now you can rotate the joint without changing the rest of the skeleton. You can use the Ctrl key to constrain to 45 degree increments. 

02 In the Scene View, press p to bring up the parameters for this joint. To orient the COG with the world, Set Rotate and Local Rotate to 0, 0, 0. 

Click in empty space to deselect the COG joint then click on the Pelvis joint. Set Rotate and Local Rotate to 0, 0, 0. 

03 Aft er the Skeleton joint, insert a Orient Joints node which will by default point the orientati ons along the positi ve Z axis. Click on the arrow next to Orient group and in the Scene view, select all the joints. Press Ctrl and select the COG, pelvis and neck1 joints to remove them from the selecti on. Press Enter. 

Now all of the joints are oriented along positi ve Z except for the three deselected joints. 

04 Set the display fl ag back to the Bone Deform node to allow all the other nodes to update and accept the new joint orientati ons. 

The results don’t look any dif erent than before you oriented the joints but it will af ect how you pose and manipulate the character when you are animati ng. 

# PART FIVE Atach Capture Geometry

Right now you are using the skeleton joints to capture geometry and assign capture weights to each point on your character. To manage this with more control, you can atach curves to the joints that will extend the influence of that joint. This provides a method for achieving your goals as quickly as possible. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fa9662d8bc03628af292cab477b79ae176b51d656fe180aaa24208ba33b0f74c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f69d657b77a7f0826e790bc221e67fc15f3608eb9c26b615400dd6ca96b70150.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/807fb236d7b8bb07f5d4da03c63b15e2e9bdf79641c1bd7b17203c69951149a8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ec1a039364685d9e277779eee60dbf1ee87d5f7be90e3838a3c9524bc96c2592.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d91a79d880110f9afdb8775d06c44d00093e7286246e03e784314d376bd9687e.jpg)


01 In the Network View, press tab > Split and place the node between the File node and the jointcapturebiharmonic node. The first output of the split node should be wired into the first input of the jointcapturebiharmonic node. 

Click on the pull down menu in the Group field and choose the fur_dude_body and fur_dude_tongue groups. These are now feeding the first output of the split node and all the remaining pieces such as the eyeball, teeth and claws are going out the second output. You will use a diferent method to bind those to the skeleton after painting weights on this geometry. 

02 In the Network View, press tab > Visibility and place the node between the jointcapturebiharmonic node and the bonedeform node. Click on the pull down menu in the Group field and choose the fur_dude_tongue group. 

This node hides the selected geometry but does not remove it. This ensures that point numbers and primitive numbers don’t get changed which is important when working with the paint capture weight tool. You don’t want to change this information every time you hide some geometry during this process. 

03 Press S to get the Select tool and 3 to go to Edge selection. Select an edge in the middle of the lower lip on the left then press Shift-A and select an edge on the other side. 

04 Press tab > Curve from Edges and the selected edge will be extracted from the geometry. Rename this node lower_lip. 

The curvefromedges node gets placed in between the file and jointcapturebiharmonic nodes. Move it to the side and then reconnect the file node output to the first input of the jointcapturebiharmonic node. This branches the curvefromedges node of to the side. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3be4ea743e6b25d7c7d9221e420d6b5f360233dad4d36dcca575e89c83dcc604.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/59ca46c0eb7c0bd5d7be3e8025c4314549d08ec3f131aa45a2d2857f3701f778.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4350f7f4391fa7615fb14bb3719b4dd232aaddb0a21924c8246c867acb2d1b30.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7dcb9b4c83c79476503dd3fff5a0759c27b7787d21292093f48b0f92a6af02f8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3cd148ff6bc2d340e69c05da48b26d448e33c80f04e8cbcc8e63dbe17b6f6207.jpg)


05 Press S to get the Select tool and 3 to go to Edge selection. Select an edge on the upper lip on the left then press Shift-A and select an edge on the other side. 

Press tab > Curve from Edges and the selected edge will be extracted from the geometry. Rename this node upper_lip. 

Branch this node of the same as you did with the other one. 

06 Press tab > Merge Packed and place this node down underneath the two extracted curve nodes then feed the output of those nodes into the mergepacked node. 

Press tab > Atach Capture Geo. Add this node to the network then feed the skeletonmirror node into the first input and the mergepacked into the third input. 

07 Feed the add_capture_geometry node’s output to the middle input of jointcapturebiharmonic. Under Advanced Shape Setings, click the Assign Shapes plus sign buton two times. For the first one, set: 

 Group to @name=lower_mouth 

 Shape Name to lower_lip 

And the second one to; 

 Group to @name=neck2 

 Shape Name to upper_lip 

Turn On keep Shape World Transform for both Shapes. 

08 Set the Display Flag on jointcapturebiharmonic. Now bypass the add_capture_geometry node to show diference in the capture weights. 

When this node is turned on, the atached curves are assisting with the capture of geometry to the associated joint. This allows for more control as you set up your character. 

09 Set the Display flag on the bonedeform node. Click on the rigpose node and in the Parameter pane, click on the Clear buton next to Transformations. This will reset the joints. Now with the Handle tool active and in the Scene View click on the jaw joint. Rotate it to lower the lips down. 

You can see that this still deforms parts of the belly. To correct this, you need to paint capture weights to reassign capture weights to diferent joints. 

## PART SIX Paint Capture Weights

The biharmonic capture added weights to the character’s geometry that are associated with the diferent skeleton bones. You can now use a new node to adjust the capture weights using a brush workflow. For this creature, the goal will be to get the top of the mouth to not be influenced by the lower mouth joint and to tweak how the feet area is weighted. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4717c3593c786caee3961c6da5e1871c3646b663bd66fe320f34fb04d61ba0e0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ba92fb89234645e70caa80a24827d9af8767eaf728f9388769a2b693a5dc4765.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/adfc146fa3d62135234489a521f8aee923cb822c8743387f5689e34067b978ef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f997cd184d0a3472105e667aeefa5c295080ce2c8ab99ed88f6a27c5208990a0.jpg)


01 In the Network View, press tab > Joint Capture Paint and place the node just above the bonedeform node with all three connectors geting connected. Set its Display Flag then click on the pull down menu next to Target Joint and choose the neck2 joint. 

In the Scene view, you will also see a big round paint icon on your cursor which you can use to paint weights. Paint on the head area and this part of the geometry will be captured to the neck2 joint. 

02 You want to capture the head and the upper lip area to the neck2 joint. The geometry will appear red when it is at its strongest. 

Use big strokes for the top of the head then use the Scroll wheel on your mouse to reduce the brush radius or go to the Brush tab in the Parameter pane to change the radius. 

03 Paint on the upper lip to increase the influence of the neck2 joint on this area. Make sure you are painting the top lip and not the botom lip. If you mess up, use Ctrl-Z to undo your stroke. Tumble around, even inside the mouth to get the upper part of the mouth. 

In the Operation Controls panel, you can see options to Display Deformed Geometry, Display Joints and Display Color. You can turn these on and of to help you evaluate your capture weights as you paint. 

04 Press F and choose Smooth to smooth out what you have painted here with other capture weights. Make your brush radius a bit bigger to create more smoothing. 

Once this is finished, click on the rigpose node with the Handle tool active and in the Scene View click on the jaw joint. Rotate it to lower the lips down. You can see that now the top lip isn’t moving but other parts of the head are being rotated. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/97cb753390ecc50258ae7f3152545bcc2c566e8a72d834f7a29fddac21bf18c2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7e860ee4064613586396e501fe4469d55c466c7b429956a92ab1f432e24d5fd1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aaab85b4d39db9b76d815ee3e6620dc023df820c086618851611921e218b6ef2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f1db793a9b493b3562969fda213a3fd40b8379c06bf98daa9ef513c76546687a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ca94ad33977b7ff03f4adb644270cc357d2a5ccd7e505edb768d35ef9d3eb06e.jpg)


05 Select the jointcapturepaint node. Click on the pull down menu in the Capture Region field and choose the jaw joint. Press F and choose Subtract to take away influence of this joint on the top of the head and eye area. 

You can also use this method to remove the influence of the jaw and the lower_mouth joints on the belly. That way when the mouth moves the belly isn’t afected too much. 

06 From time to time, go back to the and test out the jaw. Once you have it no longer influencing the head area then you are good to go. You can also go back to smoothing to clean things up once you are finished. 

You can now paint weights for other joints in the skeleton. The Biharmonic should have done a good job on the legs and feet but you can test the rig using rigpose then paint weights to refine the results. 

07 Select the toe joints and make sure that the ends of the feet are captured to those joints. Later you will use a reverse setup and having the geometry atached to the toes . 

## 08 On the visibility node set Apply to Non-Selected Primitives . Now you only see the tongue.

It should also be weighted fine by default but you can paint weights if you need to. Select the jointcapturepaint node and paint weights for the neck1 and jaw joints. 

When you are finished then Bypass the visibility node again. 

## 09 On the visibility node set Bypass Flag.

Once this is finished, click on the rigpose node with the Handle tool active and in the Scene View click on the jaw joint. Rotate it to lower the lips down. If you are happy with how all the parts are working then you are ready to capture the rigid geometry. 

# PART SEVEN

# Capturing the Rigid Geometry

Earlier you split out the eyes, teeth and claw geometry. Now you are going to pack this geometry then assign each part to a joint using the capture packed geometry node. This is the equivalent of parenting each object to the skeleton since parenting isn’t an option at the geometry level when using KineFX. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e2facf0ec9a972a44d8e2b5363cb28ca0c14f26e9c7adfeba839fc17ee3283ad.jpg)



objfur_dude


<table><tr><td colspan="3">Node:pack1</td></tr><tr><td></td><td>name</td><td></td></tr><tr><td>0</td><td>fur_dude_eye</td><td></td></tr><tr><td>1</td><td>fur_dude_gums</td><td></td></tr><tr><td>2</td><td>fur_dude_lclaws</td><td></td></tr><tr><td>3</td><td>fur_dude_lowlid</td><td></td></tr><tr><td>4</td><td>fur_dude_lowteeth</td><td></td></tr><tr><td>5</td><td>fur_dude_rclaws</td><td></td></tr><tr><td>6</td><td>fur_dude_uplid</td><td></td></tr><tr><td>7</td><td>fur_dude_upteeth</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d616ee6c030b888d8c948934d464983eafb949b14e63a1179a2b24f419487d4d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/61a4ddd9afa2fa67c04e61dd8c11fd45ae493bb34b8041f2cd3f51fe4bfe2004.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1ac40be4af26e8a2157647df3063a6012618297025db688646eda62e3eac2df2.jpg)


01 In the Network View, press tab > Name from Groups and place the node between the File node and the split node. Change the Group Mask to *. This will turn all of the groups into name atributes. 

To see this, click on the Geometry Spreadsheet Tab and click on the Primitives buton at the top left. Scroll down to see that there is a name atribute and the group names are used as the values for all of the geometry. 

02 In the Network View, press tab > Pack and place the node down to the right of the split node. Wire the second output of the split node into the pack node and set its Display Flag. You can see the body parts in the Scene View. 

Turn the Path Atribute checkbox to Of then the Name Atribute checkbox to On and set Transfer Atributes to name. 

Using the arrow in the top right of the Network view, choose Split In the Geometry Spreadsheet, you can see the 8 packed primitives. These can now be captured to the skeleton as rigid geometry. 

03 <sub>Geometry</sub> <sub>and</sub> <sub>place</sub> <sub>the</sub> <sub>node</sub> <sub>down</sub> <sub>under</sub> <sub>the</sub> <sub>pack</sub> node. Wire the output of the pack node into the first input of the capturepackedgeo node. Next wire the output of the skeletonmirror node into the second input of the capturepackedgeo node then set the Display flag on the capturepackedgeo node. 

Nothing has happened yet - you need to associate the bones and the geometry you want to capture. 

04 In the Parameter pane, click on the plus sign next to Manual Capture. Click on the arrow next to Capture Geo and in the Scene view, select the lower teeth. One click is all you need because the lower teeth are one of your packed groups. Press Enter to accept. 

Now click on the arrow next to Joint. The geometry disappears and the skeleton is shown as lines and points. Select the lower_mouth joint and make sure your cursor is over the Scene View then press Enter to accept. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3bf35d8223b8daa672d1d8b51d1f0ec110a3adbc3fad755e08550ab0462cd01d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/81b590ac3c481bf6ba912557316d35e7400e751e1e7029888e6302ecd9967ec1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0ab314d9ba586d4649b39767cffd341b784bb99817f235f9c76b38ce1041e405.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c93c7fec3c848248b71a70817a2bad967f9d0a3e0548804f2dddc1610cee1908.jpg)


05 Click the plus sign and then the arrow next to Capture Geo and in the Scene view, shift select the fur_dude_ upteeth and fur_dude_gums . Press Enter to accept. Now click on the arrow next to Joint. Select the neck2 joint and press Enter. 

Repeat these steps two more times to associate the following: 

 fur_dude_rclaws to r_toe 

 fur_dude_lclaws to l_toe 

 fur_dude_eye to eyeball 

 fur_dude_uplid to upper_lid 

 fur_dude_lowlid to lower_lid 

06 Wire the output of the capturepackedgeo into the first input of the bonedeform node. Set the Display flag on the bonedeform node. 

Select the rigpose node and then select and rotate joints in the Scene view. You can see that the geometry is being captured to the joints without any deformation. 

The eye and eyelid joints overlap therefore when you click a litle menu pops up leting you choose - you may need to click a few times to get the joint you need. You can then use them to rotate the eye and the eyelids separately. 

07 In the Network View, press tab > Merge and place the node down in-between the capturepackedgeo and bonedeform. Wire the capturelayerpaint node into the merge node. On the merge node, press the blue up arrow next to capturelayerpaint to reorder the inputs. 

Now everything is deforming but the body and tongue are grey while the packed geometry has its colors. There is also an error on the merge node because the one side has color (Cd) as a primitive atribute and the other side has it as a point atribute. 

08 In the Network View, press tab > Unpack and place the node down between the capturepackedgeo and the merge nodes. Set Iterations to 2 and Transfer Atributes to * ^Cd. The * grabs all the capture atributes and the ^Cd make sure that you do not remove the original color atribute. Now both sides are using point colors and the rig looks correct. 

Now you can select the rigpose node and then select and rotate joints in the Scene view. You can see that all the captured geometry is now working together. 

Save your work. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6292d423fc0772362d0f6cd779a629aa0ac515cc5976df7e0c8fa9fc5ef8d9e4.jpg)


## FLATTENING THE NETWORK

The network that you have created to capture the geometry, paint weights and prepare the geometry for animation works well but can take a litle time to update when changes are made. 

To create a more eficient rig, you will flaten the network into a single file that has capture weights stored in the geometry. This file will deform eficiently when fed into a bone deform sop when accompanied by a skeleton with the same bones that were used to capture the geometry in the first place. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/04f7383fe2af7259520fbbd903f489b554696912f3135ac97ca05a3819a9aac7.jpg)


furdude_capt 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab0a17c24378d5885a5cb708a5f94694a90d4d9c8552add53f4cf3fa6f2a1f23.jpg)


furdude_skel 

# PART EIGHT Create Capture Rig Digital Asset

The captured geometry and the skeleton can now be wrapped up into a digital asset that can be used as the foundation for the animation rig. To start, you will export the geometry with its capture weights and the skeleton then embed these into the digital asset file. This will help make the capture rig more eficient when animating the character. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7a74e9a940b0fb526fa42203412919332bebf29a996714ce1b4d56ab0e2fbe05.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/58c7c814882c034b2d42a7459c53df7c9b9fe8de586df64d64d5a1c5e661f8b9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/edaa1bd92920ef8036d8cf0c8cccf4c4ee2619e98308e99d1c11914e79ff7524.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d83f2141230a661fd9fedece575020fc6393b92c6a53c8ef1b37036a49ed3a2c.jpg)


01 In the Network View, press tab > ROP Geometry Output and place the node down under the merge node. Wire the output of the merge node into the input of the rop_geometry node. In the Parameter pane, set Output File to: 

## $HIP/geo/furdude_capt.bgeo.sc

Click Save to Disk to save the geometry to your geo directory. This geometry looks like the geometry you imported at the beginning of the lesson but now it includes important data such as capture atributes that allow it to deform. 

02 In the Network View, press tab > ROP Geometry Output and place the node down next to the skeletonmirror node. Wire the output of the skeletonmirror node into the input of the rop_geometry node. In the Parameter pane, set Output File to: 

## $HIP/geo/furdude_skel.bgeo.sc

Click Save to Disk to save the geometry to your geo directory. This geometry represents your skeleton and can be used to build up an animation rig asset. 

## 03 Go back up to the Object level. Rename the object to fur_dude_capture. Turn of it’s Display flag.

Click on the File buton on the Create shelf. Click on $HIP then go into the geo directory and select the furdude_capt.bgeo.sc file. Press Enter to place it at the origin then rename the new object node to furdude_rig. Double click to dive into this object. Alt-drag on the File node to create a second one. Set its Geometry File to: $HIP/geo/furdude_skel.bgeo.sc 

Rename it furdude_skel.bgeo then set the Display Flag on the furdude_capt.bgeo node. 

## 04 Select the two File nodes then from the Assets menu select New Digital Asset from Selection. Set the following:

 Operator Name to fur_dude_capture_rig 

 Operator Label to Fur Dude Capture Rig 

 Save to Library to: $HIP/hda/fur_dude.hda 

Click Accept to create the HDA file. An Edit Operator Type Properties window pops up. Set Maximum Outputs to 3 and click Accept. Rename the subnet to fur_dude_capture_rig. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c4a520e11e730516ba8d544dc348e3ff64b9e4a85310b9b2768b4d04954babe3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c9198f8275b5f4692984467887aa5fa6ccb8c02df5538593934b100cff7842c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4e18fb5b4ab64537c006214d5442b1bae46d76778816b08ef16bbf46690a1c85.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6ae1ffc4b550efda43be3d0d6966d44712f4cc30f4f08233fc238dff5e632737.jpg)


05 Double click on this node to dive into the subnet. Press tab > Output and place an output node beneath the fur_ dude_geo_capt File node. Wire the File node into the output node. Rename it CaptureGeo. 

Alt-drag twice to create two new Output nodes. Name the second one RestSkeleton and set its Output Index to 1. Name the third one AnimSkeleton and set its Output Index to 2. Wire the fur_dude_skel. bgeo File node into both the second and third output nodes. 

Set the Display Flag on the CaptureGeo output node. 

06 From the Asset menu, select Edit Asset Properti es > Fur Dude Capture Rig. This opens up the Operator Type Properti es window. Click on the Extra Files tab. 

Click on the chooser but on next to Filename in the lower left and navigate to $HIP/geo/fur_dude_capt.bgeo.sc. Click Accept. Then click Add File. 

Repeat these steps for the fur_dude_skel.bgeo.sc fi le. Now you have placed these fi les inside the digital asset fi le which will make them easier to share with other people as a complete package. 

Click Accept to fi nish. 

07 On the fi rst fi le node, click on the Chooser icon next to Geometry File then click on opdef:/ in the Locati ons sidebar then double click on the sop directory then again on the fur_dude_capture_rig folder. Select the fur_dude_capt.bgeo.sc fi le then press Accept. This creates the following opdef expression: 

opdef:/Sop/fur_dude_capture_rig?furdude_capt.bgeo.sc Repeat these steps for the fur_dude_skel.bgeo.sc File node. 

From the Assets menu, select Lock Asset > Fur Dude Capture Rig. Save Changes to protect the contents of this asset. Later you can unlock it and update these fi les if needed. 

08 Go up one level where you will see the capture rig with three outputs. Press tab > Bone Deform and place this node underneath. Wire the three outputs of the fur_dude_capt_rig into the three inputs of the bonedeform node. Now add a rigpose node in the middle of the third chain. Set the Display Flag on the bonedeform node. 

Select the rigpose node and make sure the Handle tool is acti ve. You can again see all the skeleton joints. Pose the skeleton to test that the deformati ons are working in the same way as before. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b5573288e99abe68c21eb985f6d5f5e132672c40aaa4602c48f1e5b1b4e76523.jpg)


## HDA

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ce5d1b9a0d35dfb09d3fda6454aaa562468d8aae5510fcf334ba7336c706f537.jpg)


# PART NINE

# Create the Animation Rig Asset

You are now going to create a second digital asset that has the capture rig nested inside it. This new asset will be the one that can be animated to create the final motion of the character. This new asset will contain all of the rigging tools such as inverse kinematics and aim constraints that assist with animation. In order to test these controls as you add them, you will set up a test version of the rig that is locked and visible in a second Scene view pane. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/802d82a401ef8d4f3f45178078b6a9b085dd1c79c4ebd56da74807924a057167.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0a58f5b3e401bb4e334cf86945a5035abde3ca882e5b3c5e94371deb3ddacb52.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f35a6186c0b11aff5976c78ea0af0a9b377a7ee205f7e9b991729a7f07bdcfb2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5c597183d0387f494665b39f8f2d0f47767c458e33a50d70e157be2ee40ccd04.jpg)


01 <sup>Select</sup> <sup>the</sup> <sup>three</sup> <sup>nodes</sup> <sup>then</sup> <sup>from</sup> <sup>the</sup> <sup>Assets</sup> <sup>menu</sup> <sup>select</sup><sub>New</sub> <sub>Digital</sub> <sub>Asset</sub> <sub>from</sub> <sub>Selection.</sub> <sub>Set</sub> <sub>the</sub> <sub>following:</sub> New Digital Asset from Selection. Set the following: 

 Operator Name to fur_dude_anim_rig 

 Operator Label to Fur Dude Anim Rig 

For Save to Library, click on the browse buton then click on $HIP the double click into the HDA directory. Select the fur_dude.hda file then click Accept. It is now set to: $HIP/hda/fur_dude.hda 

Click Accept then Accept again in the Type Properties panel. This adds the new asset definition to the same HDA file. Rename the subnet to fur_dude_anim_rig. 

02 Go to the Object level. Alt drag on the furdude_rig node to create a new geometry node and name it test_rig. Press t and move the test rig over to the left. 

Double click to dive into it. Select the fur_dude_anim_rig node and from the Asset menu, select Lock Asset > Fur Dude Anim Rig. 

Go back up one level. You now have two versions of the rig - the test_rig is locked and shows you what it is like to interact with the completed asset. Right now you have nothing to interact with. You will fix that soon. 

Click in the Network editor, and press Ctrl 1 to set a quickmark. 

03 Navigate back to the furdude_rig object then into fur dude_anim_rig. Click in the Network editor, and press Ctrl 2 to set a quickmark. Now you will be able to quickly jump back and forth between these networks. 

Select rigpose then click on the Clear buton next to Transformations. Go to the Asset menu, select Save Asset > Fur Dude Anim Rig. From the Asset menu, choose Edit Asset Properties > Fur Dude Anim Rig. Click on the Node tab and set Default State to: <sub>kinefx__rigpose</sub>. Click Accept. 

## 04 In the Network view, press 1 to navigate back to the test_rig. In the Scene View on the left, expand the toolbar and click on the Handle tool.

You will now see joints displayed on the test rig. If you click on any of them, you will see that they can’t be changed because their parameters have not been promoted to the asset. This is the beginning of building an animatable interface for this character. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/55e9cddb862f13d155eec62d2da2de2437f0340afd8abd0ae9cf3a0260412f30.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/879fa0cbaaa7f1213ab384bfcfebfecf93baa0f6112c34e3f51d661c65c3f0fd.jpg)


## PART TEN Add More Control Joints

To provide more fl exibility with the control rig, you can add joints such as a root joint for the whole skeleton, heel joints for a reverse foot setup or a look-at point for you to target with your eyeball. These joints will have the same names as the ones in the original rest skeleton and that will ensure that they are used to drive the moti on on the character. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c18b13a50f2f11a6a82bcf0556e9dbd988cfb7f89591e02f95bb9c94abce76d4.jpg)


01 In the Network view, press 2 to navigate back to the fur_ dude_anim_rig and set its Display fl ag. Set the Template fl ag on the fur_dude_capture_rig node. 

Branch of a Delete Joints node from the third output of the fur_ dude_capture_rig node. Click on the arrow next to group then select fur dude’s right leg joints. Press Enter. 

Add a Skeleton node. Change to Create Mode. Turn on Grid snapping and add a point to the origin. Change back to Modify mode and rename the new joint to furdude_main. 

02 Go to right view. Go back to Create model and MMBclick to break the connecti on to the main joint. Click on the l_toe joint then add a new joint where the heel would be. Change back to Modify mode and rename the new joint to l_heel. Press p and with Child Compensate set to On, set the Rotate to 0, 0, 0. 

03 Pan to the area around the eye. Go back to Create mode and MMB-click to any connecti ons. Now add a new joint out in front of the eye. 

Change back to Modify mode and rename the new joint to eye_ target. Press p and make sure that Rotate is set to 0, 0, 0. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2b0b3a55afbb31a336b727e061a4a8344cae425ead6da6a62c51550c0d09d432.jpg)


## ADDING EXTRA JOINTS TO THE RIG

These extra joints were added to the stream of nodes on the far right while the middle rest skeleton will conti nue with the original joints. When fed into the bone deform, the extra “phantom” joints are ignored and only the original joints determine the fi nal output of the rig. 

If you were to feed these into the middle rest skeleton input on bone deform you would get an error because these extra joints would not have corresponding capture weights in the incoming geometry. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/db1ac11237cb54e74a8e2d6bb431ffefcf7272c1425310503bf50a32454ac8dd.jpg)


Skeleton with Extra Joints 

bonedeform 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6a0335893e638218b655e80fe03abbfc5cf7247998f8eaddd885515195e48634.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/928f66efa679d147f79152d5d11868cd9154b464f6766503980ffe49d122b8f4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/12a2367b7ad135186b5bfee6578961c80770e9b061340af1b30dbbeab77b71b4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/785994bd66882cbef82e1a5e11ea188fb8f97cd373d0b2491678ed646cf995a8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4d6d6699ceb4b41ede61609f6892b7f3a9660de87fa3a9efbbedcb9f3e9d3be7.jpg)


04 Add a Parent Joints node. Click the plus sign twice. Click on the arrow next to Joint1 and in the scene view click on the COG joint. Press Enter (with your cursor over the Scene View) to accept. Now use the arrow next to Parent1 and select the furdude_main joint. 

For the second entry, click on the arrow next to Joint2 and in the scene view click on the eye_target joint. Press Enter (with your cursor over the Scene View) to accept. Now use the arrow next to Parent2 and select the COG joint. 

05 Add a Skeleton Mirror node to the chain. This creates a mirror copy of all the joints. Go to the Parameter pane and click on the arrow next to Group. Select only the left leg joints, including the new l_heel joint,and press Enter. Now only the leg is being mirrored. 

Under naming, set Find Tokens to l_ and Replace Tokens with r_. Now you have the right leg joints properly named. 

06 Feed the skeleton mirror node into the rigpose node. Set the Display fl ag on the bonedeform node. The claws on the foot appear to have fl ipped. Go back to the skeleton joint, select the l_toe and press p to bring up the parameters. Set Rotate to 0, 0, -90. 

Select the four nodes you used to add joints and click on the Add Network box but on. Positi on the box and center the nodes. Click on the box’s ti tle and enter Add Joints. 

07 From the Assets menu, select Save Asset > Fur Dude Anim Rig. This saves the changes into the asset defi niti on which will update on the test_rig. You sti ll can’t do anything with the test_rig because there are no parameters promoted to the top level. 

You are now going to setup the main controls and promote parameters to start bringing the test_rig to life. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ebe9743be202c052b1641fbec505407de7a06a66722da3b4774161984d593cca.jpg)


## WHAT IS THE ROLE OF THE TEST RIG?

The rig you are working on is an unlocked asset which gives you the ability to work with all the joints inside the asset. But when the asset is published to an animator, they can only work with parameters that have been promoted to the top level of the character. 

The test_rig is a second locked version of the asset and unti l you start promoti ng parameters and building controls, you will not be able to manipulate it. That is what makes it a great tool for verifying that the asset is ready for animati on - if you can’t work with the test rig then the animator will not be able to pose the character. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4e1ffa4ad80b43998ff6f5e86f335026a6e7f4a6c0c398d0eb3d7eb3123d6220.jpg)


# PART ELEVEN The Main Controls

To add kinematics, you need to break the current hierarchy where the feet are under the COG. You can break of a few joints and reparent them to build the hierarchy you need. This reparenting happens of to the side then you will blend the results back into the original skeleton hierarchy which is important to make sure the bone deform functions properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/91429705bf65de0f541fece5cba64a67bcb87486cd7eb12bd8161238e7855539.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/482441028505aa43819fb95e95ef6d1ec0cf49295df41dd7ff33431512a89f01.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a7562f5698b4c713036e0ed4094668635f8d2a432ad196183f283c714826ad8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e5c2da64cab7d0c3c819791ddfff08e3abb26a4d20e65d5e78941b85432f84ea.jpg)


01 Branch of a Delete joints node from the skeletonmirror node. Click on the arrow beside Group and in the scene view select the furdude_main, the COG, the pelvis, the l_heel and r_ heel joints. Press Enter then set Operation to Delete Non-Selected. 

02 Add a Parent Joints node after the deletejoints node. Click on the + sign to add a joint listing. Click on the arrow next to Joint1 and in the scene view select the two heel joints. Press Enter. 

Click on the arrow next to Parent1 and in the scene view select the furdude_main joint. Press Enter. 

Now the heel joints are free from the COG and can be used to drive the IK on the legs down the line. But all of the joints are parented to the furdude_main joint except for the pelvis joint which is parented to the COG joint. 

03 Wire the parentjoints node into the rigpose node. Clear any existing joints from this node then set the Display flag on it. Now click on the furdude_main joint, the COG joint, the pelvis joint then the two heel joints. 

If you now set the Display flag on the bonedeform node everything is mixed up because most of the joints are now missing. This can be fixed with a skeleton blend. 

04 Add a Skeleton Blend node into the Network editor. Wire the skeletonmirror node into the left input and the rigpose into the right input. Then wire the skeletonblend node into the third input of the bonedeform node. 

In the skeletonblend Parameter pane, set the World Space checkbox to On and weight1 to 1. 

## CONTROL GEOMETRY

When you add a joint to a rigpose, it can be promoted to the top level of the asset to select and animate. The At ach Control Geometry node lets you assign geometry you build to dif erent parts of the rig to make it easier to select joints for manipulati on. You can create any shape you want for these controls. A good example where this will help is the eyeball and the two lid joints which overlap. Control Geometry will make it easier to select these when you set up that part of the rig. For now you will use it for the main controls. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b9b3c60d1f8568110b3d88ef75456631e8d79d514322e160c8c19676de32c1d8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/96d67323c2e64a22c6500970e07761fee09d69f42a31994141b0a15737480a17.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/828114ab8eed49d2cac25ec9847ab2d15640a5ade56ff58838e4d7f33afc6b20.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/11f7b96f93ab3b2a61d6245bb9824a490353529f2e72d5e3bf16a5e067ad802e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0f6e20e33ada7a7dffc4383ba16fe5eb4f9a019ab3c5f45810b72c83132335fc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/46ab9e18e704ce3aa1788e005c7b959c012e28385f4a4ee05fdde34192bf9b41.jpg)


05 From the Assets menu, select Save Asset > Fur Dude Anim Rig. This saves the current setup. In the Network view, Press 1 to navigate back to the test_rig where you can see that only the fi ve joints listed in the rigpose are visible. 

You cannot select and move them because the parameters haven’t been promoted yet. 

06 In the Network view, press 2 to navigate back to the fur_ dude_anim_rig. Add a Circle node to the network. Set Orientati on to XZ. Set Uniform Scale to 0.2. Set Divisions to 36 and Arc Type to Open. Add a Color node and set Color to yellow. 

Follow with a Merge Packed node and set Name 1 to circle_ctrl. 

Place an At ach Joint Geometry node between the parent node and the rigpose node. Wire the mergepacked node into the second input. Set the Display Flag on this node and press Enter in the scene view. Select all the visible joints then press G and use your scroll wheel to fi nd the circle_ctrl geometry. It gets assigned to all the joints. 

## 07 In the Operati on Control bar at the top, change the Mode to Tweak Shapes.

Select the COG and Pelvis joints then press G to bring up a transform handle. Press E to get the scale handle then click drag on the middle handle to scale in all three directi ons unti l these controls are a bit smaller (around 0.67 in the parameter pane). 

Select the two heel joints then press G to bring up a transform handle. Press E to get the scale handle then click drag on the middle handle to scale in all three directi ons unti l the heel controls are much smaller (around 0.3 in the parameter pane). 

08 Select the rigpose node then select the four joints using the control geometry. To make this work on the test rig you need to promote parameters. 

From the Assets menu, select Edit Asset Properti es > Fur Dude Anim Rig. Click on the Parameters tab. 

On the rigpose node go to furdude_main, RMB-click on Scale and choose Lock Parameter. Now drag the on Translate and move it over to the Parameter list under root. Set it’s Label to Main Translate. Repeat for the Rotate parameters and name them Main Rotate. Click Accept to fi nish and save the results to the asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1d47a7eb543db4c6efe7cb36005b1ad4f8f4e05b509abb1087c3cf90a9b60045.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2011197a91ce9fce340008218018066599fc5dc561492feee9ca973cabdaa7dd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8771c65fbaae35c4444ca365f05de33e4ad3d1e310e868af8958f9e22c185461.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aba6652b45208ebbe7dfbad32897401cb1090cba8367525f109ca5ee2b830e66.jpg)


09 In the Network view, press 1 to navigate back to the test_rig. The test rig now updates to show the new controls - as long as you have the Handle tool acti ve. Select the furdude_main joint using its control geometry and now a transform handle appears that you can use to move the rig around. Undo when you fi nish to put it back at the starti ng point.. 

10 In the Network view, press 2 to navigate back to the fur_ dude_anim_rig. From the Assets menu, select Edit Asset Properti es > Fur Dude Anim Rig. Drag the Translate and Rotate for the COG, l_heel and r_heel joints and the Rotate for the pelvis. In each case, lock the unused Scale or Translate (for the pelvis) parameters for each joint. 

Click Accept to fi nish and Save the results to the asset. 

11 <sup>In</sup> <sup>the</sup> <sup>Network</sup> <sup>view,</sup> <sup>press</sup> <sup>1</sup> <sup>to</sup> <sup>navigate</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>test_</sup><sub>rig</sub> <sub>which</sub> <sub>has</sub> <sub>been</sub> <sub>updated</sub> <sub>to</sub> <sub>show</sub> <sub>the</sub> <sub>new</sub> <sub>controls.</sub> rig which has been updated to show the new controls. Select the COG and heel joints using the control geometry and transform the parts around. 

Undo when you fi nish to put all the parts back to their original locati on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/031059f943cdc767d4e0c78b0f9be0b365808b130a59735a2f5c55e574cd81aa.jpg)


12 In the Network view, press 2 to navigate back to the fur_dude_anim_rig. Select the nodes you used to set up the main controls and click on the Add Network box but on. Positi on the box and center the nodes. Click on the box’s ti tle and enter Main Controls. 

From the Assets menu, select Save Asset > Fur Dude Anim Rig. This has no ef ect on the rig but keeps the asset up-to-date. You may want to Save your Scene fi le too. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1d0abc2c2ec117ebebafddfaaff6cd07bbd78c293c48e50c298677dc9435e4a5.jpg)


## ORGANIZING YOUR NETWORK

Lining up nodes and adding network boxes are extra steps that are worth the added ef ort. The more organized your network is, the easier it is for you to work with later or for others to read what your intenti ons are. 

You can also add comments to each node and display them in the network or you can use sti cky notes to explain larger blocks of nodes. Communicati on is always benefi cial when creati ng networks in a team seti ng. 

This part of the network organizes the main controls such as the root, the COG and the heel joints. 

# PART TWELVE Inverse Kinematics for the Legs

To animate a character, Inverse Kinematics allow you to set up the legs so that moving either the feet or the hips causes the knee to bend appropriately. You are again going to pull out some joints from the main skeleton and set them up using KineFX. You will again blend the results back into the original hierarchy. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5fd96c0db5ecf6ffc9b054cec42e18c8d00e3d8b43f58dd376fb4c51d7b1df19.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3c80166be719aab5e7da0af12809f9920ab240c835c8a126da04a7907a4ce929.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/005858a049056afe83e38f310a7aeb6b2b244e7bf797d11c04eacbc6b335faf7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/04f4baa8736a8365420f0b04893ba5fee26c1e15a145bb8b7f582e83ed3bdb4c.jpg)


01 Rename the skeletonblend node to skeletonblend_controls. You are going to use these nodes a lot and it will be helpful to be able to identify them. 

Branch of a Delete joints node from the skeletonblend_controls node and set its Display flag. Click on the arrow beside Group and in the scene view select the left and right hip, knee and ankle joints. Press Enter then set Operation to Delete Non-Selected. 

02 Branch a Parent Joints node and set its Display flag. Click the + sign to add a Joint and set Joint1 to *. Leave Parent1 left blank. Now all of the joints are unconnected. This will leave you free to use them independently. 

03 Place an IK Chains node into the Network editor. Feed the skeletonblend_controls into the first input and the parentjoints node into the second one. Set its Display Flag. 

In the Parameter pane, click on the + sign and in the folder click on the arrow next to Root name. Select the l_hip joint and press Enter (with your cursor over the Scene View). Set the Mid Name to l_knee and the Tip Name to l_ankle. You can use the arrow to select the joints or just type in the name. Set Match by Name to On and Blend to 1 then set Orient Tip to On. 

Click the + sign again and do the same for the right leg. 

04 Add a Rig Pose node in-between the parent node and the ikchains node. Click on the ankle joints and move them around to see the Inverse Kinematics at work. Because you used Match by Name the ankle joints are acting as the end efectors for the IK chain. 

You will see some flipping as you move the ankles. This is because the knee joints are being used as the twist efectors and they are not positioned very well - you need to move them in front of the legs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c7a11ed73270e14b20960391a30f6a3d2c76ebeb7ca0877a6a096f02835fcc7f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9e2394dfed12368a667af9f8cf1efb0b4f65135666db92a468e9a441dfded1bd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/400b2e1dcda03d9fb470b55204bffe0126a3a51bd7e1e6000c1ca27b03226ff8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/01997fa3c3087a08bc97b87a91253357de95b6a0928e818f68339deddfa5844f.jpg)


05 Add another Rig Pose node in-between the first rigpose node and the ikchains node. Press the Shift key and select both the knee joints and move them in front of the character. Now any flipping you had in your IK will have flipped back. 

Name the first rigpose node to rigpose_ankles and the second one to knee_ofset. 

06 You can now go back to the rig_ankles node and test out the ankle joints. They don’t flip now that you have the knees ofset. You can also go to the knee_ofset node and move the knees to act as a twist efector for the IK chain. 

07 Add Skeleton Blend node and wire the skeletonblend controls node into the first input and the ikchains into the second input. Then plug the output of the new Skeleton Blend node into the third input of the bone deform. 

Rename the node to skeletonblend_ik and set the World Space checkbox to On and weight1 to 1. 

08 You can now go back to the rigpose_ankles node and test out the ankle joints to see how it afects the captured surface. 

At this point, you are not going to save the digital asset to push these changes to the test rig. The rigpose_ankles node will not be how you control the ankles in the final rig. You are now going to build a reverse foot setup that will allow you to drive the whole foot setup and then the whole leg setup will be saved to the asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bd87767584a5a4613f4fb564d237d33e4ff4131c62bbbaf16b9c701146d2cbf6.jpg)


## FK/IK BLENDING

There are a couple of ways to blend IK and FK but you wont’ be using them in this lesson because you will only be using IK for the legs. To get blending to work, you would need to promote parameters for the leg joints to the asset using a rigpose then you could either use the Blend atribute on the IK Chains node or use a Skeleton Blend between the IK solution and the rotating joints in the rigpose. If Fur Dude had arms then it would make more sense to set this up. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c454bb5ca9ea61dbfb883d2340f3492b5b17cfc75d976f43f5273c0cb69c81a2.jpg)


# PART THIRTEEN Reverse Foot Setup

To control the feet, you will create a classic reverse foot setup where the heel becomes the root then the toe, ball and ankle are parented to that. This can be easily accomplished in KineFX and the results blended back into the original skeleton. In this case you will completely rebuild the right foot but since the joint names align everything works properly. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e1e052aa0c2cb1b95d25626cc56722f3eccd10fd5ed03be07b998f28784e1ef5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/02a3d5c48d32a63cb461ecbebee56be0c0f62b68a91e27770b8b452eb4b98e7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ecfca901dc8b5a95c573f60504d6eb63e416d5167ffe23a4066db3e251480b4a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fab8dab763dabb7e8e62739ba99349b4efabea793696e3f6b011f7f92c7e5c90.jpg)


## 01 Delete the rigpose_ankles node. You will control the ankles using a reverse foot setup.

Branch of a Delete joints node from the skeletonmirror node and set its Display flag. Click on the arrow beside Group and in the scene view select the l_ankle, l_ball, l_toe and l_heel joints. Press Enter then set Operation to Delete Non-Selected. 

Note: If you want redirect the connecting wire to go around the network box then you can Alt-click on it to add dots. 

02 Add a Parent Joints node and set its Display flag. Click the + sign to add a Joint and set Joint1 to *. Leave Parent1 left blank. 

Branch a second Parent Joints node and set its Display flag. In the Scene View click on the l_heel joint then the l_toe joint then the l_ball joint then the l_ankle joint. MMB-click to finish. In the Parameter pane they will be displayed in the following order: 

 Joint1 to @name=l_toe | Parent1 to @name=l_heel 

 Joint2 to @name=l_ball | Parent2 to @name=l_toe 

 Joint3 to @name=l_ankle | Parent3 to @name=l_ball 

03 Add a Skeleton Mirror node to the chain. Go to the Parameter pane and under naming, set Find Tokens to l_ and Replace Tokens with r_. This creates us the reverse foot for the right leg. 

Because all the joints in this hierarchy have the same names as the original skeleton it will transfer the information properly when this rig is posed. 

04 Now add a Skeleton Blend between the deletejoints and parentjoints that you set up earlier for the leg. Rename the node to skeletonblend_reversefoot and set the World Space checkbox to On and weight1 to 1. Click on the arrow next to Group and select the two ankle joints. Press Enter. 

Add a Rig Pose node after the skeletonmirror. Rename it rigpose_ foot. Feed it into the second input of the skeletonblend_reversefoot node. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e4eb05bf0d1c120487c7a185b8e2bd32b3a19f064ef9bfbb063370f04260da02.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f6e25580eb4dca3a02cd52b8ad885874f7ca4362af40323e3ed188ea842be1c2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/57ba8c36ba038af5d44700a7f2f1a888fb51df04b3a6b5129b7da71750358f0a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bbf070c8d52a2b0ce9002d2be39e017a869e0f700126197118bdd0db02d4bcf0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e47c081c883f520c466280de3a40a11c1e156fbe0cd3f7ed7f02f52e2bc0cdba.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/66a6241b4acefedc2b04e5e1b8e78b09c37c26c5d438c2364c70e4c30dad2b21.jpg)


## REVERSE FOOT SOP

There is a Reverse Foot SOP that you could use to control the feet and drive the leg kinemati cs. The Reverse Foot SOP has sliders for controlling the roll of the foot an individual controls for all the parts. But you are not using it in this lesson. 

Instead you will create a hand-built reverse foot soluti on to learn how joints can be manipulated to give you the control you need. 

05 Set the Display fl ag on the ikchains node. Now go to the rigpose_foot node and select the l_heel joint. Now when you move it you are moving the whole foot and the leg chain. Select the l_toe joint and rotate it. Again the reverse foot works and the IK chain is acti vated. 

When you fi nish press Clear to remove all the joints. You will add some of them back later. For the heel joints, you want to use the heel joints you set up earlier as part of the main controls. 

06 Now add a Skeleton Blend between the reverse foot skeletonmirror and rigpose node you were just using. Rename the node to skeletonblend_heels and set the World Space checkbox to On and weight1 to 1. Now feed the output of the skeletonblend_controls node into the second input. 

Click on the arrow next to Group and select the two heel joints. Press Enter. Now you can select the rigpose for the controls and move the left or right heel to control the whole setup. You can also grab the COG joint and if you move it up and down the IK chain works properly. 

07 Put an At ach Joint Geometry node between the skeletonblend_heels node and the rigpose_foot node. Wire the mergepacked node from the Main Controls network box into the second input. Set the Display Flag on this node and press Enter in the scene view. 

Select the toe and ball joints then press G and use your scroll wheel to fi nd the circle_ctrl geometry. In the Operati on Control bar at the top, change the Mode to Tweak Shapes. Select the toe and ball joints then press G. Press E to get the Scale handle then click drag on the middle handle to scale the controls to around 0.3. 

08 Set the Display fl ag on the bonedeform node. Pose the l_ball using the rigpose_foot node. You can see that rolling the ball causes the toe to point down instead of bending. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/94ffc59d69f49b451fbf70209115d0f24a01c9bd23fdd51ee24948c69a4bac3c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ac13eff136a1d92393c41b3295eb0a901b33c17e00f70dc0d0551b5feaacaaa8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/398e4b1c6f17a96904584c99257798455f7e8a54f5a01853a6ec47f37e3f0fdf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fbb3916fd8529105924275d4d35a022f4797ede60c105a1ebdc9497f11975547.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fa84890314e90a48a5c0938f37a3ed4c8872375cc0bd9c5a95aedd4f71cead63.jpg)


09 Now add a Skeleton Blend between the ikchains and skeletonblend_ik node you were just using. Rename the node to skeletonblend_toes and set the World Space checkbox to On and weight1 to 1. Now feed the output of the rigpose_foot node into the second input. Click on the arrow next to Group and select the toe and ball joints. Press Enter. 

Now the toe will point in the right directi on if you roll the ball joint. 

10 Select the rigpose_feet node. Make sure only the left and right ball and toe joints are listed on this node. For all of them, RMB-click > Lock Parameter on the Translate, Rotate and Scale parameters. Then go to the Rotate Y for each of them and RMB-click > Unlock Parameter. 

Now if you select any of these four joints you will only get a Rotate Y handle. 

11 <sup>Go</sup> <sup>back</sup> <sup>to</sup> <sup>the</sup> <sup>Main</sup> <sup>Controls</sup> <sup>Network</sup> <sup>box.</sup> <sup>Add</sup> <sup>a</sup> <sup>Box</sup><sub>node</sub> <sub>to</sub> <sub>the</sub> <sub>network.</sub> <sub>Set</sub> <sub>its</sub> <sub>Uniform</sub> <sub>Scale</sub> <sub>to</sub> <sub>0.02.</sub> node to the network. Set its Uniform Scale to 0.02. Follow this with a Color node and set it to a red color. Feed this node into the mergepacked node and set Name 2 to box_ctrl. 

Put an At ach Joint Geometry node between the parentjoints node and the knee_of set node. Wire the mergepacked node into the second input. Set Mode to Tweak Shapes then select the knee joints then press G and use your scroll wheel to fi nd the box geometry. 

12 Go to the knee_of set rigpose node. Make sure that only the two knee joints are listed. For both of them, RMBclick > Lock Parameter on the Rotate and Scale parameters. You will control these joints by moving them around. 

Set the Translate values to -0.15, 0, -0.05 for both knees. 

Add a Network Box around all of these nodes used to defi ne the spine and head joints and name it Leg Controls. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c65d490a18b197a6a4b166f7352a298cd112e193aa9167fc86065eed1cf56da9.jpg)


## THE ROLE OF RIG POSE

Up to this point the Rig Pose node has been used to test out the rig. When building an animati on control rig, this node is also used to set up the param eters that will be promoted to the top level and defi ne which joints will be visible when working with the digital asset. 

As you set up these nodes it is easy to accidentally add parameters that you don’t need which will add extra joints at the top level. You can also make the mistake of deleti ng parameters that you do need by clicking on the x but on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b019469e35eb48768998a92c11e046974f45bd3c40f4579d93d9cd769953ece3.jpg)


# PART FOURTEEN

# Promote the Leg and Spine Controls

To make all of the leg and spine controls available to the animator, the parameters need to be promoted to the top level of the asset. This is an important step that is always needed to give the animator the control they need. This also means that you can keep certain parameters hidden that you don’t want animators to work with. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/516e77113064a6400328ba09498595af2cb2f04ef9739d5873409fa88aae50ee.jpg)



ut Help Code Scripts Interactive Extra Files Save


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c19b85bd857d64c02d8890a5c7bf619f8bcfd20c6dda687c850aaada8b7e780b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1fb9326fbfeef5bbd148bd0709612c4902a177008c942ef2cda51740c1c1da39.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d570a921568445657915f8af0272bd629f8d9c9ec18e0e097f9a3be87591d23b.jpg)


## 01 <sup>From</sup> <sup>the</sup> <sup>Assets</sup> <sup>menu,</sup> <sup>select</sup> <sup>Edit</sup> <sup>Asset</sup> <sup>Properti</sup> <sup>es</sup> <sup>></sup> <sup>Fur</sup><sub>Dude</sub> <sub>Anim</sub> <sub>Rig.</sub> <sub>Click</sub> <sub>on</sub> <sub>the</sub> <sub>Parameters</sub> <sub>tab.</sub> Dude Anim Rig. Click on the Parameters tab.

Create four folders. Name them Head, Body, Legs and Main. Drag the COG parameters onto the Body folder and the Main parameters onto the Main folder. 

Put two folders inside the Legs folder and name the Left and Right. Add the Left Heel parameters into the Left folder and the Right Heel parameters into the Right Folder. 

02 From the knee_of set rig pose node, drag the l_knee translate values into the Left folder in the Leg folder. Rename it Left Knee Of set. Click on the Channel tab and set the default to -0.15, 0, -0.1. 

From the rigpose_foot node, drag the Rotate Y from the l_ball joint, name it Left Ball Rotate and set its Range to 0 to 30. Rotate Y from the l_toe joint, name it Left Toe Rotate and set its Range to 0 to 20. Drag a Separator in between the Knee Of set and Ball Rotate parameters. 

Repeat for the right knee and the right foot. 

## 03 Click Accept and now the new parameters and controls are saved into the asset. Go up one level to see the asset parameters laid out on the furdude_rig.

These parameters are for the unlocked rig that you are working on. Rather than test out these parameters, it is a bet er idea to play around with the test_rig. 

## 04 In the Network view, press 1 to navigate back to the test_ rig which has been updated to show the new controls.

Play with the test rig in the Scene view using the handles or using the parameters in the fl oati ng panel. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aaeea2a647dd943a678628c6a570394a713ecba1a3d499fd0b449e9c3a442c01.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/54a4d1fb88371b70e56a3151ac71f304c4ea72e7ea87d28580d6fbd57f72ea3f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0785439c69e8c64a5cb9e465fabd93bc95efc568fac4f592161ee62f5f1b526f.jpg)


## 05 Branch of a Delete joints node from the skeletonblend_ik node and set its Display fl ag. Rename the node deletejoints_spine.

Click on the arrow beside Group and in the scene view select the spine1, spine2, spine3, neck1, neck2 and jaw joints. Press Enter then set Operati on to Delete Non-Selected. 

06 Add a Rig Pose node and rename it rigpose_spine. Now add a Skeleton Blend between the skeletonblend_ik and bonedeform node. Rename the node to skeletonblend_spine and set the World Space checkbox to On and weight1 to 1. Now feed the output of the rigpose_spine node into the second input. 

Add a Network Box around all of these nodes used to defi ne the spine and head joints and name it Spine Controls. 

07 Set its Display Flag then in the Scene view press and hold the S key then select all the joints. This will add them to the rigpose list. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fdc2a0dbacc22b8ef0bd4e603241526df46913bee3042bf023ffd1a34f51db62.jpg)


Lock the Translate and Scale parameters for all of these joints. You will only be rotati ng them. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/feb8885dc85965e5ffff4cfbe4d9bd6bec65214b3a737cdba93f2f3b73c854ce.jpg)


## 08 From the Assets menu, select Edit Asset Properti es > Fur Dude Anim Rig. Click on the Parameters tab.

Drag the neck1, neck2 and jaw onto the Head folder and name them Neck 1 Rotate, Neck 2 Rotate and Jaw Rotate. spine1, spine2 and spine3 onto the Body folder and name them Spine 1, Spine 2 and Spine 3. Add a separator between the COG parameters and the spine parameters. 

Click Accept. This will save the new controls to the rig. You can now explore them using the test_rig. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4f6d79f26f0aaf828e802f9aa14444415380e32d22c83c0b2f6cb3eb10f77448.jpg)


## SPINE CONTROLS

For this rig, you set up the spine using joint rotati ons. This is known as Forward Kinemati cs and just like other parts of the rig, you pulled these joints out from the main skeleton then set them up in a Rig Pose to be promoted to the top level. 

You did not use control geometry for these parts because the joints are easy to select in the Scene view. You don’t need to have control geo for all the joints. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0e32efec2f124f0efc92c6e25f78584db8d4189024865dca4ca2b793b4a35bb7.jpg)


## PART FIFTEEN Eye Controls

The next step is to set up the eyelids with control geometry to make it easier to select these overlapping joints. You will also set up the eye target joint as a look at for the eyeball using a dif erent secti on of Houdini called VOPS. When these parts are rigged, you will again promote the appropriate parameters to the character’s asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5798c134fd8923a298d5d6308836083d0d11ea86545956b6ae6d3f339e37cd8b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ae53658ffffd0467746745d361cf36e8a541c7b6f22bcba8cd216e9c8fcd073f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/36e5ee3426f2176eefe4b94957d0c9a268bb7667915a8f2ba0f8f2ec8a51443a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f3cd82d5c237828196e6098772289e7415e7a46db6624228acb1a1553f6d8c83.jpg)


01 <sup>Branch</sup> <sup>of</sup> <sup>a</sup> <sup>Delete</sup> <sup>joints</sup> <sup>node</sup> <sup>from</sup> <sup>the</sup> <sup>skeletonblend</sup><sub>spine</sub> <sub>node,</sub> <sub>set</sub> <sub>its</sub> <sub>Display</sub> <sub>fl</sub> <sub>ag</sub> <sub>and</sub> <sub>name</sub> <sub>it</sub> <sub>deletejoints_</sub> spine node, set its Display flag and name it deletejoints_ eyelids. Click on the arrow beside Group and in the Rig Tree select upper_lid and lower_lid. Move your cursor over the Scene View and press Enter then set Operati on to Delete Non-Selected. 

Add a Rig Pose node and rename it rigpose_eyelids. Set its Display Flag then in the Scene view press and hold the S key then select all the joints. This will add them to the rigpose list. 

02 Now add a Skeleton Blend between the skeletonblend spine and bonedeform node. Rename the node to skeletonblend_eyelids and set the World Space checkbox to On and weight1 to 1. Now feed the output of the rigpose_eyelids node into the second input. 

03 Place an At ach Joint Geometry node between the deletejoints node and the rigpose node. Wire the mergepacked node into the second input. Set the Display Flag on this node and press Enter in the scene view. Make sure the Mode is set to Assign Shapes. Select all the two eyelid joints then press G and use your scroll wheel to fi nd the circle_ctrl geometry. 

## 04 In the Operati on Control bar at the top, change the Mode to Tweak Shapes.

Select the eyelid joints then press G to bring up a transform handle. Press E to get the scale handle then click drag on the middle handle to scale in all three directi ons unti l these controls are a bit smaller (around 0.5 in the parameter pane). 

Now select the upper_eyelid joint and move it up by 0.02 then select the lower_eyelid joint and move it down by 0.02. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/676901b654539eedbdde76cd726f614adbdaafab19ca458644a7db1fcb4421fa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9750e650d82b2794d23b39def2557af9cac9d4dbf0ee89207fd91cc804b6729c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/04b2e1c98696ccaafc2ed25a32e113ceff37ff9b5200e198d444c79fbff2cf5f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/fb4453caad97bf15f3df7f0ce403b47ece501bd02fa8a1167c04f259d7b73d70.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c585438130c9edc910bacecc7984f5364462cdf2f0369ada09512b293e205798.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/988a4160297e202c21e3d7f09d1a508dea62b643fc1c5e85fe2af15d67253988.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e3c6ac69440a287749f4195eedffcd8324b5c4268de4cc5593c6357daf778825.jpg)


## 05 From the Assets menu, select Edit Asset Properties > Fur Dude Anim Rig. Click on the Parameters tab.

Lock the Translate, Rotate and Scale parameters for all of these joints. Unlock the Rotate X parameters. From the rigpose_eyelids node, drag the Rotate X from the upper_lid to the Head folder. Set the Range from -10 to 30. Next, drag the Rotate X from the lower_ lid to the Head folder. Set the Range from -20 to 20. 

Add a Separator to divide the eye controls from the head controls. Click Accept. This will save the new controls to the rig. You can now explore them using the test_rig. 

06 Branch of a Delete joints node from the skeletonblend_ eyelids node, set its Display flag and name it deletejoints_ eyes. Click on the arrow beside Group and in the scene view select the eyeball and eye_target joints. Press Enter then set Operation to Delete Non-Selected. 

Add a Rig Pose node and rename it rigpose_eyetarget. Set its Display Flag then in the Scene view select the eye_target joint. This will add it to the rigpose list. You do not need the eyeball joint - it will be controlled by a look at constraint. Lock the Rotate, and Scale parameters for the eye_target joint. 

07 Add a Rig Atribute VOP node. Wire the deletejoints_eyes node into the first input and the rigpose_eyetarget into the second one. 

Now add a Skeleton Blend between the skeletonblend_eyelids and bonedeform node. Rename the node to skeletonblend_eyeball and set the World Space checkbox to On and weight1 to 1. Now feed the output of the rigatributevop node into the second input. Set the Display Flag on the bonedeform node. 

08 Double click on the rigatributevop node to dive into it. In the Scene view, click on the eyeball joint then drag the eyeball (deletejoints) version into the Network editor. This gives you a Get Point Transform node that focuses on the eyeball joint coming from the First Input. 

Click on the eye_target joint then drag the eyetarget (ripose_ eyetarget) version into the Network editor. This gives you a Get Point Transform node that focuses on the eye-target joint coming from the Second Input. 

09 Click on the eyeball joint then drag the eyeball version into the Network editor. This gives you a Set Point Transform node that focuses on the eyeball joint. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6efe5147a1fc655ef7b9d4fa6c4e9862c4091aca3547f78a42beb546f10b3dd4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9a2b3ff4d34b95751bd7398a9f5604a71a6f13689c3ab87aaebc4a3aeec8f4c3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6a8b09d8bb77c1455e30c4c21817099637d698b356506f27582496bc0dcd97f4.jpg)


10 Now press tab > Look At (KineFX) and place the node in the middle. Wire the xform output on the eyeball getpoint ransform node into the from input on the lookat node. Wire the xform output on the eye_target getpoint ransform node into the to input on the lookat node. Wire the outxform output on the lookat node into the xform input on the eyeball_set node. 

The eyeball geometry fl ips. Select the lookat node and set the Look At Axis to Z to match the orientati on you set on the rig when it was fi rst set up. 

11 deletejoints_eyes node and the rigpose_eyetarget node. Wire the mergepacked node from earlier in the network into the second input. Set the Display fl ag on this node and go to the Handle tool. Make sure the Mode is set to Assign Shapes. Select the eye_target joint in the 3D view then press G and use your scroll wheel to select the square_ctrl. 

Set the Display Flag on the bonedeform node. Click on rigpose_ target. Select and move the eye_target joint. This orients the eyeball. Undo to set it back to it’s original positi on. 

## 12 Add a Network Box around all of the nodes used to defi ne the eyes and name it Eye Controls.

From the Assets menu, select Edit Asset Properti es > Fur Dude Anim Rig. Click on the Parameters tab. 

From the rigpose_eyetarget node, drag the Translate parameters from the eye_target to the Head folder in the eye secti on. Name them Eye Target Positi on. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4d7dc7d583641615dd95323eeab8742fc078ff6a4de4e83a437a7cd1ce1ba90e.jpg)


Click Accept. This will save the new controls to the rig. 

## 13 You can now explore them using the test_rig. Ve. now have all ef the parts finiched for this

You now have all of the parts fi nished for this control rig. It is now ready for you to animate a walk cycle. To do this you will create a second copy of the test rig and animate using that network. 

This digital asset can create multi ple instances in multi ple scene fi les and if you later need to come back and make a change, all of the assets will update. This is the pipeline advantage of working with a digital asset rig. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3ada3ce15b4c05c1d245573ccde0d699ce2553eeae67786c0c10749ce6036b8e.jpg)


## RIGGING IN VOPS

The Rig At ribute VOP of ers a range of dif erent soluti ons beyond what you have seen in this lesson. IK chains can be built using this approach and the IK chain SOP you used earlier has one of these inside it. 

You can also use VOPS to set up a curve solver, realisti c shoulder, reverse foot and more. The ability to drag joints from the Scene view to the VOP network is a unique workfl ow that helps speed up workfl ow. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e49f70bcaaef62c9ffc1c72dd0c9d006edc8f644eb7f6dc11809334479d73888.jpg)


## PART SIXTEEN Animate the Rig

It is ti me to keyframe a walk cycle for the fur dude character. This will involve new tools such as the Channel List to pin down channels for blocking out the moti on. The results will be a quick and dirty walk cycle designed to see fur dude in acti on. The goal is to map out a basic keyframe workfl ow to learn a bit about how to animate KineFX rigs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c411735c7c10a66af74fd648f1f7d361201e5350b1b256f4bf4fe134fcc06903.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e24b72c1b5b2e5f287c5792a7a610a3c634c899db05c4ce21d3276b21c4fe16c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bf98265b89e825a32b2b27b2bb18c5ef8a5b10fdc3f54a264bede1a2c04356c0.jpg)


01 <sup>Go</sup> <sup>to</sup> <sup>the</sup> <sup>object</sup> <sup>level.</sup> <sup>Press</sup> <sup>tab</sup> <sup>></sup> <sup>Geometry</sup> <sup>and</sup> <sup>place</sup><sub>down</sub> <sub>the</sub> <sub>node.</sub> <sub>Rename</sub> <sub>it</sub> <sub>walkcycle.</sub> <sub>Turn</sub> <sub>of</sub> <sub>the</sub> <sub>Displ</sub> down the node. Rename it walkcycle. Turn off the Display Flags on all of the objects. 

Double-click to dive into walkcycle and in the Network view, press tab > Fur Dude Anim Rig. Press Enter to place it at the origin. This is a new locked version of the fur dude rig that you will animate from scratch. 

This puts another version of the character asset into the scene. You can have multi ple versions in this scene fi le or in other scene fi les and they will all reference the same asset defi niti on on disk. 

02 From the Desktop menu (the one that currently says Build), choose Animate. This gives you panes that are designed to work with a keyframe workfl ow. You may need to go back into the walkcycle object. 

The Channel List on the left will play a key role in blocking out the animati on of the character. The Animati on Editor lets you display and edit animati on curves. In this lesson you will block out the moti on and won’t be doing any curve editi ng. 

03 In the Network view, select the fur_dude_anim_rig inside the walkcycle object. Go to the Parameter pane and click on the box icon in the top right. Choose Parameters and Channels > Create Nested Channel Groups. Click Close in the pop up window. The parameters from your asset are now listed and organized based on their folders. 

Click on the Pin icon next to the fur_dude_anim_rig channel group to pin these channels. Make sure your ti meline is set to frame 1 then press k to keyframe all the channels. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e42c9acbf7487d1786a7fa7774bca4664630d2c1557f2ec1cbe38604e001a028.jpg)


## HOW CHANNELS WORK

When you select a joint, the channels load into the channel list. Press k to keyframe them. If you want to keep them loaded in the list for blocking purposes, you can pin them or add them to a channel groups to pin them all together. You can build the Channel groups directly from the asset. They are organized based on how you built the UI for your character. You can also build your own groups to pin down specifi c channels. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f2295517f65ab154433621ef8f860b4b2c34150ab13f8097d5b754ef2b51c44a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1270ac0b76183ee2368a1a8dda269cc0787185682aa1a8bd648881bed846980f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/69c894ffacda340fcdae46f40fd1e7b470bfa9da9ca554d2a2d826fd458efb94.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0f1bdcc0b9cfd5c709ea10ae107323dbf56a304ad6b000e564bf845a9fb2bdf2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/988ea62450df7e15fa427c6385e90539bfda3b8d2519804482260f5326e1c5ad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1240dd35eca636fc8a79608673e7a55b755302e6f6327b66b20c41f658d184f4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3a7bae6cc5c969d9732384397548f2e6cd36b2a5980c93e28000505329f9050b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b6ce046d4518e25e85daa7bca61fb1f539d69e8a734e168b22fa69cc1e74ec07.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/10b22ddd58f38e187b5c7a24702e2a37be13eeecebfe5a5e960dd2e85f028489.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/95b9acedd9a37b76a882a1504ea858b0686d5417ec0ba5c70dd1751dca137d31.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2dd03cc2de504f7c574e422a97286df541cc5794a85149913958002085fc8c37.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7401781db6989b7287f1ad9c9273b95ea7f9dd0b6183d7a12971d5d7240ec149.jpg)


04 Set the Timeline to start at 10 and end at 50. Go to frame 10. With all the channels pinned, press k to set another keyframe. You want to keyframe first then pose. Any posing will update the value for that keyed frame. 

You want to create a pose where the left heel moves forward and rotates up. The COG will go down a bit and the right ball rolls forward. 

## 05

## Go to frame 15 and press k.

Roll the left heel flat but don’t move it. Move the COG to align with the left foot. Move the right heel up in line with the other foot. Rotate the right ball back to flaten the foot. 

Rotate the COG a bit towards the left foot. You can also add some rotation to the three spine joints to emphasize this tilt. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6c124dc4bc15222621fd2d7a3fb62e4dabd67b76a98a43927549b9f6f7349d9c.jpg)


## Go to frame 20 and press k.

Now you want to create a pose where the right heel moves forward and rotates up. The COG will go down a bit and the left ball rolls forward. This is the opposite of the pose at frame 10. Rotate the COG and spine joints back to center them. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/34f0ff55872d9698c08b8b940559319b03e0bef9b668ea5abb483bf9150c6684.jpg)


## Go to frame 25 and press k.

Roll the right heel flat but don’t move it. Move the COG to align with the right foot. Move the left heel up in line with the other foot. Rotate the left ball back to flaten the foot. 

Rotate the COG a bit towards the right foot. You can also add some rotation to the three spine joints to emphasize this tilt. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d2e41a1cd5bb672e99af2d10df2985453c64adb7b79fce6cf704e0e672da41fc.jpg)


## Go to frame 30 and press k.

You want to create a pose where the left heel moves forward and rotates up. The COG will go down a bit and the right ball rolls forward. 

Rotate the COG and spine joints back to center them. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/b471ea1b4af8346f5412471a7f134baeadf50c6634c78075cb6638165f904270.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2cdcf9487534e1b6210ae473fcc6c8359b2bb2fc505aced5e5aadba47a77dbe4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6c94f24b4e6eb9ea9192c094bf39e853428128e4a47de684a731439eee85cec3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e07ab40ec3fd2793585c0a7fc139849fa231cec1ba4e4cd9093cda990ed9a7bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/474566cc3aab9e5dcdd6924305e65bb466b0cee61b040e4c2aac6121b809f3df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/74fe607c8cd874c0009cc68f0e0b4e62dd7404ee96ddc823e46a5c8152c30702.jpg)


## 09 <sup>Conti</sup> <sup>nue</sup> <sup>this</sup> <sup>pat</sup> <sup>ern</sup> <sup>up</sup> <sup>unti</sup> <sup>l</sup> <sup>frame</sup> <sup>50.</sup> <sup>You</sup> <sup>can</sup> <sup>repeat</sup> the same poses to keep the walk cycle moving forward.

At this point you can go back and tweak any pose to refi ne the moti on. You can also explore creati ng some overlapping acti on using extra keyframes. You can animate some eye movement and maybe the eyelids blinking. You can also go beyond 50 frames if you would like a longer animati on. 

10 <sup>Connect</sup> <sup>the</sup> <sup>output</sup> <sup>of</sup> <sup>the</sup> <sup>fur_dude_anim_rig</sup> <sup>node</sup> <sup>into</sup> <sup>a</sup><sub>ROP</sub> <sub>Geometry</sub> <sub>node.</sub> <sub>This</sub> <sub>will</sub> <sub>allow</sub> <sub>you</sub> <sub>to</sub> <sub>export</sub> <sub>out</sub> <sub>a</sub> ROP Geometry node. This will allow you to export out a cache of the fur dude geometry. Set the Output File to 

$HIP/geo/furdude_walk.$F.bgeo.sc 

Next Set Valid Frame Range to Render Frame Range. RMB-click on the Start/End/Inc parameter and choose Delete Channels. Set the Start to 1 and the End to 50. 

Click the Save to Disk but on to store the cache to disk. You will use this to add fur. 

11 Branch an At ribute Delete node of of the fur_dude_ anim_rig node. Under Primiti ve At ributes choose Cd. This removes the color from all the body parts. 

12 <sup>Connect</sup> <sup>the</sup> <sup>output</sup> <sup>of</sup> <sup>the</sup> <sup>at</sup> <sup>ributedelete</sup> <sup>node</sup> <sup>into</sup> <sup>a</sup> USD Export node. This will allow you to export out a the fur dude geometry to the USD format. Set the Output File to 

$HIP/usd/furdude_walk.usd 

Next Set Valid Frame Range to Render Frame Range. RMB-click on the Start/End/Inc parameter and choose Delete Channels. Set the Start to 1 and the End to 50. 

Click the Save to Disk but on to store the cache out the USD fi le. You will use this later in the rendering process. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/efdea60590bb38853453045992b409ac49bdcb14c8173adf92b6242f60d7f3c3.jpg)


## CACHING OUT ANIMATION

Because of Houdini’s procedural nature it is not really necessary to cache out the animati on. You could reference it from this network to another network for grooming or to Solaris for conversion to USD. The advantage of caching is that you lock down your animati on and work with a fl at ened fi le on disk. This is a very producti on-friendly approach In Solaris a USD fi le referenced from disk is also more efi cient. Since Houdini references fi les from disk, you are always free to change your animati on and output the new sequence and it will be picked up automati cally. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d731e2af16cb3158fc556b1ca9196ab298cade28ad938eed895a906b92cf1d25.jpg)


# PART SEVENTEEN Add & Groom the Fur

Fur dude gets his name for a reason and you are going to work with a variety of grooming tools to add and shape the hair. Using a desktop designed for grooming, you will add frizz, clumping and hair dynamics which will simulate as fur dude walks. The end result will be ready to be exported for rendering. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/43b7fe7b1c9b4437d127572958d2a404622489c7def390456e70a802d9aa8c43.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4db2014c30df4c55cce4ab5bfa3bae2a3c3f7eba5010551255235d7abab9b3a8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/65d123f948c83e7826621671e3786c4f3267120fb7995979e1b3d1fbce56cdb5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/50a785e6e780a242dfce5dc40b584c6b6c763529784a0efc37f75f13bb7ee993.jpg)


01 <sup>Got</sup> <sup>to</sup> <sup>the</sup> <sup>Grooming</sup> <sup>desktop.</sup> <sup>Put</sup> <sup>the</sup> <sup>four</sup> <sup>existing</sup><sub>objects</sub> <sub>into</sub> <sub>a</sub> <sub>network</sub> <sub>box</sub> <sub>and</sub> <sub>call</sub> <sub>it</sub> <sub>box</sub> <sub>Rig</sub> <sub>&</sub> <sub>Anim</sub> objects into a network box and call it box Rig & Animate. 

In the Network editor, press tab > File. Place the node then double click to go into it. Click on the browse buton next to Geometry File and go to $HIP/geo. Select furdude_walk.$F.bgeo.sc. Press Accept. 

Add a Blast node, set it’s Group to fur_dude_body and turn On the Delete Non-Selected checkbox to focus on the body. Set the Display Flag then go to the Object level and rename this fd_anim. 

Alt drag to create a copy it and name it fd_rest. Dive in and change Geometry File to $HIP/geo/ furdude_walk.1.bgeo.sc. 

02 Now move the time slide forward a bit. One object has a static version of fur dude and the other is animated. Click the Add Fur buton . Select the fd_rest object and press Enter. 

Now select the fd_anim object and press Enter. Turn of the Display Flag on fd_rest_anim, fd_rest_deform and fd_rest_hairgen. 

Turn on the Display flag for fd_rest and fd_rest_groom. 

03 Select the fd_rest_groom node and from the Hair Tools shelf, click on Set Guide Length. Turn the Randomize Buton to On. Set Min Length to 0.03 and from the menu on the right select Texture. 

Use the file browser buton to select $HIP then go into the tex directory and choose fur_length.jpg. 

Now set Max Length to 0.15 and again choose Texture. You can use the arrow on the right to select the fur_length.jpg image. 

You now have the eye, lip and the botom of the feet masked out and the rest of the fur with random lengths. 

04 From the Hair Tools shelf, click on Bend Guides. Set Angle to 45 to add some bending to the guides. 

Next, click on the Frizz Guides tool. Set the following: 

 Frequency to 15 

 Amplitude to 0.005 

 Random Amplitude to 0.02 

This keeps the hairs from looking too straight when rendered. You can add more frizz if you want a more tangled look. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/32d0d93a590f7d16f639e5e85dbc8a041b0fc02f750d86ba7e2a851a92959317.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2a92b5fbe5256a5ee11d68906270324685271bbc0782110f340229c36f561922.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c7ee16b9d8f388b2dae921537bf558c3ccf4afff410283b9795fb624f6543217.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6339d416fdc6fd2db24c4aaaea45f4610be0e4f07bf55b83338f4b5396b71617.jpg)


## 05 From the Hair Tools shelf, click on Clump Guides. Set Clump Size to 0.02 to Tightness to 0.5.

Next change the Clump Profi le so that it stays high for a bit longer then tapers of near the end. 

Now go to the Object level and turn of the display on the fd_rest and the fd_rest_groom and turn on the display on the fd_anim and fd_rest_sim and fd_rest_hairgen. 

Select the fd_rest_groom node and set Density to 20000. 

06 Select the fd_rest deform node and from the Hair Tools shelf, click on Simulate Guides. On the fd_rest_sim node, go to the Vellum Constraints tab and under Bend set Sti f ness to 5. 

Alt-drag on the fd_anim node to make a copy and rename it fd_collision. Dive into this node and on the blast node set Delete Non Selected to Of . Add the tongue, upper teeth and gums to the Group selecti on then add a Null node and name it COLLISION_OUT. 

At the object level, select fd_rest_sim then under Vellum Collisions, set External Collisons to On then set Collider SOP to ../fd_collision/ COLLISION_OUT. 

07 Click on the Caching tab and set Set Valid Frame Range to Save Frame Range. RMB-click on the Start/End/Inc parameter and choose Delete Channels. Set the Start to 1 and the End to 50. Click Save to Disk to run the simulati on. 

Now set the Load from Disk checkbox to On. The cache will now be used to defi ne the fur instead of the hair calculati ng for each frame. 

08 Select the fd_rest_hairgen node. Under Distributi on, set Density to 1000000. Scroll down to Guide Interpolati on and set Clump Crossover to 0.25 to create a it of overlap between clumps. This gives you an idea of what furdude looks like with a full head of hair. 

These are not the hairs that you will render in Houdini’s lighti ng context called Solaris. You will instead bring in the guide hairs and render using a hair procedural at render ti me. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7434e8f015b1051429f766145ab13ab490f6cb09adab45d78ca4bfb88923f417.jpg)


## HAIR BRUSHES

The grooming desktop also has hair brush tools that let you work interacti vely on the character’s surface. You can lengthen, smooth, cut and extend hair. These tools were not needed to set up fur dude’s grooming but later you may want to explore them to further style the fi nal look. 

Hair Brushes 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/515e6550a864cf43a4271416cda7781b307600c0ede5d93bcd2f7405b076426c.jpg)


# PART EIGHTEEN Set up an Render the Shot

To render the shot, you will reference the USD files into the Solaris Stage then add a backdrop. Solaris is a Houdini context that uses LOP nodes to set up a USD Scene Graph. Next, you will import the fur then add and position a camera and a light. The Karma renderer will then be invoked to create a preview render of the shot then render out the animated sequence. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/06b1c833a939af875874395bea5bed37b6cb3034f8c89dcdb44c87f1ce5fd40c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1c0da6b4d4efe56902e03df2d9255c27f8e98d8cafea216215a1495e82c2317b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/875cf3e3dada928231a9981563f9373a1a143ab49107ed41d33c59dd75be64e1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cb3d197cf731d2879faeaac502756c6c702fb497d1284cdef504e3a8e7ad506a.jpg)


01 <sup>Change</sup> <sup>the</sup> <sup>desktop</sup> <sup>to</sup> <sup>Solaris.</sup> <sup>Choose</sup> <sup>Stage</sup> <sup>from</sup> <sup>the</sup><sub>path</sub> <sub>bar.</sub> <sub>In</sub> <sub>the</sub> <sub>Network</sub> <sub>View</sub> <sub>press</sub> tab > Reference then click to add a Reference node. 

Next to Reference File, click on the File Patern and find the furdude_walk.usd file. Rename the node to furdude. Set the Primitive Path to /char/`@sourcename` - this will use the node name and place it into a group called char. In the Scene Graph Tree expand char then furdude to see all of the named primitives. 

In the Scene View, use your view tools such as spacebar-h for homing the view to get a beter look at the walk cycle. 

02 Press tab > Material Library. Wire it into the output of the reference node then set its Display Flag. 

Go to the Material Palete pane. Click on the arrow next to /stage/ materiallibrary to open up this area. Scroll through the material gallery on the left of the palete and drag a Principled Shader materials into the materiallibrary working area. 

Go to the Network view and Alt-drag this material to create four more. Rename the five materials body_mat, eyeball_mat, eyelid_mat, teeth_mat, and tongue_mat. You can also see the materials in the Scene Graph Tree. 

03 For furdude_body_mat, under the Surface tab, set Base Color to 1, 1, 1. Click on the Textures tab and under Base Color click on Use Texture then use the buton next to Texture to call up the file window. Click on $HIP in the side list then click on the tex folder to open it and then click once on skin_color.jpg to select it. Click Accept to assign the texture to the material. Next set the Roughness to 0.5 and Reflectivity to 0. 

Assign eye_color.jpg and eye_lid.jpg to their materials using the same method. Set tongue_mat to a redish pink and teeth_mat to a yellowish-white. 

04 Go to the Stage level. After the Material Library node, add an Assign Materials node. From the Scene Graph, drag the fur_dude_body to the Primitives field then click on the arrow next to Material Path and choose body_mat. Now click the Plus Sign next to add four new entries. Assign them as follows: 

 fur_dude_eye > eyeball_mat 

 fur_dude_lowid/uplid > eyelid_mat 

 fur_dude_lowteeth/upteeth/claws > teeth_mat 

 fur_dude_tongue/gums > tongue_mat 

When working in Solaris, the geometry and materials you add using LOP nodes are added into the Scene Graph and converted to USD. When you add a light and a camera, they will also become part of the USD Scene Graph. 

It is not necessary to completely understand USD to light and render in Houdini as an artist but once you start thinking about the pipeline of your project, USD will become a useful tool in managing your shots. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/082d424807a7f106b68f983e740a936a3befc17bd6c13c56980727c7de87f0a8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2e70909ad0d143ed19ec842385baf498bc9010cd5a11756640ca4d095ed3a8c7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/64107202bd778f8d0b15e8fd8852c8ca2234640898e6f47c333e4c02498d5d0e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/666ed455c009a0f7309f4af6c741dede4af8df0ef8f6d4d8c2fe4db268d67c3a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5a391d733446eee18b3c7e58e51780754147b08748011f542fb836d457618e4b.jpg)


05 In the Network view, press tab and type out SOP Import. Click to place the node. Rename it hair. Set Import Path Prefix to /char/$OS. Click on the node icon net to SOP Path and navigate to the fd_rest_hairgen node. 

Add a Merge node in-between the furdude and materiallibrary nodes. Wire the hair node into it. 

06 Go back to the Material Palete pane. Open up / stage/materiallibrary. Drag the Hair material into the materiallibrary working area. 

Leave the Root Color and Tip Color set to the defaults for the hair. Next click on the Secondary Reflection tab and set Root Color to dark grey and Tip Color to medium grey. 

Go back to the Assign Material node, From the Scene Graph, click on the arrow next to Primitives and select the fur curves. Next, click on the arrow next to Material Path and choose hair. 

07 In the Network view, press tab and type out Grid. Click to place the node. Rename it backdrop and wire it into merge. Set Import Path Prefix to /geo/$OS. Double-click on the backdrop node to dive down to the geometry level. 

Select the Grid node and set the Size to 50, 50 and Rows and Columns to 10. RMB-click on the grid node’s output and type Bend. Place the bend node and set its Display Flag then set: Bend to 75, Capture Origin to 0, 0, -10, Capture Direction to 0, 0, -1, and Capture Length to 10. RMB-click on the bend node’s output and type Subdivide. Set its Display Flag then set Depth to 2. 

08 Go to object level and set Rotate Y to -45 degrees. Add material and assign it. You can leave the default grey or add your own base color. 

Set time range from 10-50. You will be rendering this sequence after the hair has had 10 frames to setle down. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3c593966ac93955d4cf02a439efa10bacb649aa0445c63236b8dc2d0f7f3b707.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2c7279d8e7bb50e31dc3ccd9e32de4abe974c04acc844fb4f03baa8371ace1a0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a8b3a3909e5cbc480959a91e0417e5605905fa04126efe5cd54fbffcb8270612.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f05f3f7aa4d8cebc820a42e28acfb32ab91a19223a6b5e7d92344cae80a80a21.jpg)


09 Use your view tools to look at furdude from the front. From the LOP Lights and Camera shelf, Ctrl-click on the Camera tool. This adds a camera node into the network and you are now looking through the camera in the Scene View. 

Press the Lock Camera/Light to View buton so that view changes can be used to reposition the camera. Now Tumble, Pan and Dolly in the Scene View to reposition the camera so furdude starts on the left and the moves to the right. Scrub the timeline to make sure the camera works for the whole sequence. 

10 Now turn Of the Lock Camera/Light to View buton then tumble around until you are looking down on Fur Dude. From the LOP Lights and Camera shelf, Ctrl-click on the Area Light tool. This adds an arealight node to the end of the chain. Select the arealight node and from the Base Properties tab, set the Intensity to 2. 

## 11 <sup>From</sup> <sup>the</sup> <sup>Persp</sup> <sup>menu,</sup> <sup>choose</sup> <sup>Karma</sup> <sup>to</sup> <sup>render</sup> <sup>with</sup><sub>Karma</sub> <sub>in</sub> <sub>the</sub> <sub>Scene</sub> <sub>View.</sub> <sub>You</sub> <sub>can</sub> <sub>move</sub> <sub>to</sub> <sub>diferen</sub> Karma in the Scene View. You can move to different frames in the timeline and the Scene View will update quickly.

Karma is designed to work with USD which is why everything in the LOP context is converted to the USD scene graph. You can only use the Karma renderer from this part of Houdini. 

To get a cleaner image when you render, you can turn on the Denoiser if you have an Nvidia graphics card. Be sure to install the Denoiser from the Render menu and then turn it on in the Display Options bar. 

12 Press tab > Karma to add a Karma Render Setings and USD Render ROP node. Wire them into the end of the chain. Select karmarendersetings and on the Image Output > Filters tab set Denoiser to nvidia Optix Denoiser. Set the Output Picture to $HIP/render/walk/furdude_walk_$F2.exr. The $F in the name is needed to add frame numbers to the renderings and the 2 is the padding of the frame number. 

Select usdrender_rop. RMB-click on the Start/End/Inc parameters and choose Delete Channels. Set the Start to 10 and the End to 50 Select the usdrender_rop node. Click on Render to Disk. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8908d158457727c431bb5c50e898f2826abd8e94a74df362b603d4769f8b2e7c.jpg)


## KARMA RENDERER

persp1 

Set View 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5b376c3394a19a740583d30539901f3b8f0824f159c4e45080e0bb1a37832151.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/553f6d0628c3229a65dcb9037103e0f50dcebcbfea2990f32e3a295470641cef.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ae9006a659b3a020370c3754c66679a836d1b688f481b0f22a02be9cdebdd7aa.jpg)


## CONCLUSION

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/97c953bf848cb0d1a668a947d4ccb99c6458720232583c233fe85eecca9116a8.jpg)


You have now rigged, animated and rendered the Fur Dude character using the KineFX tools in Houdini. Along the way you have touched on various important steps including the creati on of a capture rig then the layering of a animati on control rig on top of that. You have packed up the character into a Houdini Digital Asset and then keyframed a traditi onal walk cycle. 

15 You can then go back to the Solaris network and maybe change the colors on the fur and re-render. 

13 When you fi nish, choose Render > Mplay > Load Disk Files and open up the rendered images to review the fi nal sequence. 

For the fi nal render you may want to up the resoluti on to 1920x1080 and change some of the quality seti ngs. For instance you can set Pixel Samples to 128 and Light Sampling Quality to 16. 

You then added fur with various grooming tools then rendered using Karma. This gives you a complete workfl ow for creati ng a shot using this character. You can then go back and refi ne any aspect of the procedure to create multi ple iterati ons as you seek out the perfect result. 

14 If you want to tweak the hair and fur seti ngs, you can pin the Scene View to the LOP network then go back to the object level and from the Simulate Guides node, set the Load from Disk checkbox to Of . This will allow any changes to fl ow through to the fi nal rendering. 

Later you can branch of another Karma node to up the resoluti on and render seti ngs for your fi nal rendering. It is always good to complete test renderings at a lower resoluti on fi rst to make sure that everything is working the way you expect it to. 

Here you can see that the hair was shortened and made much frizzier. You can do anything you want. When you are fi nished be sure to re-cache and then turn Load from Disk back to On. 

As menti oned before, the KineFX toolset is currently designed for retargeti ng and moti on editi ng which are not covered in this lesson. These rigging and animati on tools will conti nue to evolve and this lesson provides a taste for what is coming in Houdini’s procedural rigging workfl ow in future versions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3d9ae118480c8ba4adf61f2a5c05248c6dfdca88ef8b6c8f5ae257ca71833473.jpg)


# HOUDINI FOUNDATIONS PROCEDURAL ASSETS FOR UNREAL

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/3d571d2ce6081db71a77dddf4549f659f47a0da29c73cfd1a422b02d5af84363.jpg)


To create game assets using Houdini’s node-based workfl ow, it is important to start learning how to think and work procedurally. In this lesson, you will learn how to create game assets using procedural nodes and networks then deploy them directly into Unreal using the Houdini Engine. 

Along the way, you will get to use dif erent aspects of Houdini’s user interface. You will learn how the dif erent UI elements work together to support you as you build your game assets. 

This lesson was completed using Unreal Engine 5. Note that while the lesson focuses on Unreal, you can import the same assets into Unity using the Houdini Engine. 

## LESSON GOAL

To create assets that can be imported into Unreal as game art. 

## WHAT YOU WILL LEARN

 How to work with Nodes and Networks to control the fl ow of data 

 How Houdini Digital Assets can be used to package and share your soluti on with others 

 How to load Houdini Digital Assets into the Unreal Editor 

 How to instance objects to points and control the orientati on and scale of the objects using at ributes 

 How to create a game asset with Collision Geometry for use in Unreal 

 How to export a Rigid Body Simulati on as an FBX fi le for Unreal. 

## LESSON COMPATIBILITY

The steps in this lesson can be completed using the following Houdini Products: 

<table><tr><td>Houdini Core</td><td>√</td></tr><tr><td>Houdini FX</td><td>√</td></tr><tr><td>Houdini Indie</td><td>√</td></tr><tr><td>Houdini Apprentice</td><td>✕</td></tr><tr><td>Houdini Education</td><td>√</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/054cf2424ebbdf8640b0c4fd9f11cbbc64b99bac20742bcdb1810bd2526b3bde.jpg)


# PART ONE Create a Simple Building

Learn how to build a simple building using a procedural network of nodes. Some of the nodes will be created by interacting in the Scene View and others in the Network view. You will use channel references to connect parts of one node with other nodes in the system. This creates a procedural solution that you will wrap up into a Houdini Digital Asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ba58c9a26340a7e6ade6609c3bab5e01f2dff93cea4e95a53723d083306eb31f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e7b3244900884b9c1e49409b5a8bd3072aae84320709c6aca25a152ea496f380.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/aa9d498038cdd10a92896cbd03b96cc47ae13502e192b48e9cfd470de6bbc458.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/93a75be01c653ab23e04fe82be156cbd820c86fc31c7237aa1b48b9661c49f40.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0a90dace31c5a9008995756a77b51e96c4f36b4da8a49462d53aef7dcb1751f1.jpg)


01 <sup>Select</sup> <sup>File</sup> <sup>></sup> <sup>New</sup> <sup>Project.</sup> <sup>Call</sup> <sup>it</sup> <sup>hengine_lesson</sup> <sup>and</sup><sub>press</sub> <sub>Accept.</sub> <sub>Select</sub> <sub>File</sub> <sub>></sub> <sub>Save</sub> <sub>As...</sub> <sub>Set</sub> <sub>the</sub> <sub>file</sub> <sub>na</sub> press Accept. Select File > Save As... Set the file name to hengine_01.hip and click Accept to save. 

In the viewport, press c and choose Create > Geometry > Grid. Press Enter to place it the grid at the origin. In the Operation Controls bar at the top of the Scene View, set: 

 Size to 5, 3 

 Rows to 4 

 Columns to 6 

Press v and choose Shading > Smooth Wire Shaded. 

02 Press c and choose Create > Geometry > Box. Press Enter to place it at the origin. Double click on the box_ object in the Network view. This puts you inside the object at the geometry level. Set the following: 

 Size to 0.1, 1, 0.1 

Rename the box node to column. In the Scene view press tab and start typing Match Size then select Match Size . Press n to select the box and then press Enter. This adds a new node. In the Parameter pane, under Matching, set Justify Y to Min. This raises the box up so that it sits on the ground. 

03 Press u to go back up to the object level or click on ob on one of the Network Path bars. Click on the Select tool and click in empty space to deselect all the objects. 

On the Modify shelf, click on Copy to Points. Select the column as the geometry to copy and press Enter then click on the grid as the geometry on whose points to copy and press Enter. 

In the Parameter pane, set Transform Using Implicit Target... to Of. Now the columns will be pointing up. Turn on Pack and Instance to ensure instanced geometry in Unreal. Press 4 to go to primitive selection mode. This will hide all the corner points. 

04 Press tab > PolyExtrude in the Network View. Place it to the side. Wire the grid node into the polyextrude node and set its Display flag. Set Distance to 0.1 and under Output Geometry and Groups turn on Output Back. Set the Template Flag on the copytopoints node. 

Add a Match Size node to the network and wire polyextrude into the first input and copytopoints into the second. Set Justify Y to Max to Same, Ofset by 0.1. Now the extruded shape will sit on top of the columns. 

Add a Merge node and wire copytopoints and matchsize into it. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/df8c6780ed07b44e595cfe4d612e7c194213f1272233d6ede20ee5146cf52f8b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/75f09a7832f0bb1a696909706a4ca4e6adf8052669d432c226af1f0bb79f1ed7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f32721868967368eb7538a1334b390a1b75db86dd870009d956f91e7a899ce8b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bb280fdef4c7f6b0ec04f16841a97cf81d6d06a35f04e85172a2d1450f47bd7b.jpg)


05 In the Network view, press tab > group. Wire it between polyextrude and matchsize. Change Group Name to edges. 

Alt drag to create a another group node and set its Display fl ag. Keep Group Name set to edges and then set Initi al Merge to Subtract from Existi ng. Turn of Enable under Base Group and turn on Enable under Keep by Normals. Set Directi on to 0, 1, 0 and Spread Angle to 0. Alt drag on this node to make a copy and wire it into the chain. Change Directi on to 0, -1, 0. Now only the sides of the box are in the edges group. 

Add a PolyExtrude node. Set Group to edges and Directi on to 0.15. 

06 Set the merge node’s Display Flag to see the fi rst fl oor of the building complete. Turn of the Template Flag on the copytopoints node. 

In the Scene view, press n to select all and then press tab > Copy and Transform. Select the column node and RMB-click on Center Y and choose Copy Parameter. Go to the copy node and RMB-click on Translate Y and choose Paste Relati ve References. Add a + 0.1 to the expression. 

Now increase Total Number to 4 to add three more fl oors. 

07 Select all the nodes in the Network editor. From the Asset menu, choose New Digital Asset from Selecti on. This will collapse the network into a subnetwork then use that subnet node to create the Digital Asset. 

Set the Operator Name to building which will change the Operator Label to Building. Click on the but on to the far right of Save to Library. In the Locati ons sidebar, click on $HIP/ and then doubleclick on the hda directory. Press Accept and then Accept again to save the asset to disk. 

08 The Edit Type Properti es window opens up. This panel is where you will build the user interface for your asset. You will revisit this window later. Click Accept to close this window. 

Rename the node in the network view to building. 

The nodes you have used to build the asset will remain a part of the asset even aft er you save it. This will allow you to conti nue making changes even aft er you have started using it in your Unreal game levels. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c938a5d8b3b94710c56b91a6dfe9b3d019d10b0201b723b3dcc586b82b986b77.jpg)


## WHAT IS AN HDA FILE?

Houdini nodes and networks can be encapsulated into single nodes called Houdini Digital Assets which let you share your techniques with colleagues. These assets are saved to disk inside fi les known as .hda fi les. 

Asset fi les created in older versions of Houdini may have a dif erent extension .otl which means Operator Type Library - both these fi le types work the same way. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/671c37b32f331a1636e5db73c7fda58e39e1a81c9f4607d5a469e5e3b1657693.jpg)


# PART TWO Import the Asset into Unreal

Now that you have a digital asset file on disk, you can import it into the Unreal Engine. This is possible because of the Houdini Engine plug-in which connects the two applications. Houdini Digital Assets that are loaded into Unreal are cooked using Houdini under the surface. The Houdini Engine for Unreal plug-in must be installed to complete this les son (See Sidefx.com/unreal for instructions). Please note that Houdini Apprentice does not work with Engine. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/576f221208b69c007e02375adcbc3f0affdc46bbc52ac601f397aba42d902b36.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/a0e822fe1ecac01ce979d51314a72a7989d35bdf05b6e53487fecdbd90935c12.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ab5482802f0aea07c1b67a411adaf3725231cb5545ef892a26cd8fd50c3b4b68.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f95f5b21643b73b25b845efcd4781d577434e4ac8c094e887f18dc01efd769cb.jpg)


01 IN UNREAL – Set up a Third Person Template with Blueprint support. Delete the TextRenderActor. Open the Content Drawer and click on the Import buton. You may want to dock the Content Drawer. Navigate to your Houdini project and find the building asset. Click Open. 

Set the Scale to 2, 2, 2 and move it into the corner. If you press the Play buton you will see the building during gameplay. 

02 <sup>IN</sup> <sup>HOUDINI</sup> <sup>–</sup> <sup>To</sup> <sup>add</sup> <sup>normals</sup> <sup>and</sup> <sup>collisions</sup> <sup>to</sup> <sup>your</sup><sub>geometry</sub> <sub>you</sub> <sub>need</sub> <sub>to</sub> <sub>add</sub> <sub>some</sub> <sub>nodes</sub> <sub>to</sub> <sub>the</sub> <sub>netwo</sub> geometry you need to add some nodes to the network. 

Dive into the building network and between the polyextrude and matchsize nodes, add a Normal node. This will add normals for the geometry to display properly in Unreal. Under the normal node add a Group node and set the Group Name to rendered_collision_geo. This will turn your geometry into collision geometry. 

Copy and Paste these two nodes and insert the new nodes after the column node. 

03 IN UNREAL – In the Generate section of the building asset’s Details panel, press Rebuild. Press Play to explore the scene. 

The normals are working properly and now you will collide with the columns if you try to run through them. 

04 IN HOUDINI – Select Assets > Edit Asset Properties > Building. In the properties window, click on the Parameters tab. Now select the column node and drag the Size Y parameter to the Parameter tab. Rename it Floor Height. Now from the copy node, drag the Total Number parameter over and rename it Number of Floors. Click Accept. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/f680229730f9557d35ca0f16fbcb20b81de1a6786f44d2d0c4d2ca5100152294.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/738e760466837f3575bdb279b353847737abcd650217c90494cbff1fcf5f5194.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/4ef60f9dd4ca56c85696d92d338f7d4a68f1ae2dc10dfb141106872e7383eac1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/601a9bc2700eb54f5a91aab80d8c435eb3f93b789d38030989657ffb5f6ec16b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/d5f5e5e0b2805a3be52868e04244ffda8a66a2c3be6afc220d5a2bd31481e552.jpg)


05 IN UNREAL – Press Rebuild in the building asset’s Details panel. Scroll down to see that there are now parameters for Floor Height and Number of Floors. Set Floor Height to 1.5 and Number of Floors to 2. You can Play the level to walk around the asset and review the changes. 

06 IN HOUDINI – Go back and set the Display flag on the floor slab’s polyextrude node. Press 4 to get primitive selection. Select the middle three primitives from the top then tumble around and shift-select the three primitives from the botom of the slab. Press Delete. This adds a Blast node. 

Press 3 to get edge selection. Double click on the botom edge of the hole to select the whole loop. Go tab > Polybridge. Press Enter. Now double click on the top edge of the hole then press Enter. This will add geometry to the inside of the hole. 

## 07 Set the Display Flag on the matchsize node. You will see the new hole with an overhang.

Press 4 to get primitive selection. Get the Select tool then select the end face of the opening. It may not appear selected but it is. Press tab > PolyExtrude. Under Extrusion, turn on Transform Extruded Front. Start pulling the face out and down. 

08 Copy the column node’s Size Y channel and Paste Relative Reference to the new polyextrude node’s Translate Y. Add a - sign to the expression then subtract 0.1. The expression should read: <sub>-ch(“../column/sizey”)-0.1</sub> Set Translate Z to 2.7. 

Move the normal and group nodes to after this polyextrude node. Otherwise, the new extrusion won’t be collision geometry and the ramp won’t work properly. 

Set the Display Flag on the output node. Choose Assets > Save Asset > Building to save the changes to the HDA file on disk. 

09 IN UNREAL – Press Rebuild then set the Floor Height to 1 and the Number of Floors to 6. Press Play and walk up ramps and around the building. 

Houdini has a number of nodes at the geometry level for seting up and managing UVs. In this lesson, you will use UV Unwrap and UV Transform to add UVs to the building. These work well with the simple shapes used to model the building. For more complex shapes you will use tools such as UV Flaten and UV Layout. You can see a UV Grid on your geometry once UVs are in place. To hide the grid, you can click on the Show UV Texture buton on the Display Options bar to toggle it on and of. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8ee6f3d2892452018f6aa48d8ba6d022cb16a809b08eefcd6faf442ecd21ca54.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/223e0c1a03a6766bb78ff850c23189dd052528f8695ad854ca6a513f3a1f8cd6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/34f006835b79f4445377104bf568407710f75f98511545af4cdf174b87e6df9a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/88d4e3f56fa7d496222ed92cecdfba998dfd6d50454651d668c95978aef562aa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/54b8209a35c31be42b34712c583ed36b443dd654a7e3b678f6188a47889140c3.jpg)


10 IN HOUDINI – You need to add some UVs to the geometry for use in the game editor. Go to the part of the network with the column node. Press tab> UV Unwrap and place the node between the column node and the matchsize node. 

Go to the part of the network with the second polyextrude node. Press tab > UV Unwrap and place the node between the polyextrude node and the matchsize node. 

11 You will see a UV grid on the columns. They are a diferent scale compared to the columns. Press tab > UV Transform and place the node between the uvunwrap node and the matchsize node. Set the Scale values to 5, 5, 5. Now the UVs appear more alike. 

Choose Assets > Save Asset > Building to save the changes to the HDA file on disk. 

## 12 IN UNREAL – Press Rebuild. You won’t see the UVs until you add a Material.

In the Content Browser, navigate up to Content > Starter Content > Materials. Make sure the Building asset is selected then add a Material such as M_Concrete_Tiles to the building geometry in the scene view. You may need to drag it to both the columns and the slabs. 

## 13 Press Play to walk through the level and explore the textured building.

This asset could be used more than once on a level to create diferent buildings with diferent floor heights and building heights. You could also promote more parameters to the asset to add more control. All the assets on your level that come from this digital asset can all be updated at once when a change is made to the asset’s network or its parameter interface. 

## PART THREE Copy to Points

In this part of the lesson, you are going to copy some boxes to points of another grid. You will then randomize those points to achieve a more organic look and add random atributes to rotate and scale the boxes to create more variety in the distribution of the shapes. This creates another procedural system that you will wrap up into a Houdini Digital Asset. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/521931e064f8ed9f86f5af70c7b2f09f8a7ba30df1da12b8fa04da12d0d3605f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c478659f0d3dcae7af2b81ca141efa990bf334c20851ba07d5cccbee5cfe8752.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c5837f27b914f356248df89f270137cfd148ba9fb0b66571d3db01091bc9e152.jpg)


01 IN HOUDINI – Go to the Object level and hide the building. In the viewport, press the c key to bring up a radial menu and select Create > Geometry > Grid. Release and then press Enter to place at the origin. You will start by using the points on this grid surface to instance geometry. 

Use the same radial menu to Create > Geometry > Box and again press Enter to place at the origin. In the Operation Control bar at the top of the viewport, set the Size to 0.1 0.1 0.1. This is the geometry that you will be copying to the points on the grid. 

02 With the box still selected, go to the Modify shelf and click on the Copy to Points tool. Select the grid and press Enter. Now the boxes have been copied to all of the grid points. 

You can now adjust the look of the system by editing parameters. Select the grid node and change the Size to 6, 6 and the Rows and Columns to 12. The grid gets bigger and has more points but the boxes aren’t being copied to all the points. Click on the copytopoints node where you can see that Target Points are set to 0-99 to match the points on the original grid. Remove the 0-99 to copy boxes to the whole grid. 

03 In the Network Editor, press tab > Scater. Place the scater node in the Network editor between the grid and the copytopoints nodes. It will wire itself into the network automatically and the boxes will now be copied to these new points. 

Set Force Total Count to 250. Play with the Relax Iterations to adjust how the points are being laid out. The scater node gives you a more organic layout compared to the original grid points. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/83333988767fe6fd36abc4dd7597bd032aebb49731ade021dbdc94c67aaf38f6.jpg)


## SOURCE GROUP

When you model in the Scene view, your selected geometry will get placed into the Source Group field as either numbered points or primitives depending on the tool. If the field is empty then the tool will work on ALL of the points or primitives. 

When you use tools at the geometry level this field will be left empty when you choose Select All [n] before using the tools. Because you set up copytopoints at the object level, it filled in the points as 0-99. 

copytopoints1 x Take List × Performance Monitor × + 

objbox_object1 

Copy to Points copytopoints1 

Source Group 

Source Group Type 

Target Points 

Guess from Group 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c4ef269c86dfdf4f1dcedd780415c39168985d5ef61cc820c883676b45e3c480.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c70a302fde393289acc180447d2b0c869c27b065a9c15712447a33afbd6cf7fc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/2028d63d28e503949293c9ff3144408897f599a36bb75e394b1d7cc21e7b6588.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c2520ed2c76012265c1239ee8eaec57aba9c54c0cd15b9a93c4334007b167b2a.jpg)


## HOW ATTRIBUTES WORK

04 In the Network view press tab and start typing Match Size then select Match Size . Place this node between the box node and the copytopoints node. In the Parameter pane, under Matching, set Justi fy Y to Min. . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/9618c46aaef9503f537263de506818c73f9f98ce35f2bab87846a3934879403d.jpg)


On the box node, set Size Y to 0.3 to test the expression. You can see that all of the boxes are siti ng on the ground. 

05 In the Network Editor, press tab and begin to type rand... then choose the At ribute Randomize tool. Place the at ributerandomize node between the grid and the scat er nodes. At fi rst, you will see random colors on your boxes because the default at ribute is color (Cd). 

At ributes that are assigned to geometry are passed down the network chain to dif erent nodes. In the case of this network, the at ributes being assigned to the grid geometry are passed on to the scat ered points which in turn af ects the copied geometry. This is an important way to control the fl ow of data in Houdini. 

Set the At ribute Name to N. This changes the at ribute to the normal directi on and all the boxes are now pointed in dif erent directi ons. Set Max Value Y to 0 which will limit the randomness to the X and Z directi ons. Rename it at rrandomize_rotate. 

06 Press the Alt key and drag on the at rrandomize_ rotate node to make a copy of it. Drop it between the at rrandomize_rotate and the scat er nodes. Rename it at rrandomize_scale. 

Set the following: 

 At ribute Name to pscale. 

 Max Value to 2. 

 Min Value to 0.5 

07 Select the grid node and increase the Rows and Columns to 30 – this creates more points on the grid which creates a wider variety of values on the scat er points. Save your work. 

This gives you a nice variety of sizes for the boxes on the grid. 

# PART FOUR

# Create another Houdini Digital Asset

In this part of the lesson, you are going to create a digital asset and test the system in Unreal. Just like the building this means wrapping up the network and saving the results to disk as an HDA file. You will promote some parameters to allow you to control the grid size, number of points and the relaxation. The parameters will then be available to you in Unreal. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/834fedbae130cd67f5a89d875d00fcfcae2cfac42050d1396ae6d705c43cf069.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/5d8996f870357eda9d707a5d7f45d06a97a2586f9b6968f971f7b63ae94e109c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ebba3d0f35667f5b0e4f6a29ad4a427a11f64f4ac587da6162e95c21d9b05629.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/c42becb5012e1c41d1d1d003d6928a27705163dbf1e5a383f4dd9eadb801ca2a.jpg)


01 <sup>Select</sup> <sup>all</sup> <sup>the</sup> <sup>nodes</sup> <sup>in</sup> <sup>the</sup> <sup>Network</sup> <sup>editor.</sup> <sup>From</sup> <sup>the</sup><sub>Asset</sub> <sub>menu,</sub> <sub>choose</sub> <sub>New</sub> <sub>Digital</sub> <sub>Asset</sub> <sub>from</sub> <sub>Selecti</sub> Asset menu, choose New Digital Asset from Selection. This will collapse the network into a subnetwork then use that subnet node to create the Digital Asset. 

The nodes you used to build the asset will remain a part of the asset even after you save it. This will allow you to continue making changes even after you have started using it in your game levels. 

02 Set the Operator Name to populate which will change the Operator Label to Populate. Click on the buton to the far right of Save to Library. In the Locations sidebar, click on $HIP and then double-click on the hda directory. Press Accept and then Accept again to save the asset to disk. 

This creates a new Houdini Digital Asset file (.hda) on disk that is being referenced by this scene. It can also be referenced into other Houdini scenes or into other applications such as Unreal using the Houdini Engine. 

03 The Edit Type Properties window opens up. This panel is where you will build the user interface for your asset. You will revisit this window later. Click Accept to close this window. 

In order for you to maintain the procedural nature of the Houdini Digital Asset, you can build a high level interface that can be used to access the nodes inside the network. You will add to the interface for this asset later on in the lesson. 

04 IN UNREAL – In the Content Browser, go back to the Content directory. Click Import to and find the populate. hda asset file in the current project directory. Drag the asset from the Content Browser to the 3D workspace. 

Press Play and walk around the asset. It is there but there is nothing special about it. Press Esc to return to the asset UI. 

By default, Houdini objects like the box have point normals but don’t have vertex normals. To make sure that you have proper vertex normals, you can add the Normal node which uses a cusp value to decide which edges should appear hard and which ones appear soft . Game editors such as Unreal need vertex normals to display properly which can be set up easily in the existi ng network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/57ac0c6a5ffd16b41a3c5c0a0f85e526613b3ca3625d06e1d9e8c46fd495fbd0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/e07c666bba29c54bd2ef6efae1c1f70d403ff3757263e13d92cd508daf51fb30.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/811f27c6c8964ef391264cb265f865a7094af67994cc2891c4e563277e8f377a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/8b6495e56740e62408d2ccd1bcefcaa04f3e11518e0744e496a30d9392be6df4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/825abb221c4d3dc242cd2daa9e99562a7e971d1302313287fe745428f69f78d9.jpg)


05 IN HOUDINI – One thing that you will noti ce about the asset in Unreal is that the boxes don’t have sharp corners. To fi x this you should go back to Houdini and in the Network editor, press tab > “norm...” then choose the Normal tool. 

Add the Normal node right aft er the box node. From the Asset menu, choose Save Asset > Populate. This saves the change to the .hda fi le which makes the updated asset available to anyone who is has it loaded. In this case it means that you can update the asset defi niti on inside Unreal and the correct normals will display. 

06 IN UNREAL – In the details panel, under Houdini Asset, open the Cooking Acti ons secti on. Click the Rebuild Asset but on to accept the changes. This makes sure that the changes you made inside Houdini are properly updated in the Unreal scene. 

The asset now has proper normals but you don’t have any control over the procedural network. To create an interface that you can use in Houdini, you are now going to promote some parameters from inside the asset to the top level. 

07 IN HOUDINI – Choose Assets > Edit Asset Properti es > Populate. Click on the Parameters tab. In the Network editor, click on the grid node. From the Parameter pane, drag the Size parameter onto root in the Existi ng parameters list. 

In the Network editor, click on the scat er node. From the Parameter pane, drag the Force Total Count parameter onto root. In the Parameter descripti on, change the Label to Number of Instances. Drag the Relax Iterati ons and Max Relax Radius to add these parameters to the asset. Click Accept which saves these new parameters to the asset. 

08 IN UNREAL – Click the Rebuild Asset but on to accept the changes. The promoted parameters show up in the Parameter pane. Change the Size and Number of Instances to see how they af ect the look of the resulti ng grid of boxes. 

Now the procedural nature of the asset has been exposed and you can create unique versions of the asset in dif erent levels. You can add more than one of these populate assets in this level and each of them can have unique seti ngs while referencing the same asset in the .hda fi le. You can also use this asset in multi ple levels being worked on by multi ple arti sts. 

## PART FIVE Set up Instancing

When you set up instancing in Houdini properly, you can replace the default shape you have copied to the points with other Unreal props. You can add more than one prop that will be randomly distributed in place of your default shape. You are now going to make sure that instancing is in fact set up properly and then you will use this to add some other props into the system. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/cf6a13aea48e78712a597911adff9693b2dad6b806528b9a11aa69dd13809ae9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/6d3671b499a8fb4cb69759d10557fa371545c5183a64782f7e84f5bc1130d16a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/1fa08e9ee1c5592105fb8e83bee9821db03929c6612d4321855c0a571081adff.jpg)


01 IN UNREAL – In the Details panel, go to the Houdini Outputs section. You can see that the whole collection of boxes is being imported as a single mesh. This means that you are not yet using instancing. Houdini is copying the boxes to the points then outputing the resulting geometry for Unreal. 

## PACKED PRIMITIVES IN HOUDINI

This is not very eficient for gameplay. Therefore you need to set things up just a litle diferently to get the instancing that you need for this tool to work properly. 

02 IN HOUDINI – Select the copytopoints node and turn on Pack and Instance. From the Asset menu, choose Save Asset > Populate. 

03 IN UNREAL – Click the Rebuild Asset buton to accept the changes. Go to the Houdini Outputs section. You can see that only a single box is being imported and instanced to the points. It is then rotated and scaled based on the atributes you set up earlier. 

By using packed primitives, the box geometry feeding into the copytopoints node is treated as a single primitive. This sets up instancing in Houdini and in turn triggers instancing in Unreal when this asset is loaded into the editor using the Houdini Engine plug-in. 

In Houdini, packed primitives provide an eficient way of managing instances for viewport display and rendering. The geometry feeding the copy node is packed into a single primitive and then treated like an instance. For the copied boxes shown in this lesson, this takes you from 1,500 primitives down to 250 once packing is in place. With the Houdini Engine plug-in for Unreal, the packed primitive is recognized as a Unreal instance which will allow for more eficient gameplay. 

Now you can replace this default box with other geometry in your Unreal environment. This is the ideal way of populating a series of points because you have lots of flexibility in the editor to add diferent objects to the system. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/ed36d63eccd94dde0bd53ec15e1efccecf534fbb64167e2ad1adcb6896dcaa07.jpg)


Points 2,000 

Primitives 1,500 

Vertices 6,000 

Polygons 1,500 

Points 250 

Primitives 250 

Vertices 250 

Packed Geos 250 

Center -0.0227511, 0.286 

Min -3.12244, 

Max 3.07694, 0.573 

Size 6.19938, 0.573 

Center -0.0227511, 

Min -3.12244, -1.0 

Max 3.07694, 

Size 6.19938, 

# INSTANCES IN UNREAL

When the Houdini Engine plug-in detects packed primitives, a Houdini Output Instancer is created in the Details tab that contains the input geometry and some parameters for Rotating and Scaling the instance. You can replace this with geometry from your Unreal content window and size it accordingly. The Plus sign lets you add more instanced inputs to create more variations in the same system. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/0296bd01eaf9028eaa4067486cd0efcf0f7c77d280dc0bc91f0023a09f0b9b53.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/98ce760a27ef1db34e6000045a82f8653e7ba98008c4627eeb3734db8d23bf99.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/598d0b1db0fbe0636ce4f683a0db9783caad21787c03d28438518610fa3d4f52.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/bfac0b84381c9f3bde9b11a41a68474aab8b18e5553b87e672ce40a49d2d31b0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-07-21/42696519-5211-49e5-9230-4da81214f844/7120ff25d24d411f3b44ce003b2254a861d50b48f92af884ca2c2c0db2c1892f.jpg)


04 Go to the Houdini Outputs section and expand HoudiniOutput1 instancer. This is the box instance which you can replace with content from within Unreal. 

In the Content Browser, open Starter Content > Props. Drag the SM_Bush prop over to the Houdini Outputs. Set the Scale Ofset to 0.25 in all three axes. The geometry is instanced to the points in the populate asset and rotated and scaled just like the boxes. 

05 Now click the Plus [+] sign next to the instance object. This adds a second one. Drag the SM_Rock prop over to the new Houdini Instanced Input. Set the Scale Ofset to 0.1 in all three axes.. 

In the Details panel, scroll to the Houdini Engine section and click the Bake buton. In the Outliner, scroll to the HoudiniAssetActor. Click the eye icon to hide it so you can focus on the digital asset. Press Play and walk around the scene to see the instances in action. 

06 Now click the Plus sign next to the bush object. This adds a third one. Navigate to the Content > LevelPrototyping > Meshes folder. Drag the SM_ChamferCube over to the new Houdini Instanced Input. Set the Scale Ofset to 0.4 0.4 0.2. 

You can continue to add more instanced objects to create more variety and maybe change the size. You can use the Relax Iterations parameter if you need to separate the instances from each other a bit more. 

07 In the Generate section of the building asset’s Details panel, press Rebuild. In the Bake section, turn on Replace Preview Bake then click on the Bake buton. 

Press Play to walk around the scene to see the instanced geometry in action. Now you can see that you are colliding with the cubes which already had collision geometry set up properly. You should always make sure your instanced objects have collision geometry set up properly. 