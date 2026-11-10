
"""
Note Sorter Web Page (Gradio).
Keep this file in the same folder as note_sorter.py.
Run: python note_sorter_app.py
Then open http://127.0.0.1:7860
"""

import gradio as gr
import note_sorter as d


def sort_note(text):
    # Check if the user entered a note
    if not text.strip():
        return "Unknown", "Please type or paste a note above."

    # Classify the note
    verdict = d.classify(text)

    if verdict == "unknown":
        report = "### Result: Unknown\nNot enough evidence. Try a longer note."
    else:
        report = f"### Result: {verdict}\nYour note has been sorted into the **{verdict}** category."

    return verdict, report


def categories_known():
    lines = [
        f"- **{name}**: {len(profile)} different words"
        for name, profile in d.PROFILES.items()
    ]

    return (
        f"The Note Sorter knows **{len(d.PROFILES)} categories:**\n\n"
        + "\n".join(lines)
    )


with gr.Blocks(title="Note Sorter") as demo:

    gr.Markdown("# 📝 Note Sorter")
    gr.Markdown("Enter a note and the system will automatically find its category.")

    with gr.Tab("Sort Notes"):

        text = gr.Textbox(
            lines=4,
            label="Your Note",
            placeholder="Type or paste your note here..."
        )

        result = gr.Textbox(label="Category")
        report = gr.Markdown()

        gr.Examples(
            [
                ["the goal won the match"],
                ["he bakes the cake and the bread"],
                ["the singer plays the guitar"],
                ["pasta with sweet cream"],
                ["the band wins the match"],
            ],
            inputs=text
        )

    with gr.Tab("Categories I Know"):
        known = gr.Markdown()

    text.change(
        sort_note,
        inputs=text,
        outputs=[result, report]
    )

    demo.load(
        categories_known,
        inputs=None,
        outputs=known
    )


if __name__ == "__main__":
    demo.launch()
