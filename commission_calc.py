import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Setup
sns.set_style('whitegrid')

avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000

sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]

def calc_commission_rate(x_to_target):
    if(x_to_target < 0.9):
        return 0.02
    elif(x_to_target >= 0.9 and x_to_target < 0.99):
        return 0.03
    elif(x_to_target >= 0.99):
        return 0.04
    else:
        print('error in the function')

# Monte Carlo simulation
# Storing a list to keep all the results from each simulation that we want to analyze
all_stats=[]

# Loop through many simulations
for i in range(num_simulations):

    # Choose random inputs for the sales targets and percent to target
    sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)
    pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)

    # Build the dataframe based on the inputs and number of reps
    df = pd.DataFrame(index=range(num_reps), columns=['Sales_Target','Pct_To_Target'])
    df['Pct_To_Target'] = pct_to_target
    df['Sales_Target'] = sales_target

    # Back into the sales number using the percent to target data
    df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

    # Determine the commissions rate and calculate it
    df['Commission_Rate'] = df['Pct_To_Target'].apply(calc_commission_rate)
    df['Commission_Amount'] = df['Sales'] * df['Commission_Rate']

    # We want to track sales, commission amounts and sales targets over many simulations
    all_stats.append([df['Sales'].sum().round(0),
                     df['Commission_Amount'].sum().round(0),
                     df['Sales_Target'].sum()])

# Save the results as a dataframe
results_df = pd.DataFrame.from_records(all_stats, columns=['Sales','Commission_Amount','Sales_Target'])

# Display summary statistics
print("\nSummary Statistics:")
print(results_df.describe().round(0).to_string())

# Create histogram plot
results_df['Commission_Amount'].plot(kind='hist', title='Total Commission Amount', bins=20)
plt.xlabel('Commission Amount')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('/Users/ilyabelyaev/repos/Monte Carlo/commission_histogram.png')
print("\nHistogram saved as 'commission_histogram.png'")

# Show the plot
plt.show()
