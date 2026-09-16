# Communicating AI use in your course

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

Three steps, shown as a flow diagram at the top of the page:

1. **Set your comfort level.** Five course-level options, from no AI at all through open
   exploration, drawn from the AI Assessment Scale.
2. **Pick an assignment.** Find the kind of work in the collapsed A-G list, then the
   skill you want students to develop, then take the sample wording.
3. **Copy and edit.** Selections collect in a draft panel. Copy all, or download a `.txt`.

Everything is framed as sample language to be edited, not policy to be pasted. Saying
no AI at all is presented as a legitimate position that still needs spelling out for
students.

Other behaviour:

- The **field** box fills `[field]` and `[discipline]` throughout.
- **Skills** fill `[list the skills here]` and populate themselves from the assignments
  picked in step 2. Remove one and it stays removed; add your own and it survives later
  changes. Anything unfilled is highlighted, and the draft banner links to the control
  that fixes it.
- The word "cognitive" appears nowhere in the document or the app. Goal names and policy
  text are written in plain language for students; the faculty guidance says "target
  skill" rather than "cognitive target".
- Each entry says which course-level statements it sits under. If it conflicts with the
  statement chosen, the note turns amber and says which way.
- When selections depart from the course statement, the draft writes the exception
  sentence for the syllabus and puts it in the export.

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
