---
title: "Art of Rally low-poly look, one readable silhouette per unit type"
order: 9
epics: [E-18]
distinctiveness: 2
risk: 2
cost: 3
priority: 1.3
hypothesis: "H12: in a screenshot preference survey, the game's look is preferred over two reference styles by a majority; every tester can name the six unit types from silhouettes."
round: "2"
source_commit: e10649a13c6681968dec563f525ea71160a8d606
---

## Why this is here

Low-poly, Art of Rally: flat shading, clean silhouettes, the shape is the information. Six unit silhouettes that persist across every era so a Raider reads as a Raider whether it is a dart of a ship or a longboat. Three tiers that read at tactical zoom in three words each: boxy, seamed, matte; smooth, integrated, polished; flowing, luminous, abstract. Combat that conveys mass: nothing snaps or pops, hits bloom slowly, dead ships drift. Four attack visual categories and three ability overlays that every era skins from a manifest without new rendering code. Menus and transitions animated from simple elements composed with precise timing.

The era-agnostic rule holds here as everywhere: the engine emits abstract events and state; the era manifest maps them to look.

## What it feels like in a 60-second session

Put one of each unit on screen at Tier 2: six silhouettes distinguishable at tactical zoom, Strike smallest and Siege largest, Bastion wider than long, Bombard longest. Fire a Raider at a Vanguard: a projectile with a trail travels, an impact burst drifts out over half a second, the Vanguard blooms warm for a third of a second, no shake. Kill it: a death flare, fire and sparks, a slow drift along its last heading, darkening over 3 to 5 seconds. Pop Barrage: a warm ring telegraph, then a heavy volley. Swap to a Tier 1 manifest: the same units, boxy and painted.
