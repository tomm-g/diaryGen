import pandas as pd



def entriesLogging(df):
    sectionTitle = 'Week Starting {weekStart}'.format(weekStart=df['Week Start'])
    sectionTitle = '\section{' + sectionTitle + '}'
    tasks = df['Tasks'] 
    taskTitle  = '\n\subsection{{Tasks}}'
    skills_req = df['Skills Required']
    skillsTitle = '\n\subsection{{Skills}}'
    if pd.isna(df['Comment']) == True:
        comments = ""
    else:
        comments = df['Comment']
    commentsTitle = '\n\subsection{{Comments}}'

    section = '\n\n'+sectionTitle + '\n' + taskTitle + '\n' + tasks + skillsTitle + '\n' + skills_req + commentsTitle + '\n' + comments + '\n\n'
    return section

def diaryLatexGen(dataFile):
    #dataFile = 'diaryEntries.csv'

    entries = pd.read_csv(dataFile)


    entries = entries.dropna(subset=['Tasks'])
    entries['LaTeX'] = entries.apply(lambda df: entriesLogging(df), axis=1)

    preamble = r'''
    \documentclass{article}
    \usepackage{graphicx}
    \usepackage{float}
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{bbm}

    \graphicspath{{./images}}
    \title{Internship Diary}
    \author{}
    \date{}

    \begin{document}

    \maketitle
    \pagebreak
    \tableofcontents
    \pagebreak


    '''

    ending = r'''
    \end{document}
    '''
    fileName = dataFile.split(".")
    texFileName = fileName[0] + ".tex"

    with open(texFileName, 'w') as file:
        file.write(preamble)

        for string in entries['LaTeX']:
            file.write(string)
        file.write(ending)
    print(texFileName, ' written')

    print(entries)

