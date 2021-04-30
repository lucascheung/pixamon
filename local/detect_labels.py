import os
from google.cloud import vision

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    print(labels)
    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./service_account.json'
    url = 'gs://pixamon_images/cat.jpeg'
    detect_labels_uri(url)