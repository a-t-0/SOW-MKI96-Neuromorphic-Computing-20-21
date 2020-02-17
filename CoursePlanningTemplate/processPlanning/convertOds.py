# prerequisites: 
# 0. requires python 3.x (or higher)
# 1. Depending on locations might require long path enabled for win32: 
# 1.1 Press: start>Type: run>Type: gpedit.msc <enter>>Go to: Computer Configuration\Administrative Templates\System\Filesystem
# 1.2 And enable: "Enable Win32 long paths".
# 2. Then also enable long paths in regedit:
# 2.1 Press: start>Type: regedit<enter>>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
# 2.2 And enable: LongPathsEnabled
# open cmd
# browse to this directory
# install pyexcel with:
# python -m pip install pyexcel
# python -m pip install pyexcel-ods (outdated)
# python -m pip install pyexcel-ods3 (outdated)
# python -m pip install pyexcel-xlsx
# python -m pip install pyexcel-xlsxw (ignored)
# run this script with:
# python convertOds.py
import pyexcel
import glob
import os
import subprocess

def convert_to_xlxs():
    os.chdir(".")
    for file in glob.glob("../*.ods"):
        #for sheet in file:
         #   print(sheet)
        #sheet = pyexcel.get_sheet(file_name = file)
        sheet = pyexcel.get_sheet(file_name = file,sheet_name = "Course")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Lectures")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Assignments")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "OldExams")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Exercises")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "StudyMaterial")
        sheet += pyexcel.get_sheet(file_name = file,sheet_name = "Exam")

        #print(sheet)
        sheet.save_as(file + '.xlsx')

def run_excel_module_from_python():
    import os, os.path
    import win32com.client

    if os.path.exists("GenerateTwCommandsAndLatexTemplates.xlsm"):
        xl=win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath("GenerateTwCommandsAndLatexTemplates.xlsm"), ReadOnly=1)
        xl.Application.Run("GenerateTwCommandsAndLatexTemplates.xlsm!Module1.main")
        ##    xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit() # Comment this out if your excel script closes
        del xl

def create_latex_exam_solution_templates():
    import os, os.path
    import win32com.client

    if os.path.exists("GenerateTwCommandsAndLatexTemplates.xlsm"):
        xl=win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath("GenerateTwCommandsAndLatexTemplates.xlsm"), ReadOnly=1)
        xl.Application.Run("GenerateTwCommandsAndLatexTemplates.xlsm!Module2.createExamSolutionTemplates")
        ##    xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit() # Comment this out if your excel script closes
        del xl

convert_to_xlxs()
print("Converted .ods to .xlxs in parentfolder.")
run_excel_module_from_python()
print("Completed evaluation of excel subroutine")
subprocess.call("cscript CsvTasks/readCSV.vbs") # works
print("Created taskwarrior commands.")