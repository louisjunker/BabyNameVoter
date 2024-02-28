# Application for choosing baby names.

Small program build in PyQt5 to help parents to be in choosing a name for their new family member.
The program is set up with *Danish* names, but is build to manage names provided to it in a .csv-file. The structure can be seen in the section **Importing Names**. The danish names have been found at [Familieretshuset](https://familieretshuset.dk/navne/navne/godkendte-fornavne). 


## Program walk-through
The program consist of 5 pages.  
The user logins by writing their initials, which will be stored in the local SQLite3 database. 

 - Login page.
 - Menu for voting or searching on name.
 - Menu for choosing baby's gender.
 - Page for searching for name.
 - Page for voting on random names.



## Importing and exporting names
The program allow for both importing a dataset with new or other names, and exporting votes for later analysis. 

### Exporting Votes
With the menubar it is possible to export the data that contain votes. This can be used to see what names all users likes.
This will be exported into a .csv-file and saved at the user location of choice. 

### Importing Names

To import a list of other names, the structure must be as followed:

| Name     | Make | Female |
|----------|----------|-----------|
| Peter    | 1        | 0         |
| Hillary | 0        | 1         |
| ...      | ...      | ...       |
| Rene     | 1        | 1         |

The first column simply lists the name.
The two columns Boy name, and Girl name is an indicator for whether the name can be used for a boy, girl, or both sex.  
This still imports the Danish names, but allows for adding names not used. 

## Acknowledgment
This project was inspired by [Jason Kiley](https://github.com/jtkiley). Thanks for a great introduction to python. 


