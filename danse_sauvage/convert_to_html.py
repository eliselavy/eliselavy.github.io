import markdown

# Read the Markdown file
with open("resume_dance.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Save the HTML content to a file
with open("resume_dance.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print("Conversion complete! HTML file saved as resume_dance.html")
