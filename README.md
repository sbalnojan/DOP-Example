## Data-oriented python examples and tutorial
This repository hosts a bunch of examples of data oriented Python programming and it hosts the code
for a beginner tutorial in data oriented python.

Everything works with batect, so...


### Getting Started
Just fire up batect via ```./batect --list-tasks``` or launch straight into
```./batect dev``` to open up a Jupyter notebook server.

### Tutorial
To follow along with the tutorial, fire up the notebook server and open up work/DO-Tutorial.ipynb.

### WIP
Add another set of cool examples from https://vimeo.com/649009599,

The basic idea is to use heuristics about the actual state of things...

- 0. not storing computations
- 1. monster with bools => alive_monsters, dead_monsters, question: what do I wanna do with this?
- 2-3. Use AoS <=> SoA again question of use cases!
- 4. held_items vs. storing them externally, such that we don't need them if we don't need them (use ID)
- 5. heuristic again tag encoding like human_clothed and then have an array of clothedHumans with their stuff
(use roughly whatever combination makes sense, try to avoid sparse stuff) <-> vs. using OOP and polymorphism
(explain that maybe using the "create a new class thingy...")
