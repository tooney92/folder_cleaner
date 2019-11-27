import re, os, shutil
os.chdir('\\Users\\anthony.ime')
os.getcwd()
os.chdir(os.getcwd()+'\\Downloads')
samp = []

user_doc_type = input('what file type do you want to clean? \n a.)pdf \n b.) word-docs: ')
if user_doc_type == 'a':
    user_doc_type = '.pdf'
elif user_doc_type == 'b':
    user_doc_type = '.docx'

def folder_cleaner():
    
    for dirpath,directory,filename in os.walk(os.getcwd()):
        samp.append(filename)
        break
    pattern = re.compile(f'{user_doc_type}')
    count = 0
    file_count = 0
    docx_count = 0
    for file in samp[0]:
        if len(pattern.findall(file)) == 1:
            try:
                if user_doc_type == '.pdf':
                    if os.path.exists(os.getcwd()+'\\pdfs\\'+file) == True:
                        user_response = input(f'the file: {file} already exists in destination folder, would you want to delete it? [WARNING!!! this is permanent!]')
                        if user_response == 'yes' or 'Yes' or 'y'or 'Y':
                            os.unlink(os.getcwd()+'\\'+file)
                            print()
                        #print('already exists: ', file)
                                    
                    else:
                        file_count += 1
                        shutil.move(os.getcwd()+'\\'+file, os.getcwd()+'\\pdfs')
                elif user_doc_type == '.docx':
                    if os.path.exists(os.getcwd()+'\\docx\\'+file) == True:
                        user_response = input(f'the file: {file} already exists in destination folder, would you want to delete it? [WARNING!!! this is permanent!]')
                        if user_response == 'yes' or 'Yes' or 'y'or 'Y':
                            os.unlink(os.getcwd()+'\\'+file)
                            print()
                
                    else:    
                        file_count += 1
                        shutil.move(os.getcwd()+'\\'+file, os.getcwd()+'\\'+user_doc_type[1:])
                        
            except FileNotFoundError:
                continue
            except PermissionError:
                print('Could not delete!! This file is opened in some other application.\n If file is a pdf check adobe or any other pdf reader.\n If file is docx, check Microsoft word or other docx readers')
        count+=1
    if user_doc_type == '.pdf':
        print(f"there were {file_count} '.pdf' files moved from {os.getcwd()} to {os.getcwd()}\\pdfs'")
        print()
        file_count = 0
    elif user_doc_type == '.docx':
        print(f"there were {file_count} '.docx' files moved from {os.getcwd()} to {os.getcwd()}\\docx")
        print()
        file_count = 0
folder_cleaner()b