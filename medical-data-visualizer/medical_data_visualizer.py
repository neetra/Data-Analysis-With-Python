import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Add 'overweight' column and calculate bmi values     
height_m = df["height"] / 100

# Step 2: Calculate BMI
bmi = df["weight"] / (height_m ** 2)

# Step 3: Create overweight column (1 if BMI > 25, else 0)
df["overweight"] = (bmi > 25).astype(int)

# 3
# Normalize cholesterol and glucose
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)
# 4
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],  # keep the target variable
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # Step 2: Group and reformat the data to get counts for each feature split by cardio
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # Step 3: Draw the categorical plot
    fig = sns.catplot(
        data=df_cat,
        kind="bar",
        x="variable",
        y="total",
        hue="value",
        col="cardio"
    ).fig

    fig.savefig('catplot.png')
    # Step 4: Return the figure
    return fig   

# 10

def draw_heat_map():
    # Step 1: Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &  # diastolic <= systolic
        (df["height"] >= df["height"].quantile(0.025)) &  # height >= 2.5th percentile
        (df["height"] <= df["height"].quantile(0.975)) &  # height <= 97.5th percentile
        (df["weight"] >= df["weight"].quantile(0.025)) &  # weight >= 2.5th percentile
        (df["weight"] <= df["weight"].quantile(0.975))    # weight <= 97.5th percentile
    ]

    # Step 2: Calculate the correlation matrix
    corr = df_heat.corr()

    # Step 3: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Step 4: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Step 5: Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,          # show correlation values
        fmt=".1f",
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig('heatmap.png')
    # Return the figure
    return fig
