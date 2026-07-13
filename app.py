from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

# Read CSV file
df = pd.read_csv("quantium-starter-repo/output.csv")

# Convert columns
df["Sales"] = pd.to_numeric(df["Sales"])
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values("date")

# Total sales KPI
total_sales = df["Sales"].sum()


# Function to create chart
def create_chart(region):

    if region == "all":
        chart_data = df.groupby("date")["Sales"].sum().reset_index()
        title = "Total Pink Morsel Sales"

    else:
        chart_data = (
            df[df["region"] == region]
            .groupby("date")["Sales"]
            .sum()
            .reset_index()
        )
        title = f"{region.capitalize()} Pink Morsel Sales"


    fig = go.Figure(
        data=[
            go.Scatter(
                x=chart_data["date"],
                y=chart_data["Sales"],
                mode="lines",
                name="Sales",
                line={
                    "shape": "spline",
                    "width": 4
                }
            )
        ]
    )

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Sales (USD)",
        template="plotly_white",
        hovermode="x unified"
    )

    return fig



# App layout
app.layout = html.Div(
    [

        # Header
        html.Div(
            [
                html.H1(
                    "Soul Foods",
                    style={
                        "color": "white",
                        "fontSize": "42px",
                        "marginBottom": "5px"
                    }
                ),

                html.P(
                    "Pink Morsel Sales Dashboard",
                    style={
                        "color": "white",
                        "fontSize": "22px"
                    }
                )

            ],
            style={
                "padding": "20px",
                "textAlign": "center",
                "background": "linear-gradient(90deg, #ff758c, #ff7eb3)",
                "borderRadius": "20px",
                "boxShadow": "0px 5px 15px rgba(0,0,0,0.3)"
            }
        ),


        # Total sales card
        html.Div(
            [
                html.H3(
                    "Total Sales",
                    style={
                        "marginBottom": "5px"
                    }
                ),

                html.H2(
                    f"{total_sales:,.0f}",
                    style={
                        "color": "#192344",
                        "fontSize": "36px"
                    }
                )

            ],

            style={
                "backgroundColor": "white",
                "borderRadius": "15px",
                "padding": "15px",
                "marginTop": "20px",
                "textAlign": "center",
                "boxShadow": "0px 4px 10px rgba(0,0,0,0.2)"
            }
        ),


        # Radio button widget
        html.Div(
            [
                html.H3(
                    "Select Region",
                    style={
                        "color": "white"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",

                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],

                    value="all",

                    inline=True,

                    style={
                        "color": "white",
                        "fontSize": "18px"
                    }
                )

            ],

            style={
                "backgroundColor": "rgba(255,255,255,0.1)",
                "borderRadius": "15px",
                "padding": "20px",
                "marginTop": "20px",
                "textAlign": "center"
            }
        ),



        # Chart widget
        html.Div(
            [

                dcc.Graph(
                    id="sales-line-chart",
                    figure=create_chart("all")
                )

            ],

            style={
                "backgroundColor": "white",
                "borderRadius": "20px",
                "padding": "15px",
                "marginTop": "20px",
                "overflow": "hidden",
                "boxShadow": "0px 8px 20px rgba(0,0,0,0.25)"
            }
        )

    ],


    # Page styling
    style={
        "backgroundColor": "#192344",
        "minHeight": "100vh",
        "padding": "20px"
    }

)



# Update chart when region changes
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(region):
    return create_chart(region)



if __name__ == "__main__":
    app.run(debug=True)