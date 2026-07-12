---
title: "Advanced Road Generation | Erwin Heyms | Games Workshop"
source: "https://www.youtube.com/watch?v=G5Iq-jxgZn0"
author:
  - "[[Houdini]]"
published: 2022-11-14
created: 2026-07-03
description: "LESSONS & PROJECT FILES: https://www.sidefx.com/tutorials/games-workshop-tech-track/In this workshop Erwin will explain how to use his road network tools, recently added to the Sidefx LABS toolkit,"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=G5Iq-jxgZn0)

LESSONS & PROJECT FILES: https://www.sidefx.com/tutorials/games-workshop-tech-track/  
  
In this workshop Erwin will explain how to use his road network tools, recently added to the Sidefx LABS toolkit, to easily edit and manage complex road networks. Maintaining clean road networks is vital for expansive environments, be it for open worlds in video games, or procedural city generation. However, cutting and merging curves can quickly destroy the attributes that carry useful information, like the road width & road type. The new LABS “Merge Splines” & “Poly Scalpel” SOP nodes can be used to create and edit these complex networks or roads splines, while managing attributes, groups and curve direction. Combined with a few tricks of the trade, Erwin will demonstrate how managing and merging road splines and surfaces has never been easier.

## Transcript

**0:02** · \[Music\] thank you hello everyone and welcome to this Workshop about Advanced Road editing using Houdini and side effects labs my name is Erwin heimes and I'm a technical artist at Ubisoft for the past nine years and I've worked on multiple titles

**0:29** · including ghost week on wildlands Ghost Recon breakpoint and most recently why this Republic and next to that I'm also a Houdini teacher and consultant and I've been teaching Houdini for the past six years or so now over the past year I released my first free course out on my YouTube channel udini Academy it's basically the introduction module and the foundation module which teaches beginners how to use Houdini next to that I'm also a procedural r d

**1:00** · consultant and currently I'm working on Pipeline and World building with an architectural company okay so let's talk about what this Workshop is going to be about so over the course of this presentation I'm going to cover how procedural Road networks are constructed we'll have a quick look at the road pipelines of Ghost Recon wildlands and what I've learned by studying the Unreal Engine 5 City sample demo and then we'll cover the new tools that I've developed for side effects labs and how they can help you among other things

**1:34** · to build and manage Road networks with Houdini so first I'd like to have an overview about how roads are built and I'd like to start using Ghost Recon wildlands as an example let's have a look at the roads that were generated in Ghost Recon wildlands and how they were constructed for a project of this scale so for Ghost Recon wildlands my focus

**1:59** · was on the road building tool set and it allowed us to produce procedurally over 600 kilometers of roads at various sizes material Styles and also in included Road propsing and terraforming for the entire world now over here on the right we have the terrain as it was originally and then we have the roads stamped into it and the way how this worked is that we had a pathfinding system that would find

**2:30** · a path across the terrain from point A to B and it would then do all the processes after that to stamp it into the terrain so if we look at it from this point of view our terrain was divided into 64 2 by 2 kilometer tiles each of these tiles had a generated app finding grid we could then connect together these waypoints into a larger lattice that would eventually form the basic connections of our road Network the Pathfinder would pass over these connections and then output the roads

**3:05** · that would then be terraformed into the terrain so over here I have an example of the road Pathfinder in action we have points A and B and then it will pathfind between those creating Switchback turns if it has to go up a steep slope but in general the Pathfinder here tries to find the shortest path possible while

**3:25** · making the least amount of turns though how many turns it makes is configurable then we would combine these together we had railroads we had large medium and small roads and then we had villages and if you combine that all together then you get quite an extensive Road Network that had to be managed and maintained over a long period of time during development of the game

**3:51** · so the way how this was done was using a road generator tool now version one basically worked like this here we had our two by two kilometer tile and then we could place waypoints on that tile to go from point A to B like so we could also Place uh guides if you will for Bridges and later tunnels

**4:15** · and then if the Pathfinder would try the path between this point and that point then it would basically follow this connection here creating a bridge and then finally we could draw an exclusion curve which would prevent the Pathfinder from going through this area so it would have to find a way around so if these connections defined we can then run them to the Pathfinder system and this will produce these raw curves now these are too rough to produce final roads so first we have to clean them so we do a smoothing pass

**4:50** · we also take any intersections and flatten them this is better for the vehicle traffic in the game I would take any Switchback turn or sharp turn in a hilly environment or on a slope and I would widen it out give more space for the cars to Traverse

**5:09** · and then finally we can create a ribbon from that and prepare a terraforming stamp so the first thing I would do is export out this result here to a road curve Network and then also run this through a terraforming stamp which we can then turn into terraforming textures one for each tile of the world map so it's easy to composite together speaking of compositing here is the road system so on the left we have the input tools then we had the grid and the connections

**5:43** · and how they would pathfind across the world this would then be combined together into a larger network of roads for the entire world we would run the terraforming through that for every tile and that would then be run through the compositor to be stamped into the terrain now this tool set worked but it had its downsides mainly that the Pathfinder could be unpredictable and we had the issue that roads could shift

**6:09** · so as a second version of this tool I changed it around a bit basically I took the pathfinding grid system and I moved it to the front so we first have the grid for every tile in the world then I combined all of these editing

**6:27** · tools into one tool and I turned that into an editor meaning that we saved the result to a cache and I also performed the pathfinding whenever I draw a road so the pathfinding is now inside the editing tool this basically meant that we had immediate results from the editing tool that we could then also immediately push into the game engine so here's a little demonstration of this version 2 of the row Builder this is basically an editor meaning that

**6:57** · we have a road here in the world but we also have it in Houdini because I'm using a cache I can see it both in the game engine and in Houdini at the same time I just have to refresh the tool now what I can do is I can add remove or update roads and I can set their settings as well so the type of Road and

**7:16** · its size I can then draw waypoints and move around my waypoints until I'm happy with the path and then save it to a cache if I don't like something and I also remove it so here I can draw two points and specify I want this section to be removed and then draw a new part in between or I can specify this section of the route needs to be changed to a different type and then maybe add some more routes as

**7:42** · well now once this is all done and I'm happy with the result I can then run it through the render form and get the result back and in about 30 seconds to a minute I would have the final Road Network or at least I would have a preview that I can then preview in the world in the game and then I can bake it to the final terraforming now in this case I was editing the roads in Houdini I could

**8:08** · also edit them in the game engine but if I were to edit them in Houdini I would need to also be able to see where they are in the world and for that I could use this rode viewer this basically viewed the um cache and it also allowed me to test a couple of other things like dead ends and find out if there were any disconnections

**8:28** · basically if there was a disconnection or an end of a road it would indicate it with a giant cone um Bridges were blue and then we had different Road types as well as the railroads so that's a pretty quick and easy way to see where your road network is

**8:48** · now those Road curves had to be clean because otherwise a lot of other systems wouldn't work properly they relied on the road Network to be cohesive and this was important because we used it for a lot of systems like we had Bridges and tunnels we had power lines that had to be placed along roads the decals and the markings had to be placed procedurally um the vehicle AI of course needed to know where to go and for that they needed a consistent Road Network The Village tools had to connect to them

**9:19** · and finally we also had other checks that we could do like prop clearance and the in-game map so a lot of systems relied on a clean and properly managed network of Roads now as for villages basically they hooked into the main road Network they would flow from a town center outwards but then in the end they will be added to the road Network as well and since Villages had a lot of AI activity and AI paths in them also food

**9:49** · paths for NPC traffic all of this had to be managed procedurally and connected together so as we added more content to the game we had a consistent and functional Road Network all throughout that was very important finally we also had cities and these got quite extensive and these included rural roads like the ones you saw before we also had these grid patterns in the center of town we had sidewalks that NPC traffic had to

**10:20** · go over and food paths in between that connected to the houses like in the backyards so a lot of pathing a lot of little connected paths that had to all make sense so we go from this

**10:35** · to that basically a complete town with full AI vehicle traffic going through it and everything the only thing we might have to do after the procedural pass was do an art pass okay so let's move on to the next topic I would first like to talk about how we can take procedural roads and break them down into their most core components so what do we actually need in order to build residual roads now over here I have the city sample for

**11:05** · unreal um you can get it for free from the epic game store and it uses Houdini to construct the entire city with malt kits that includes the streets as well the streets themselves are made by combining multi kits together so that means the network has to be quite clean and it has to be predictable now if you want to look at this for yourself you can find it with the city sample so you can look for the Houdini files in there now over here we have a typical

**11:37** · intersection in the city environment and you can just imagine that there are lines running along the roads like so and then if they intersect we have an intersection Point okay so this is where the lines are connected we can then break it down even further by cutting the intersections into these roads as well the intersections themselves scale

**12:03** · depending on the road width and the angles of the intersection so they need to provide enough space at the ends to um properly create sidewalks because otherwise they won't have the space to exist plus it creates a nice space for the Stop area where cars would wait it's quite useful actually so here we can look at it from above and we have again a road Network here of connections and intersections and then here on the left we have a couple of green dots and these are basically

**12:38** · corners so in the unreal City Sample Road segments are always straight and that means that any turn is basically treated like an intersection with only two exits but these don't need any uh stop areas like there and then if we look at the intersections again you can see how the intersections reserve some space on the roads around them but then in between we have these straight segments that are basically just one section of

**13:10** · Road it has a width that width does not change and it has a certain amount of lanes and a style okay so since this is generated in Houdini we can look at the files and check how they are constructed under the hood so over here we have the proxy geometry basically the roads but also the

**13:33** · highways or the overpass and the proxy buildings now if we have a closer look at that and we ignore the highways for a moment then here we have the proxy mesh for the road Network like I said the roads in this project are created for mod kits and these are basically all the models combined but if we look at it even deeper then we can see that all the sections in between the intersections are basically just

**14:01** · lines with a width and maybe a road type value and then if we look even further this is basically the network of roads that you get at the very beginning of the tool after this network is constructed but before intersections or mod pieces are placed in position and with this I'm basically trying to prove my point having a clean Road network of Curves is very important and the way how data on those curves is carried like in this case the road with is also important we

**14:34** · don't want to mess up that data however the unreal City sample is a procedural tool that generates the entire city from scratch from the road Network here up until the buildings from start to end meaning that we don't have to worry about users drawing roads that maybe won't work with our city but the moment we need to make something that needs to be editable it gets more complicated

**15:03** · so here is something that I've been working on this is a tool that I'm currently developing for an architectural company called immersa and I'd like to thank them for giving me permission to demonstrate a part of this tool for the workshop because I think it will help me prove my point so this here is basically a road mesh and it's constructed from a couple of different key elements

**15:28** · so first we have the intersections now these are quite complex to build and if you don't limit what kind of intersections and angles you can create like they did in the unreal City sample um it gets quite complicated however in their simplest form they simply require enough space to round a corner and they need to support the width of the roads that go into the intersection on all sides now in between we can create these

**15:58** · fillets or basically a connection that goes from one end to the other and then we fill it up with some geometry inside of the intersection Square now I'm not going to focus on this today but you can see here that intersections with different roads at different angles can get quite complicated and these are still simple intersections because they only have three or four exits they can get way more complicated real quick if you're not careful now next we have the road segments in

**16:33** · between and in this case they can round corners so at the very least I need to make sure that the corners of these roads have enough radius in order to allow the corners to exist properly especially when the roads get bigger when they get wider right um now you can also notice that we have a couple of side roads in here these don't create intersections instead they connect directly to the sides of a bigger Road like the orange one does here with the blue Road

**17:03** · now in order to construct the roads from these lines over here we need to have a couple of variables for example we need to know the road width right each Road has a certain width and we need to store that and I prefer to store them on The Primitives because The Primitives themselves describe the entire section of a road

**17:23** · segment if we were to store it on the points instead it could cause problems when we start combining roads or cutting them I'd prefer to store it on Primitives but we also might want to store other variables on them such as the speed limit which might differ depending on

**17:42** · the environment that the road is in and of course if we want to store a road name then that's going to be different for every Road in general right other attributes we wanted to store are elevation angle and Road grade and these

**18:00** · need to be included for um say if you don't want certain elements to be spawned on a steep road if you want to know where Corners are or just in general know how high a road is and all of this data needs to be maintained if you want to work with your road network if you edit it these attributes need to be kept now other information we can store are groups so we can for example here group intersections we could group every intersection with a single group or we can maybe differentiate between

**18:36** · these types of intersections with side roads and then the bigger main intersections as well and then finally we have Road Direction now the store Road direction we could use a Point Vector attribute on the points of this road that would aim along the road Direction but this will have to be constantly recomputed every time we change the

**19:02** · curves and this risks the curves being corrupted if you will so the thing is polyline Primitives already have a direction in their vertex order so if we look at these lines themselves you can see that their vertex order will follow along the direction of the curve each primitive starts at vertex zero and

**19:26** · ends on how many points it has so in this case we could say this line here has 11 points so it starts at zero and it ends at 10. right however working with vertex order isn't the most intuitive thing in Houdini because there is no way to view the curve directions by default you can only do it by looking at the vertex numbers here and also some tools degrade your curve

**19:57** · Direction like it's easy to flip a curve around if you start doing operations on it so we need to know what the curve direction is and we need to be able to edit it safely now for that I've been making a couple of tools and I'll be sharing those with you right here in this Workshop they're now part of the labs toolkit

**20:18** · so for the labs toolkit I've developed three new sub nodes which include the labs poly scalpel the merge splines node and the view vertex order node now these three nodes together are useful because they allow us to cut poly lines and services and then merge polylines back together which is great for roads because it

**20:42** · means we can cut them where we want them merge them back together the way we want them and we maintain all of our attributes our groups and our vertex order as well which is not something that the default nodes in Houdini can really do so what I mean with that is there is no simple way to edit Curves in Houdini there are a lot of nodes dedicated to editing curves but they all have some kind of downside or some kind of thing

**21:13** · you have to keep in mind for example the convert line and polypath node can be very useful if you want to segment or recombine a curve however they redraw the Primitive and this means that they will destroy primitive groups and primitive attributes when they are run so you always have to export those attributes to say the points and then re-export it back to The Primitives after you do these operations next to that the carve node will

**21:45** · disconnect all points when it segments things unlike the convert line node but it does maintain primitive attributes so there's a trade-off there right you have two nodes that basically do the same thing but there's something that doesn't quite work the way we want it next to that the polycut can cut on points but unfortunately when it does it tends to destroy Point groups so if you cut a point on a point group usually that point group only gets moved to one of the two points one of the two ends where the cut was made not both and

**22:21** · then next the result will node can resolve all your curves but when it does so it also redistributes the attributes and also Point groups in between so oftentimes when you store data on points in a curve and you run into a resample your attributes get Blended and that's

**22:42** · not something we always want to do right so it's actually really useful to store it on Primitives but these other nodes tend to destroy primitive groups so yeah you can easily see how this gets complicated right there's no straight way true editing a curve

**23:01** · and then next when it comes to cutting curves so not just using a poly cut on a point to cut at that point but maybe we actually want to inject a new point on an edge where there's no point right so there is no easy way to take a point and place it on top of the surface and then just inject it into say the edges of that surface there's no Standalone

**23:27** · node that does it for us similarly um slicing surfaces with curves is not easily done we can also often not preserve our Edge groups Edge groups are kind of like a third-rate citizen in Houdini lots of nodes do use Edge groups however they're easily destroyed and then finally we have the vertex order or the curve Direction and like I said there's no easy way to view that

**23:58** · so with the labs tool set I've included a couple of different notes the first one is the labs poly scalpel and this node basically allows us to slice new polygonal edges or points into the source geometry with a secondary cutting geometry and we can do this in various configurations we can do it with points we can do it with edges we can do it with surfaces

**24:24** · next to that it also keeps all the attributes and groups intact and it will propagate them through the cutting operation we can cusp the geometry and it will also allow it to deal with coincident faces depending on the method inside the tool that we use next I also have the labs merge splines node and this one allows us to merge

**24:52** · disconnected poly lines together like the pulley path soap cutting them at intersections but with specific conditions now this one actually keeps your primitive groups and attributes intact as well as the vertex attributes and the vertex order and then finally this one's called The View vertex order and it basically just visualizes the direction of each curve and it will create a arrow it will place it in the center of all the points on a curve

**25:22** · and it's basically a standalone component from the merged lines node so you can use this anywhere and quickly visualize your curve Direction okay so now let's dive into the example

**25:37** · files and let's first have a look at the example files for the poly scalpel okay so over here we have the example file for the polyscalpel node and over here I have two geometry nodes the top one has some examples of different types of cutting where we use different methods using the polyscalpel to cut our geometry and get different results it highlights how we can use the tool then down below I have some additional examples on how we can cut geometry and how it

**26:14** · compares to the existing types of cutting present within Houdini so let's have a quick look at that and the different functions of the node and then let's dive into the main examples I invite you to have a look through these files they should be included with the poly scalpel in the labs toolkit now the polyscalpel node is a multi-purpose node that can be used to cut new edges and points into geometry based on its different modes right now for example I am cutting a polygon surface using a polygon surface

**26:49** · and I'm using the poly split method this means that I'm basically using the pulley split node over here but it's constrained in such a way that it can run in a loop and it is a lot more reliable than as a simple node next to that we can also use the Boolean method this one is faster because unfortunately the poly split is not the most performant node and depending on which mode you use you

**27:17** · do inherit some of the limitations as you can see here but overall these nodes are able to work we can cut this geometry so in this case I'm cutting a surface with a surface if I move this around then you can see how the cut moves along with the cutting surface next to that it does also work with

**27:42** · coincident faces or overlapping geometry in this case I have these two boxes overlapping exactly and in this case I'm cutting the first box with the second box but only with its edges so in this case I've set it to polyline mode not polygon surface mode and this allows me to take the edges of the second box and even though they're overlapping exactly on the other geometry it will allow me to make a cut

**28:13** · and as you can see from the Primitive numbers this is reliable okay so next let's try to cut a box using just edges so instead of using the edges from this geometry let's just create a couple of Curves so in this case we have a couple of Curves here that are overlapping our box and based on their proximity they will either cut into the geometry new edges or they will add new points so as you can see these overlap

**28:45** · perfectly and this one here is a just approximate to the mesh so if I move this one it may or may not make a cut this is pretty useful because it allows you to create Precision Cuts along your geometry in whatever way you want to now it is important that your Cuts actually meet the edges of a surface if they are near the surface it will try to auto complete and if we want to instead of slicing the surface we can also decide to only inject points into the surface wherever our Cuts cross

**29:20** · an existing Edge so if we switch this to points on edges mode and we look at the point groups you can see that here we have some cuts that were made

**29:36** · moving on here we have a plane and we can cut it with another plane and in general if we have a high enough snapping value like let's say a value of one and I move this close enough to the other Edge it will snap and complete the cut

**29:58** · it is important that you set the snapping value correctly if you set it too high it may over snap now this snapping feature is only enabled when we are in poly split mode in Boolean mode which is the auto mode tool we don't have this behavior and in this case we do need to make a complete cut in this case the geometry has to either be exactly on top or overlap

**30:28** · but in fully split mode we do have the ability to auto complete our Cuts even if they are partial so in this case you can see that it makes the cut just fine now at the moment the tool is in Auto Precision correction mode and this basically means that it will try to look at the geometry its size and the size of your cutting geometry and create a reasonable snapping value this is useful to make sure that the poly split method doesn't over snap

**30:58** · if we turn this off however then now it will no longer make a proper cut and this is because it's collapsed or cut into the existing edges of the geometry so basically if you set the snapping value to high it may over snap and cause undesired results so you can control this and set it low enough so that it works or ensure you have Auto Precision correction enabled follow these instructions up here and you should get a reliable cut which

**31:30** · is useful if you want to use the tool procedurally and the rest of these examples basically demonstrate that we are able to cut our geometry using edges as well so over here I am cutting a surface with an edge and that works just fine or I can use a point so in this case I can take a point on an existing Edge or near an existing Edge

**32:00** · and then if I set the tool into polylines are cut with points because these are polylines I'm now injecting a point into this Edge and dividing it into two Primitives if I switched it over to a solid piece of geometry like this one I switch the tool into cutting pulling on surfaces with points and then look at the result again we've injected a point into this Edge

**32:33** · and added another Point into the geometry which is not a feature that Houdini has by default so there's a basic overview of what the tool is capable of there are more features here as well but if I go over everything this would take too long let's instead have a quick look at the Practical examples and what

**32:54** · we could potentially do with it okay so let's quickly have a look at a couple of examples on how we can actually use the polysyllable node in different configurations so let's have a look at this one here so this example actually demonstrates how we can cut a complex surface using a couple of simple shapes we start off with a floor plan and then I have some corridors that are overlapping that these are two meshes they are basically poly curves right

**33:28** · I overlap them and I set the tool into cross-cutting mode and cross-cutting mode allows me to cut using a hull from the original geometry basically in the cross direction of the geometry itself and it will then cut the other geometry with that we are currently in Boolean shatter mode meaning that it is cutting using a faster method but we can also cut using the poly split method if we want now this will inject new points and

**34:02** · edges into the geometry and also subdivider geometry into different Primitives let's group the central Corridor here this uh Central primitive and I do need to make sure that I have the right one selected right and then let's feed it into the next one so in this case I have some edges here and these edges are overlapping our

**34:28** · geometry but I have told the tool that it should exclude the corridor group we made over here meaning that it will now cut into this geometry but it won't cut the corridors so here we have a couple of lines that describe say for example the edges of a

**34:48** · room or the walls of a room right now the tool itself has snapping features enabled so even though my edges themselves don't perfectly overlap the geometry they do snap and we can use that to our advantage for example if I move this point and it will try to auto complete and create a cut like that

**35:15** · can be pretty useful then next let's say we want to add some points into these edges for places where support pillars should be located well if we were to grab a couple of points that are near the existing edges of our geometry we can then feed them to this poly scalpel which is configured into polygon surfaces cut with points we have a snapping distance which is visualized by this guide here

**35:45** · and then it will inject it into the edge we are using this group however to exclude one of the points from our cut so we're only cutting these points here and then finally I would like to add some doors now let's say these boxes here they represent the the space where a door should go well I have them overlapping the edges let's use the cutting mode points on

**36:15** · edges only and this will allow me to inject new points where this box intersects the edge but it won't actually cut the shape of the box into the surface which it would do by default it only cuts the edge

**36:34** · so with that if we then feed it through say a little procedural process we can create a couple of walls out of it and like create a little floor layout basically now there's something that you might have noticed and that's that we have some Edge groups over here and throughout the entire cutting process these were maintained so for example we created this first cut over here and created this Edge group throughout the cutting process this Edge group has been maintained and the same thing is true for primitive

**37:11** · group and my point groups and if we had attributes on here those would have been maintained as well so in other words the tool maintains your groups and your attributes throughout the cutting process so if we have say for example a couple of UVS on our geometry regardless of the cut they are maintained the same thing is true if we have some other attributes like in this case we have some attributes set up here

**37:43** · and throughout the cutting process they are redistributed depending on what type of cuts we made depending on what type of attribute it is but they are maintained like in this case for example this group here was maintained even though this box has been cut so having the ability to maintain attributes in groups means that we can make Cuts without having to worry about our existing information being deleted and finally as I mentioned we are also

**38:13** · able to cut polygon edges or poly lines with any of the existing methods so surfaces edges or points so in this case I have a simple curve object and I am cutting it with a plane and I've also for fun animated that plane so here you can see we're injecting new points into the curves we're also gusping this geometry using cusp cut points and when we do that that means

**38:44** · that we can explode the mesh maybe add some geometry where our cutting groups are our Point groups and there we go we have a nice little animation using the tool so yeah we have a lot of options here um I invite you guys to look through this in the workshop and then let's move on to the next tool which is the merge splind node because now that we know how we can cut geometry let's look at how we

**39:11** · can put it back together which is especially useful for Road curves all right so next let's go over to the merge splines node and also the view vertex order node and let's check out those examples but first let me introduce you to how this tool came to be so originally a few months ago maybe a

**39:34** · year I started working with a mentor student in my e Houdini Academy Mentor program and he wanted to create a race track and he needed to manage a lot of different roads now for that we started working together on this uh little tool I explained to him how we can make editors and how we could combine roads together but it quickly became apparent that these roads were very complex and he needed something more thorough so that's where the merge blinds node was born out of now what you see here is the final result he managed to turn this into a racetrack generator now he made this on

**40:10** · his own for a company called America Brands after we completed our Mentor sessions and it was able to create a very thorough race track with side roads parking lots main roads and the main connections between those roads were all managed by an early version of the merge spline saw but basically this is what

**40:32** · the road Network looked like when he was done with this racetrack and here you can see the node in action okay so here again we have the example file in this case for the merge splines node and I have several examples laid out here so you can see how you can use it let's first have a look at the node itself and what the icons here in the screen indicate to the user so the node actually has several functions but its main function is to take curves such as these and combine

**41:06** · them together based on criteria or merge conditions and then also manage the attributes that come with them so in this case I have several curves here that are supposed to be merged these do need to be connected and these are already connected now if I run that through the merge blind node you will notice that it starts showing several different icons on it the icons indicate different types of merging Behavior or the state of certain

**41:35** · curves so for example here you can see whenever you have a blue sphere it means two points were fused but there was nothing to merge if it's a green sphere they were fused and they were merged meaning that this primitive and that primitive were combined together if it's an orange sphere it means they were already fused but they were merged because they were already connected but they were two separate Primitives that could be combined into one

**42:05** · next up we have these arrows the arrows indicate the curve direction or the vertex order of this part of the spline and they will be visible on the center of each spline now the smaller arrows indicate the curve direction of the original curves so the original curves before this curve was merged into one curve

**42:26** · and finally we also have these little red arrows you can see and those indicate the end of a curve or if there was no merge made so basically if nothing else connects to the end point of these splines so now that we have an idea about what the tool does let's look at the individual functions one by one and then see what we can do with a more complex Road network over here I have an example which I'll go through in a moment where I have a series of Curves I can clean

**43:00** · them and then I can edit them or recombine them basically as a means to inject certain elements like these round corners and I can do that really easily while maintaining all of my attributes and groups now to do that you need to understand how the tool works so let's first dive into these examples here and have a look at that over here I have an example about how

**43:28** · Primitives can be merged so let's take this one here I have two lines and these lines come with a couple of attributes first we have the Primitive string attribute here which has ABC or this string on the left and Def on the right we also have the color which in this case is a primitive color and of course we have the vertex Direction which is inherent to these

**43:58** · curves now I'm viewing the vertex direction using this view vertex order salt which is the other labs node that I've included but if we want to merge these blinds normally if we were to use a polypath swap we wouldn't have a lot of control over which curve and its attributes are

**44:17** · used now with the merge spline salt this is quite easy all we have to do is feed these curves that emerge lines node and assuming they can connect they will merge together and all the attributes from one of the curves will be used for the entire curve so in this case I have snapped it using a snapping value up here if I lower this notice how the curves don't snap and if I increase the value you'll notice how the curves will start

**44:46** · merging now if I set the value too high the curves will start snapping to themselves and then you won't get a good result so if you want to you can also specify that it should only snap the end points or any endpoints and intersections so if that even our snapping value is very high it will still merge the curve into one now the way how it grabs the attributes from one of our two curves here determined by the Primitive merge Behavior we can specify that on the Node

**45:17** · over here so right now it's grabbing the attributes that is the attribute ABC and the color and it's grabbing it from the lowest primitive number we can also make it grab it from the highest primitive number in which case it gets grabbed from the second curve this one

**45:39** · now if we want to separately change the vertex order let's say we want to grab the attributes but not the vertex order we want to keep it going this way to the right and we can also specify that separately over here right now it's matching this parameter but we can also specify it separately

**45:59** · so let's say we use the attribute over here and use its alphabetical order to determine which vertex order it should ground if I set this to by attribute first value and then I specify it to the Primitive string then now you can see that since the perimeter string on the left was ABC and on the right was def it grabs it from this curve but the merge Behavior still tells it to grab the attributes from the second curve

**46:34** · and just like the vertex order we can also use attributes to drive the attribute promotion as well so over here I have a weight value on the blue line of four and on the red line I have a weight value of 1. so if I set this node

**46:51** · to use the attribute by first value the lowest value and I use the Primitive weight and now it will grab the attribute value from the left curve based on this weight value here not on the Primitive order so if I drop a sort node in here and I flip it around

**47:13** · then now even though the curves have a different primitive order it still grabs the attributes from the curve on the left because of its attributes being the lowest okay so let's move on because besides being able to merge attributes from Primitives we are also able to merge Point attributes as well so over here I

**47:33** · have an example where I have three curves and these curves have a couple of values so they have this string value here a b and c they have Point weights and they also have primitive weights and we can merge these attributes whenever points are fused together based on those attributes

**47:54** · so over here I am merging them Based On A Primitive weight and it's grabbing the last value so if I look at that I look at the Primitive weight it will grab it from the blue curve and when I look at how the points were merged here you can see attribute B was kept now this one is using a primitive attribute we can also use a Point attribute as well so in this case we are

**48:20** · using a point attribute to drive the promotion method if we look at the weights you can see that the highest value on our Point attributes is 5 and when the curves are merged it will grab the attribute from this curve because right now this point attribute is set to use the last value if I use the first value it will use the Blue Line because the blue line has a value of 2 over 3 and 5.

**48:47** · and with this we can have different types of merging Behavior we can use the point order or we can use for example the sum of all the points together and return that value so in this case that would be 1 2 and 3 becomes 6.

**49:04** · so yeah basic promotion systems all built into the tool now next over here we have the snapping behavior in this case we can determine how points should snap I have two curves and depending on which one I use it will snap to a different location in this case they're snapping to their average position we can also snap by Point number or buy an attribute value

**49:32** · or in this case we can snap by a Target group so the points will always snap to that point if they are merged now if we want to merge a couple of Curves but not everything like in this case for instance we can use a fuse filter and only fuse points that were selected in this case these two points were selected so when I use those it will only combine these and

**49:58** · leave this curve alone likewise we can also use this by attribute so I can tell it to only snap curves together that share the same attribute in this case this one has ABC and this one has Def and only these two because they have matching attributes can merge so this is also again very useful if you want to make sure only certain curves are merged together

**50:25** · and then finally let's have a look at how we can use that filter to limit our operations and only affect curves we actually want to adjust and when I go to the final example for the roads this is very useful so over here I have several curves and they're all being combined together at least as long as they are within this filter here they can snap these two cannot so they are kept apart but because these were already connected they are also merged into one curve you can see there used to be two curves now that one now in case I only want to merge points

**51:00** · that are in my selection like in this case for example where I have a group selection on this point and I only want to merge those I can turn on only merge on huge filter selection when I do that only these two curves are merged and these are left alone they won't be processed and they won't be altered in any way so this is pretty useful if you want to limit your operations to only a certain set of your Primitives

**51:30** · now in another case like this one I have only combined these two curves and these two based on a shared attribute so right now these have the attribute ABC and these have def these could also be numbers they're not limited to Strings and if these attributes match then it will merge them now if I disable these options it will merge everything into one

**51:55** · because of the snapping distance so we have a lot of control over this now I mentioned that we can use a fuse filter let's get this example over here where I have a very large network of connections and if I want to merge these it's actually quite heavy because I'm running a lot of operations at once If This Were A Road Network or a maze like

**52:19** · in this case um it would take quite a lot of time to merge these together now let's say we want to make this run a bit faster we can what we can do is we can create a group for say all our points that have two connections so no intersections but only straight

**52:39** · pieces of curve that consist out of separate Primitives well we can group those and then we can run them through a merge blind cell with a simple fuse filter selection we can then run fusing operations only on specific parts of our geometry and by doing this we are only executing

**53:03** · this operation on a subset of our geometry the rest is left alone and this is a lot faster which is useful if you want to only connect very specific parts of your network together but leave the rest of your network completely untouched in some cases that's necessary and this facilitates that so now that we've had a deeper look at the emerge blinds node and the polyscalpel let's see how we can use them in practice when we want to edit a couple of Roads so over here I have the workshop example file in this I have two examples one for

**53:39** · cleaning Road curves and one for creating a road mesh from those curves and combining different sets of meshes together so you get one single coherent mesh now there are different ways to create roads this is just one of them but you can take some of the practices from this example and use it for yourself now let's get started um first I would like to say that these

**54:05** · examples especially example two um are partially facilitated by imaza which allowed me to use part of my road Builder I made for them now let's have a look here first we have this road Network here let me change the color and these are a series of curves that form a road network but as you can see

**54:31** · they aren't completely clean first some of these curves are disconnected and are actually facing in the opposite direction from one another even though this is arguably a single Road next some other curves span multiple intersections and aren't cut properly

**54:51** · and this one does share the same direction but is cut in the middle so we want to clean this now it is important that these curves do meet on their points and I also have a couple of groups in them but I'm not going to use those right now okay so first let's see what we can do with this problem here and also clean the other issues that I just mentioned so what I would like to do is take the

**55:21** · curve that's the longest in this case and take its vertex order so in this situation this curves vertex order is used and overtakes this one we can do that by measuring the perimeter of this Edge and if we were to visualize that plug that in we can say perimeter

**55:54** · and then you can see that this one has the largest perimeter of about 400 meters and this one's 200 meters so if we sort by that now this one will be the highest primitive number and that one will be the lowest so let's run that through the merge blind node here what I'm gonna do is tell it to use the vertex order by the last value for the perimeter and when we do that it's going to use this curve and

**56:25** · overtake its direction and combine it right there next to that some of these other curves that were disconnected before are now combined so here's one and all the segments on these curves here are now segmented by their intersections because this node is being run on the entire geometry all at once all the intersections will be cleaned at the same time and you'll notice that we do have some guides indicating that some points were snapped or fused and that's because they were also disconnected so now we have a

**57:02** · fully recombined Road Network that has been cleaned and we can proceed then down here I have two examples so let's say we're going to edit our road Network and we need to post process it to make sure it still makes sense after we're done editing it so let's remove a couple of these uh curves here

**57:27** · now as a result over here we have a single Road which consists out of two separate segments with two separate values and curved directions if I visualize my road width for example you can see that this is a road of 35 meters wide and this one is 20.

**57:47** · now the problem with that is that if we want to support that in our road builders we need to make sure that our roads can transition from one road size and one road style into another without joining at an intersection that might be a problem so we have to

**58:03** · keep that in mind or we have to fix it now we can fix that quite easily by using a merge client node we can plug it in and if we merge the Primitive attributes and vertex order by the last value in the road with then the largest Road will always overtake any smaller roads that are merged together so we can use that to clean this up as you can see we now have one segment here with one curve Direction and one

**58:31** · size now in case we do want to use these as separate curves we can do that we can specify that we only want Primitives that have the same value to merge so if we set our road width over here then now it will only merge

**58:52** · these curves up here but leave these alone because these don't have the same route width so they cannot merge so we have control over this and depending on your needs depending on what your road tools are supposed to do and what they can support you can configure the tool appropriately okay so we can easily use the merge blind swap to clean curves that connect and have different attributes but let's say we want to cut some of these curves and then inject new segments in between and when we do that we still need to

**59:27** · make sure that we recombine them to valid route curves so over here I have a situation where I have a couple of very sharp angles because I've removed this curve here now if we were to try and sweep these and I can demonstrate that let's go down here grab our sweep node

**59:51** · plug that in and I'm going to add a merged spline salt to fix these lines up make them continuous if I sweep that you'll see that we do have some Corners here but they're so sharp that the geometry self-intersects and in general this wouldn't make a very good um Road turn right

**1:00:17** · now if we don't use the merge blind salt in this case it will be disconnected and we wouldn't even have a continuous Road segment so we do need to fix this what I would like to do is turn into something more like this where we have a rounded term that works well so to do that what we want to do is first mark off all these sharp angle points so I'm going to show you my point groups and I'm going to use a little expression

**1:00:49** · here to grab any intersections and sharp Corners as well so any Corner that is sharper than 65 degrees is going to be selected that's based on the curve directions that come out of each point then next let's unique all of the intersections in our Network and I'm going to grab my Corners here and I'm going to expand their group I'm going to expand it by a couple of steps in this case I'm just going to

**1:01:20** · grab it from this corner outward and move it across the points for about nine steps then let's promote that to an edge group and what that will do is we'll turn it into an edge group selection and then we can use a polycut here to cut it out so pretty straightforward on the left we have the original Network cut out on the right we have the fully cut of course we could use the poly scalpel

**1:01:50** · node specify a couple of points on these curves and then say cut splines with points but this works too all right so in this case what I want to do is take these segments that I've cut out and just like I showed you before I want to re-merge them into single segments because we do need to run these through a nurbs operation to then turn them into proper curves

**1:02:19** · so I'm going to resample them at a lower resolution you run into a nurbs operation and then resample them again that will give us some nicely rounded corners finally let's take the outermost points the ones with only one neighbor and let's group those

**1:02:40** · so now we have that we can recombine everything and now we need to merge these curves back together now these curves do have a Vertex order as you can see here and in some cases these will conflict so we need to resolve that we can again use a merge splines node combine it all together but if we run this on the entire network

**1:03:06** · then this might become a bit heavy if this network were 10 times the size it will become a bit slow and we'd be running a lot of unnecessary operations we only really want to inject these Corners in here right so instead let's use a fuse filter with a only merge on fuse filter selection mode enabled if we do that then only these turns here are going to be merged and the rest of

**1:03:36** · our network will be left alone and this is a lot faster so with this if we run that through a sweep node then now we'll have some proper curves proper curvature no self intersection and they're continuous right we have One

**1:03:57** · Direction one attribute everything is clean now in this case you might have noticed that these aren't proper intersections now I haven't included my intersection code in this example but I have provided for example two a couple of the outputs from my bigger row tool and you can see here is a road Network and this one has been cleaned then I have some intersection meshes

**1:04:27** · that intersect basically between these lines and they have correct widths based on the road width of each line and then finally I have a couple of fillets these little pieces and these can be used to merge roads together where they meet So eventually we'll get this road Network here and for intersections it will look something like that

**1:05:01** · okay so how do we get to this point first here is my road Network let's look at just the curves and first I would like to cut these networks where the intersections occur so from the intersections I can extract these edges and these are just polygon edges that describe where the intersection ends

**1:05:30** · and if I run that through this polyscalpel I can cut polylines with polylines and it will cut the roads right there at the intersection then next let's remove the road sections that are inside the intersection by using a XYZ disk on the original intersection geometry so we have this shape here

**1:06:00** · if we just run a XYZ disk from its Center position and if that is less than a certain amount and the point on this line is a intersection point which we have grouped using this node then we can mark off that this is a intersection point on a mesh

**1:06:24** · so you can see here this point here is now marked let's promote that up and we promote it to the Primitive so now these are marked as being on a mesh and then we can remove them so basically first we've cut our curves and then we removed the section in the

**1:06:50** · middle that was overlapping our intersection moving down I'm just going to run this through a sweep operation we're going to get the orientation the up Vector and the side direction of each line and uh from there we sweep it

**1:07:12** · so now we have a couple of ribbons basically rolled ribbons but we still have these side roads now these side roads didn't actually generate with their own intersection they can maybe generate intersections with one another but they don't do that with the main roads these are secondary roads and these are primary roads

**1:07:32** · in this case they don't form an intersection so we have nothing to cut it with now we don't want these roads to intersect of course so we need to fix that now to do that first let's use a split node to split our primary roads out from our secondary roads

**1:07:50** · so on the left we have the output with just the secondary road on the right we have our primary roads I'm then going to remove all the edges from our primary roads and only keep the outer shared edges and let's run that through a poly scalpel in this case I'm going to cut polygon surfaces with polygon surfaces and use the cross cut mode and this will give me a cutting shape

**1:08:20** · or a cookie cutter basically that will cut this curve right here now let's display the edge groups right here we have a seam

**1:08:35** · so that's now cut these curves and it's also injected points based on the geometry of these roads here so you can see we now have points right there which means that it will match the main road geometry wherever this cut was made then we can simply check again if these sections overlap a road and remove them

**1:09:02** · okay so now that we've cut our side roads and they no longer intersect we can now merge them back together with the main roads but in order to do that properly we need to make sure that the main roads also have points in them that correspond to the side roads otherwise we'll have gaps in our mesh for example here you can see how the Side Road has been cut based on the main roads points

**1:09:30** · but the main road does not have points based on the side road so we also need to inject some points into the main road to make sure they can connect properly first let's run a couple of fuse operations at a reasonable snapping distance to get rid of any points that might be too close together then I'm going to extract The Edge so

**1:09:55** · here I'm going to use a edge group to curve node which is a Labs tool I've in this case simply extract a bit um and then we can run that through a couple of operations to create a cutting shape now with this shape we can overlay it on the main road and inject some points so there we go we now have points that match the side road and that should now work properly if we want to connect them

**1:10:28** · together because now both roads match each other let's do a bit of snapping again transfer some groups and connect it together so there we go as you can see these are properly connected together because the edges indicated by this blue line

**1:10:46** · um show that there's no seam in between and then finally I would like to add a fillet in between this little section here I already have that so over here I have the fill it and then if I look at this blast node you can see that we have some points I just want to take the outer

**1:11:07** · corners of this fillet and combine them into the main road so we can just use those use a polyscal plugin and inject those points and then we can merge it all together so yeah as you can see we now have a clean complete route network with no seams and we can use that to grab for example the outer edges create some sidewalks from that or do

**1:11:42** · whatever else you want to do with this road Network and with that I just like to say thank you for watching this Workshop um if you want to watch more of my tutorial videos feel free to go to my YouTube channel at euddini Academy or visit my website at euddiniacademy.com you'll be able to find the links to the master class and the example files for the masterclass right there

**1:12:08** · and of course if you want to join the eugudini academy Discord Community feel free to join us at this link I have over 300 people on the channel I regularly post progress updates there as well as on my patreon account as well so if you were to back me on patreon you're going to get some benefits from that some

**1:12:27** · people such as the mentoring and student tiers they get guidance on this chord and for the rest feel free to check out my patreon channel for other information and of course it helped me create more content such as these tools or more video lectures for the Master Class

**1:12:47** · so with that we've come to the end of this presentation I'd just like to thank side effects software for giving me the opportunity to host this Workshop and other than that thanks for watching and see you out there have a good one