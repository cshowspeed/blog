# Import necessary libraries
import re

# Define copyright information to insert
copyright_info = '''<footer style="text-align: center; padding: 5px 0; margin-top: 10px;">
    <p>Copyright &copy; 2018-2024 <a href="https://cshowspeed.github.io/blog">C's Blog</a>. All Rights Reserved.</p>
</footer>\n'''

# Open the index.html file
with open("index.html", "r+", encoding="utf-8") as file:
    # Read the content of the file
    content = file.read()
    
    # Find the </body> tag and insert the copyright information before it
    updated_content = re.sub(r"(</body>)", copyright_info + r"\1", content, count=1)
    
    # Rewind to the start of the file and write the modified content
    file.seek(0)
    file.write(updated_content)
    file.truncate()  # Remove any remaining old content in the file

print("Copyright information has been added just above the </body> tag in index.html.")
