# DESIGN.md — Ouroboros Manifold site

Look-and-feel brief for the *Ouroboros Manifold* site (`ouroboros-site.fly.dev`). This is a creative brief, not a rulebook: it gives you the game's identity, the raw material, and the current structure, and then asks you to **explore**. Nothing here is locked. Push it — polished, cinematic, aspirational directions are wanted. Where this brief and a better idea disagree, bring the better idea.

## The one hard rule

**No existing intellectual property.** No names, logos, insignia, ships, characters, or plot from any existing franchise (Star Wars, Halo, Stellaris, anything). Thematic inspiration only — never copied or recognizable content. Everything else on this page is a starting point you are free to move.

## What this site is

The public face of *Ouroboros Manifold*, a multiplayer, generational, strategic real-time-strategy game set in a living, stochastic galaxy. Today it recruits and orients a small group of playtesters — but those testers are early customers, and this site may grow into the marketing site. Design it as if it could carry that weight: it should be able to sell the game, not just brief a tester.

Its job is to make someone *feel* what this game is and want in. Explore the full range — an intimate invitation, a bold marketing landing page, or anything between. **Mockups are the point.** Aspirational, mocked-up "screenshots" of the game, hero renders, in-context UI, imagined moments — all welcome and expected. This is exploration; there are no limits right now.

Current pages: Home, Offers, an interactive layer demo, and a Roadmap. Treat these as the starting structure, not a boundary — propose new sections, heroes, or flows if they serve the game.

## What the game is (the raw material)

Use this as the source you design from — lean into whatever resonates.

- **Commander, not king.** The player is one person handed a task force and an impossible job by a civilization with its own plans. The world does not revolve around them; it moves on its own. Not a god game, not an empire manager — you are *in* it.
- **Generational.** A chain of missions across decades. Between chapters, time jumps and the galaxy evolves through the simulation; the player returns as someone new — a descendant, an old enemy's heir, a stranger. A civilization's rise, crisis, and potential fall, experienced from inside.
- **A living, stochastic galaxy.** A genuinely uncertain simulation turning underneath the strategy — factions rise and fall whether or not the player acts.
- **The tragedy of understanding.** Mastery is knowing *why* you lost. You can read the situation, make the right call, commit, and it still might not be enough — because the world is too big and too alive for one hand to hold.
- **Positional skill, turned up.** Full real-time combat, no pause; surrounds, high ground, and a 2.5D layer-and-vision system push positional skill past the genre's bar.
- **One skeleton, many eras.** Maps, civilizations, and eras are transferable systems; players who own the same eras can meet on one shared map. The near-future *Settled Reach* is the launch setting.

**Tone available to draw from:** elegiac, not grim — the feeling of a real history being recorded, with tragedy, dry earned humor, beauty, and unexpected hope. This is a *register you can reach for*, from quiet and intimate to vast and cinematic — not a mandate to be subdued. Range is welcome; a marketing hero can be bold and still feel like this game.

**Reference points the game itself cites** (for feel, never for copied assets): StarCraft 2 (combat feel), Halo Wars / AoE3 (large battles, force handling), Immortal: Gates of Pyre (accessibility, low floor / high ceiling), **Art of Rally (the look — low-poly, stylized, clean silhouettes)**, Halo: CE (world-building and generated music).

## The look of the game

The game's own art is **low-poly, blocky, toy-like — flat and warm**, in the *Art of Rally* register: clean, readable silhouettes, one per unit type, a cinematic sense of scale behind the action. This is the game's visual DNA and a rich well to draw the site's imagery from. `docs/northstar/mvp/site/prompt_kit.md` in the `ouroboros-manifold` repo has the exact concept-art register and per-offer prompt lines; Westley will also provide low-poly game screenshots as reference.

Note the freedom here: the *game* is low-poly, but the *site* can be as slick, polished, and cinematic as you like. A low-poly game can have a gorgeous, high-craft marketing site. Explore that contrast.

## Color — starting point, open to explore

The site currently runs a warm, dark palette. It's a good starting identity; extend it, evolve it, or propose a bolder direction — this is not a lock.

| Token | Value | Current use |
|---|---|---|
| `--bg` | `#0d0f14` | Near-black blue ink background |
| `--bg-raised` | `#161923` | Cards, panels |
| `--fg` | `#e8e6df` | Warm cream text |
| `--fg-dim` | `#9a9aa6` | Secondary text |
| `--accent` | `#d98e3a` | Ember — the warm signature color (lamplight, the glow of a chronicle at night) |
| `--border` | `#2a2e3a` | Hairlines |

Warm-and-dark reads as the natural home for an elegiac, history-of-a-galaxy feeling, and the ember accent is a strong, ownable signature. But treat all of it as a hypothesis to test against your mockups — introduce faction colors, a cool starlight counter-accent, richer gradients, a brighter marketing variant, whatever the design calls for. Show options.

## Typography — a direction to try

The site currently uses a system sans. Worth exploring a **pairing**: a warm serif or characterful display face for titles and any chronicle / in-universe voice (it carries the "recorded history" feeling well), against a clean humanist sans for body and UI. This is a suggestion to prototype, not a requirement — propose the type that best sells the game. Self-hosting fonts keeps the static site fast, but that's an implementation detail, not a design limit.

## Structure & pages (current shape)

Design these; reinvent or extend them freely.

1. **Home.** The first impression — say what the game is and make someone want it. A strong hero (the strategic galaxy, a commander's moment, the low-poly fleet — your call), a distillation of the fantasy, a taste of the distinctive offers, a pull toward the demo, and a clear call to action (join the playtest / follow along). Range from restrained to full marketing hero — show a couple of directions.
2. **Offers.** The game's distinctive bets (pulled from `distinctiveness.md`) — a grid or gallery, each with a title, a hook, and room for a mocked-up image that sells that idea. A detail page per offer (`/offers/[slug]`) goes deeper: the pitch, imagined art, the systems behind it.
3. **Layer demo (`/layers/`).** Frames a live interactive three.js demo of the 2.5D layer-and-vision idea. Design the chrome around a live canvas so it feels like a real, exciting piece of the game.
4. **Roadmap.** Where the game is going — as a table, a timeline, or something more visual. Can be honest and still be compelling.
5. **404** and shared components: nav, hero, offer card, image/figure treatments, call to action, footer.

## Imagery & mockups

This is the heart of the exploration. **Create the imagery the game deserves and doesn't fully have yet** — mocked-up game screenshots, hero renders, in-context UI, cinematic key art, the strategic galaxy map, a tactical moment, the low-poly fleet in formation. Show the game at its best. Aspirational mockups are exactly what's wanted; they don't need to be captured from a shipped build.

Draw imagery from the game's world: a galaxy of small systems joined by glowing routes (bright and thriving, dim and contested — a living network); the generational carry-forward of a place changed by time; a tactical surround through a chokepoint; the six low-poly unit silhouettes. The **living-network / galaxy** motif and the **ouroboros loop** (generation feeding into generation) are both strong visual ideas to build heroes, backgrounds, and dividers around — go big with them if it works.

The only imagery limit is the hard rule above: no existing-IP ships, insignia, characters, or logos.

## Motion

Open. A cinematic hero, a drifting starfield, a galaxy that quietly turns, reveal transitions — explore ambitious motion where it strengthens the feeling, and keep a graceful reduced-motion fallback as good craft. Nothing here is off-limits; let the mockups show what motion could do.

## Craft baseline

Not constraints on creativity — just the floor for a shippable result:

- **Astro static site**, deployed on Fly, scales to zero; the three.js layer demo is the one heavy interactive piece, isolated to its page. Favor fast, mostly-static output.
- **Responsive** — many testers open the link on a phone; everything should work beautifully from phone to desktop.
- **Accessible** — good contrast, keyboard navigation, real focus states, alt text, `prefers-reduced-motion` honored.
- The offers/home/roadmap copy is pulled mechanically from the game bible (`scripts/pull_content.py`), so **style those content areas; the words in them are generated**. Design freely around that shape.
- The site is currently private/unlisted (`noindex`) while it's a playtest — a fact about today, not a design constraint. Design it to be marketing-ready for when that changes.

---

*Companion inputs, alongside this file:* the live site (`https://ouroboros-site.fly.dev/`), the concept-art register (`docs/northstar/mvp/site/prompt_kit.md` in `ouroboros-manifold`), and the low-poly game screenshots Westley provides as visual-register reference. This file is the identity and the invitation; the exploration is yours.
