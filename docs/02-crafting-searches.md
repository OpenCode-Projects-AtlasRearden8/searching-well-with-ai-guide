# Chapter 2 — Crafting Searches That Find the Good Stuff

*The chatbot answers whatever you said. The search engine answers whatever you
*typed* — and typing it well is a skill worth about ten minutes to learn.*

## The three-question pre-search check

Before you type, spend ten seconds:

1. **What exact words would appear on the page I want?** Search engines match literal text. "refund policy" appears on policy pages; "how do I get my money back" appears on forum rants. Search for the first.
2. **Who publishes the page I want?** A hospital, a government (`.gov`), a university (`.edu`), a company? You'll use that below.
3. **When did it need to be true?** You'll add a date filter (Chapter 5).

## Operators: the whole list you actually need

You don't need twenty operators. You need six.

| Type | What it does | Example |
|---|---|---|
| `"quotes"` | Match the exact phrase | `"w-4 form 2026 instructions"` |
| `site:` | Search one domain or domain type | `site:cdc.gov hand washing guidelines` |
| `-word` | Exclude a word | `jaguar -car` |
| `filetype:` | Find documents | `filetype:pdf apartment lease checklist` |
| `after:` / `before:` | Date-bound results (Google) | `best bassinets after:2025-01-01` |
| `OR` | Either term (in CAPS on Google) | `(resume OR CV) template nurse` |

Combine them freely:

```
site:.edu filetype:pdf "study skills" workshop
"order of draw" site:cdc.gov OR site:who.int
```

## Queries that change your results quality immediately

- **Search the error, not the frustration.** `python KeyError 'status' pandas merge` beats `program keeps crashing when working with data`.
- **Search for the document, not the topic.** `filetype:pdf "food handler" certificate texas` beats `how to get a food handler card in texas`.
- **Search the site you'd trust by name.** `site:mayoclinic.org sciatica exercises` beats `best sciatica exercises` (which invites content-farm listicles).
- **Put the year in when freshness matters.** `best free accounting software 2026 small business` beats the un-dated version, which surfaces old listicles.
- **Use one "OR" branch for synonyms.** `(keto OR low-carb) meal plan beginner` — catches results whichever word the good pages use.

## Reading results like a pro (30 seconds per page)

1. **Read the green/grey URL first**, before the title. Titles are clickbait; URLs are identity. Is that really `irs.gov` or `irs-gov-help.info`?
2. **Trust structure, not sizzle.** Pages with citations, dates, and an author name beat pages with ten autoplay ads.
3. **Prefer the "advanced" tab of search settings** — you can permanently force "past year" there.

## When to stop searching

Three good tries and you have nothing? Flip back to the chatbot and ask it:
*"I'm looking for [X]. What's the technical term or official document name for this?"*
Then search that new term. Chatbots are excellent at naming things; search engines
are excellent at finding named things. (See the hybrid move in Chapter 1.)
