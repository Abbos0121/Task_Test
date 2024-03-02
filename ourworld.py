# Report to Line Manager:

# To: my manager
# From: Abbos
# Date: 03.02.2024

# Subject: Data Analysis Exercise Report

# Dear my manager,

# I have completed the data analysis exercise as instructed. Below is a summary of my process:

# Firstly, I imported the necessary libraries in Python, namely pandas for data manipulation and numpy for numerical calculations.

# Next, I created a DataFrame to store the age-specific death rates for COPD in both the United States and Uganda for the year 2019.

# Then, I calculated the crude death rate by summing up all the age-specific death rates for each country and rounding the result to one decimal place.
# This provides an overall death rate per 100,000 people for each country.

# After that, I calculated the age-standardized death rate using the WHO Standard Population.
# I followed the age-standardization process by multiplying each age-specific death rate by the corresponding WHO Standard Population value for that age group,
# summing up the standardized rates, and then dividing by the total Standard Population.
# Finally, I multiplied the result by 100,000 and rounded it to one decimal place to get the age-standardized death rate per 100,000 people.

# Throughout the process, I made the assumption that the provided age-specific death rates are accurate representations of the entire population for each country.

# The differences between the crude and age-standardized death rates can be attributed to variations in the age distributions of the populations in the United States and Uganda.
# Crude death rates provide a simple measure of the overall risk of death from COPD within each country, whereas age-standardized death rates adjust for differences in age distributions
# and allow for a more accurate comparison between countries with different age structures.

# Please find the Python script attached for your review.

# If you have any questions or require further clarification, please do not hesitate to contact me.

# Thank you for the opportunity to complete this exercise.

# Sincerely,
# Abbos

import pandas as pd
import numpy as np

# Age-specific death rates for COPD in 2019
data = {
    'Age group (years)': ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                          '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85+'],
    'Death rate, United States, 2019': [0.04, 0.02, 0.02, 0.02, 0.06, 0.11, 0.29, 0.56, 1.42, 4.00, 14.13, 37.22, 66.48,
                                         108.66, 213.10, 333.06, 491.10, 894.45],
    'Death rate, Uganda, 2019': [0.40, 0.17, 0.07, 0.23, 0.38, 0.40, 0.75, 1.11, 2.04, 5.51, 13.26, 33.25, 69.62, 120.78,
                                  229.88, 341.06, 529.31, 710.40]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Crude Death Rate
df['Crude Death Rate, United States'] = df['Death rate, United States, 2019'].sum()
df['Crude Death Rate, Uganda'] = df['Death rate, Uganda, 2019'].sum()

# Calculate Age-Standardized Death Rate
# WHO Standard Population
who_standard_population = {
    'Age group (years)': ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                          '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85+'],
    'Standard Population': [1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381,
                            1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381, 1941381]
}

# Create DataFrame for WHO Standard Population
df_who = pd.DataFrame(who_standard_population)

# Merge DataFrames
merged_df_us = pd.merge(df, df_who, on='Age group (years)')
merged_df_uganda = pd.merge(df, df_who, on='Age group (years)')

# Calculate Age-Standardized Death Rate
merged_df_us['Age-Standardized Death Rate, United States'] = \
    (merged_df_us['Death rate, United States, 2019'] * merged_df_us['Standard Population'] / merged_df_us['Standard Population'].sum()) * 100000

merged_df_uganda['Age-Standardized Death Rate, Uganda'] = \
    (merged_df_uganda['Death rate, Uganda, 2019'] * merged_df_uganda['Standard Population'] / merged_df_uganda['Standard Population'].sum()) * 100000

# Print Results
print("Crude Death Rate for United States:", round(merged_df_us['Crude Death Rate, United States'].iloc[0], 1), "deaths per 100,000 people")
print("Crude Death Rate for Uganda:", round(merged_df_uganda['Crude Death Rate, Uganda'].iloc[0], 1), "deaths per 100,000 people")
print("Age-Standardized Death Rate for United States:", round(merged_df_us['Age-Standardized Death Rate, United States'].iloc[0], 1), "deaths per 100,000 people")
print("Age-Standardized Death Rate for Uganda:", round(merged_df_uganda['Age-Standardized Death Rate, Uganda'].iloc[0], 1), "deaths per 100,000 people")
