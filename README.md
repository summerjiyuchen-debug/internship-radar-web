# Internship Radar Web

Live demo: https://internship-radar-web.vercel.app

A privacy-first web MVP for turning messy job-alert emails into a CV-ranked internship shortlist.

## Why I built this

The first version of Internship Radar lived on GitHub as a developer-facing project. People understood the value, but very few actually downloaded it because the setup flow was too technical: clone the repository, install Python, edit config files, and run scripts.

That revealed the real adoption problem:

- The pain point was real.
- The delivery channel was wrong.
- Job seekers wanted an answer, not a repo.

This web MVP is the next iteration. It removes GitHub, installation, and email authorization from the first user experience. The goal is to let someone test the core value in under one minute.

## User flow

1. Upload CV as PDF, DOCX, or TXT
2. Paste job-alert emails or job descriptions
3. Generate a ranked shortlist with:
   - match score
   - company
   - location
   - source
   - deadline
   - application link
   - reasons
   - risk checks

## Product decisions

- Browser-first: users can try it from a link instead of downloading code.
- Privacy-first: CV and job-alert text are processed in the browser session.
- No account required: users see value before being asked to sign up.
- No email permission required: users can paste or forward content manually at first.
- Explainable ranking: each recommendation includes reasons and risk checks.
- Student-focused filtering: the scoring favors internships, graduate programs, and early-career language.

## How to copy job alerts

Links may not always copy cleanly from email clients. The app treats missing links as a usability note, not a job-quality risk.

Recommended copy methods:

- Open a job-alert email, click inside the message body, press Ctrl+A and Ctrl+C, then paste into the app.
- If links are missing, use Forward, Print view, or View original, then copy the full message.
- For school newsletters, copy the section containing the actual job listings, not only the email introduction.

## Current limitations

- This is a lightweight MVP, not a full applicant tracking system.
- Parsing is heuristic and can miss unusual email formats.
- It does not submit applications or connect to Gmail, Outlook, LinkedIn, or job boards yet.
- A future version could add user accounts, forwarding inboxes, saved reports, and calendar reminders.

## Privacy

This MVP processes files in the browser session. The CV and job-alert text are not saved by the page.

## Positioning

Built for students who do not want to use GitHub, install Python, or configure email access before seeing value.
