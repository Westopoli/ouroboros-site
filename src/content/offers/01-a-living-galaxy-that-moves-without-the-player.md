---
title: "A living galaxy that moves without the player"
order: 1
epics: [E-02, E-03, E-04, E-05, E-07]
distinctiveness: 5
risk: 3
cost: 2
priority: 7.5
hypothesis: "H1: after the first time jump, at least 70 percent of testers name a galaxy change they did not cause, and call it interesting rather than random."
round: "1"
source_commit: e10649a13c6681968dec563f525ea71160a8d606
---

## Why this is here

Every region in the galaxy carries four numbers that say how it is doing: military strength, economic output, factional tension, and population. Two derived numbers, stability and capacity, summarize them for everything that makes big decisions. Every tick, slow forces move the four numbers a little: armies cost money, people make money, hardship breeds unrest, unrest hurts production, prosperity grows population. Under those forces a healthy region hums along, a stressed region slides, and a region at the bottom spirals unless someone outside helps it.

This is the ground the whole simulation stands on. Events, factions, missions, and the chronicle all read these numbers. The player never edits them directly; missions do. The equations are retained verbatim from the Python sim (`algorithms.md`), and the C rewrite must reproduce them to the bit.

## What it feels like in a 60-second session

The technical end-state: what a fixed-seed run proves when this epic is done.

Run one region alone for 300 ticks from population 60, economy 66, military 42, tension 18 with a fixed seed. Economy climbs toward the mid-50s then oscillates with a 15-tick period; tension settles into a low equilibrium with an 18-tick wobble; military decays a little then recruits back and holds under 90; population creeps up. Run it again with the same seed: every number identical to the last decimal. Cut economy to 9 by hand: tension climbs, population falls, and it does not recover on its own.
