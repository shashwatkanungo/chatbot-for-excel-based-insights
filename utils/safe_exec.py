import matplotlib.pyplot as plt
import pandas as pd
import io
import contextlib
import traceback


def execute_code(code: str, df: pd.DataFrame):

    local_env = {'df': df, 'pd': pd, 'plt': plt}
    result = None
    fig = None

    try:
        lines = code.strip().split('\n')
        if not lines:
            return "No code to execute.", None

        *body, last = lines


        print("=== Executing Code ===")
        print("Body:")
        print('\n'.join(body))
        print("Last Line (eval or exec):")
        print(last)


        exec('\n'.join(body), {}, local_env)


        try:
            result = eval(last, {}, local_env)
        except SyntaxError:
            exec(last, {}, local_env)
            result = None


        if plt.get_fignums():
            fig = plt.gcf()

        return result, fig

    except Exception as e:
        error_trace = traceback.format_exc()
        return f"Execution Error:\n{str(e)}\n\nTraceback:\n{error_trace}", None