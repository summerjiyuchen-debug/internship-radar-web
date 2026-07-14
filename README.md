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
- Usage-aware: anonymous events help measure whether users actually reach the core value moment.

## How the job analysis works

The app separates extraction from scoring:

1. **Job evidence check**: first decide whether a pasted block is actually a job listing. Social media footers, WeChat mini-program notices, guidebook links, event promos, newsletter introductions, and unsubscribe/contact blocks are filtered out.
2. **Field extraction**: extract likely title, company, location, deadline, source, and application link when present.
3. **Detail quality check**: if a block only says something generic like `Summer Intern` or `Asia Internship Programs`, but lacks company, function, requirements, domain signals, deadline, or application context, it is marked as `Needs detail`.
4. **Fit scoring**: compare the job text with CV keywords, student/internship language, target role terms, source quality, location, and risk terms.
5. **Risk checks**: flag experienced-hire requirements, insurance/sales terms, missing student-program wording, unclear domain, missing employer, and insufficient copied detail.

This matters because school career emails often mix real jobs with announcements. A higher-trust source should help real listings rank higher, but it should not turn Instagram, WeChat, or guidebook text into a fake job.

The product rule is: when the copied text is too thin to judge, the app should say so instead of pretending the match is accurate.

## Usage metrics

The web app records lightweight anonymous events through `/api/track` and writes them to Vercel runtime logs.

Tracked events:

- `page_view`: someone opened the page
- `cv_loaded`: a CV file was loaded, with file type, file size, extracted character count, and keyword count
- `job_text_pasted`: job-alert text was pasted, with character count only
- `analyze`: the user generated a shortlist, with job count and bucket counts
- `download_report`: the user downloaded the report
- `print_report`: the user opened print/save-to-PDF
- `sample_loaded`: the user tried the sample data

Not tracked:

- CV content
- job-alert content
- names
- email addresses
- application links
- exact pasted text

Where to view:

1. Open the Vercel dashboard.
2. Select the `internship-radar-web` project.
3. Open Runtime Logs.
4. Filter for `usage_event`.

This gives an early funnel:

`page_view -> cv_loaded -> job_text_pasted -> analyze -> download_report`

## How to copy job alerts

Links may not always copy cleanly from email clients. The app treats missing links as a usability note, not a job-quality risk.

Recommended copy methods:

- Open a job-alert email, click inside the message body, press Ctrl+A and Ctrl+C, then paste into the app.
- If links are missing, use Forward, Print view, or View original, then copy the full message.
- For school newsletters, copy the section containing the actual job listings, not only the email introduction.
- If the output only shows generic titles, open the original job card and copy the expanded section with company, requirements, responsibilities, and application button.

## Current limitations

- This is a lightweight MVP, not a full applicant tracking system.
- Parsing is heuristic and can miss unusual email formats.
- It does not submit applications or connect to Gmail, Outlook, LinkedIn, or job boards yet.
- A future version could add user accounts, forwarding inboxes, saved reports, and calendar reminders.

## Privacy

This MVP processes files in the browser session. The CV and job-alert text are not saved by the page.

## Positioning

Built for students who do not want to use GitHub, install Python, or configure email access before seeing value.
