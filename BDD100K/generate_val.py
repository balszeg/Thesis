import os

image_files = []
os.chdir(os.path.join("bdd100k","images","100k","val"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/bdd100k/bdd100k/images/100k/val/" + filename)
os.chdir("..")
with open("val.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")