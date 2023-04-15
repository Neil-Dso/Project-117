import cv2, os

path = "assets"

images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    if ext in ['.png']:
        file_name = path+"/"+file

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channel = frame.shape

size = (width, height)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.2, size)

for i in range(0, count):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done!")