import unittest
from src.product_predict import FEATURES, validate_inputs

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.values = {name: "1" for name in FEATURES}
        self.values["ph"] = "7"

    def test_normal(self):
        self.assertEqual(validate_inputs(self.values)["ph"], 7.0)
    
    def test_ph_boundaries(self):
        for value in ("0", "14"):
            self.values["ph"] = value
            self.assertEqual(validate_inputs(self.values)["ph"], float(value))
    
    def test_invalid_ph(self):
        for value in ("-1", "15", "", "abc", "nan", "inf"):
            self.values["ph"] = value
            with self.assertRaises(ValueError):
                validate_inputs(self.values)
    
    def test_negative_measurement(self):
        self.values["Turbidity"] = "-1"
        with self.assertRaises(ValueError):
            validate_inputs(self.values)

    def test_missing_feature(self):
        self.values.pop("Hardness")
        with self.assertRaises(ValueError):
            validate_inputs(self.values)

if __name__ == "__main__":
    unittest.main()