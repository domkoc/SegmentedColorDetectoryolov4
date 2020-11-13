import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", help="path to the images")
ap.add_argument("-c", "--class", help="no of class")
args = vars(ap.parse_args())
folder = args["folder"]
imgclassnum = args["class"]



filesnum = len(os.listdir(folder))

for idx, filename in enumerate(os.listdir(folder)):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        imgoriginal = cv2.imread(os.path.join(folder, filename))
        img = cv2.cvtColor(imgoriginal, cv2.COLOR_BGR2GRAY)
        rows, cols = img.shape
        rmin = rows
        rmax = 0
        cmin = cols
        cmax = 0

        for r in range(rows):
            for c in range(cols):
                k = img[r, c]
                if k >= 30:
                    if r < rmin:
                        rmin = r

                    if r > rmax:
                        rmax = r

                    if c < cmin:
                        cmin = c

                    if c > cmax:
                        cmax = c

        #print("rmax: " + str(rmax / rows))
        #print("rmin: " + str(rmin / rows))
        #print("cmax: " + str(cmax / cols))
        #print("cmin: " + str(cmin / cols))

        coordx = ((cmin + cmax) / 2) / cols
        #print("coordx: " + str(coordx))
        coordy = ((rmin + rmax) / 2) / rows
        #print("coordy: " + str(coordy))
        width = (cmax - cmin) / cols
        #print("width: " + str(width))
        height = (rmax - rmin) / rows
        #print("height: " + str(height))

        #cv2.rectangle(imgoriginal, (cmin, rmin), (cmax, rmax), (0, 0, 255), 2)
        #cv2.imshow("detect", imgoriginal)
        #cv2.waitKey(0)


        filePath = os.path.join(folder, filename)
        filePath = os.path.splitext(filePath)[0] + ".txt"
        f = open(filePath, "w")
        f.write(imgclassnum + " " + str(coordx) + " " + str(coordy) + " " + str(width) + " " + str(height))
        f.close()
        print("progress: " + str(idx / filesnum * 100) + "%")

print("done.")
