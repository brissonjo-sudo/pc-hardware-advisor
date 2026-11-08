# Common brief for audit sub-agents (orchestrator, 2026-11-08)

Audited artifact: Claude plugin `pc-hardware-advisor` v0.3.3, repository root `E:\Claude code\Projects\pc-hardware-advisor`, branch `audit/0.3.4`. Today is 2026-11-08.

## Rules

1. Read only the files your brief names. Do not modify any file in the repository except your own output file (or, for the test writer, the new test case folders).
2. Never invent. A claim you cannot support with a file line you read, or a URL you fetched in this session, is not a finding.
3. External facts: every `confirmed` or `changed` result needs a URL you actually fetched today, quoted in the row. A value you "know" from memory is `could-not-verify`.
4. Blocked pages (403, captcha, rate limit, JavaScript-only): record `blocked (<reason>)`, try ONE alternative official source, then stop. Never use caches, mirrors, archive copies, alternate user agents or any workaround.
5. English output, plain sentences. No em dash character (use a colon, comma or parentheses). No personal data.
6. Return a result file, not a journal. Reply to the orchestrator in at most 100 words: counts, main findings, what you could not do.

## Findings table (mandatory header, one table per output file)

```
| id | axis | severity | evidence | failure_case | minimal_fix | effort |
```

- `id`: kebab-case naming the problem, not the file (example `safety-line-missing-check-compatibility`).
- `axis`: A, B, C, D, E or F.
- `severity`: `blocker` (a user can be harmed or misled on money, or a hard rule can be violated by following the text as written), `major` (two rules disagree and the model may follow the laxer one, or a check that would catch a blocker is missing), `minor` (wording, counts, readability), `info` (suggestion).
- `evidence`: `path:line`, or `URL (checked 2026-11-08)`, or `run:<json path>#<case>`. A row without evidence is rejected.
- `failure_case`: one concrete situation that produces a wrong or unsafe result.
- `minimal_fix`: the smallest change that removes the failure case.
- `effort`: S, M or L.

## Claim table (axis A only, second table)

```
| claim_id | file:line | stated_value | official_source_url | checked_on | result | note |
```

`result` is one of `confirmed`, `changed` (give the new value in `note`), `could-not-verify`, `blocked`, `not-checked`. End the file with counts per result value.

## Output location

`E:\Claude code\Projects\pc-hardware-advisor\research\audit\<axis>-<n>.md`, exact name given in your brief. Start the file with a title, the files read, the date, the model you are, and your tool-call count.
