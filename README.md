AI From Scratch

Learning modern AI from first principles, in the open. One idea at a time, explained for a curious beginner, with small runnable code you can break yourself.

Every lesson has the same four parts:

File	What it is
notebook.py	Under 50 lines, seeded, runnable. Ends with a five-minute tweak challenge.
concept.md	The idea in plain English, a vocabulary table, and the misconception to dodge.
medium_draft.md	The long-form chapter.
linkedin_post.md	The short version.

Every number quoted in the writing is the actual output of the code in the same folder.

Lessons
Phase 1 — Foundations

01 — Linear Regression from Scratch A blindfolded walk down a foggy hill. How a program finds a rule nobody told it, using nothing but NumPy. Covers feature, label, weight, bias, loss, gradient, gradient descent, learning rate, epoch, convergence, divergence.

02 — The AI Vocabulary Machine Every core AI word made concrete in one small program, built around an exam you haven't seen yet. Covers algorithm vs model, parameters vs hyperparameters, training vs inference, train/test split, generalization, overfitting, and why a perfect score is a warning sign.

Next: loss functions — why we square the error instead of just subtracting it.

Running the code

Python 3.9 or newer.

bash
git clone https://github.com/sarangbondre/learn-ai-in-public.git
cd learn-ai-in-public
pip install numpy scikit-learn matplotlib
python curriculum/01-linear-regression/notebook.py

Each file runs on its own. Nothing depends on anything else.

Glossary

Every term introduced across the lessons, defined in plain English: GLOSSARY.md
