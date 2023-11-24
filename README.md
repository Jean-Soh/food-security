# DTP DDW website

**Table of Contents**


- [Setup](#setup)

- [Install Git](#install-git)

- [Downloading Repository](#downloading-repository)

- [Create Virtual Environment](#create-virtual-environment)

- [Brief Overview of Flask Project Structure](#brief-overview-of-flask-project-structure)

- [HTML](#html)

- [Using Transcrypt](#using-transcrypt)

- [Run Flask](#run-flask)

- [Page 1](#page-1)

- [Page 2](#page-2)

  

<!-- markdown-toc end -->
## Predict food security
The Web app has a function to make predictions using a ML model developed by the team. The Web app has two pages, one takes in the parameters and predicts the food security. The other function takes in a percentage change of a certain variable and returns the percentage change of food security. The goal is to help policymakers researchers and buisness owners predect food security. 
## Setup

  

### Install Git

  

You need to have Git to do the project. Download and install the software according to your OS:

- Windows: [Git for Windows](https://git-scm.com/download/win)

- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

  

### Downloading Repository

Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

  

```shell

cd  Downloads

git  clone  https://github.com/Jean-Soh/food-security.git

```

  

### Go to main folder page

  

Once you have downloaded the repository, you can go to the repository and to the folder called `Main` 

  

Windows:

```dos

cd Web_app\main

dir

```

  

Unix/MacOS

```shell

cd  Web_app/main

ls

```

  

The last command should output the following:

  

```shell

runflaskvoc.sh

application.py

Pipfile

app

```

  

### Create Virtual Environment

  

**You should open Command Prompt to do the following steps.**

  

In the following steps, whenever there is a different between the OS commands, the **Windows** prompt will be represented by:

```shell

>

```

while the MacOS/Linux prompt will be represented by:

```shell

$

```

  

Go to the root folder `Main`.

  

Windows:

```dos

> cd %USERPROFILE%\Downloads\food-security\Web_app\main

```

  

Unix/MacOS:

```shell

$  cd  ~/Downloads/food-security/Web_app/main

```

  

First make sure that you have installed `pipenv` package.

  

```shell

python  -m  pip  install  --user  pipenv

```

We will call `mp_sort` folder as the **root** folder of our application.

From the root folder, install the packages specified in the `Pipfile`.

```shell

python  -m  pipenv  install

```

  

The above steps will install Flask and Transcrypt Python libraries and some other necessary packages.

  
  

To activate the virtualenv, run

```shell

python  -m  pipenv  shell

```

  

Alternatively, you can choose everytime you run a command to prepend that command with the following:

```shell

python  -m  pipenv  run

```

  

Ok, so let's enter into the shell by typing:

```shell

python  -m  pipenv  shell

```

  

You should see the word `(Main)` in your prompt something like:

  

Windows:

```dos

(Main) folder >

```

Unix/MacOS:

```shell

(Main) user $

```

  

_To exit the virtual environment at the end of this mini project, simply type:_

```shell

exit

```

  

All the subsequent exercises assumes you are in the virtualenv shell.

  
  

## Brief Overview of Flask Project Structure

  

We are using Flask web framework to create this web app. The first file you may notice is `application.py` in the root folder. Open that file using a text editor. You should see the following:

  

```python

from app import application

  

if  __name__  ==  "__main__":

application.run(host="0.0.0.0", port=8080, debug=True)

```

  

The last two lines runs the `application` object when it is run on the shell. The value will be used when you deploy it to Amazon Elastic Beanstalk. It also enables the debug mode to `True` so that you can see any error messages when they occur. The `application` object is imported in the first line from the `app` package. The `app` package is in a folder called `app`:

  

```shell

Main/

app/

__init__.py

middleware.py

routes.py

static/

templates/

```

  

The file `__init__.py` contains the line that creates the `application` object as a `Flask` instance.

  

```python

from flask import Flask

  

application =  Flask(__name__)

  

from app import routes

```

  

This file also import the file `routes.py` which defines the URL routing.

  

```python

from flask import render_template

from app import application

  

@application.route('/')

@application.route('/index')

def  index():

return  render_template('index.html', title='DTP project')

  

@application.route('/ex1')

def  exercise1():

return  render_template('ex1.html', title='Page 1')

  

@application.route('/ex2')

def  exercise2():

return  render_template('ex2.html', title='Page 2')

```

  

The first route indicates when a user enter the URL with "/" or "/index" at the end, our web app will serve this request by calling `index()` function. The `index()` function will return a HTML response following a template called `index.html`. This file `index.html` can be found inside the `templates` folder.

  

```shell

Main/

app/

__init__.py

routes.py

static/

templates/

base.html

index.html

ex1.html

ex2.html

```

  

The other two routes does the same by serving any request to "/ex1" and "/ex2". The templates for these two are provided inside the `template` folder.

  

### HTML

HTML code normally contaixns of two section, the header and the body.
Let's open `index.html`. The first few lines are shown here.

```html
{% extends "base.html" %}

{% block app_content %}
<h1>This is our DTP project</h1>
```

- The first line `{% extends "base.html" %}` inherits the `base.html` for some of the common elements such as the navigation bar, importing certain scripts, and CSS files. The javascript which we will translate from the file `library.py` is imported in the last few lines of `base.html`.
- The second line indicates the block `app_content`. Each html file templates we have will modify this block `app_content`. 

The `<title>` set the title of the page. Inside this tag we found `{{title}}`. The two curly braces is a Jinja template syntax that allow you to change the HTML code. It is a kind of variable that you can set. This variable `title` is actually set when `render_template()` is called in `routes.py`.

  

```python

@application.route('/ex1')

def  exercise1():

return  render_template('ex1.html', title='Page 1')

```

  

In this code, the variable `title` is set to `Page 1`.

  

The second tag `<script ...>...</script>` is to import our script. We will generate this Javascript file `library.js` from our Python `library.py` file inside the `static` folder.

  

```shell

mp_sort/

app/

__init__.py

routes.py

static/

library.py

```

  

All the logic for this web app is done inside `library.py`.

The web app can also has a dark mode function. It can be found in the `base.html`file.  

    <div>
		<button  class="btn btn-primary"  onclick="darkMode()">dark mode</button>
	</div>

  This button element calls the function darkMode() which can be found in the script element 
  

	   <body  data-bs-theme="dark">

		<script>

			document.body.dataset.bsTheme  =  localStorage.getItem("dark_mode")

			function  darkMode() {

				var  element  =document.body;

				element.dataset.bsTheme  ==  'light'  ?  localStorage.setItem("dark_mode", "dark") :  localStorage.setItem("dark_mode", "light")

				element.dataset.bsTheme  =  localStorage.getItem("dark_mode")

			}

		</script>
At the top of the code is `data-bs-theme="dark"`styeling tag, this controls if the page is in dark mode or not. The following code in the script element first checks a local storage value of dark_mode and assigns it's value to the styeling tag for the body. Within the script element there is also the fuction that is called with each button press.  

### Using Transcrypt

  

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

  

Windows:

```dos

> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort\app\static

> dir

```

  

Unix/MacOS:

```shell

$  cd  ~/Downloads/d2w_mini_projects/mp_sort/app/static

$  ls

```

  
  

The last command will list the file in that folder, and you should see:

```shell

library.py

```

  

Run Transcrypt on `library.py`:

  

```shell

python  -m  transcrypt  -b  -n  library

```

  

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

  

Windows:

```dos

> dir

> dir __target__

```

  

Unix/MacOS:

```shell

$  ls

$  ls  __target__

```

  

The output should be something like the following:

```shell

__target__/

library.js

library.project

math.js

org.transcrypt.__runtime__.js

random.js

```

  

You should see `library.js` created inside this folder.

  

### Run Flask

  

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

  

Windows:

```dos

> cd ..\..

```

  

Unix/MacOS:

```shell

$  cd  ../..

```

which means go up the folder two times. Or, simply

  

Windows:

```dos

> cd %USERPROFILE\Downloads\d2w_mini_projects\mp_sort

```

  

Unix/MacOS:

```shell

$  cd  ~/Downloads/d2w_mini_projects/mp_sort/

```

  
  

You should see `application.py` in this root folder.

  

Now, you can run Flask by typing:

  

```shell

flask  run

```

  

You should see that some output will be thrown out, which one of them would be:

  

```shell

* Running on http://127.0.0.1:5000/ (Press  CTRL+C  to  quit)

```

  

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app.

To stop the web app, type `CTRL+C`.

## Page 1

 The goal of the page is to Predict the state of food insecurity of a nation, given their GDP per capita and % of population with basic handwashing facilities
 
```html<h1>Welcome to {{title}}</h1>
<div  class="col-lg-4">
<label  for="var"  class="form-label">GDP per capita, PPP</label>
<input  for="var"  class="form-control"  id="var"  placeholder="21020"  name="num1">
<label  for="var"  class="form-label">People with basic handwashing facilities including soap and water</label>
<input  for="var"  class="form-control"  id="var"  placeholder="61"  name="num2">
<div  id="sorted">...</div>
<button  class="btn btn-secondary"  onclick="library.function1()">prediction</button>
</div>
```
We have two input for the two variables. The first is for the GDP per capita, ppp the second is for the percent of people with basic handwashing facilities. the button then calls the function `function1` which calculates the predicted value of food security based on the input values
## Page 2

  
Predict changes in food insecurity of a nation, given changes to their GDP per capita and/or % of population with basic handwashing facilities

```html
<div  class="col-lg-4">
<label  for="var"  class="form-label">GDP per capita, PPP</label>
<input  for="var"  class="form-control"  id="var"  placeholder="16553"  name="num1">
<label  for="var"  class="form-label">People with basic handwashing facilities including soap and water</label>
<input  for="var"  class="form-control"  id="var"  placeholder="75"  name="num2">
<label  for="var"  class="form-label">Change in GDP per capita, PPP</label>
<input  for="var"  class="form-control"  id="var"  placeholder="12036"  name="num3">
<label  for="var"  class="form-label">Change in people with basic handwashing facilities including soap and water</label>
<input  for="var"  class="form-control"  id="var"  placeholder="5"  name="num4">
<div  id="sorted">...</div>
<button  class="btn btn-secondary"  onclick="library.function2()">prediction</button>
</div>
```
We have two sets of inputs. The first pair is for the current values the second is for the change in value. the button then calls the function `function2` which calculates the predicted % change of food security based on the input values