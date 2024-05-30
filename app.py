from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/timeseries')
def timeseries():
    # 生成示例数据
    dates = pd.date_range(start='2020-01-01', periods=100, freq='M')
    data = {
        'Date': dates,
        'Interest Rate': (0.02 + 0.03 * np.random.randn(100)).cumsum()
    }
    df = pd.DataFrame(data)
    
    # 创建图表
    fig = px.line(df, x='Date', y='Interest Rate', title='Time Series of Interest Rates')
    graph_html = pio.to_html(fig, full_html=False)
    
    return render_template('timeseries.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
