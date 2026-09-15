import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const offers = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/offers" }),
  schema: z.object({
    title: z.string(),
    order: z.number(),
    epics: z.array(z.string()),
    distinctiveness: z.number(),
    risk: z.number(),
    cost: z.number(),
    priority: z.number(),
    hypothesis: z.string(),
    round: z.string(),
    source_commit: z.string(),
  }),
});

const pages = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/pages" }),
  schema: z.object({
    title: z.string(),
    source_commit: z.string(),
  }),
});

export const collections = { offers, pages };
