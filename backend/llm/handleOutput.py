import json
import markdown
import pdfkit

def combineJsonToMD(filename: str):
    markdown = ""
    with open(filename, "r") as file:
        data = json.load(file)
        for item in data["content"]:
            concept = item["concept"]
            questions = item["questions"]
            markdown += f"# {concept}\n\n"
            markdown += "## Questions\n\n"
            markdown += questions
            markdown += "\n\n---\n\n"
    return markdown

def saveMarkdownToFile(markdownStr: str, filename: str):
        # Convert Markdown to HTML
    html_content = markdown.markdown(markdownStr)
    with open(filename, 'w') as file:
        file.write(html_content)
    # Save HTML content as PDF
    #pdfkit.from_string(html_content, f'{filename}.pdf')

if __name__ == "__main__":
    # Combine JSON to Markdown
    markdown_content = combineJsonToMD("questions.json")
    
    # Save Markdown to PDF
    saveMarkdownToFile(markdown_content, "questions.md")