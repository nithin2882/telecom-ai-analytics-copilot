import ollama

from prompts import INSIGHT_PROMPT

MODEL = "qwen3:4b"


def generate_insight(question, sql, result):

    prompt = f"""
{INSIGHT_PROMPT}

Business Question:
{question}

Generated SQL:
{sql}

SQL Result:

{result.to_markdown(index=False)}

Respond using EXACTLY this format:

## Executive Summary

## Key Findings

## Business Impact

## Recommendation

Keep the response under 150 words.
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

    return response["message"]["content"]