# AI policy language for College of the Environment courses

A single-page tool that turns the AI Policy Pick-List into something a faculty member
can work through in five minutes. Pick a course-level statement, pick language for
individual assignments, copy or download the result.

Built for a 90-minute faculty workshop, where the deliverable is that everyone leaves
with policy text they can paste into a syllabus and an assignment.

## Publish it on GitHub Pages

1. Create a new repository, for example `ai-policy-picklist`. Public.
2. Upload `index.html`, `README.md`, and the `tools/` folder. (Or `git push` them.)
3. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. Wait about a minute. The site appears at
   `https://<your-username>.github.io/ai-policy-picklist/`.

That URL is stable, free, and yours. Every later edit you push is live in under a minute.

### Before the workshop

- Open the link in a private browsing window to confirm it works for someone who
  is not signed in to anything.
- Put the URL on a slide as a QR code.
- Email `index.html` to attendees as an attachment too. It is fully self-contained,
  so it opens from a download with no internet connection at all. That is your
  insurance against room wifi.

## What it does

- **Step 1** picks one of the five AIAS course-level statements for the syllabus.
- **Step 2** works like a key: task type, then cognitive goal, then the policy language.
  Search covers task names, goals, and the policy text itself.
- The **field** box at the top fills `[field]` and `[discipline]` throughout.
- **Cognitive outcomes** fill `[your course-specific cognitive outcomes]`. The options
  are the cognitive goals already named in the pick-list, so they stay in the
  document's own language; there is also a box for writing your own. If someone has
  already picked assignment language, one button pulls the outcomes from that.
  Anything still unfilled stays highlighted and is listed in a banner on the draft.
- **Your draft** collects every selection. Copy all, or download a `.txt`.

## Privacy and limits

Everything runs in the browser. No server, no analytics, no account. A draft is saved
in that browser's local storage only, so it does not follow anyone to another device
and it disappears if they clear site data. Nothing is collected centrally: if you want
to compile what faculty produced, ask them to paste their downloaded text into a
shared document.

## Editing the content

All the policy language lives in `index.html`, on the line beginning `const DATA =`.
For a one-off wording fix, edit it there.

To change the content properly, edit the Word pick-list and regenerate:

```
pip install python-docx
python tools/rebuild.py AI_Policy_Pick-List_CEnv.docx
```

That rewrites only the data line and leaves the page design alone. The parser depends
on the Word styles in the source document; `tools/rebuild.py` documents which ones.

## Attribution

Course-level statements adapt the AI Assessment Scale (Perkins, Furze, Roe & MacVaugh,
2024). Cognitive goals are tagged with Bloom's revised taxonomy (Anderson & Krathwohl).
Check the AIAS licence terms before redistributing outside the college.
