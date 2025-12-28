from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv"
# )
#df.to_csv("apple_2014.csv", index=False)   # 新增：保存到本地

df = pd.read_csv(
    "apple_2014.csv"
)
app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Simple stock plot with adjustable axis"),
        html.Button("Switch Axis", n_clicks=0, id="plot-data-from-csv-x-button"),
        dcc.Graph(id="plot-data-from-csv-x-graph"),
    ]
)


@app.callback(
    Output("plot-data-from-csv-x-graph", "figure"),
    Input("plot-data-from-csv-x-button", "n_clicks"),
)
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = "AAPL_x", "AAPL_y"
    else:
        x, y = "AAPL_y", "AAPL_x"

    fig = px.line(df, x=x, y=y)

    # === 新增：插入背景图 ===
    img_url = app.get_asset_url("charming-plot.png")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  # 让绘图区域背景透明
        images=[dict(
            source=img_url,
            xref="paper",
            yref="paper",
            x=0,
            y=1,
            sizex=1,
            sizey=1,
            sizing="stretch",
            layer="below"
        )]
    )
    # ==========================

    return fig


if __name__ == "__main__":
    app.run(debug=True)
