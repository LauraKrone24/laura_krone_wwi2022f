# Lecture Test

Here you can write some documentation as markdown file (md5). It will be added to the python package

## Getting Started
When you face ModuleNotFoundError: No module named 'pyspark' then you most like miss an enviornment.

![Settings](No_Module_Found_Error.png)

### Resolution
Your python distribution cannot find pyspark. You have to run pip (the packaging manager of python) before.
1. Create a virtual environment, see https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env
2. Do not create them in the same project directory, e.g. create a separate Folder for the virtual environment (venv). 
For Example: ![folder](folder_venv.png)

Example is the extracted code from this repository, whereas venv is the folder where you create an environment
3. Open the extracted (unzipped) Project or create a new one
4. Head to IDE and Project Settings in the right above corner
   ![Settings](IDE_and_Project_Settings.png)
5. Go to Preferences and following window will pop up
   ![Python Interpreter](Python_Interpreter.png)

If you have never set anything up, it will be looking like that. Python Interpreter <No Interpreter> 

6. Click on the small error and open all available interpreters by selection "Show All", a list similar to the list below
appears
   ![Available_Interpreter](Selected_VEnv.png)
7. Click on "+" to add your interpeter. Fit the interpreter to your environment, for example:
   ![Create Interpreter](create_python_interpreter.png)
8. Your created environment appears on the list. By default following packages are installed:
   ![Installed Packages](Installed_Packages.png)
9. Select it and close the wizard. Your IDE should now recognize the missing packages
   ![Install_requirements](Install_Requirements.png)

Click on install requirements, then restart your IDE. 

10. You're ready to go, if everything looks like
    ![Ready2Go](final_State.png)