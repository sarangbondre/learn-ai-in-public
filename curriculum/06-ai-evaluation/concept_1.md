# Lesson 06 — Evaluation: How Do You Know an AI Works?

**The question:** Can an AI grader be fooled by a wrong answer?

## 1. The picture: two ways to mark a test

Think of two ways a teacher could mark your homework.

**The answer key.** The teacher has the right answers in front of them and ticks or crosses each line. Fast, exact, and impossible to sweet-talk. But it only works for questions with one right answer.

**Reading and judging.** For an essay, there's no answer key. The teacher reads it and decides how good it is. That's the only way to judge clarity or tone, but a confident, well-written essay can hide a wrong fact.

Checking an AI is the same. You can check facts with plain code, like an answer key. Or you can ask another AI to read the answer and judge it. That second idea is called **LLM-as-judge**, and it's now everywhere.

## 2. The words, in plain English

| Word | What it really means |
|---|---|
| Evaluation ("evals") | Repeatable tests that tell you whether an AI system is doing its job. |
| Code check | Plain rules written by a person: "the reply must mention the hold", "the reply must not say delivered". The answer key. |
| AI grader (LLM-as-judge) | Another AI asked to score the answer. The teacher reading an essay. |
| Reference | The source of truth the grader can compare against: here, the shipment's system record. |
| False pass | A wrong answer that gets marked as right. The dangerous kind of mistake. |
| False fail | A right answer that gets marked as wrong. Annoying, and it wastes people's time. |
| Regression set | A saved list of test cases you re-run after every change, so old mistakes can't come back. |

## 3. Where it shows up

Every AI system that talks to customers or makes decisions: support assistants, document readers, agents. Without evaluation, every prompt change or model upgrade is a guess shipped to customers.

## 4. Is it the right choice? A simple rule

**If a rule can check it, use code. Use an AI grader only for what code can't judge, and always give it the evidence.**

- Facts (status, amounts, dates, which action was taken) → code check against the record.
- Tone, helpfulness, clarity → AI grader, with the record in front of it.
- An AI grader with no record → it can only judge how an answer *sounds*. Don't trust it on facts.

## 5. What the experiment showed

15 support replies about shipments: **10 correct, 5 wrong**. Each grader marked each reply PASS or FAIL. The AI graders were real AI models; their verdicts are recorded in `notebook.py`.

**Round 1:** the wrong replies oversold themselves ("I've verified this with the delivery team", "Good news! Your shipment has been located").

| Grader | Wrong replies it passed | Right replies it failed |
|---|---|---|
| Plain code check | 0 of 5 | 0 of 10 |
| Small AI, no records (run 1) | 0 of 5 | 1 of 10 |
| Small AI, no records (run 2, same input) | 0 of 5 | 3 of 10 |
| Larger AI, no records | 0 of 5 | 0 of 10 |
| Small AI, with records | 0 of 5 | 0 of 10 |

My guess was wrong: no grader was fooled. But read their reasons: they failed the wrong replies for **sounding too sure** ("claims a check it shows no evidence of"), not for being wrong.

**Round 2:** the same wrong facts, written calmly ("It's in transit and on track for delivery on 26 Oct").

| Grader | Wrong replies it passed | Right replies it failed |
|---|---|---|
| Plain code check | 0 of 5 | 0 of 10 |
| Small AI, no records | **2 of 5** | 2 of 10 |
| Larger AI, no records | **3 of 5** | 0 of 10 |
| Small AI, with records | 0 of 5 | 1 of 10 |

What stands out:
- **Without the record, the graders judged the tone, not the facts.** Calm wrong answers got through, and the larger model let through more of them.
- **Two replies were word for word the same:** "It's out for delivery today, expected by about 6 PM." For one shipment that's true. For the other, the parcel was delivered two days earlier. No grader can tell them apart without the record.
- **With the record, the grader caught every wrong reply.**
- **A few lines of plain code did just as well**, at no cost, and gave the same answer every time. The small grader, given identical input twice, failed 1 correct reply the first time and 3 the second.

**A fair note:** this is a small test: 15 replies, one or two runs per grader. The point isn't the exact counts; it's the pattern.

## 6. The CTO lens

Many teams now set up an AI grader, see high scores on a dashboard, and assume the system works. If that grader only sees the answer, the score measures how *convincing* the AI sounds. In logistics, a convincing wrong answer is the expensive kind: "out for delivery" for a parcel that was delivered two days ago sends a customer on a wild goose chase and an angry call to your team.

The questions I'd ask in an AI review:
1. What does our grader actually see: just the answer, or the source of truth too?
2. Which checks could be plain code instead?
3. Do failures from production become new test cases?

## 7. Common misconception

**"A bigger, smarter grader is safer."** In round 2 the larger model was fairer to correct replies, but it let through more wrong ones. Without evidence, a smarter grader is just better at being convinced.

## 8. Connecting the lessons

This is the loss-function idea from Lesson 02 again: what you measure decides what you get. And it's the harness from Lesson 03: evaluation is part of the system around the model, deciding what's allowed to reach a customer.
