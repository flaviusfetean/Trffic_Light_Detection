import cv2
from imutils.paths import list_images
import os

PATH = "traffic_light_cropped"
BASE_PATH = "traffic_light_dataset"
color_paths = {"0": "0_green", "1": "1_yellow", "2": "2_red", "3": "3_not"}

images_paths = list(list_images(PATH))
images = [cv2.imread(img_path) for img_path in images_paths]


offset = 0
images = images[offset:]

for (i, image) in enumerate(images):
    cpy_image = cv2.resize(image, (80, 160))
    cv2.imshow("img", cpy_image)
    k = cv2.waitKey(0)
    if k == ord('q'):
        print("Stopped at img number {}".format(i))
        break
    if k == ord('4'):
        continue
    destination_path = os.path.sep.join([BASE_PATH, color_paths[chr(k)], "{}.jpg".format(i + offset)])
    cv2.imwrite(destination_path, image)

print("Successfully sorted all images")
cv2.destroyAllWindows()
