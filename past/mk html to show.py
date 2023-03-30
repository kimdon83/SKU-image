# %%
from jinja2 import Template

template_html = """
<table>
    <thead>
        <tr>
            <th>Material</th>
            <th>Image URLs</th>
        </tr>
    </thead>
    <tbody>
        {% for material, urls in image_urls.items() %}
        <tr>
            <td>{{ material }}</td>
            <td>
                <ul>
                    {% for idx, url in urls.items() %}
                    <a href={{ url }}> img{{idx}}</a>
                    {% endfor %}
                </ul>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
"""
# %%
import pandas as pd
image_urls=pd.read_csv("img_draft3.csv",)
image_urls=image_urls.set_index('material')
dic=image_urls.to_dict('index')

template = Template(template_html)
html_out = template.render(image_urls=dic)

# %%
with open('teste_rendered.html', 'w') as file:
    file.write(html_out)
# %%
