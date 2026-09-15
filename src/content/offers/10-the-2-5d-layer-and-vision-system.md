---
title: "The 2.5D layer and vision system"
order: 10
epics: [E-01]
distinctiveness: 5
risk: 5
cost: 5
priority: 5.0
hypothesis: "H7: with the option chosen in the layer design phase, at least half of losses are attributed by the tester to layer reading; cross-layer vision is described as a rule they used, not a surprise."
round: "3"
source_commit: e10649a13c6681968dec563f525ea71160a8d606
---

## Why this is here

The layer system is the game's strategic defining characteristic. The battlefield is not a flat plane. It is a stack of three to five vertical layers, and a unit is always on exactly one of them. Terrain blocks layers at specific places, so a force can go over an obstacle on a high layer or around it on a low one. Vision across layers is worse than vision on your own layer, so a force on a layer you cannot see is a threat you do not know about. Changing layers costs time and leaves the unit briefly vulnerable.

The promise this keeps for the player (vision_v2 Q6): a smaller force that understands surrounds, high ground, and layers beats a larger force that does not. Every rule below exists to make that promise testable.

Era-agnostic: the engine knows "layers 1 and 2 are blocked here." The era pack decides whether that is an asteroid, a mountain, or a reef. Launch ships the Settled Reach with no per-unit-type layer restrictions.

## What it feels like in a 60-second session

Spawn a Raider and a Bastion on layer 3 next to a tall obstacle. Order both to layer 5. The Raider rises visibly within a second, the Bastion takes several seconds, and each unit's ring changes color when its layer changes. Place an enemy on layer 1 under the obstacle: neither unit sees it. Move an enemy onto layer 4 within half the Raider's sensor range: the Raider sees it, the Bastion does not until it is closer. Fire a pulse: the layer-1 enemy appears for two seconds, then vanishes. Order the Raider to layer 1 through the obstacle: it does not change layer until it moves clear of the blocked zone, then drops.
