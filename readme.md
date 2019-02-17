# Repertoire
Spaced repetition is a technique that [some people](http://augmentingcognition.com/ltm.html) like to use to remember things.
In particular, things they would like to remember over many years, perhaps for the rest of their lives.
[Anki](https://apps.ankiweb.net/) is a popular program for doing this, but it seems unlikely that it will still be possible to run this program 10 years from now (its UI is already showing its age).

Repertoire is a minimalistic, extensible program for spaced repetition.
Memories are stored in plain text (which, in my view, will never become obsolete), and the testing interface can run in nothing more than a text-based console.

# Binders
There are three built-in *binders*, formats for flashcards (*sheets* in the musical analogy): quotes, people, and math.

## Quotes
Quotes ask you to identify your favorite quotations, their authors, and the dates when they were published.
The file is organized by work, decreasing overhead when you have multiple quotes from the same work:
```yaml
binder: quotes
sheets:
- title: Discourse on Method
  author: René Descartes
  date: 1637
  quotes:
  - quote: I think therefore I am
  - quote: Good sense is, of all things among men, the most equally distributed
- title: Crime and Punishment
  author: Fyodor Dostoevsky
  date: 1866
  quotes:
  - quote: Only to live, to live and live! Life, whatever it may be!
```

## People
The *people* binder tests you on topics of interest and important contributions of major figures in your field, as well as (optionally) their birth and/or death years.
It is organized by person:
```yaml
binder: people
sheets:
- name: Bill Thurston
  dates: 1946-2012
  topics: low-dimensional topology; foliation; geometrization conjecture
- name: Luitzen Egbertus Jan Brouwer
  dates: 1881-1966
  topics: fixed point theorem; intuitionism
```

## Math
The *math* binder is relatively open-ended, but can test you on definitions, theorem statements, proof key ideas, etc.
Its key feature is support for latex rendering in iTerm2:
```yaml
binder: math
sheets:
- name: Strong law of large numbers
  statement: |
    $\bar{X}_n \overset{a.s.}{\to} \mu$
- name: Weak law of large numbers
  statement: |
    $\lim_n \mathbb{P}[|\bar{X}_n - \mu| < \epsilon] = 0$
- name: Heine–Cantor theorem
  statement: |
    If $f : M \to N$ is a continuous function on a compact metric space $M$, then $f$ is uniformly continuous
  proof: |
    Find a finite subcover of the balls of half the radius needed to make $f$ change by no more than $\epsilon$, and take $\delta$ as their minimum radius.
```

# Installation
1. Install repertoire with `pip install repertoire`
1. If you want to use the math binder, make sure you have LaTeX installed (and use iTerm2), as well as ImageMagick (`brew install imagemagick` on MacOS)
