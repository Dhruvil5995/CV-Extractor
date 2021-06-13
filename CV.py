def extract_Address(add):
   import fitz
   import spacy
   import nltk
   doc= fitz.open(add) 
   text=""             #crate string
   for page in doc:
      text= text + str(page.getText())  #conver pdf text into stringnlp

   st=0
   end=0
   wo= nltk.word_tokenize(text)
   for add_va in wo:
      if add_va== 'Anschrift' or add_va=='ANSCHRIFT' or add_va== 'Address' or add_va=='ADDRESS' or add_va=='ADDRESSE' or add_va=='Addresse' or add_va=='Adresse' or add_va=='ADRESSE':
        start=wo.index(add_va)
        st=start+1
        end= st+6
   lis=[]

   for item in wo[st:end]:
      lis.append(item)
   stringList = ' '.join(lis)

   return stringList
def extract_computer_skill(skill_doc_cv):
    import spacy
    import sys, fitz
    nlp = spacy.load("de_core_news_lg")  # load large German  model

    doc = fitz.open(skill_doc_cv)  # crate string
    text = " "
    for page in doc:
        text = text + str(page.getText())  # conver cv text into string

    ski=[]
    doc_pipe = nlp(text)

    for ent in doc_pipe:     # Add manually different language and level... you can add more language in this list
       if ent.text in  ['ABAP','ActionScript','Ada','ALGOL','Alice','APL','ASP','ASP.NET','Assembly Language',
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

             ski.append(ent.text)
             computer_string=' '.join(ski)
   
    return computer_string

def extract_education(study_cl):
    import spacy
    import fitz
    import nltk
    doc= fitz.open(study_cl) 
    text=""             #crate string
    for page in doc:
       text= text + str(page.getText())  #conver pdf text into string
  
    words= nltk.word_tokenize(text)
    education_list=[]
    edu=['Bildung','Ausbildung','AUSBILDUNG','BILDUNG','EDUCATION','Education','Hochschul','HOCHSCHUL','Studium','STUDIUM']
    st=0
    end=0
    for variable in words:
       if variable in edu:
         start=words.index(variable)
         st=start+1
         end= st+25
    for item in words[st:end]:
       education_list.append(item)
    education_string = ' '.join([str(item) for item in education_list])
    

    return education_string

def extract_email_addresses(mail):
  import re
  import spacy
  import fitz
  import nltk
  doc= fitz.open(mail) 
  text=""             #crate string
  for page in doc:
     text= text + str(page.getText())  #conver pdf text into string
    
  r = re.compile(r'[\w\.-]+@[\w\.-]+')  # for find email Address 
  mail= r.findall(text)
  mail_string= ' '.join(mail)
  return mail_string

def extract_experience(ex_cl):
  import spacy
  import fitz
  import nltk
  doc= fitz.open(ex_cl) 
  text=""             #crate string
  for page in doc:
    text= text + str(page.getText())  #conver pdf text into string
  s= nltk.word_tokenize(text)
  exp=['Erfahrung' ,'Laufbahn','ERFAHRUNG' ," Erfahrungen" ,'LAUFBAHN' ,'Praktische','PRAKTISCHE','ERFAHRUNGEN','Praktika','PRAKTIKA' ,
     'Berufserfahrung' ,'EXPERIENCE','Experience' ,'BERÜFSERFAHRUNG','Berufserfahrung']
  st = 0
  end= 0
  for vari in s:
    if vari in exp:
      start=s.index(vari)
      st= start+1
      end= st+35
  
  f_list=[]
  for item in s[st:end]:
     f_list.append(item)
  stringList = ' '.join(f_list )
 

  return stringList


def extract_hobbies(hobbie_doc_cv):
    import re
    import spacy
    import fitz
    import nltk
    nlp = spacy.load("de_core_news_lg")  # load large German  model

    doc = fitz.open(hobbie_doc_cv)  # crate string
    text = " "
    for page in doc:
        text = text + str(page.getText())  # conver cv text into string

    hob=[]
    doc_pipe = nlp(text)
    new= ['Garten','Gartenarbeit','Shoppen','Einkaufen gehen','Essen','Restaurants','Ausgehen','Trinken',
                        'Bars','Cocktails','Rätsel','Rätseln','Computer','Computerspiele','Spiele','Sport','Joggen',
                         'Laufen','Rennen','Marathon','Triathlon','Iron Man','Fitness','Fitnessstudio','Kraftsport',
                            'Gewichtheben','Rudern','Fahrradfahren','Basteln','Schrauben','Reparieren','Radfahren',
                           'Malen','Malerarbeiten','Zeichnen','Kunst','Museen','Wandern','Bergsteigen','Gesellschaftsspiele',
                           'Brettspiele','Rollenspiele','Cosplay','Sauna','Saunieren','Therme','Waldlauf','Geländelauf',
                            'Mountainbike fahren','Walking','Meditation','Fussball','Football','Baseball','Tennis','Badminton',
                           'Rugby','Ringen','Turnen','Leichtathletik','Squash','Golf','Minigolf','Boxen','MMA','Karate',
                           'Yoga','Camping','Rennrad fahren','Kino','Reisen','Fliegen','Bootfahren','Angeln','Reiten',
                        'Ski','Fischen','Snowboard','Jagen','Tauchen','Schwimmen','Kochen','Segelfliegen','Sportfliegen',
                          'Motorrad','Motorsport','Socialising','Schach','eSports','Klavier','Piano','Gitarre','Fußball']
    for ent in doc_pipe:    
       if ent.text in new:
          hob.append(ent.text)
    hobbies_string=' '.join(hob)
  
    return hobbies_string

def extract_language(language_doc_cv):
    import re
    import spacy
    import fitz
    import nltk
    nlp = spacy.load("de_core_news_lg")  # load large German  model

    doc = fitz.open(language_doc_cv)  # crate string
    text = " "
    for page in doc:
        text = text + str(page.getText())  # conver cv text into string

    ab=[]
    doc_pipe = nlp(text)

    for ent in doc_pipe:     # Add manually different language and level... you can add more language in this list
       if ent.text in ['Deutsch','bulgarisch','kroatisch','Tschechisch','Dänisch','Niederländisch','Estnisch','Chinesisch','Spanisch','Englisch',
                       'Hindi','Arabisch','Portugiesisch','Bengalisch','Russisch',
                       'Japanisch','Javanisch','Indonesisch','Lahnda','Deutsch','Koreanisch','Französisch','Telugu',
                       'Marathi','Türkisch','Tamil','Vietnamesisch','Urdu','Italienisch','Schwedich','Afrikanisch',
                       'Niederländisch','Griechisch','Polnisch','Belgisch','Dänisch','Kroatisch','Tschechisch','Finnisch',
                       'Rumänisch','Ukrainisch','Finnisch','Griechisch','Ungarisch','Irisch','Italienisch' ,'Englisch','Spanisch', 
                       'Portugiesisch', 'Französisch','Chinesisch','Hindi','Arabisch','Bengali', 'Russisch',
                       'japanisch','Lettisch','Litauisch','Maltesisch','Polieren','Rumänisch','Slowakisch',
                       'Slowenisch','Schwedisch''Javanese', 'Koreanisch', 'Telugu', 'English','Marathi','Türkisch',
                       'Tamil','Gujarati','Vietnamesisch', 'Urdu','Muttersprache',
                       'A1','A2','A3','B1','B2','B3','C1','C2','C3','Fortgeschritten','Gut','Durchschnittlich','Sehr gut', 'Mittlere']:
            ab.append(ent.text)
            language_string=' '.join(ab)
  
    return language_string

def extract_name(name_doc_cv):   #function of extract name from cv
    import re
    import spacy
    import fitz
    import nltk
    from spacy.matcher import Matcher
    nlp = spacy.load('en_core_web_lg')

    doc = fitz.open(name_doc_cv)  # crate string
    text = ""
    for page in doc:
        text = text + str(page.getText())  # conver cv text into string

    doc_pipeline = nlp(text)  # add text to english pipeline model
    c = []  # create list
    for i in (doc_pipeline):
        c.append(i)

        # initialize matcher with a vocab
    matcher = Matcher(nlp.vocab)
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]  # create pattern for PROPN in POS
    matcher.add('PROPN', [pattern])  # add pattern to in matcher
    matches = matcher(doc_pipeline)
    d = []
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc_pipeline[start:end]
        # print(match_id, string_id, start, end, span.text)
        d.append(span.text)
    person_name = d[0]
    return person_name

def extract_phone_numbers(num):
  import re
  import spacy
  import fitz
  import nltk
  doc= fitz.open(num) 
  text=""             #crate string
  for page in doc:
     text= text + str(page.getText())  #conver pdf text into string
  regrex=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
  num=regrex[0]
  return num


def place_date_birth(DOB):
  import re
  import spacy
  import fitz
  import nltk
  doc= fitz.open(DOB) 
  text=""             #crate string  
  for page in doc:
     text= text + str(page.getText())  #conver pdf text into stringnlp
  st = 0
  end = 0
  wo= nltk.word_tokenize(text)
  for va in wo:
    if va == 'geb.' or va== 'GEB.' or va== 'geb' or va== 'GEB' or va== 'Geburtsdatum' or va== 'GEBURTSDATUM':
      start=wo.index(va)
      st=start+1
      end= st+4
  lis=[]

  for item in wo[st:end]:
     lis.append(item)
  stringList = ' '.join(lis)
  return stringList


def all_CV_information(cv):  # create another function for all 
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
final_list= all_CV_information('023.pdf') 


result='Name of Person : ' +final_list[0]+'\n'+'Date and Place of Birth: '+final_list[1]+'\n'+'Language :  '+final_list[2]+ '\n' +'Computer Skills :  '+final_list[3]+'\n'+'Hobbies :  '+final_list[4]+'\n'+'Education Information :'+final_list[5]+'\n'+'Experience Information :'+final_list[6]+'\n'+'E-mail :  '+final_list[7]+'\n'+'Contact Number :  '+final_list[8]+'\n'+'Address : '+final_list[9]

print(result)






