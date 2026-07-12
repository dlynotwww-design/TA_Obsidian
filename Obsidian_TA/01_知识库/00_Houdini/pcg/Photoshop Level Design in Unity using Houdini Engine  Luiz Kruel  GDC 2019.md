---
title: "Photoshop Level Design in Unity using Houdini Engine | Luiz Kruel | GDC 2019"
source: "https://www.youtube.com/watch?v=sDDruhbcEAk&t=1565s"
author:
  - "[[Houdini]]"
published: 2019-03-26
created: 2026-07-04
description: "Using the Unity-Houdini Engine plugin, Luiz demonstrates a pipeline that lets you make and edit PSD files in Photoshop then convert them into full playable levels in Unity.This in depth talk goes th"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=sDDruhbcEAk)

Using the Unity-Houdini Engine plugin, Luiz demonstrates a pipeline that lets you make and edit PSD files in Photoshop then convert them into full playable levels in Unity.  
  
This in depth talk goes through the process of building this asset and explaining the different methods used for converting images into scatter zones, spawn point placements, terrain and more.

## Transcript

### Intro

**0:00** · \[Music\] all right thanks everybody for coming end of the first day at GDC so it's awesome so my talk is about this unity demo that we did the thought here is we had this demo that you guys might have seen on the Unreal fest or not the root Festa epic state of unreal and that was

**0:29** · our kind of high-end Unreal 4 demo and then we kind of wanted to do a mobile version as well to just show the range of Houdini and it show kind of the breadth that you can do the thought about this title was we wanted to basically try to make it as easy as possible to make a game so we actually run it through Photoshop to where you can make the levels of Photoshop run them through buddhini and then get him running on your mobile phone so I'm gonna give a brief demo overview and then I'm trying something different here to where this is a super deep level talk so I'm actually gonna go through all of

### OUTLINE

**0:59** · the nodes and try to explain exactly how to do it so instead of me showing hey look at this cool demo it's like here's how it actually is and here all the nodes hope stick with me some part of it sort we might get dry I'll try to crack some jokes here and there to keep the moon going but I hope you guys like it and do they give the feedback if you guys appreciate this type of deep dive or if you guys want to keep it a little simpler yeah so basically we're going to talk about the demo itself there's two kind of components to the way the work so basically we have a tool to read a

**1:29** · Photoshop file and basically transform Photoshop file layers into curbs and then we have another tool that is a Unity engine tool that basic we can take a curve and then have different modes for different types of assets so I'll show a quick video of the demo itself and this is not supposed to be like beautiful art or anything so this is just it was myself Mike and Paul but there's a lot of cool stuff so this was recorded out of my phone there's

**1:55** · different art styles there's a lot of tools that came out of this the explosions are actually vertex animation textures running on a mobile phone so there's some stuff that we had to do to get the shaders to work on the low render lightweight render pipeline in unity and there's all of the modeling was done adeney some of it we started with a base mesh in Houdini went into ZBrush brought it back with cozy and did a decimation paul is going to give a more overview talk to where he kind of covers everything and but the

**2:23** · I'm really gonna focus on is actually on the the level generation itself so in production usually when you're making a game you usually start with a napkin sketch of your map and it's just an idea and you're trying to be like okay I want some trees over here this is the general flow of the map I want this general shape for the map I want to put some enemies over here some bushes over here some rocks over here and the thought that we had is like what if that's all you need it so what if you just had that done the napkin sketch and then that napkin sketch transferred into an actual playable level so it would that's that's

**2:56** · what we did and here's another video to where I Paul actually runs through the the whole stage I'll talk a little bit about it but the video self-explanatory but we'll start with just the the playable level and this is the terrain layer and the terrain layer is actually like a height map layer to where white is the highest spot middle gray is nil null and then black is darker so you can get some

**3:20** · elevation changes so in this case we want it basically to look like a canyon to where the walls are really high so then we bring it into unity we drop in the HDA we hook up the PSD file straight into it and then we tell the PSD file which layer we want out of the or the unity file h day which unity file do we want and then what mode to interpret that layer s so in this case is the terrain layer and that's what it basically you get out of it and the general idea is to give this to your

**3:48** · level designer and even if they don't know anything about Houdini anything about modeling anything about 3d they can basically make a map and start playing in the game it's not supposed to look like final art they're supposed to look like block out or at least you have something that is playable and then Paul started to and wanted to add enemies so it was just too boring to just run around and give a little path to kind of guide the player so there's two different layers one for roads and the other ones for enemies and I'm actually going to go through and exactly explain how each of these are figured out and

**4:18** · Vacancy fairly easily you just go back into unity you reload the map you kind of recoup the HTA's and you go back and you can play it now we kind of wanted to add fences so that's the other capability that we have to wear so if you drive a curve in Photoshop we can actually transfer those curves and turn them into little fences or the enemies and that way you can kind of like protect the player a little bit from it or you can in some cases in some

**4:42** · of the levels we have really straight air bridges and we can kind of give a little bit of so they don't fall from the world so that case it was actually too hard and you couldn't shoot through the barriers so we went back in and just erased some of the barriers so the the fences you can shoot through them and then we just wanted some decoration because the extra stuff around the path is something that we didn't care about so we filled it with foliage there's a tree layer and then there's a bushes layer and then there's a rocks layer and then it's that's generally it and then

**5:12** · because the the assets are just assets you can change their art style like any other swap that you would want to do so this is an older version to where we kind of had proxy art and we downloaded a asset back from the asset store and like hey we want to use this one so it's a completely different art style and we generated I think ten maps in an afternoon just really quickly and kind of got them all in and playable so here's some shots of the different maps and we might be able to make the apk

**5:45** · like the actual game available to you guys too and we're planning on making the project and the tools available we did another demo last year that we weren't able to share it so this one we made sure that we were going to be able to share it so under the hood what's actually happening so we have these layers and there's different types of modes so there's the terrain point where is basically just a point with an orientation decal which is like projection essentially to where you

### UNDER THE HOOD

**6:11** · want to have the roads originally we started to think the roads would be actual Road splines but that just looked bad and it just it wasn't what we wanted we actually wanted to paint some more organic roads some of then we moved into this decal mode and then we had the scatter and so what Houdini does it basically generates either instances or actual geometry to get it into unity and then the HDA actually just you can load it into unity and go through it so these are the maps that we generated and the pseudocode for the HDA itself is we have a node that it's called PSD layer to

### HOUDINI ENGINE CONVERSION

### PSEUDO CODE PSD Layer to Curve Curve Processing Based on Type

**6:45** · curve and that one is available on the other github already that tool so you can just use it and then we process that curve so let's actually go through the note itself so the first step is actually reading the Photoshop file so if you guys aren't familiar we do have a full kind of image processing system inside of Houdini called cops and that's we're kind of reading and writing in manipulating images so a little bit of the pseudocode Network all we want to do here is we want to read the PSD file as a whole we want to isolate the layer that we care about as the color and basically remove everything else so it's super simple

**7:21** · really basic what you're trying to do and the general just of the stock is just to kind of show how a lot of really simple basic tools can generate something that's really complex and really powerful for your users so here's what the Photoshop file actually looks like in Photoshop and you can see there's all of these different layers inside of keops there's a file cop which is kind of like a file shop that reads the PSD file natively and if you can see the layers in the or the image planes inside of the the cop matches the ones that were in Photoshop so what we can do

### FILE COP - READ FILES INTO HOUDINI

**7:55** · then is we can basically remove the siene which are the kind of default ones because we want to override them so we drop a delete node and then we rename the custom one that we care about so in this case I think use roads and then we renamed that to C so basically you just kind of shifted that so that's now the new default in our case we actually had to fill the Alpha with black because if we don't you kind of get some red overlays and some extra information that you don't want to kind of pre multiply against the the curves themselves and then you delete all the other planes so that's it and then you have an app node so with just these few nodes and I know

### RENAME TARGET LAYER TO C

### FILL ALPHA W/ BLACK

### DELETE OTHER PLANES

**8:31** · it might seem like I don't know if you guys got lost in the middle of it or it's kind of hard to see on a PowerPoint but again we just read the file we isolated the layer and then we remove the other layers so really really basic then we actually want to take that image

### TRACE SOP

**8:48** · and then do something with it so on Houdini there's a shop called the trace op and the trace app is designed for basically converting images into curves but by default it kind of generates a lots of points so what we want to do first is do a little bit of cleanup so we fused the points so we drop a fuse no to just well points that are really close together and then we do a facet node with remove in line points checked on which basically if the if you basically have a straight line with a lot of little points on it it kind of just gives you two points at the two ends of it as opposed to kind of giving you a

### CLEAN UP CURVE

**9:19** · lot of points along the way so that just simplifies things a little bit what we want to do next is actually we want to read the color that was in the Photoshop file and then use that as the color in your vertex colors because of the way the trace node works you might be at the very edge of your color so what we need to do is actually shrink the UVs a little bit and the way we shrink the UVs is actually kind of cool to where we can take the UVs of the model and basically

### SHRINK UVS

**9:46** · use those as the position so if you just use a pointer angle and all you do there is just set the UV to equal or the position to equal the UVs what you do is you basically move from UV space to world space and what that allows you to do is now use all of the rest of stops to manipulate your UV s so in this case the way we shrink our UV s is by doing a poly extrude with an inset so we basically in set your UVs or you inset your mesh and then you kind of take that new position and then you set that as your UVs and then you restore your

**10:19** · original positions so now you basically shrunk your you V's you using regular stops so there's a ton of stuff you can do by kind of going doing this kind of going back into you V's and the other way around too so you can take an object that is in the world space kind of throw it into UV space do things like UV layout to pack things and then kind of move them back into world space and then for loading UV color or loading vertex color so we're actually now when I blow that the colors again is just this attribute from map node and that one you basically just point it to the same know that you had are the same file that you had and that's gonna set the vertex

### LOAD IN VERTEX COLORS

**10:53** · colors for every point and then finally we just rotated because by default the trace op is going to give you something that's vertical you want something that's horizontal and we're gonna reverse it because by default the trace node kind of gives you backwards things and we set normals to make sure that you get good geometry so again it's it's a lot of little steps but they're really simple and if we look at the the kind of overall pseudocode is like we're at a PSD file with the trace op we cleaned it up with

### ROTATE + CLEAN UP

**11:23** · the fuse and the clean in the pass it we shrank the UVs we loaded the vertex colors and then we rotated and added the normals so this is something that once you kind of get the hang of it you can really throw it together in a few minutes but again now it's it's a powerful system that's backing the bad the the kind of heart of this game and we figured that this tool was just generally useful so we actually package that up and then we made that into a game development toolset note so you didn't even have to do this again so if you want to try setting this up yourself you can just start from this trace PSD file and use that so now we want it now

### PACKAGE IT UP

**11:58** · we have PSD files in Houdini as curves which is awesome what we want to do now is kind of process that curve in different ways so there's lots of different ways we are processing it I'll show I think there's a picture of the the note is basically one big switch so it's like multiple changes that are on the HD a and then a switch in the bottom they can kind of control which one who goes where as this is just a pass through so if you're kind of trying to debug it it just passes those curves straight through so you can see what you're doing sweep within and use but the idea here is to try to generate roads to rare

### PROCESSING THE CURVES

**12:30** · if you have something that might be a little sloppy or the the your curves aren't perfect they will kind of give you a perfect ribbon based on those point is for instancing so for spawn points and the cool thing here is that we can actually get directions so instead of just placing something and you're gonna get random directions there you don't know what the enemy is going to face we can actually do a stroke towards the direction and then we get the centroid with the kind of direction of where the enemy should be facing terrain is the terrain bit scatter area

**13:00** · is like the kind of heart of it to where we just take the curves and add a bunch of points inside of it fence and then building is something that Paul is going to show I don't show it here I think I'll have a slide for it but we actually have a building generator so we actually did at one of the levels you draw a shape in your PSD file and then that runs through a building generator and then you get a full building in the game man and finally is the decal so now we get into the the meat of it so get ready for this awesome so the a this is just a passive so

**13:33** · basically all we're doing here is we're scaling it at up a hundred because that's basically put it in unity space and then there's a parameter called size that we multiply it by and that's it so basically it just comes in we read that curve we pass it through the roads are a little bit more complicated so what we do is we get the straight skeleton so basically you have the the kind of shape of your curve and we want to get the kind of center spine of that shape and that's called the straight skeleton and then we want to basically get the distance of that straight skeleton to the edge and set that as the P scale so

### SWEEP - PSEUDO CODE

**14:07** · the P scale is a special attribute in Houdini that basically gives you the thickness so when we sweep it if you have something that went from sent to thick your sweep will actually match it but the nice thing about the sweep is that you'll get UVs and you get kind of like a perfect ribbon and nice segmented things as opposed to kind of really triangulate a mesh so here is the note

**14:27** · itself and this is it's kind of like a simple little chain and I'll go into details but you can see how I have different thicknesses for the different curves so first we sample the curve just to kind of make sure that it's not super dense so we kind of simplify it a little bit and then we have a game dev straight skeleton node that basically just gives you that curve now before you have to do a poly expand 2d and then do some

### SWEEP-GET STRAIGHT SKELETON

**14:53** · shenanigans to try to pull out that Center spine we simplified that to where now there's just a node called straight skeleton and it has a lot of extra fancy bits so the the straight skeleton will usually not go to the edge of it because it kind of shrinks it down and you kind of get the main core but we have an ability of basically projecting that last point back out to where it touches the original curves so now we actually have something that looks like what you guys are seeing then we do that attribute rango to basically move the edge distance attribute that we get from the poly expand to D to P scale we blur

### SWEEP LINE

**15:26** · a little bit just in case it's a little bit noisy and then there's another new node called the curve sweep which is basically a wrapper around the sweep node that hides all of the nonsense that you have to do to get UVs on the sweep node so there's also so that's kind of one of those Houdini historical things that it's like here's the secret magic for you to get you visa on a sweep and you got to convert it to NURBS and then you got to add this attribute and then you got to convert it back to polygons and you got to make sure that the sweep is set to the specimen like I even I do it and I

**15:56** · remember it once and then I have a file that I refer to whenever I have to do it again because I don't have mental capacity to store that stuff so I finally just said screw it I'm just gonna build a no that does it and the nice thing here too is that I found myself whenever I did a sweep node I would either do it with a box a curve or a circle and that was like 90 percent of my use cases for the the sweep node so I just built those in so by default you just pass a curve and you have some built-in options to basically do those shapes you also have an optional second input

**16:26** · to pass in a custom shape if you want to do a custom profile and then you have a optional third input which is a naming angle so basically like an up Vector so you can have another curve that kind of drives it and that curve doesn't have to be the same topology as the original one which is kind of nice because then it just simplifies it you can kind of if you want banking or some special behavior on the sweep um it allows you do that so that that's basically back on the sweep so it did take a couple of special magic notes but again those are now just done and built into Houdini through the game dev tools so and then

**16:59** · the transform at the end is just are going to push it up to unity scale so realistically all we had to do is we got the straight skeleton with the straight skeleton node we did a little bit of attribute management to kind of polish it or blur the attribute and then move it from one place to the other one and then we were in the sweep node and now we have a really solid tool to be able to kind of take a general brush stroke and then convert that into a proper Road and then we get into the point which is kind of cool cuz we use this all the

**17:27** · place for all of this fonts so before the spawn point of the player and then the spawn point of the enemies we use this and like I said before the general pseudocode is because you just have kind of like a streak you want to figure out the 2d bounds of that streak and then figure out what's the longest edge so

### POINT - PSEUDO CODE

**17:45** · you isolate the two shorter sej so now you have these two guys and then you find the center of those so now you basically have two points and then you basically just subtract the position from one point to the other point which will give you a direction and then you move that point either the points to the centroid and I basically have a point in the center that's aiming as the general bounding box direction of the the the input curve so if you see here's the kind of the

### POINT - SPAWN PLACEMENT

**18:10** · result to where I just do a for loop for each of the island shapes I run through this kind of generate orient at point subnet that will go into it and that that's a really good job even like these weren't designed to be these were the decal curves but it's still it kind of gives you the general orientation really solidly so how are we actually in doing

**18:28** · this so what is in that magic generate pouring your point node so we use the bound node so the bound node will give you a bounding box of that object that is properly 3d oriented but because we're in 2d space we only care about the top face so what we do is we do a delete node and the delete node has an option to basically delete things by normal so you can just basically say anything that's not facing up get rid of it so that gives you a single face that is the kind of general 2d bounding box then we can do a measure so the way to get the longest edge is we measure with it

### POINT-DELETE LONGEST EDGES

**19:02** · we have to do a carve to basically split each of the edges individually so now we basically have four primitives we do a measure node to basically get the perimeter of each of those so basically got the length of each of those and now we promote that attribute from each of those primitives up to the detail level and the attribute promote is super powerful because what there's different

**19:23** · modes of how to promote it so basically you're saying there's four primitives and I want to take those four attributes and I want to promote that up to the geometry level the kind of detail level but you can say how do you want to put like how do you want to promote that you want to promote it with this you add all of them together do you get the average of them or you get the max of them or the min of them so if you set that to the min or the max now you basically get the max value of that your longest edge

**19:47** · so then when we do a blast we can actually look into that detail attribute and say hey if my perimeter attribute of this current primitive is smaller or equal than this kind of promoted one I will get the shortest edges then we get the midpoints and the midpoints is super easy to get we just do a carve and I think it's goal so you can basically extract the points that's this option over here if you guys can see my mouse know this option yeah

### POINT - FIND MID POINTS

**20:18** · there and that basically you just say extract the points a halfway point at the halfway line and then finally we have a little bit of a wrangle and that angle is basically you're just subtracting one position from the other position so basically on your point Rango you basically pipe in the first point and the second point and you use that you can split them up using the split node and you basically just have two inputs now and you basically remove subtract the position of the first input from the position of the second input right now we get that and I'll I'll make

### POINT-GET N AND CENTER POINT

**20:53** · these HD availables for everybody so you guys can kind of go in and look at their angles their angles are the only a little bit that are slightly more complex but you'll see they're kind of one line or two lines each - it's a really nice introduction in triangles to just kind of do these little tricks so again all we did here was we got the 2d bounds we figure out what the shortest edge are we got the center of those and then we kind of subtract that both of those to get a vector and now we use the

**21:22** · left and right to be able to kind of get oriented things the one thing to know is that you can either get something pointing this way or that way in our case it didn't matter because the turrets can rotate so that's the only kind of catch you can probably do some bias to where you can make instead of uh you can you can do a closer fit instead of just a bound to it you can kind of get a taper and you can kind of get a slightly closer fit so that's the one

**21:48** · caveat yeah and then the terrain itself so the terrain is the slightly relatively more complicated one so the first thing we need to do is actually we need to add more resolution to the terrain and then reload those vertex colors so because we only have curves and we actually want more of the detail from the interior shapes we kind of need to add a lot more resolution and be able to kind of reload those and then we need to displace the points based on that vertex color and then we basically extrude things down and we've oxidized it to basically turn it into

### TERRAIN - PSEUDO CODE

**22:21** · excuse me as solid shaped so sometimes the extrude we're kinda extrude through things and do some weird stuff so voxel icing will kind of send them to volumes and send them back into polygons and then we add the vertex colors to basically isolate grass from walls so we do a really simple just if something is up facing its white and if it's not it's black so then on the unity side we can do some vertex colors and then I'm

**22:47** · looking some water and then finally we just add the ramesh note that kind of gives us that kind of broken up organic look and we add your visa and collision welcome okay so let's see how we're

**23:03** · actually doing that excuse me okay so the first thing that we needed to do is basically add that resolution back in and the way that we do that is with a divided node so the divide node can do things like triangulated it's kind of like an uber node where you can triangulate objects you can remove everything but the border but it also has a school feature of a Bricker and the Bricker just basically adds a grid of polygons to your curve so in this case we just basically lay it out a grid inside of your shapes and then now we

### TERRAIN - BRICKER DIVIDE

### TERRAIN - RE READ TEXTURE

**23:35** · just do the same attribute for a map that we did before but because we have a lot more resolution we're actually getting more of the data as opposed to kind of getting this streak EMS that we were getting before because we didn't have the resolution so then we do the displacement so for the displacement actually we do need to do a little bit of gamma correction on the vertex colors so we do a power function by point twenty five point forty five which is one divided by two point two and that would just kind of I want it to be a stickler to where if I painted middle gray on the Photoshop file I want a middle great to be no movement at all

### TERRAIN - DISPLACE HEIGHTMAP

**24:10** · and if you bring it into through cops there there's a game I apply it on reading that texture so we basically want to dia ply that gamma and basically force that value to be again 0.5 and then we unpack that value because we're going from zero to one and with my point five being the middle point we actually want to switch that range back to being negative one zero and one so what we do there is we just multiply it by two and then shift the back down by one and then there's an offset which is kind of like a strength parameter that we can use so then we just drop a poly extrude

### TERRAIN - EXTRUDE AND VOXELIZE

**24:45** · and a reverse and a box alight so basically we extrude the mesh down we flip it the normals inside out because we kind of move things down so we kind of get the inside rotated and then we have a node in the game dev tools called voxel mesh which all it does is basically sends the mesh into voxels and then send them back into polygons so it goes through open V DB and then back through man this starts giving us some a little bit softness and it starts getting some cool little bridges that start to happen naturally to where if things are just slightly closer together

**25:15** · there's a little bit of that kind of metaball feel to it then we add vertex colors so this is super simple we basically make a group based on the normals so basically we just select any normals that are facing up and then we set a color to those that we're gonna pick up on the unity side and then finally we do this remesh and the remesh is just like our artistic choice and if you're just doing blackouts might not matter before the game we wanted it to look a little more organic and then finally we just there's two little steps

### TERRAIN - TOP FACING VERT COLOR

### TERRAIN - REMESH FOR ORGANIC LOOK

**25:46** · to where we added UVs because we want to have textures on it at normals and then there's this kind of secret group that adds collision to unity so this is a kind of naming convention that we have with unity or with the unity plugin for Houdini and you can look this up on the unity plugin documentation there's a few kind of known groups or special words that tell unity to do something specific or the unity plugin so in this case we just wanted to say take my polygons and

### UNITY HOOKS - COLLISION

**26:12** · use those as the collision as well so we basically make a group and we say this is render collision geo and it's just something that the unity plug-in understands and can set that up properly so again that was kind of long and it has a lot of steps but if we kind of pull it back down and break it down conceptually we just added the vertex colors back in we displace the mesh based on those vertex colors we extruded the the mesh down and kind of gave it the kind of metaball look to it we added some vertex colors that are going to be useful in unity and then we remesh it

**26:43** · and add the UVs and collision so the end looks like this it's a little blobby before our blackout purposes it's more than enough and once you kind of put it on a phone and you kind of zoom in you really don't see the shape at all you just kind of see the textures which works really well I'll do questions lean

**27:01** · over to you so we'll stick through and we'll do questions after then we have the scatter so the scatter is really simple so the only difference here on scatter is just a built in no.2 Houdini to where you can just take a shape and you scatter a number of points and we wanted to do something slightly fancier to where we wanted to do a measurement of that island and then use that as a multiplier into the scatter numbers so basically if an island is really tiny we don't want a thousand points on it we want to multiply that by the the size of it and then we have another little bit which is we're snapping to the ground so all we do there is we move all of the

### SCATTER - PSEUDO CODE

**27:34** · points up into space and then we kind of raycast them down to basically so if we have the terrain now can change and we didn't want floating rocks so we basically move everything up and then we basically shoot everything down and then we delete anything that didn't hit the terrain and kind of stayed up at a specific number so again this is what the the the chain looks like which is relatively non-threatening and so what

**28:02** · we do is first we do a for loop based on the connectivity so basically for each Island which is fairly standard thing you want to do basically for each connected piece you want to iterate through it in this case we do a measure stop again which is super useful but in this case instead of looking at the perimeter we're measuring the area and then on the scatter we're kind of indexing into that measure shop and getting the value that it was and just using that as a multiplier so I'm gonna say my base value is 200 points but then

**28:30** · I'm going to multiply that by the area so if the area is big I'm not gonna get less and or more so then we basically do that loop so for each of the four islands we scatter it and then we add some random attribute so you can see I'm and I'm randomizing the P scale attribute which is the scale that the attribute that unity is going to use on the instances themselves and also the rotation wise so I actually wanted them to not be perfectly laid out we wanted them to be randomized but we only wanted them to be randomized along the way so we just kind of wanted to twist the trees around and the bushes around

### UNITY HOOKS - INSTANCING

**29:02** · yeah and then we actually just have points so these are just raw points that we are sending to unity and again another one of those connections conventions is if we add an attribute called unity instance that string that gets passed to it is the actual path for the instance in unity so in this case we're actually exposing that as a parameter so when the user uses in unity they can drop it in those set up their

**29:27** · layers and then there's gonna have a parameter which is okay what do you want to scatter here and then you can take your prefab that is a rock or a tree or a bush and you can basically just drag and drop that and it will instance those so again super simple we're doing some fancy stuff with scattering based on area but this is relatively straightforward and a couple of attributes to basically make unity do slightly more fancier things and then the snapping to ground I'm not even showing here but it's basically you move everything up it's two nodes you basically use the transform node to move everything up and then use the raid node

**29:57** · to basically move everything back down against the drain and then fences fences this kind of bread and butter for Houdini so this is actually even cheaper fences than the usual one so the the

### FENCE - PSEUDO CODE

**30:13** · pseudo code here is basically similar to the sweep one to where we are getting that straight skeleton from the shape we're deleting the curves based on a threshold so if we have like little flakes here and there we want to get rid of those and then we do a little bit of cleanup and basically welding curves that are kind of together and that's an awesome note that if you guys don't know it's called the poly path node and then we're adding the kind of normals and up vectors so whenever we're placing the objects they kind of face towards each other and they're kind of generally point up so you kind of have these two vectors so you have an up vector and then you have a normal that looks like that and then again we add those unity instance objects so the way we're doing

**30:49** · we're kind of cheating it to where we have two assets one is the pole and one is the slats and the points kind of overlap themselves so basically for every point we have two points one for the pole and the other one for the slats and we basically place them and then for the slats chain we delete the very last one so you don't have a slat kind of hanging out the end so again what we're

**31:12** · doing is that straight skeleton gamedev node that give you the kind of spine for the curve that you used then we are doing this kind of cool trick which is you basically do a for each node and instead of doing a delete you actually do a switch to a node so you basically do a check and you say if this is true use the incoming geometry if this is false

**31:35** · use the null which is basically essentially deleting it so in this case basically we pass all of the curves that came out of the straight skeleton and we do a measurement check basically getting the arc length which is like the length of the curve so you can say if the link length of this no three node and then there's like a couples like we basically want the zero like basic from 0 and 1 is smaller than 3 or greater than 3 it's true then we want to get the branch check came in and if it's false we're gonna get that null which means we're basically deleting it then we do a little bit of cleanup so the straight

**32:10** · skeleton will basically give you more primitives than you want so you kind of want to weld the two curves together and the way you do that is with the poly path node so this is super useful and sometimes we even use it like on the OSM data torii basically have a lot of general curves together and you kind of want to weld them into a single long curve that's what it's for and then finally we just sort because once you add things together the vertex waters gonna be wrong to our like you might have zero halfway through the curve and you actually want to sort them based on the vertex coder so it does you the original one is actually zero at the end for the normals it's just the

**32:46** · polyframe node so if you guys are familiar with that it's fairly straightforward it's also as of 17:5 the polyframe node can generate McTeague tangents which is kind of cool for shader stuff and more generally tangent work and then we do add an up Vector so now we have that those two vectors that we need for unity to be able to instance

**33:07** · things together and then finally we kind of split it into two chains one where we get again we loop through every curve and we delete the first point out of that curve so we don't have that kind of dangling slat and then the other one we just pass through and then we set two different in unity instance attributes one which is the slots and then the other one that's the pole and that we get something that looks like the fence so again like it takes a little bit to go through it but realistically all we did was we got the

**33:37** · straight skeleton we deleted the small curves we cleaned it up a little bit we added a couple of attributes that we needed for making sure that things were placed and oriented right and then we added those instance attributes then the final one is the decal mode so the decal mode is really cool because it's just generally useful and what we're doing

**33:56** · here is we're kind of almost projecting the geometry onto the terrain and the way we do that is we thicken the curve to right now it has volume and then we boolean that against the terrain and then we get the intersection boolean so what you're really doing is you're basically almost creating a cage and then you're getting the piece of the terrain that's within that cage so instead of getting the curve and trying to raycast that into it which might give

### DECAL - PSEUDO CODE

**34:21** · you the results you want or not you actually just get the terrain geometry that you want and the nice thing is that terrain is already you vide and has vertex colors and other stuff so you can leverage those to make sure that the textures blend properly so let's go into the nodes yeah so basically we have the snapping to the ground to make sure we just move everything up because we don't want any curves beneath the terrain we want to move them up snap them back down and then there's a thickened node and the thickened node basically just extrudes things on both directions and kind of welds them in the middle which gives you this nice cage then we do a

**34:57** · boolean which will basically is that to intersect mode which will give us that plane and then I'm actually grouping the edges so actually what I wanted to do is I wanted to fade the edges of these guys because I thought I wanted a nice transition into the the terrain because I wanted these to be like little dirt patches and like little roads that basically behave like decals so what we do is we drop a color node to basically flood them to black or flood it to white and then we do a group with edges set and basically select unbound edges which

**35:31** · is me or unshared edges which is going to be your borders and then we set those to black so if you can see the kind of last polygons are kind of fading to back and then we use that on the shader so if you can see now we have everything together so the the roads are here and you can kind of see that they fade a little bit we have the fences we have the everything the rocks the scatter the points and again just to see it one more time now they kind of have the perspective of everything the roads are

### ALL TOGETHER

**36:02** · the the kind of grassy lighter bit the instances are placed the fences you can see there's actually the bug in this case I'm actually not the leading the last lap I'm actually leaning the last Pole so now I get that double a long little bit and I've been blamed Paul for it so be on record and in this case we actually like Paul has some amazing other talk store he goes through some of the modeling that was done for it which is super basic but it's again just to show how really easily you can do and then this is me dying on my own game

**36:33** · because I couldn't beat it well that's it so now you have all the knowledge that you need to do to basically recreate this game yourself and you can basically go through and hopefully set this up so again just a recap of what we went through we have this tool to basically convert PSD layers to curves and then we have lots of different ways of processing those curves lots of little tricks in there lots of cool

### RECAP

**36:59** · little things lots of new tools that came out of this because we basically ran through it and then we're like this straight skeleton thing is kind of generally useful so maybe let's just make a tool out of it and we do that on our work when we're close and you should do it too like if you guys see that you're doing things over and over again and you have these little changes that you always use just make that into an HD and put it on the back pocket and then now you don't have to kind of keep dropping these even if it's like two nodes it's two nodes they have to know which nodes are to drop and the right properties that you need to know to drop so it simplifies things a lot and now you basically have a system for generating procedural Maps easily and

**37:34** · the cool thing is that you can hand this as the tech artist you can hand this over to your designers you can hand this up to the concept artists you can have up to your directors and your art directors and they don't really need to know about 3d they can just draw some stuff on a napkin and basically start playing their game and be able to kind of have their own feedback which is kind of your democratizing the book which will try it it's like the the creation so the other two talks that have so Paul actually has another

### FOR MORE INFO

**38:06** · talk on basically this rapid level creation he's not gonna go as deep it's more of an overview but he's gonna touch like the building generator we have like a snow build up tool that we release to basically generate the kind of snow cap on the trees we have a dirt skirt generator for the desert and we have I think a branches curve to generate the kind of dead trees so it's kind of like a cheap L system system or to where you can kind of not have to deal with our system but you can start still gonna get recursive curve generation and then he actually has another one which is creating functional prefabs using engines so he actually goes further to where not only you're handing off unity

**38:40** · a couple of points and some attributes he's scaling off like full destructible scripts and for kind of extra things to do on the flip side so there's nothing that you need to do there's a lot of other talks that we have but for this kind of demo those are it so thank to you and have a great day okay now take questions do you guys have any you have

**39:15** · to update so dude there's like a button they just get it I thought about making it auto update but I thought that was a little jerk Oni and on people with protection because they might want to lock the version and be like don't but I might add an auto update if you feel that's useful we're actually gonna try doing some other stuff too where we actually ship them with Houdini now for people that are behind firewalls but we kind of ship them hidden not as a zip file in the Houdini installation but we might make an option that's like do you want to use the built in one or do you want to get the github one so you can kind of ensure that everybody is on the same version that is the tie to the

**39:50** · Houdini version alright yeah that's the souville and the github downloader is actually a script so if you guys want to kind of automate that process you can but we should be able to make it auto populate it's a good idea and we want to add release notes whenever you update you know what you got and you can say hey here's the new things yeah so we do

**40:37** · so you probably saw the quick so demo today yeah so that was our Unreal demo for the year and then this one was the Unity one but they're kind of mutually like you could be able to you could definitely do the exact same thing in unreal we have an unreal plug-in that basically has the same capabilities so it's kind of a stick so if you set up these systems here you can work there and then the nice thing about the unreal one is that there's no runtime capability at all so you can basically bake those out the blueprints so

**41:09** · whenever you have the scatters you can say just decoupled the Houdini actor altogether and then you bake it over to thing yeah if you have more questions on chat with you later yeah yeah the fuse

**41:31** · is the one that tries to catch that because sometimes you basically have like a beveled corner and then some like the fuse will try to kind of stick that into a single one so that's you have the fuse and the facets of the fuse tries to kind of force those 90 degrees curves and then the other one yeah yeah but it's it's weird because it's like a pixel perfect so if there's two pixels that are here it's not gonna give you that 90 degree it's gonna give you the little one you can import SVG files so

**42:05** · you can export vector files I don't know if like a dot AI file will come through that's worth testing yeah and then that that might just come in cleaner - that just might come in as curves I know we had like EPS support too so that's something to consider like if you do need perfect exact things anything else too low-level decent a little bit all right cool yeah thanks