# Creating python project using cookicutter

## Environment setup
* `pip install --upgrade pip setuptools wheel`
* while installing, if you selected: `Add Python to PATH` then python and pip should be available in cmd
  * open cmd
  * check pip: type pip and enter (will show pip commands)
  * check python: type python and enter (will show python version)
  * If "Add Python to PATH" not selected, make `pip` available (`pip` is installed with python):
    * launch python installer
    * modify
    * add python to environment variables
    * (can manually add Scripts folder to environment variable to make pip available if Add Python to PATH did not work for pip)
    * https://docs.python.org/3/using/windows.html#finding-the-python-executable
* install cookiecutter
  * `pip install cookiecutter` and `pip install --upgrade cookiecutter`
  * https://cookiecutter.readthedocs.io/en/latest/installation.html
* add `cookiecutter.exe` location to environment variable
  * environment variable > system variable > path > new 
  * `C:\Users\<foo>\AppData\Roaming\Python\Python38\Scripts`
  * check cookiecutter: open cmd, type cookiecutter enter (should show: `Usage: cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]...`)

## Creating project from template
* create a folder and name it: "py project generation"
* download python project template (download zip, extract)
  * https://github.com/Kwpolska/python-project-template
  * https://github.com/wdm0006/cookiecutter-pipproject
  * https://github.com/cookiecutter/cookiecutter#python
* put extracted template to "py project generation" folder
* install requirements for template:
  * "py project generation" folder > right click > open git bash
  * `pip install -r python-project-template/requirements.txt`
  * (`pip install -r python-project-template-master/requirements.txt`)
* edit `python-project-template/cookiecutter.json` (add your information):
	```json
	{
		"full_name": "HASSAN MD TAREQ",
		"email": "hassan@hovermind.com",
		"aur_email": "aur@hovermind.com",
		"github_username": "hovermind",
		"project_name": "Foo",
		"repo_name": "foo",
		"project_short_description": "Foo python app",
		"release_date": "2019-12-31",
		"year": "2019",
		"version": "1.0",
		"entry_point": ["none", "cli", "gui"]
	}
	```
* generate project:
  * check current location in git bash or cmd (it has to be in "py project generation" folder, `cd py project generation` if needed)
  * Command: `cookiecutter --no-input foo` (i.e. `cookiecutter --no-input python-project-template-master`)
    * `--no-input`: does not ask questions for tempate replacement, uses `cookiecutter.json`
	* `foo`: name of the tempate to use (template should be in [where you are generating project])
    * Usage: `cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]`
    * for help: `cookiecutter -h`
  * check: project should be created inside "py project generation" folder (repo_name/project_name from `cookiecutter.json`)
