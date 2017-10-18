from textblob.classifiers import NaiveBayesClassifier
import csv

""" Class which classifies the summary of a plane crash into a reason.
    The used small training set includes the following categories:
        * Adverse weather conditions.
        * Recklessness of the pilot.
        * Low flight.
        * Conflagration.
        * Engine failure.
        * Attacked.
        * Bad takeoff.
        * Bad landing.
        * Unknown.

    Resource:
    http://stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/
"""

class ReasonClassifier():

    def __init__(self, train_set_filepath):
        self.filepath = train_set_filepath
        self.training_data = []

        self.__read_training_examples()
        self.classifier = NaiveBayesClassifier(self.training_data)

    def __read_training_examples(self):
        with open(self.filepath, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            training_data = list(reader)
            # Remove tuples with size != 2
            filtered_training_data = (
                [tup for tup in training_data if len(tup) == 2])

        for i in range(len(training_data)):
            training_data[i] = tuple(training_data[i])

        self.training_data = training_data

    def classify(self, summary_str):
        return self.classifier.classify(summary_str)
