# Application for choosing baby names.

Small program build in PyQt5 to help expecting parents in choosing a name for their new family member.
The program is setup with *Danish* names, but is build to manage names provided to it in a .csv-file. The structure can be seen in the section **Importing Names**.


## 

## Importing Names

To import a list of other names, the structure must be as followed:

| Name     | Boy name | Girl name |
|----------|----------|-----------|
| Peter    | 1        | 0         |
| Kathrine | 0        | 1         |
| ...      | ...      | ...       |
| Rene     | 1        | 1         |

The first column simply lists the name.
The two columns Boy name, and Girl name is an indicator for whether the name can be used for a boy, girl, or both sex. 

## 



This could be inspiration. At least for creating the GUI.
https://www.geeksforgeeks.org/python-quiz-application-project/
