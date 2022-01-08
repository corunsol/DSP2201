<!-- #region -->
# Converting HTML to a Jupyter Notebook (.ipynb)

by [Erik Marsja](https://www.marsja.se/author/marsja/) | Oct 21, 2019 | [Programming](https://www.marsja.se/category/programming/), [Python](https://www.marsja.se/category/programming/python/) | [0 comments](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#respond)

![img](https://www.marsja.se/wp-content/uploads/2019/10/how_to_scrape_code_from_html_to_jupyter_notebook-1080x675.jpg)


In this short post, we are going to learn how to turn the code from blog posts to Jupyter notebooks. Specifically, we will learn how to convert HTML to Jupyter Notebooks (.ipynb).

In this post, we are going to use the Python packages [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [json](https://docs.python.org/3/library/json.html), and [urllib](https://docs.python.org/3/library/urllib.html). We are going to use these packages to scrape the code from webpages putting their code within *<code></code>*.

<!-- #endregion -->

Note, this code is not intended to steal other people’s code. I created this script to scrape my code and save it to Jupyter notebooks because I noticed that my code, sometimes did not work as intended. That is, scraping code elements from my own blog posts enabled me to test my scripts in my tutorials.

![img](https://www.marsja.se/wp-content/uploads/2019/10/how_to_convert_a_website_to_jupyter_notebook-1024x361.png)Save

Table of Contents



[Install the Needed Packages](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#Install_the_Needed_Packages)[How to Install Python Packages using conda](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#How_to_Install_Python_Packages_using_conda)[How to Install Python Packages using Pip](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#How_to_Install_Python_Packages_using_Pip)[How to Convert HTML to a Jupyter Notebook (.ipynb)](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#How_to_Convert_HTML_to_a_Jupyter_Notebook_ipynb)[1. Import BeautifulSoup, json, & urllib](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#1_Import_BeautifulSoup_json_urllib)[2. Setting a Custom User-Agent](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#2_Setting_a_Custom_User-Agent)[3. Read the URL](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#3_Read_the_URL)[3. Use BeautifulSoup to Scrape the HTML](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#3_Use_BeautifulSoup_to_Scrape_the_HTML)[4. Create Jupyter Notebook Metadata with json](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#4_Create_Jupyter_Notebook_Metadata_with_json)[5. Getting the Code Elements from the HTML](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#5_Getting_the_Code_Elements_from_the_HTML)[Conclusion: How to Convert HTML to Jupyter Noteboks (.ipynb)](https://www.marsja.se/converting-html-to-a-jupyter-notebook/#Conclusion_How_to_Convert_HTML_to_Jupyter_Noteboks_ipynb)

## Install the Needed Packages

Now, we need to install BeautifulSoup4 before we continue converting HTML to Jupyter notebooks. Furthermore, we need to install lxml.

### How to Install Python Packages using conda

In this section, we are going to learn how to install the needed packages using the packages manager *conda*. First, open up the *Anaconda Powershell Prompt*

Now, we are ready to install BeautifulSoup4.

```
conda -c install anaconda beautifulsoup4 lxmlCode language: Bash (bash)
```

### How to Install Python Packages using Pip

It is, of course, possible to install the packages using *pip* as well:

```
pip install beautifulsoup4 lxmlCode language: Bash (bash)
```

See the more recent post about[ installing packages in Python](https://www.marsja.se/learn-all-about-installing-updating-packages-in-python/) for more information. Now, when you are using pip, you might get a message that there’s a newer version available. If this is the case, upgrading is easy: learn[ how to upgrade pip using pip, conda, and Anaconda variable](https://www.marsja.se/three-easy-methods-to-upgrade-pip-to-the-latest-version/).

## How to Convert HTML to a Jupyter Notebook (.ipynb)

Now, when we have installed the Python packages, we can continue with scraping the code from a web page. In the example, below, we will start by importing BeautifulSoup from bs4, json, and urllib. Next, we have the URL to the webpage that we want to convert to a Jupyter notebook (this).

### 1. Import BeautifulSoup, json, & urllib

Start by importing the needed packages:

```
from bs4 import BeautifulSoup
import json
import urllib

url = 'https://www.marsja.se/python-manova-made-easy-using-statsmodels/'Code language: Python (python)
```

### 2. Setting a Custom User-Agent

In the next line of code, we create the dictionary *headers*.

```
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'\
             '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}Code language: Python (python)
```

This is because many websites (including the one you are reading now) will block web scrapers and this will prevent that from happening. In the next code chunk, we are going to create a Request object. This object represents the HTTP request we are making.

### 3. Read the URL

In the third step, we use Request to read the URL:

```
req = urllib.request.Request(url,
    headers=headers)
  page = urllib.request.urlopen(req)
  text = page.read()Code language: Python (python)
```

Simply put, in the code chunk above, we created a Request object that specifies the URL we want to retrieve. Furthermore, we called *urlopen* using the Request object. This will, in turn, make a response object for the requested URL. Finally, we used*.read()* on the response to get the data.

### 3. Use BeautifulSoup to Scrape the HTML

We are now going to use BeautifulSoup4 to get make it easier to scrape the HTML:

```
soup = BeautifulSoup(text, 'lxml')
soupCode language: Python (python)
```

![img](https://www.marsja.se/wp-content/uploads/2019/10/convert_html_to_jupyter_notebook_scraping.png)Save

### 4. Create Jupyter Notebook Metadata with json

Now we’re ready to convert HTML to a Jupyter Notebook (this code was inspired by this [code example](https://icecube.wisc.edu/~icecube-bootcamp/bootcamp2019/introduction/convert.py)). First, we start by creating some metadata for the Jupyter notebook.

![img](https://www.marsja.se/wp-content/uploads/2019/10/convert_website_to_jupyter_notebook_code.png)Save

Jupyter notebook metadata

In the code below, we start by creating a dictionary in which we will, later, store our scraped code elements. This is going to be the metadata for the Jupyter notebook we will create. Note, .ipynb are simple JSON files, containing text, code, rich media output, and metadata. The metadata is not required but here we will add what language we are using (i.e., Python 3).

```
create_nb = {'nbformat': 4, 'nbformat_minor': 2, 
              'cells': [], 'metadata': 
             {"kernelspec": 
              {"display_name": "Python 3", 
               "language": "python", "name": "python3"
  }}}Code language: Python (python)
```

![img](https://www.marsja.se/wp-content/uploads/2019/10/how_to_scrape_html_convert_python_code_to_jupyter_notebook-1.png)

Example code cell from a Jupyter Notebook

More information bout the format of Jupyter notebooks can be found [here](https://ipython.org/ipython-doc/dev/notebook/nbformat.html).

### 5. Getting the Code Elements from the HTML

In the last step, we are creating a Python function called *get_code*. This function will take two arguments. First, the beautifulsoup object, we earlier created, and the content_class to search for content in. In the case, of this particular WordPress, blog this will be *post-content*

```
def get_data(soup, content_class):
    for div in soup.find_all('div', 
                             attrs={'class': content_class}):
        
        code_chunks = div.find_all('code')
        
        for chunk in code_chunks:
            cell_text = ' '
            cell = {}
            cell['metadata'] = {}
            cell['outputs'] = []
            cell['source'] = [chunk.get_text()]
            cell['execution_count'] = None
            cell['cell_type'] = 'code'
            create_nb['cells'].append(cell)

get_data(soup, 'post-content')

with open('Python_MANOVA.ipynb', 'w') as jynotebook:
    jynotebook.write(json.dumps(create_nb))Code language: Python (python)
```

Next, we are looping through all *div* tags in the soup object. Here, we only look for the post content. Next, we get all the code chunks searching for all *code* tags

In the final loop, we are going through each code chunk and creating a new dictionary (*cell*) in which we are going to store the code. The important part is where we add the text, using the *get_text* method. Here we are getting our code from the code chunk and add it to the dictionary.

![img](https://www.marsja.se/wp-content/uploads/2019/10/convert_html_to_ipynb.png)

Finally, we add this to the dictionary, *nb_data*, that will contain the data that we are going to save as a Jupyter notebook (i.e., the blog post we have scraped).

- More about [parsing JSON in Python](https://www.marsja.se/how-to-read-and-write-json-files-using-python-and-pandas/)

Note, we get the *nb_data* which is a dictionary from which we will create our notebook. In the final two rows, of the code chunk, we will open a file (i.e., test.ipynb) and write to this file using the json dump method.

[Here’s a Jupyter notebook ](https://github.com/marsja/jupyter/blob/master/convert_html_jupyter_notebook_tutorial.ipynb)containing all code above.

## Conclusion: How to Convert HTML to Jupyter Noteboks (.ipynb)

In this post, we have learned how to convert HTML pages to Jupyter notebooks. Specifically, we used BeautifulSoup, lxml, and Python.
