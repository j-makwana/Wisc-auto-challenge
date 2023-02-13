# Wisc-auto-challenge

## Perception Challenge Submission
submitted by: Jenil Makwana (jmakwana@wisc.edu)

## answer.png

![answer](https://user-images.githubusercontent.com/99378825/218344484-59b659f2-2df5-485e-b389-02f5502c540a.png)

## methodology
1. created a mask for red objects and detected the cones
2. divided the image into two seperate region of interests(roi)
3. performed contour detection
4. found the center of each object and eliminated the ones with small areas(that can't be cones)
5. made a best fit line using the contour centers as points on the line

## What did you try and why do you think it did not work
since I didn't know openCV, I tried a range of thresholding and blurring techniques to detect cones. I was also trying to use numpy.where() to find x and y locations
but eventually realised that the contour detection method works the best.

## What libraries are used
- openCV
- numpy
- matplotlib (only when I was working on juptyer to view the results)

