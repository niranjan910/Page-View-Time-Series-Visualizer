import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data: Remove top 2.5% and bottom 2.5% of page views
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    """Draws a line plot of daily page views."""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    """Draws a bar chart of average monthly page views by year."""
    df_bar = df.copy()
    df_bar["year"] = df.index.year
    df_bar["month"] = df.index.month
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_grouped.plot(kind="bar", figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Average Daily Page Views per Month")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.xticks(rotation=0)

    plt.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    """Draws box plots for yearly trends and seasonal trends."""
    df_box = df.copy()
    df_box["year"] = df.index.year
    df_box["month"] = df.index.month_name()

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, order=["January", "February", "March", "April", "May", "June", 
                                                           "July", "August", "September", "October", "November", "December"], ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.xticks(rotation=45)
    plt.savefig("box_plot.png")
    return fig
