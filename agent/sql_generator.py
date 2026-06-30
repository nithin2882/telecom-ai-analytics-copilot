import ollama

from prompts import SQL_PROMPT

MODEL = "qwen3:4b"


def generate_sql(question):

    prompt = f"""

{SQL_PROMPT}

Question:

{question}

"""

    response = ollama.chat(

        model=MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    sql = response["message"]["content"]

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql