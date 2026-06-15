from django.shortcuts import render
from myapp.models import Uploads
from keras.models import load_model
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

# Create your views here.
def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        upload = Uploads(file=file)
        upload.save()
        print('File uploaded successfully')
        print('File name:', file.name)

        # Load the saved model
        model = load_model("static/cnn_model_from_train_dataset.h5")

        # Get the base directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print("Base directory:", upload)
        sample_path = base_dir + upload.file.url

        sample = np.load(sample_path)

        # Reshape the sample to match the input shape of the model
        sample = sample.reshape(1, sample.shape[0], 1)

        # Predict using the model
        prediction = model.predict(sample)
        prediction = "Abnormal" if prediction[0][0] > 0.5 else "Normal"
        print("Prediction:", prediction)

        # Save the plot
        static_dir = os.path.join(base_dir, 'static')
        os.makedirs(static_dir, exist_ok=True)

        plt.figure(figsize=(10, 4))
        plt.plot(sample[0, :, 0], label="ECG Signal")
        plt.title("ECG Signal Sample")
        plt.xlabel("Time Index")
        plt.ylabel("Amplitude")
        plt.legend()

        plot_path = os.path.join(static_dir, 'ecg_plot.png')
        plt.savefig(plot_path)
        plt.close()

        data = {'prediction': prediction, 'plot_path': '/static/ecg_plot.png'}
        return render(request, 'index.html', data)

    return render(request, 'index.html')
