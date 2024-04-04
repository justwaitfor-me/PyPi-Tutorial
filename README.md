<div>
        <h1><span style="font-weight:normal">How to upload a Python package to Pypi?</span></h1>
        <div style="display: flex; align-items: center;">
            <p>
                The Python Package Index, abbreviated as PyPI, is the official repository of software for the Python
                programming language. By default, pip — which is the most popular Python package manager — uses PyPI as
                the
                source for retrieving package dependencies.
            </p>
            <img src="https://pypi.org/static/images/logo-large.9f732b5f.svg" alt="PyPI logo"
                style="width: 200px; height: 200px; margin-left: 20px;">
        </div>
        <h2><span style="font-weight:normal; font-style:normal">1. PyPi Account</span></h2>
        <h4><span style="font-weight:normal">1. Create an account with PyPi </span><a
                href="https://pypi.org/account/register/" style="text-decoration:none"><span
                    class="Hyperlink">here</span></a><span style="font-weight:normal"> and verify your email
                address</span></h4>
        <h4><span style="font-weight:normal">2. In your </span><a href="https://pypi.org/manage/account/"
                style="text-decoration:none"><span class="Hyperlink">account settings</span></a><span
                style="font-weight:normal">, scroll down and enable two-factor authentication (2FA)</span></h4>
        <p class="IndentedCode"><span>1. Enable *PyPI-Recovery-Codes* and save them in a File</span><br /><span>2.
                Acivate 2FA and scan the QR Code with an Authenticator</span><br /><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>- Botan (programming
                library)</span><br /><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>-
                FreeOTP</span><br /><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>- Google
                Authenticator</span><br /><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>-
                multiOTP</span><br /><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>- Comparison of
                TOTP applications</span></p>
        <h4><span style="font-weight:normal">3. Finally, you have to generate an API Token at the bottom of your
                account
                settings. You will need the Token later!</span></h4>
        <h2><span style="font-weight:normal; font-style:normal">2. Python Package</span></h2>
        <h4><span style="font-weight:normal">1. create a new Folder (package_name) and open it in your favourite
            </span><a href="https://code.visualstudio.com/download" style="text-decoration:none"><span
                    class="Hyperlink">code editor</span></a></h4>
        <h4><span style="font-weight:normal">2. create the Files and Folders in your Folder by using the templates
                listed below. Replace the [] with your own names</span></h4>
        <p><span style="font-weight:bold">NOTE:</span><span> You have to change the Information in every File to
                your
                Information</span></p>
        <p class="IndentedCode">
            <span>LICENSE</span><br /><span>MANIFEST.in</span><br /><span>pyproject.toml</span><br /><span>README.md</span><br /><span>requirements.txt</span><br /><span>setup.py</span><br /><span>/src</span><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0; </span><span>/[package_name]</span><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>src/__init__.py</span><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>(empty file)</span><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>[Modul_1].py</span><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>(your code)</span><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>[Modul_2].py</span><span style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>(your code)</span><br /><span
                style="-aw-import:spaces">&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;&#xa0;
            </span><span>you can add more
                Moduls</span>
        </p>
        <p><span>It should look like this:</span></p>
        <p><a href="https://iili.io/JJS1lRI.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.001.png" width="235" height="291"
                    alt="Data.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <h2><span style="font-weight:normal; font-style:normal">3. PyPi Package</span></h2>
        <h4><span style="font-weight:normal">0. install build and twine</span></h4>
        <p><span style="font-weight:bold">NOTE:</span><span> Make shure that you have </span><span
                class="InlineCode2">pip</span><span> installed</span></p>
        <p class="FencedCode"><span>pip install twine</span><br /><span>pip install build</span></p>
        <h4><span style="font-weight:normal">1. install the Package locally:</span></h4>
        <p class="FencedCode"><span>cd [package_name]</span><br /><span>pip install .</span></p>
        <p><a href="https://iili.io/JJSwbLB.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.002.png" width="1598" height="514"
                    alt="JJSwbLB.md.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <p><span>Now your Repo should look like this:</span></p>
        <p><a href="https://iili.io/JJSNKIR.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.003.png" width="246" height="537"
                    alt="JJSNKIR.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <p><span style="font-weight:bold">NOTE:</span><span> You can Test your Package localy before deploying
                it</span>
        </p>
        <h4><span style="font-weight:normal">2. building the Package (this Step can take some time)</span></h4>
        <p class="FencedCode"><span>python -m build</span></p>
        <p><span>output (end):</span></p>
        <p class="FencedCode"><span>Successfully built Package_Name-0.0.1.tar.gz and
                Package_Name-0.0.1-py3-none-any.whl</span></p>
        <p><span>Now you should have the /dist direcory:</span></p>
        <p><a href="https://iili.io/JJSPva4.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.004.png" width="252" height="641"
                    alt="JJSPva4.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <h4><span style="font-weight:normal">3. deploying the Package</span></h4>
        <p><span style="font-weight:bold">NOTE:</span><span> </span><span class="InlineCode2">The user 'username'
                isn't
                allowed to upload to project 'package_name'.</span><span> means that the Package Name ist allready
                taken.</span></p>
        <p class="FencedCode"><span>python -m twine upload dist/*</span></p>
        <p><span>Username = </span><span class="InlineCode2">__token__</span></p>
        <p><span>Password = </span><span class="InlineCode2">[your Token]</span></p>
        <p><a href="https://iili.io/JJSLU9R.md.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.005.png" width="667" height="207"
                    alt="JJSLU9R.md.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <h4><span style="font-weight:normal">Your Package is now online on PyPi and can be used by downloading it
                with
                pip</span></h4>
        <p class="FencedCode"><span>pip install [package_name]</span></p>
        <h2><span style="font-weight:normal; font-style:normal">4. Updating the Package</span></h2>
        <p><span>To update your Package you have to change the version in the </span><span
                class="InlineCode2">pyproject.toml</span><span> file.</span></p>
        <p class="FencedCode"><span>python -m build</span><br /><span>python -m twine upload --skip-existing
                dist/*</span></p>
        <p><a href="https://iili.io/JJSml6P.md.png" style="text-decoration:none"><img
                    src="https://raw.githubusercontent.com/justwaitfor-me/PyPi-Tutorial/main/images/Aspose.Words.84ff4c03-616d-4aac-b6a5-47737d38c75e.006.png" width="667" height="187"
                    alt="JJSml6P.md.png"
                    style="border-style:none; -aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></a>
        </p>
        <p><span>To install the new Version:</span></p>
        <p class="FencedCode"><span>pip uninstall Package_Name</span><br /><span>pip install Package_Name</span></p>
    </div>

