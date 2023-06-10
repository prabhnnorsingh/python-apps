# Code to form text files and write content into them.

contents = ['\n I am a coder\npython is my favourite language\ni also like kali linux']

filenames = ['practice.txt']

for content,filename in zip(contents,filenames):
    file = open(f"../app1/{filename}","a")
    file.write(content)
    file.close()