def getMedian(list):
  list.sort()
  length = len(list)
  
  halfLen = length / 2
  if ((length % 2) == 0):
    midAvg = 0
    midAvg = (list[halfLen] + list[halflen - 1]) / 2
    return avg
  else:
    return list[halfLen]

def makeFileList(numFiles):
  paths = []
  for i in range(numFiles):
    paths.append('/home/cole/Downloads/Project1Images/' + str(i + 1) + '.png')
  return paths
  
def makePicList(files):
  pics = []
  for i in range(len(files)):
    pic = makePicture(files[i])
    pics.append(pic)
  return pics
  
def sepperatePics(pics):
  pixelList = []
  for i in range(len(pics)):
    pixelList.append(getPixels(pics[i]))
  return pixelList

def compareColor(redPix,greenPix,bluePix):
  comparison = 0
  redAvg = 0
  blueAvg = 0
  greenAvg = 0
  length = len(redPix)
  for i in range(length):
    redAvg = redAvg + redPix[i]
    greenAvg = greenAvg + greenPix[i]
    blueAvg = blueAvg + bluePix[i]
  redAvg = redAvg / length
  greenAvg = greenAvg / length
  blueAvg = blueAvg / length
  comparison = abs(redAvg - redPix[0]) + abs(greenAvg - greenPix[0]) + abs(blueAvg - bluePix[0])
  return comparison

numSamples = 9

fileList = makeFileList(numSamples)#set paths to pictures
picList = makePicList(fileList)#make list of picture objects
  
individualPixels = sepperatePics(picList)#make a list of pixel lists
 
redList = [0,0,0,0,0,0,0,0,0]#hold the different values of red for each image 
greenList = [0,0,0,0,0,0,0,0,0]#hold the different values of green for each image
blueList = [0,0,0,0,0,0,0,0,0]#hold the different values of green for each image

show(picList[0])
    
for i in range(len(individualPixels[0]) ):
  for j in range(len(individualPixels) ):
    redList[j] = getRed(individualPixels[j][i])
    greenList[j] = getGreen(individualPixels[j][i])
    blueList[j] = getBlue(individualPixels[j][i])
  if(compareColor(redList,greenList,blueList) < 3):
    setRed(individualPixels[0][i],redList[0])
    setGreen(individualPixels[0][i],greenList[0])
    setBlue(individualPixels[0][i],blueList[0])
    
    
  else: 
    setRed(individualPixels[0][i],getMedian(redList))
    setGreen(individualPixels[0][i],getMedian(greenList))
    setBlue(individualPixels[0][i],getMedian(blueList))
  if((i % (getWidth(picList[0]) * 2) ) == 0):
    repaint(picList[0])

repaint(picList[0])  
setMediaPath()
destinationFile = getMediaPath('noTourist.png')
writePictureTo(piclist[0],destinationFile)
