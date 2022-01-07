import cv2
from imutils.paths import list_images
import os

PATH = "traffic_light_cropped"
BASE_PATH = "traffic_light_dataset"
color_paths = {"0": "0_green", "1": "1_yellow", "2": "2_red", "3": "3_not"}

images_paths = list(list_images(PATH))

f = open("info.txt", "r")
lines = f.readlines()
offset, num_traffic_lights = int(lines[0]), int(lines[1])

images_paths = images_paths[offset:]

for (i, image_path) in enumerate(images_paths):
    image = cv2.imread(image_path)
    cpy_image = cv2.resize(image, (80, 160))
    cv2.imshow("img", cpy_image)
    k = cv2.waitKey(0)
    if k == ord('q'):
        print("Stopped at img number {}".format(i + offset))
        break
    if k == ord('4'):
        continue
    destination_path = os.path.sep.join([BASE_PATH, color_paths[chr(k)], "cityscapes_{}.jpg".format(i + offset)])
    cv2.imwrite(destination_path, image)
    num_traffic_lights += 1
    print("{} images added".format(num_traffic_lights))

    f = open("info.txt", "w")
    f.writelines([str(i+offset) + "\n", str(num_traffic_lights)])
    f.close()

cv2.destroyAllWindows()
