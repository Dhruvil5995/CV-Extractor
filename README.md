# CV-Extractor 

* Extract random information from CVs, resume
* HR or company receives multiple CVs in a day, it is a time-consuming and very slow process to  review each CV one by one
* CV-extractor helps to review multiple CVs at one time.
* it is a time-saving and very fast process.

## Extract information from CVs according to company requirements.
e.g.* Name, Address, Education, experience, etc.

### 1)extract Name:
* use Spacy library
* load ('en_core_web_lg') model -- large model for English.
* convert CV(PDF) into a text string.
* Apply English model on CV(PDF) text.
* create a custom rule to extract the name
* First name and Last name are always Proper Nouns
* create a pattern for PROPN in POS
* add pattern which searches PROPN in POS
* put all PROPN words in the list and take the first PROPN, Name of person in CV always written at starting 

### 2)extract education, experience, addresses:
 ** Extract the Whole section of education, experience, addresses from CV
### by doing extract whole section you get:  
                                           1) university name (So no need to extract separately 
                                           2) Field of Study  
                                             

* use nltk                        
* create a list and write education and similar words of education.
            e.g.-    edu=['Bildung','Ausbildung','AUSBILDUNG','BILDUNG','EDUCATION','Education','Hochschul','HOCHSCHUL','Studium','STUDIUM',qualification]
            ## for English and German language ## 

* convert CV text into words(tokenization)
  words= nltk.word_tokenize(CV_text)
* find Education or similar word from CV words and take starting index of that word.
`   for variable in words:
       if variable in edu:
         start=words.index(variable)
         st=start+1`
* take randomly 30 to 25 words from start index. 
`   end= st+25
    for item in words[st:end]:
       education_list.append(item)`










### 3)extract Skills, Hobbie, language:
* convert CV text into words(tokenization)
* create a list for Computer or other skills(manually)
###       computer_skills =
                          ['ABAP','ActionScript','Ada','ALGOL','Alice','APL','ASP','ASP.NET','Assembly Language',
                          'Awk','BBC Basic','C','C++','C','C#','COBOL','Cascading Style Sheets','D','Delphi',
                          'Dreamweaver','Erlang and Elixir','F#','FORTH','FORTRAN','Functional Programming',
                           'Go','Haskell','HTML','IDL','INTERCAL','Java','Javascript','Node','Bootstrap',
                           'jQuery','LabVIEW','Lisp','Logo','MetaQuotesLanguage','ML','Modula-3','MS Access',
                          'MySQL','NXT-G','Object-Oriented Programming','OOP','Objective-C','OCalm','Pascal',
                          'Perl','PHP','PL/I','PL/SQL','PostgreSQL','PostScript','PROLOG','Pure Data',
                          'Python','R','RapidWeaver','RavenDB','Rexx','Ruby on Rails','S-PLUS','SAS','SAP',
                          'Scala','Sed','SGML','Simula','Smalltalk','SMIL','SNOBOL','SQL','SQLite','SSI',
                          'Stata','Swift','Tcl/Tk','Tex','LaTex','Unified Modeling Language','Unix Shell','Verilog',
                          'VHDL','Visual Basic','Visual FoxPro','VRML','WAP/WML','XML','XSL','Git','Github','Ubuntu',
                          'Microsoft Word','Word','Microsoft Excel','Excel','Microsoft Powerpoint','Powerpoint',
                          'Microsoft Outlook','Outlook','Microsoft Publisher','Publisher','Microsoft Access',
                          'Access','Microsoft OneNote','OneNote','Microsoft Project','Photoshop','Numpy',
                          'Pandas','Matplotlib','Scikit-Learn','Scipy','PyTorch','TensorFlow','Keras','theano',
                          'NLTK','Spark','Elm','TypeScript','Scala','Go','Swift','Objective C','Rust',
                          'Unity','Angular','elixir','Android','iOS','RIM','Symbian','Lua','Dart','Flutter',
                          'React','ML','Machine Learning','Linear Regression','Logistic Regression','Decision Tree',
                          'SVM','Support Vector Machine','Naive Bayes','GP','Gaussian Processes','kNN','K-Means',
                          'Random Forest','Convolution Neural Network','Neural Networks','Ensemble','Deep Learning','Microsoft Office','Office',
                          'Keynote','Google Spreadsheets','Slack','Skype','MacOS','G Suite','QuickBooks',
                           'FreshBooks','Xero','Tableau','Tello','Matlab','Julia','OpenOffice']:
* if any skill present in CV and it matches with CV text then it extracts that skill.

### 4)extract email and phone number:
* use regex library
* (r'[\w\.-]+@[\w\.-]+') - for find email address from CVs
 > Where, [\w\.-]- find all character from  A to Z and all digits 0 to 9
          @-  search @
          [\w\.-]+  - search (.) 
* (r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
 > use to find + and two digits for country code

### 5) create functions:
* create Functions for each information and put all functions in one main function for better view.

## 
    def all_CV_information(cv):  # create another function....which contain all other functions
       name= extract_name(cv)
       Dob=place_date_birth(cv)
       language=extract_language(cv)
       skill= extract_computer_skill(cv)
       hobbie=extract_hobbies(cv)
       educ=extract_education(cv)
       exp=extract_experience(cv)
       mail=extract_email_addresses(cv)
       cell=extract_phone_numbers(cv)
       ad=extract_Address(cv)
    
    return  name,Dob,language, skill, hobbie, educ, exp, mail, cell,ad

### main function
            final_list= all_CV_information('020.pdf') # Pdf file (CV)# input

###  create latex file
* write and save result into latex file 
## 

    with open("final_doc.tex", "w") as f:  # create latex file and write
    f.write(result)    # result store in latex file**
## 









