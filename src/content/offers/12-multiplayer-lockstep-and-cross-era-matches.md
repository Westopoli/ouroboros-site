---
title: "Multiplayer lockstep and cross-era matches"
order: 12
epics: [E-19]
distinctiveness: 3
risk: 3
cost: 5
priority: 1.8
hypothesis: "Not testable before Round 3. The determinism contract is built regardless (E-02 S-020). The research says the tribe has no unified multiplayer demand and single-player-first is fine."
round: "later"
source_commit: e10649a13c6681968dec563f525ea71160a8d606
---

## Why this is here

Ouroboros Manifold is a multiplayer strategic RTS. Every peer runs the same deterministic C simulation and exchanges only commands, so a match costs nothing to host and every player sees one galaxy and one battle. Matched players who all own the same era packs can play a match that traverses eras chronologically. What a match is, who commands what, and how the single-player generational loop becomes a shared one are the questions this epic exists to get answered.

Vision facts this epic must honor: full real-time, no pause in a match; the civilization has its own plans (agents run for every faction including human-commanded ones); bloodline and lineage are cosmetic; cross-era matches require the same era packs on every peer.

## What it feels like in a 60-second session

Two machines, one seed, one command stream captured from a 5,000-tick strategic run and a 5-minute tactical mission: byte-identical traces and checksums on Linux, Windows, and macOS. Two peers over the relay: a command issued on one appears in the other's tick delta on the same tick number, and a deliberately corrupted checksum on one peer is reported as a desync within 10 ticks.
