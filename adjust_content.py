from bs4 import BeautifulSoup, Comment

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# 1. Constrain images (placeholder divs)
# These are divs with a specific background color and border, acting as image placeholders.
image_placeholders = soup.find_all('div', style=lambda s: s and 'background-color: #f0f0f0' in s)
for img in image_placeholders:
    # Create a TODO comment
    # TODO: Replace this placeholder div with an actual <img> tag.
    # The image filename is likely related to the figure number in the caption below.
    comment = Comment(" TODO: Replace this placeholder div with an actual <img> tag. The image filename is likely related to the figure number in the caption below. ")
    img.insert_before(comment)

    # Apply styles to the placeholder
    img['style'] = "max-width:100%; max-height: calc(297mm - 24mm); object-fit: contain; " + img.get('style', '')

# 2. Add page-break-inside: avoid to tables and lists
for element in soup.find_all(['table', 'ul']):
    style = element.get('style', '')
    if 'page-break-inside' not in style:
        element['style'] = style + ' page-break-inside: avoid;'

# 3. Neutralize absolute positioning
# Find all elements with absolute positioning inside a page wrapper
page_wrappers = soup.find_all('div', class_='__page-wrapper')
for wrapper in page_wrappers:
    absolute_elements = wrapper.find_all(style=lambda s: s and 'position: absolute' in s)
    for elem in absolute_elements:
        style = elem['style']
        # Replace absolute with relative and remove top/left/right properties
        new_style = style.replace('position: absolute', 'position: relative')
        new_style = ';'.join([s.strip() for s in new_style.split(';') if not s.strip().startswith(('top:', 'left:', 'right:'))])
        elem['style'] = new_style

# Write the modified HTML back to the file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully adjusted content for printing.")