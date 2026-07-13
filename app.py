from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

# Read CSV file
df = pd.read_csv("quantium-starter-repo/output.csv")

print("Rows loaded:", len(df))
print(df.head())
print(df.columns)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Make sure Sales is numeric
df["Sales"] = pd.to_numeric(df["Sales"])

# Add all regions together per date
df = df.groupby("date", as_index=False)["Sales"].sum()

# Sort by date
df = df.sort_values("date")

# Check the data
print(df.head())
print(df.dtypes)


# Create line chart
fig = go.Figure(
    data=[
        go.Scatter(
            x=df["date"],
            y=df["Sales"],
            mode="lines+markers",
            name="Total Sales"
        )
    ]
)

fig.update_layout(
    title="Pink Morsel Total Sales Over Time",
    xaxis_title="Date",
    yaxis_title="Sales",
    template="plotly_white"
)


# App layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Soul Foods", style={"color": "white"}),
                html.P("Pink Morsel Sales", style={"color": "white"})
            ],
            style={
                "padding": "10px",
                "textAlign": "center",
                "fontSize": "24px",
            }
        ),

        html.Div(
            [
                dcc.Graph(
                    id="sales-line-chart",
                    figure=fig
                )
            ],
            style={
                "backgroundColor": "white",
                "borderRadius": "15px",
                "padding": "10px",
                "overflow": "hidden",
                "boxShadow": "0px 4px 10px rgba(0,0,0,0.2)"
            }
        )
    ],
    style={
        "backgroundColor": "#192344",
        "minHeight": "100vh",
        "padding": "20px"
    }
)


if __name__ == "__main__":
    app.run(debug=True)