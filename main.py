import os
import shutil

def transliteration(name):# транс літерація
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    name = name.translate(TRANS)
    ind = 0
    for el in name:
        if not el.isalnum():
            name = name.replace(el, '_')

        ind += 1
    return  name

def del_empty_dirs (path):# видаленя пустих папок
    for dir in os.listdir(path):
        path_dir = os.path.join(path,dir)
        if os.path.isdir(path_dir):
            del_empty_dirs(path_dir)
            if not os.listdir(path_dir):
                os.rmdir(path_dir)



def name(path):#створиня папок
    audio = path + r'\audio'
    if not os.path.exists(audio):
        os.mkdir(audio)

    images = path + r'\images'
    if not os.path.exists(images):
        os.mkdir(images)

    video = path + r'\video'
    if not os.path.exists(video):
        os.mkdir(video)

    documents = path + r'\documents'
    if not os.path.exists(documents):
        os.mkdir(documents)

    archives = path + r'\archives'
    if not os.path.exists(archives):
        os.mkdir(archives)

    for root, dirs, files in os.walk(path):#отреманя списку файлів
        if root == audio or root == images or root == video or root == documents or root == archives:#пропуск створиних папок
            continue

        for file_name in files:
            filename, file_extension = os.path.splitext(file_name)#отриманя імя та розширеня файлу
            #сортуваня та зпис файлі

            # audio
            if file_extension == '.mp3' \
                    or file_extension == '.ogg' \
                    or file_extension == '.wav' \
                    or file_extension == '.amr':
                filename = transliteration(filename)  # транс літерація
                new_file_name = filename + file_extension
                shutil.move(os.path.join(root, file_name), os.path.join(audio, new_file_name))


            # images
            elif file_extension == '.jpeg' \
                    or file_extension == '.png' \
                    or file_extension == '.jpg' \
                    or file_extension == '.svg':
                filename = transliteration(filename)  # транс літерація
                new_file_name = filename + file_extension
                shutil.move(os.path.join(root, file_name),  os.path.join( images, new_file_name))

            # video
            elif file_extension == '.avi' \
                    or file_extension == '.mp4' \
                    or file_extension == '.mov' \
                    or file_extension == '.mkv':
                filename = transliteration(filename)  # транс літерація
                new_file_name = filename + file_extension
                shutil.move(os.path.join(root, file_name),  os.path.join(video, new_file_name))

            # documents
            elif file_extension == '.dok' \
                    or file_extension == '.docx' \
                    or file_extension == '.txt' \
                    or file_extension == '.pdf' \
                    or file_extension == '.xlsx' \
                    or file_extension == '.pptx':
                filename = transliteration(filename)  # транс літерація
                new_file_name = filename + file_extension
                shutil.move(os.path.join(root, file_name),  os.path.join(documents, new_file_name))

            # archives
            elif file_extension == '.zip' \
                    or file_extension == '.gz' \
                    or file_extension == '.tar':
                filename = transliteration(filename)  # транс літерація

                dir_file_name = os.path.join(archives, filename)
                if not os.path.exists(dir_file_name):
                    os.mkdir(dir_file_name)

                new_file_name = filename + file_extension
                shutil.unpack_archive(os.path.join(root, file_name), dir_file_name)
                shutil.move(os.path.join(root, file_name), os.path.join(dir_file_name, new_file_name))

    del_empty_dirs(path)



name()






