# Chapter 3 — Ask AI for Sources, Then Verify Them

*Chatbots confidently cite papers, studies, and pages that do not exist. This is
called “hallucination,” which is a polite word for “made up.” Here's the routine
that catches it in under two minutes.*

## Step 1: Ask for sources — properly

A lazy ask gets a lazy answer. Try these prompts, in increasing strength:

- **Basic:** *"Which sources did you base that on? List them."*
- **Better:** *"List every source you used, with publication name, date, and a link if you can. If you're not certain a source exists, mark it with (NOT VERIFIED)."*
- **Strongest:** *"Answer, then list sources as a table: claim you made | source name | date | link. Mark any source you cannot fully confirm as NEEDS-CHECK so I don't mistake it for real."*

The strongest version asks the model to *separate* what it's sure of from what it's
guessing — and models are surprisingly honest when you give them an explicit slot
to admit uncertainty in.

## Step 2: Verify — the two-minute routine

For each source the AI gave you (do these in order; stop when you're satisfied):

1. **Does the link open?** A dead link is a red flag that the citation was invented. Copy and paste the title into a search engine instead: `site:journalname.org "exact article title"`.
2. **Does the source say what the AI said it says?** Open the page and Ctrl+F for the key phrase. This is the single most important step. Chatbots often cite *real* papers but *misstate* what they found.
3. **Is the date right?** A 2019 study presented as brand-new research is a different fact. Use the date-check habit from Chapter 5.
4. **Is the source the right *type*?** A blog post citing a study is not "a study." If it matters, go to the primary source: the paper, the agency page, the dataset.

## Red flags that a citation was invented

- The author names are plausible but the **journal or website isn't findable**.
- The **paper exists but the page number, year, or quoted sentence is off**.
- Mixed-up citations: the quote sounds like the *topic*, but the journal is from an unrelated field.
- The source is "personal communication" or a deleted/inaccessible page — conveniently unverifiable.
- Every source agrees with the chatbot perfectly, from the same family of sites.

None of these alone means a lie — but two or more means it's verify-first territory.

## The honesty move nobody teaches

When a chatbot can't know something (very recent events, paywalled data, signed info),
say so in your prompt: *"If you don't know or can't verify this, say 'I don't know' —
I'd rather have a gap than a guess."* This prompt line fixes more hallucinations than
any other single sentence. Use it early, not after you've been burned.

## A worked example (60-second version)

**You asked:** "Does magnesium help with sleep?" *(education only — discuss with your own clinician)*

**Chatbot says:** "Yes, studies show it improves sleep quality" and cites "Abbasi et al., 2012."

**Verify:** Paste `Abbasi 2012 magnesium sleep randomized` into a search engine.
Find the actual paper. Open the abstract. Read whether the study population,
dose, and outcome match what the chatbot told you. (In this real example, the study
does exist — but note the population was elderly people with insomnia, a detail the
chatbot dropped. Verification found the nuance.)
