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


def list_files(root, extension, output_filename):
    
    path = f'{root}*{extension}'

    try:
        # output playlist items to csv or txt file
        outfile = open(f'lists/{output_filename}', "w", encoding='utf-8')

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
folder2 = 'C:\\Users\\brian\\OneDrive - Trinity Schools\\Subjects\\Electronics\\_MY LEARNING\\'
folder3 = r'C:\Repos\13DGT\AdZ\PointsPlus\\'

list_files(folder3, "*", "list_files.txt")


#list_filenames(folder)