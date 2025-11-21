import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)

df_clean = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]
df = df_clean


def draw_line_plot():
    # Draw line plot

    # Step 1: Set up the figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Step 2: Draw the line plot
    ax.plot(df.index, df["value"], color="red", linewidth=1)

    # Step 3: Set title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Step 4: Improve x-axis formatting (optional)
    fig.autofmt_xdate()  # rotate dates for readability

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
      # Step 1: Copy the dataframe and add 'year' and 'month' columns
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()  # full month name
    
    # Step 2: Group by year and month, calculate average page views
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    
    # Step 3: Ensure months are in calendar order
    months_order = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    df_grouped = df_grouped[months_order]
    
    # Step 4: Draw the bar plot
    fig = df_grouped.plot(kind="bar", figsize=(12, 6)).figure
    
    # Step 5: Set labels and legend
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
        
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    df_box["month_num"] = df_box["date"].dt.month      # numeric month for sorting

    # Sort months in calendar order
    df_box = df_box.sort_values("month_num")

    # Set up figure with 2 subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Year-wise box plot
    sns.boxplot(
        x="year",
        y="value",
        data=df_box,
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
