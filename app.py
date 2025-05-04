{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6ff362f6-dd1e-4bf5-ab1f-26fef03f03ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x18ccb2850>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "from dash import dcc, html\n",
    "from dash.dependencies import Input, Output\n",
    "import plotly.express as px\n",
    "import seaborn as sns\n",
    "\n",
    "df = sns.load_dataset(\"penguins\")\n",
    "\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Penguin Data Explorer\"),\n",
    "    dcc.Dropdown(\n",
    "        id='x-axis',\n",
    "        options=[{'label': col, 'value': col} for col in ['bill_length_mm', 'flipper_length_mm']],\n",
    "        value='bill_length_mm'\n",
    "    ),\n",
    "    dcc.Graph(id='scatter-plot')\n",
    "])\n",
    "\n",
    "@app.callback(\n",
    "    Output('scatter-plot', 'figure'),\n",
    "    Input('x-axis', 'value')\n",
    ")\n",
    "def update_graph(x_axis):\n",
    "    fig = px.scatter(df, x=x_axis, y='body_mass_g', color='species')\n",
    "    return fig\n",
    "\n",
    "app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8bd9d8b1-90e3-40a0-a354-96863289dd89",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip freeze > requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16bc26cc-58ba-45b5-b68c-810680c41a7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
