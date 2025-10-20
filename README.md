# Monte Carlo Commission Simulation

This project uses Monte Carlo simulation to predict sales commission expenses for a team of 500 sales representatives.

## Overview

Instead of using simple averages, this simulation runs 1,000 scenarios with randomized inputs to predict realistic expense ranges. The simulation models:

- **Sales targets**: Distributed across 6 brackets ($75K-$500K) based on organizational structure
- **Performance**: Normal distribution (mean 100%, std dev 10%)
- **Commission rates**: Tiered based on performance
  - 0-90% of target: 2%
  - 91-99% of target: 3%
  - 100%+ of target: 4%

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install pandas numpy seaborn matplotlib
```

## Usage

Run the simulation:

```bash
python commission_calc.py
```

The script will:
1. Run 1,000 Monte Carlo simulations
2. Display summary statistics
3. Generate a histogram of commission amounts
4. Save the histogram as `commission_histogram.png`

## Results

The simulation provides:
- Average commission expenses
- Standard deviation
- Min/max ranges
- Distribution visualization

This gives decision-makers concrete probability distributions rather than single-point estimates.

## Based On

This project is based on the tutorial at [https://pbpython.com/monte-carlo.html](https://pbpython.com/monte-carlo.html)
