import unittest
import numpy as np
from sklearn.metrics import accuracy_score
from models.train_model import train_model
from models.predict_model import predict

class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once for all tests. Setup required data."""
        # Simulated training data (replace with real data or mock data)
        cls.X_train = np.random.rand(100, 5)  # 100 samples, 5 features
        cls.y_train = np.random.randint(0, 2, 100)  # Binary classification labels
        cls.X_test = np.random.rand(20, 5)
        cls.y_test = np.random.randint(0, 2, 20)

        # Train the model using the training data
        cls.model = train_model(cls.X_train, cls.y_train)

    def test_model_output_shape(self):
        """Test if the model output has the correct shape."""
        predictions = predict(self.model, self.X_test)
        self.assertEqual(predictions.shape, self.y_test.shape, "Prediction output shape mismatch.")

    def test_model_accuracy(self):
        """Test the model's accuracy on the test set."""
        predictions = predict(self.model, self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        self.assertGreater(accuracy, 0.7, "Model accuracy is below the acceptable threshold.")

    def test_input_data_format(self):
        """Test if input data is in the expected format."""
        self.assertEqual(len(self.X_test[0]), 5, "Input data format is incorrect, expected 5 features.")

if __name__ == "__main__":
    unittest.main()
