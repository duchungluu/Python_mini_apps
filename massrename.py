import os
  

dir =  input()

for count, filename in enumerate(os.listdir(dir)):
    dst =dir + "Photo" + str(count) + ".jpg"
    src =dir +"\_X7A1106"
    os.rename(src, dst)
  
