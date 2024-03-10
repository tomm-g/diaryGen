import pandas as pd
import resources.diaryGen as dg
import glob
import subprocess

def texCompile(tex):
    try:
        subprocess.run(["lualatex", tex], check=True)
        print("Compilation Complete...")
    except subprocess.CalledProcessError as e:
        print(f"Compilation Failed, Error: {e}")

dataFiles = glob.glob("*.csv")

for file in dataFiles:
    dg.diaryLatexGen(file)


texFiles = glob.glob("*.tex")

for file in texFiles:
    texCompile(file)






