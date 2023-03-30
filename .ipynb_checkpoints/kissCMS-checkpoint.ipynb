{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ID와 비밀번호 가져오기\n",
    "server = data['server']\n",
    "database = data['database']\n",
    "username = data['username']\n",
    "password = data['password']\n",
    "\n",
    "connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password\n",
    "connection_url = URL.create(\"mssql+pyodbc\", query={\"odbc_connect\": connection_string})\n",
    "engine = create_engine(connection_url)\n",
    "print(\"Connection Established:\")\n",
    "\n",
    "df_mtrl= pd.read_sql(\"\"\"( SELECT material FROM [ivy.mm.dim.fact_poasn] WHERE act_date >=getdate() GROUP BY material )\n",
    "UNION \n",
    "(SELECT material from [ivy.mm.dim.mrp01] WHERE total_stock>0 GROUP BY material)\n",
    "ORDER BY material\"\"\", con=engine\n",
    ")\n",
    "df_mtrl.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=input(\"you have to login to okta before going to cms\")\n",
    "\n",
    "img_list=[]\n",
    "for index, row in df_mtrl.iterrows():\n",
    "    # if index>3415:\n",
    "    try:\n",
    "        url = data['search_url']+ row.material+\"&order_by=modified\"\n",
    "        \n",
    "        driver.get(url)\n",
    "        time.sleep(1)   \n",
    "        Images=driver.find_elements(By.CLASS_NAME,\"ImageWrapperLarge\")\n",
    "        inlist=[row.material]\n",
    "        for index0 in range(len(Images)):\n",
    "            con1='Front' in Images[index0].get_attribute('title')\n",
    "            con2='front' in Images[index0].get_attribute('title')\n",
    "            con3= row.material in Images[index0].get_attribute('title')\n",
    "            if ((con1 | con2) &con3):\n",
    "                html = Images[index0].get_attribute('innerHTML')\n",
    "                soup = BeautifulSoup(html, 'html.parser')\n",
    "                img_tag = soup.find('img')\n",
    "                img_url = img_tag.get('src')\n",
    "                inlist.append(img_url)\n",
    "        img_list.append(inlist)\n",
    "    except:\n",
    "        print(row.material)\n",
    "\n",
    "img_list= pd.DataFrame(img_list)\n",
    "img_list.to_csv('img_test3.csv')\n",
    "\n",
    "driver.quit()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from jinja2 import Template\n",
    "\n",
    "template_html = \"\"\"\n",
    "<table>\n",
    "    <thead>\n",
    "        <tr>\n",
    "            <th>Material</th>\n",
    "            <th>Image URLs</th>\n",
    "        </tr>\n",
    "    </thead>\n",
    "    <tbody>\n",
    "        {% for material, urls in image_urls.items() %}\n",
    "        <tr>\n",
    "            <td>{{ material }}</td>\n",
    "            <td>\n",
    "                <ul>\n",
    "                    {% for idx, url in urls.items() %}\n",
    "                    <a href={{ url }}> img{{idx}}</a>\n",
    "                    {% endfor %}\n",
    "                </ul>\n",
    "            </td>\n",
    "        </tr>\n",
    "        {% endfor %}\n",
    "    </tbody>\n",
    "</table>\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "image_urls=pd.read_csv(\"img_draft3.csv\",)\n",
    "image_urls=image_urls.set_index('material')\n",
    "dic=image_urls.to_dict('index')\n",
    "\n",
    "template = Template(template_html)\n",
    "html_out = template.render(image_urls=dic)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('teste_rendered.html', 'w') as file:\n",
    "    file.write(html_out)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
