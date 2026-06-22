---
name: thai-playbook-pdf-builder
description: Create, improve, or QA Thai PDF playbooks, lead magnets, and Facebook giveaway packs from YouTube transcripts, briefs, notes, articles, podcasts, or supporting research. Use when Codex must build a reusable Claude Work TH playbook workflow, generate a polished A4 PDF with companion assets, turn source material into beginner-friendly frameworks, worksheets, prompt packs, captions, carousel outlines, source credits, research notes, or upgrade the playbook-building skill/template/QA process. Do not use for short summaries only, raw transcript cleanup only, full book writing, regulated legal/medical/financial advice without human review, or requests to copy third-party screenshots, thumbnails, layouts, or long source text directly.
---

# Thai Playbook PDF Builder

Turn source material into a Thai **Simple Action Playbook** that beginners can understand, follow, and reuse immediately. The default is a practical 20-32 page A4 playbook for Claude Work TH Facebook distribution, adjusted to the depth of the source clip and credible outside research. Use 33-40 pages only when the topic is genuinely deep and the extra pages are examples, worksheets, fixes, or worked examples.

## Operating Standard

Create a guide that helps readers do work without feeling the topic is too technical.

- Use the YouTube folder or provided source as the spine, not the whole body.
- Keep `source_audit.md`, `research_notes.md`, and `playbook_blueprint.md` as internal planning gates, but do not push internal/research language into the first pages.
- Start the PDF with the reader's problem, promised result, and simplest example.
- Use beginner-friendly labels in the reader-facing PDF:
  - `Module` -> `ขั้นที่`
  - `Framework` -> `วิธีทำ 5 ขั้น`
  - `QA` -> `เช็กก่อนใช้จริง`
  - `Source Map` -> `ที่มาของข้อมูล`
  - `External Context` -> `ข้อมูลเสริมที่ควรรู้`
- Build one plain 4-5 step method.
- Convert each step into a "ทำตามทีละขั้น" page with examples, copy boxes, checklists, and a small action.
- Include one full worked example that walks from problem to input to output to fix to final version.
- Include "ถ้าทำไม่ได้ ให้แก้แบบนี้" and a one-page Cheat Sheet.
- Keep source claims traceable to source material, external source, or Claude Work TH application, but place detailed source/research pages near the end.
- Write Thai that is natural, direct, and useful for beginners, creators, marketers, owners, operators, team leads, and AI workflow users.
- Redraw ideas as diagrams, tables, worksheets, and prompt boxes. Do not paste third-party visuals unless the user confirms usage rights.

## First Response Behavior

When starting a playbook task, respond briefly with:

1. Inputs found.
2. Inputs missing.
3. Research or verification needed.
4. Outputs to be created.

If source metadata is missing, create only draft-ready output and clearly flag that it is not publish-ready until credit fields are complete.

## Required Inputs

Look for these before drafting:

- Source content: transcript, brief, notes, article, podcast, video summary, VTT, or teaching screenshots.
- Source metadata: title, creator/channel, URL, publish date if available, access date.
- Audience and goal: who receives it and what they should be able to do after reading.
- Brand/context: Claude Work TH default unless the user provides another brand.
- Output brief: length, CTA, target format, required companion assets.

If the user provides a folder, inspect that folder first and classify useful files into source content, metadata, brief, brand note, supporting research, and visual references.

## Required Planning Gates

Do not jump from transcript directly to PDF. Create or clearly reason through these gates first:

1. **Source audit**
   - Output: `source_audit.md`
   - Extract Big Idea, beginner pain point, key concepts, workflow, examples, timestamps, screenshots used as references, warnings, limitations, reusable prompts, and missing metadata.
   - Separate what the source says from interpretation.

2. **Research brief**
   - Output: `research_notes.md` or `research_brief.md`
   - Verify current facts for tools, product behavior, pricing, APIs, platform rules, standards, or best practices.
   - Prefer official docs, primary sources, and reputable references.
   - Record how each source is used: verification, background, or added recommendation.
   - Mark unstable or unverified claims as `ควรตรวจสอบเพิ่มเติม`.

3. **Playbook blueprint**
   - Output: `playbook_blueprint.md`
   - Lock the beginner promise, "start here" navigation, before/after, plain-language glossary, simplest example, quick win, 4-5 step method, step pages, full worked example, copy boxes, fix guide, cheat sheet, action plan, and source credit flow before final writing.

4. **Final package**
   - Only after the gates are stable, write the playbook, companion assets, source credit, and PDF/HTML if requested.

## Length Decision

Default format is **Simple Action Playbook, 20-32 pages**.

- **18-22 pages**: narrow source, one workflow, minimal research.
- **23-28 pages**: typical useful topic with clear steps, examples, and copy boxes.
- **29-32 pages**: stronger topic with multiple steps, worked example, fix guide, and cheat sheet.
- **33-40 pages**: use only when the source is deep and every extra page adds examples, worksheets, safety checks, or worked examples.

Never add filler to hit a page count. Expand examples, worksheets, copy boxes, worked examples, and fix guidance only when they increase reader value.

## Workflow

1. **Audit source and metadata**
   - Read source files and metadata.
   - Extract thesis, beginner pain point, key concepts, examples, workflows, warnings, limitations, and reusable prompts.
   - Identify missing credit fields before drafting.
   - Save `source_audit.md` when producing a package.

2. **Create a research brief**
   - Research only where it helps readers execute or verifies unstable facts.
   - Prefer official documentation and primary sources.
   - Save research notes with source, URL, access date, usage, and confidence.

3. **Build the playbook blueprint**
   - Write a simple promise: what the reader can create or improve after finishing.
   - Define "อ่านจบแล้วคุณจะทำอะไรได้", "เริ่มตรงนี้ก่อน", before/after, glossary, simplest example, quick win, 4-5 step method, step pages, full worked example, copy boxes, fix guide, cheat sheet, and source credit flow.
   - Map source ideas into practical Claude Work TH applications.

4. **Write beginner-first step pages**
   - Each step needs: goal, when to use, inputs, simple steps, example, copy-ready prompt/template, common mistake, fix, and a small action.
   - Every 1-2 pages must include a reader aid: mini example, before/after, table, worksheet, checklist, decision guide, prompt box, fix box, cheat sheet item, or action step.
   - Include good vs weak output examples and fixes.
   - Add manual review points and practical constraints in plain Thai.

5. **Design for distribution**
   - Prefer A4 PDF.
   - The cover must use the same cream/ivory visual system as the rest of the playbook. Do not use a default dark/black cover.
   - Keep one main idea per page, readable Thai text, strong contrast, stable spacing, and mobile-friendly screenshot readability.
   - Use source images only as references for redrawn visuals.

6. **Create companion assets**
   - Facebook caption with hook, benefit, CTA, hashtags, and short credit.
   - Carousel outline, usually 8-10 slides for beginner-friendly playbooks.
   - Prompt pack when the playbook teaches AI or repeatable workflow work.
   - Source credit file.
   - Research notes when external sources shape the playbook.

7. **Verify**
   - Render PDF pages to images and inspect every page when creating PDF output.
   - Fix overflow, overlap, cramped text, weak contrast, broken Thai rendering, awkward page breaks, and overly technical early pages.
   - Confirm no long copied transcript text or disallowed third-party images remain.
   - Run `scripts/audit_playbook_package.py <outputs-dir>` when available.
   - Run `scripts/render_pdf_qa.py <pdf> --out <qa-dir>` when PDF visual QA is needed.
   - Install `pypdfium2` and `Pillow` before PDF visual QA. If the QA directory already contains generated pages, review them first and pass `--force` to replace only generated `page-NN.png` and `contact_sheet.jpg` files.

## Default Simple Action Structure

Use this page plan unless the topic requires a different length:

1. Cover: same cream/ivory palette as the rest of the PDF, title, simple promise, who it helps.
2. Problem This Playbook Solves: show the reader's real pain.
3. What You Can Do After Reading: concrete outputs readers will have.
4. Start Here: quick route, beginner route, full route, copy-box route.
5. Before / After: what changes when they use the playbook.
6. Hard Words In Plain Thai: glossary for only the terms needed.
7. Simplest Example First: tiny input, tiny prompt/process, expected output, 3 checks.
8. What To Prepare Before Starting: inputs, access, decisions, fallback.
9. Quick Win: useful result in 10-15 minutes.
10. The 5-Step Method: one simple method with plain verbs.
11. Step 1: prepare input.
12. Step 1 example or worksheet.
13. Step 2: ask/run the workflow.
14. Step 2 copy box or example.
15. Step 3: create/apply the output.
16. Step 3 example/checkpoint.
17. Step 4: check before using.
18. Step 5: save as reusable template/SOP/checklist.
19. Full Worked Example: problem, input, first output, weak point, fix, final output.
20. Copy Box / Prompt Ready To Use.
21. If It Does Not Work, Fix It Like This.
22. Good Output vs Weak Output.
23. Decision Guide: what path/tool/template to choose.
24. Common Mistakes And Fixes.
25. One-Page Cheat Sheet.
26. 7-Day Action Plan.
27. Source Credit and information used.
28. Research Notes Summary / ข้อมูลเสริมที่ควรรู้.

For longer topics, expand step examples and the worked example. Do not expand theory pages unless they directly reduce beginner confusion.

## Deliverables

Default output package:

- `source_audit.md`
- `research_notes.md` when external research is used.
- `playbook_blueprint.md`
- `playbook.pdf`
- Editable source file used to generate the PDF, such as HTML, DOCX, or Markdown.
- `facebook_caption.md` when requested or when preparing a full distribution package.
- `carousel_outline.md` when requested.
- `prompt_pack.md` when useful.
- `source_credit.md`

Use concise filenames that reflect the topic.

## Quality Gates

Before final response, verify:

- Source audit exists or its findings are represented in the final response.
- Playbook blueprint exists for full packages.
- The cover uses the same visual palette as the rest of the PDF and is not default dark/black.
- The first 5 pages show the problem, promised result, where to start, before/after, and why the reader should continue.
- Technical terms are explained before technical steps.
- A simplest example appears before deeper step pages.
- The playbook has a plain 4-5 step method and steps readers can follow.
- It includes examples, copy boxes/prompts/templates, worksheets/checklists, and next actions.
- It includes one full worked example.
- It includes "ถ้าทำไม่ได้ ให้แก้แบบนี้".
- It includes a one-page Cheat Sheet.
- It shows good vs weak outputs and how to improve weak ones.
- It includes a beginner-friendly checklist readers can use before applying the output.
- Every 1-2 pages contain an interactive or practical reader aid.
- Source credit is complete and honest.
- Outside research is labeled, traceable, and placed near the end unless needed for safety.
- No long transcript copy or direct third-party image paste remains.
- Visuals are redrawn as diagrams/mockups when source images are only references.
- Thai reads naturally and avoids stiff literal translation.
- PDF pages were visually checked for overflow, overlap, and readability.

## References

Load only the reference needed for the current task:

- `references/playbook-quality.md`: structure, quality gates, source rules, review questions.
- `references/page-pattern-library.md`: reusable page patterns and blocks.
- `references/thai-writing-rubric.md`: Thai voice, readability, and editing rubric.
- `references/research-and-credit-rules.md`: research, source labeling, and credit policy.
