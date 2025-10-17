# Algorithm Analysis Starter Code

This repository contains four different implementations of a duplicate-finding algorithm, along with tools to measure and visualize their performance.

## Files

- `implementation_a.py` - Nested loop approach
- `implementation_b.py` - Sorting approach
- `implementation_c.py` - Set-based approach
- `implementation_d.py` - Counting approach
- `measure.py` - Performance measurement and visualization tools

## Setup

Make sure you have Python 3.7+ installed, along with matplotlib:
```bash
pip install matplotlib
```

## Running the Code

To test individual implementations:
```bash
python implementation_a.py
python implementation_b.py
python implementation_c.py
python implementation_d.py
```

To run performance tests:
```bash
python measure.py
```

To create the visualizations:
```bash
python visualize.py
```

This will test all four implementations with datasets of sizes 100, 500, 1,000, 5,000, and 10,000 elements, then create a graph showing their performance.

## Your Task

Analyze these implementations, predict their complexity, measure their performance, and write a report connecting your findings to Big O, Big Omega, and Big Theta notation.