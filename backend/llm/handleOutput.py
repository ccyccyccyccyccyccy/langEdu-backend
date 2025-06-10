import json
import markdown
import pdfkit
import os

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
    json_path= r"..\..\output\questions_v0.1.json"
    markdown_content = combineJsonToMD(json_path)
    filename= os.path.splitext(json_path)[0]+".md"
    with open (filename, 'w') as file:
        file.write(markdown_content)
    
    # Save Markdown to PDF
    #saveMarkdownToFile(markdown_content, "..\..\output\questions_v0.md")