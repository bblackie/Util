import os 
import glob # https://pynative.com/python-glob/


'''
Sub-routines
output_filename = f'{producer_name}.txt' # DEFAULT 'playlist.txt'
    
    if get_playlist_info:
        output_playlist_info({channel_id}, f'lists/{output_filename}', True)

'''

def list_filenames(root):
    
    output_filename = 'go.txt'

    collection = ['first','second']
     

    try:
        # output playlist items to csv or txt file
        outfile = open(f'lists/{output_filename}', "w")

        for item in collection:
            outfile.write(f'{item}\n')

  
        

    except Exception as e:
        print(e)
    finally:
        outfile.close()


def list_files(root, output_filename):
    
    extension = '.pptx'
    path = f'{root}*{extension}'

    try:
        # output playlist items to csv or txt file
        outfile = open(f'lists/{output_filename}', "w")

        for file in sorted(glob.glob(path, recursive=False)):
            full_filename = os.path.basename(file)
            print(full_filename.replace(extension, ""))
            outfile.write(f'{full_filename.replace(extension, "")}\n')

    except Exception as e:
        print(e)
    finally:
        outfile.close()


    

'''
Main function
'''

folder = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\13DGT\\Assessments\\3.7 Computer Program\\Student work\\'
folder2 = 'C:\\Users\\brian.blackie\\OneDrive - Trinity Schools\\Classes\\12DGT\\Lessons\\Advanced Techniques\\'

list_files(folder2, "tac.txt")


#list_filenames(folder)