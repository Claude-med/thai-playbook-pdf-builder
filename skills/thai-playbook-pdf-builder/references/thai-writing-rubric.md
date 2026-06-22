# Thai Writing Rubric

Use this when editing Thai playbook copy for readability, usefulness, and brand fit.

## Voice

Default voice:

- clear and friendly
- practical, not academic
- professional without sounding stiff
- direct enough for busy readers
- grounded in real work
- beginner-friendly before it becomes advanced

The tone should feel like a skilled operator explaining what to do next.

## Sentence Rules

- Prefer short Thai sentences.
- Explain technical terms the first time they appear.
- Avoid literal English structure.
- Replace vague advice with an action.
- Use examples before long theory.
- Prefer action labels such as "do this", "copy this", "check this", and "fix it this way".
- Avoid reader-facing labels that feel internal, such as "module", "source map", or "external context", unless the topic needs them.

## Weak Phrases To Rewrite

| Weak Direction | Better Direction |
|---|---|
| understand this topic better | create a specific output |
| improve efficiency | reduce time, reduce repeat work, or check quality |
| use it better | name the exact step and result |
| suitable for everyone | name the role or real situation |
| best / guaranteed | use evidence-based or conditional wording |

## Page Rhythm

For most pages, use this rhythm:

1. Hook: why this page matters.
2. Plain explanation: the idea in one short paragraph.
3. How to: steps or table.
4. Example: concrete input/output.
5. Action: what to do now.

Do not put more than two long paragraphs together without a reader aid.

## Beginner-First Copy Checks

- The first 5 pages tell the reader the problem, outcome, starting path, and before/after.
- Hard words are explained before they are used in a step.
- The simplest example appears before the full method.
- Each section has a concrete output.
- Paragraphs are short enough for phone reading.
- The copy avoids exaggerated claims.
- The page includes an action, example, checklist, prompt, worksheet, table, fix, or decision aid.
- The playbook includes a full worked example and copy-ready assets.
- Thai text is not mojibake and does not look like machine translation.

## Final Thai QA

Search for common mojibake markers before delivery:

```text
\u0E40\u0E19\u20AC (Thai leading vowel + Thai no nu + euro sign)
\u0E40\u0E18 (suspicious repeated Thai leading-vowel sequence)
\uFFFD (Unicode replacement character)
```

If these appear in normal Thai copy, inspect and rewrite that section.
