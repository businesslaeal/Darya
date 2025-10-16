from bs4 import BeautifulSoup

# Read the original HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all direct children of the body tag that are divs
page_containers = soup.body.find_all('div', recursive=False)

# Wrap each container
for i, container in enumerate(page_containers):
    # Create the wrapper div
    wrapper = soup.new_tag('div', attrs={
        'class': '__page-wrapper',
        'data-page': str(i + 1),
        'style': 'width:210mm;height:297mm;box-sizing:border-box;margin:0 auto;padding:12mm;overflow:visible;page-break-after:always;break-after:page;position:relative;'
    })

    # Create the separator element
    separator = soup.new_tag('div', attrs={'style': 'text-align:center;'})
    separator.string = "جداشوند"

    # Insert the wrapper before the container in the DOM
    container.insert_before(wrapper)

    # Move the container inside the wrapper
    wrapper.append(container)

    # Prepend the separator to the wrapper
    wrapper.insert(0, separator)

# Write the modified HTML back to the file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully wrapped page containers.")