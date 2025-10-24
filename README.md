# Monte Carlo Commission Simulation

A Python-based Monte Carlo simulation to predict sales commission expenses for a team of 500 sales representatives. This project demonstrates how to use probabilistic modeling to make better business decisions than simple averages would allow.

<img width="1775" height="1132" alt="Screenshot 2025-10-24 at 10 45 10 AM" src="https://github.com/user-attachments/assets/91b85a63-51e3-4616-be19-684d20617abd" />

## Table of Contents

- [Overview](#overview)
- [What is Monte Carlo Simulation?](#what-is-monte-carlo-simulation)
- [Business Problem](#business-problem)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Understanding the Results](#understanding-the-results)
- [Customization](#customization)
- [Example Output](#example-output)
- [Advantages Over Spreadsheets](#advantages-over-spreadsheets)
- [References](#references)

## Overview

Instead of using simple averages to budget for sales commissions, this simulation runs 1,000 different scenarios with randomized inputs to predict realistic expense ranges and probability distributions. This gives decision-makers concrete insights into potential outcomes rather than relying on single-point estimates.

## What is Monte Carlo Simulation?

Monte Carlo simulation is a computational technique that uses random sampling to obtain numerical results. Named after the famous Monte Carlo casino, it's particularly useful when:

- You have input variables with uncertainty
- The mathematical formula is known but involves complex probability distributions
- You want to understand the range and likelihood of possible outcomes

In this project, we model two sources of uncertainty:
1. **Sales targets** - varies by sales rep based on experience and territory
2. **Performance** - actual sales as a percentage of target

## Business Problem

You need to budget for sales commissions, but there's significant variability:
- 500 sales representatives with different targets
- Performance varies from month to month
- Commission rates are tiered based on performance levels
- A single average estimate might leave you under or over-budgeted

**Solution**: Run 1,000 simulations with different combinations of targets and performance to see the full distribution of possible commission expenses.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/TheDevsGarden/monte-carlo.git
cd monte-carlo
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing and random number generation
- **seaborn**: Statistical data visualization
- **matplotlib**: Plotting and charting

## Usage

### Basic Usage

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run the simulation
python commission_calc.py
```

### What the Script Does

1. **Runs 1,000 simulations** - Each simulation represents a possible scenario
2. **Displays summary statistics** - Mean, standard deviation, min, max, quartiles
3. **Generates a histogram** - Visual distribution of commission amounts
4. **Saves the chart** - Creates `commission_histogram.png` in the project directory

## How It Works

### 1. Define the Commission Structure

```python
def calc_commission_rate(x_to_target):
    if(x_to_target < 0.9):
        return 0.02      # 2% for under 90% of target
    elif(x_to_target >= 0.9 and x_to_target < 0.99):
        return 0.03      # 3% for 90-99% of target
    elif(x_to_target >= 0.99):
        return 0.04      # 4% for meeting/exceeding target
```

### 2. Model Sales Targets

Sales targets are distributed across 6 brackets reflecting organizational structure:

| Target Amount | Probability | Typical Role |
|--------------|-------------|--------------|
| $75,000 | 30% | Entry-level reps |
| $100,000 | 30% | Standard reps |
| $200,000 | 20% | Senior reps |
| $300,000 | 10% | Territory managers |
| $400,000 | 5% | Regional managers |
| $500,000 | 5% | Top performers |

### 3. Model Performance Variability

Performance (percent to target) follows a **normal distribution**:
- **Mean**: 100% (average rep hits their target)
- **Standard Deviation**: 10% (68% of reps fall between 90-110% of target)

This models real-world sales variability where most reps cluster around their targets but some significantly over or underperform.

### 4. Run Simulations

For each of 1,000 simulations:
1. Randomly assign targets to 500 reps based on the probability distribution
2. Randomly generate performance percentages from the normal distribution
3. Calculate actual sales: `Sales = Target × Performance`
4. Determine commission rate based on performance tier
5. Calculate commission: `Commission = Sales × Rate`
6. Sum total commissions for all 500 reps

### 5. Analyze Results

Aggregate all 1,000 simulations to find:
- Most likely commission expense (mean)
- Range of possible outcomes (min to max)
- Confidence intervals (quartiles)
- Distribution shape (histogram)

## Understanding the Results

### Sample Output

```
Summary Statistics:
            Sales  Commission_Amount  Sales_Target
count      1000.0             1000.0        1000.0
mean   83636840.0          2905779.0    83653200.0
std     2690765.0           102713.0     2643569.0
min    73743750.0          2568798.0    73800000.0
25%    81803125.0          2834196.0    81900000.0
50%    83667500.0          2902965.0    83675000.0
75%    85539000.0          2975332.0    85500000.0
max    92571000.0          3225805.0    92625000.0
```

### Key Insights

1. **Expected Commission**: ~$2.9M (mean)
2. **Standard Deviation**: ~$103K (variability around the mean)
3. **Realistic Range**: $2.57M - $3.23M (min to max)
4. **Planning Range**: $2.83M - $2.98M (25th to 75th percentile)

### What This Means for Budgeting

- **Conservative Budget**: Plan for $3.0M (covers 75% of scenarios)
- **Aggressive Budget**: Plan for $2.8M (50/50 chance of exceeding)
- **Worst Case**: Have contingency plans if expenses reach $3.2M+

## Customization

### Change Number of Simulations

```python
num_simulations = 5000  # More simulations = smoother distribution
```

### Adjust Team Size

```python
num_reps = 1000  # Model a larger sales force
```

### Modify Commission Tiers

```python
def calc_commission_rate(x_to_target):
    if(x_to_target < 0.8):
        return 0.01      # 1% for under 80%
    elif(x_to_target >= 0.8 and x_to_target < 1.0):
        return 0.025     # 2.5% for 80-100%
    elif(x_to_target >= 1.0):
        return 0.05      # 5% for exceeding target
```

### Change Performance Distribution

```python
avg = 0.95           # Model more conservative performance (95% average)
std_dev = .15        # Model higher variability (15% std dev)
```

### Adjust Target Distribution

```python
sales_target_values = [50_000, 100_000, 150_000, 200_000]
sales_target_prob = [.4, .3, .2, .1]  # Must sum to 1.0
```

## Example Output

The simulation generates a histogram showing the distribution of total commission amounts:

![Commission Distribution](commission_histogram.png)

The histogram typically shows:
- **Bell-shaped curve** - Most outcomes cluster around the mean
- **Symmetric distribution** - Roughly equal chances of over/under the mean
- **Range visibility** - Clear view of best and worst cases

## Advantages Over Spreadsheets

### Python Advantages

1. **Complex Logic**: Easy to implement tiered commission structures
2. **Readability**: Clear code vs. nested Excel formulas
3. **Scalability**: Runs thousands of simulations quickly
4. **Reproducibility**: Version control with git
5. **Flexibility**: Easy to modify distributions and parameters
6. **Visualization**: Integrated charting with matplotlib/seaborn
7. **Analysis**: Powerful statistical tools with pandas

### When to Use Each

**Use Excel when**:
- Quick one-off analysis
- Stakeholders need to interact with the model
- Simple linear calculations

**Use Python when**:
- Complex conditional logic
- Many simulations needed
- Integration with other systems
- Version control is important
- Team of technical users

## References

- **Tutorial**: [Practical Business Python - Monte Carlo](https://pbpython.com/monte-carlo.html)
- **Monte Carlo Method**: [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- **Pandas Documentation**: [pandas.pydata.org](https://pandas.pydata.org/)
- **NumPy Random**: [numpy.org/doc/stable/reference/random](https://numpy.org/doc/stable/reference/random/)

---

**License**: MIT
**Author**: Recreated and enhanced from pbpython.com tutorial
**Last Updated**: October 2025
