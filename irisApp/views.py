from django.shortcuts import render
from joblib import load
import os

# Define the path to the model
model_path = os.path.join(os.path.dirname(__file__), 'savedModels', 'model.joblib')
try:
    model = load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")

# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    try:
        sepal_length = float(request.GET['sepal_length'])
        sepal_width = float(request.GET['sepal_width'])
        petal_length = float(request.GET['petal_length'])
        petal_width = float(request.GET['petal_width'])

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = y_pred[0]
        print(f"Prediction: {prediction}")

        context = {
            'prediction': prediction
        }

        return render(request, 'result.html', context)
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'error.html', {'error': str(e)})
