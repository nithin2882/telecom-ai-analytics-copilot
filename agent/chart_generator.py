import plotly.express as px


def generate_chart(df, question):

    columns = list(df.columns)

    if len(columns) < 2:
        return None

    x = columns[0]
    y = columns[1]

    question = question.lower()

    if "trend" in question or "month" in question or "date" in question:

        fig = px.line(
            df,
            x=x,
            y=y,
            title=question.title()
        )

    elif "distribution" in question or "share" in question:

        fig = px.pie(
            df,
            names=x,
            values=y,
            title=question.title()
        )

    else:

        fig = px.bar(
            df,
            x=x,
            y=y,
            title=question.title()
        )

    return fig