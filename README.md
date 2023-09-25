# How to upload a Python package to Pypi?

<div style="display: flex; align-items: center;">
  <p>
    The Python Package Index, abbreviated as PyPI, is the official repository of software for the Python programming language. By default, pip — which is the most popular Python package manager — uses PyPI as the source for retrieving package dependencies.
  </p>
  <img src="https://pypi.org/static/images/logo-large.9f732b5f.svg" alt="PyPI logo" style="width: 200px; height: 200px; margin-left: 20px;">
</div>

## 1. PyPi Account

#### 1. Create an account with PyPi **[here](https://pypi.org/account/register/)** and verify your email address

#### 2. In your **[account settings](https://pypi.org/manage/account/)**, scroll down and enable two-factor authentication (2FA)

    1. Enable *PyPI-Recovery-Codes* and save them in a File
    2. Acivate 2FA and scan the QR Code with an Authenticator

        - Botan (programming library)
        - FreeOTP
        - Google Authenticator
        - multiOTP
        - Comparison of TOTP applications

#### 3. Finally, you have to generate an API Token at the bottom of your account settings. You will need the Token later!

## 2. Python Package

#### 1. create a new Folder (package_name) and open it in your favourite **[code editor](https://code.visualstudio.com/download)**

#### 2. create the Files and Folders in your Folder by using the templates listed below. Replace the [] with your own names

**NOTE:** You have to change the Information in every File to your Information

    LICENSE
    MANIFEST.in
    pyproject.toml
    README.md
    requirements.txt
    setup.py
    /src
        /[package_name]
            src/__init__.py     (empty file)
            [Modul_1].py        (your code)
            [Modul_2].py        (your code)
            you can add more Moduls

It should look like this:

[![Data.png](https://iili.io/JJS1lRI.png)](https://iili.io/JJS1lRI.png)

## 3. PyPi Package

#### 0. install build and twine
**NOTE:** Make shure that you have ``pip`` installed
```
pip install twine
pip install build
```

#### 1. install the Package locally: 
```
cd [package_name]
pip install .
```

[![JJSwbLB.md.png](https://iili.io/JJSwbLB.png)](https://iili.io/JJSwbLB.png)

Now your Repo should look like this:

[![JJSNKIR.png](https://iili.io/JJSNKIR.png)](https://iili.io/JJSNKIR.png)

**NOTE:** You can Test your Package localy before deploying it 

#### 2. building the Package (this Step can take some time)
```
python -m build
```

output (end):
```
Successfully built Package_Name-0.0.1.tar.gz and Package_Name-0.0.1-py3-none-any.whl
```

Now you should have the /dist direcory:

[![JJSPva4.png](https://iili.io/JJSPva4.png)](https://iili.io/JJSPva4.png)

#### 3. deploying the Package
**NOTE:** ``The user 'username' isn't allowed to upload to project 'package_name'.`` means that the Package Name ist allready taken.
```
python -m twine upload dist/*
```
Username = ``__token__``

Password = ``[your Token]``

[![JJSLU9R.md.png](https://iili.io/JJSLU9R.md.png)](https://iili.io/JJSLU9R.md.png)

#### Your Package is now online on PyPi and can be used by downloading it with pip
```
pip install [package_name]
```

## 4. Updating the Package
To update your Package you have to change the version in the ``pyproject.toml`` file.

```
python -m build
python -m twine upload --skip-existing dist/*
```

[![JJSml6P.md.png](https://iili.io/JJSml6P.md.png)](https://iili.io/JJSml6P.md.png)

To install the new Version:
```
pip uninstall Package_Name
pip install Package_Name
```

