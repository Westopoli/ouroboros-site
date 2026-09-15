---
title: "Single-layer positional skill ceiling: surrounds, terrain, soft rock-paper-scissors"
order: 8
epics: [E-11, E-13, E-12, E-17, E-14]
distinctiveness: 4
risk: 3
cost: 5
priority: 2.4
hypothesis: "H6: in a fixed scripted scenario where the tester's force is smaller, at least half of testers who attempt a surround win, and they describe positioning as the reason."
round: "2"
source_commit: e10649a13c6681968dec563f525ea71160a8d606
---

## Why this is here

Six unit types, two per category, on a soft rock-paper-scissors: Strike flanks Siege, Siege crushes Line, Line absorbs Strike. Every unit has stats, exactly one ability, and a role nobody else fills. Damage is flat: base damage times a category multiplier, no falloff, no cover reduction. Fights last long enough to read and retreat from; HP, not damage, sets the tempo, so flanks resolve first, the center grinds, and Siege duels last longest. Every unit on both sides runs the same three-check decision loop: flinch from what you cannot fight, obey the player, shoot the nearest thing in range. Abilities are the mastery layer: ignorable by a new player, decisive in skilled hands, every one a commitment with a tradeoff.

The numbers below are the Tier 2 Settled Reach baseline; they are tuned by headless simulation, not by hand (Stage 1 A-261).

## What it feels like in a 60-second session

Spawn 10 Vanguards versus 10 Raiders at 250 wu apart on layer 3 and attack-move both. The Vanguards win with 5 or more survivors; the fight lasts at least 45 s. Swap the Raiders for 10 Bombards at 1,000 wu: the Bombards kill the Vanguards before they close. Send 4 Raiders around the flank into 4 Bombards: the Bombards die. Pop Surge on a Raider: it moves at 375 wu/s and hits for 18 for 3 s, then cannot Surge again for 75 s. Same seed, same fight, tick for tick.
