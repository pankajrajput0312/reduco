import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

credentials = ApiKeyCredentials(in_headers = {"Prediction-Key":"bf595a2cb1854d988a1f9d26834cd4e2"})
predictor =  CustomVisionPredictionClient("https://pankaj.cognitiveservices.azure.com/", credentials)

# ret, image = camera.read()
# cv2.imwrite('capture.png', image)
# camera.release()
with open("capture.png", mode ='rb') as captured_image:
    print("load image... and predict ")
    results = predictor.classify_image("c22b7174-dd80-457b-829e-4d05496aee33", "Iteration3", captured_image)
    # print(results)
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +": {0:.2f}%".format(prediction.probability * 100))
print("all done")
