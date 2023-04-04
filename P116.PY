import numpy as np
import cv2

img= cv2.imread("project/P116/solar-system.jpg")


cv2.putText(img,
            'sun',
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )

cv2.putText(img,
            'mercury',
            (180,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'venus',
            (120,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'Saturn',
            (800,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'Mars',
            (400,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'Jupiter',
            (540,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'Earth',
            (280,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'uranus',
            (1000,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )
cv2.putText(img,
            'neptune',
            (1060,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,225),
            )

cv2.imshow("Output",img)
cv2.imwrite("Output.png",img)
cv2.waitKey(0)
            