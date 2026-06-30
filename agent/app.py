from sql_generator import generate_sql
from sql_executor import SQLExecutor
from insight_generator import generate_insight
from chart_generator import generate_chart


def main():

    print("=" * 60)
    print(" Telecom AI Analytics Copilot")
    print("=" * 60)

    question = input("\nAsk a business question:\n> ")

    sql = generate_sql(question)

    print("\nGenerated SQL\n")
    print(sql)

    executor = SQLExecutor()

    try:

        result = executor.execute(sql)

        print("\nQuery Result\n")
        print(result)

        insight = generate_insight(
        question,
        sql,
        result
        )

        print("\n")
        print("=" * 60)
        print("BUSINESS INSIGHT")
        print("=" * 60)
        print()

        print(insight)

        fig = generate_chart(result, question)

        if fig:

         fig.show()

        

    except Exception as e:

        print("\nSQL Execution Failed\n")
        print(e)

    finally:

        executor.close()


if __name__ == "__main__":
    main()