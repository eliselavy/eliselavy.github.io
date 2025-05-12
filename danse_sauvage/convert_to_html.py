import markdown

# Read the Markdown file
with open("resume_dance.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Wrap the HTML content in a basic HTML structure with a header and link to style.css
full_html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Dance</title>
    <link rel="stylesheet" href="resume.css">
</head>
<body>
    {html_content}
</body>
</html>
"""

# Save the full HTML content to a file
with open("resume_dance.html", "w", encoding="utf-8") as html_file:
    html_file.write(full_html_content)

print("Conversion complete! HTML file saved as resume_dance.html")
