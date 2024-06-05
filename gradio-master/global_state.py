import gradio as gr
"""定义一个全局变量可供所有用户使用"""
scores = []

def track_score(score):
    scores.append(score)
    top_scores = sorted(scores, reverse=True)[:3]
    return top_scores

demo = gr.Interface(
    track_score,
    gr.Number(label="Score"),
    gr.JSON(label="Top Scores")
)
demo.launch()