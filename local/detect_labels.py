import os
from google.cloud import vision

from IPython import embed

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    labels_data = []
    for label in labels:
        label_data = {
            "mid": label.mid,
            "description": label.description,
            "score": label.score
        }
        labels_data.append(label_data)

    return labels_data

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./service_account.json'
    url = 'gs://pixamon_images/cat.jpeg'
    print(detect_labels_uri(url))