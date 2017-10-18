from textblob.classifiers import NaiveBayesClassifier

""" Class which classifies the summary of a plane crash into a reason.
    The used small train set includes the following categories:
        * Adverse weather conditions.
        * Recklessness of the pilot.
        * Low flight.
        * Conflagration.
        * Engine failure.
        * Unknown.

    Resource:
    http://stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/
"""

train_set = [
    ('Crashed into mountainous terrain while en route. Most likely ' + \
        ' weather related.', 'Adverse weather conditions'),
    ('The aircraft hit a fog shrouded hill at 1,400 ft. after descending' + \
        ' below minimum. Improper IFR operation.', 'Adverse weather conditions'),
    ('Fire aboard the aircraft in the aft right toilet was reported and' + \
        ' an emergency descent made. The plane was heavily damaged by fire' + \
        ' before fire fighters could rescue passengers. Most fatalities' + \
        ' were due to CO before rescuers could reach passengers. The fire' + \
        ' started in the aft right toilet either from an electrical short' + \
        ' or discarded cigarette.', 'Conflagration'),
    ("The aircraft flew100 miles off course and struck Black Fork" + \
        ' Mountain, 600 feet below the summit of the peak, 91 miles North' + \
        ' of Texarkana. Heavy thunderstorms were in the area at the time.' + \
        ' The captain attempt to operate the flight under VFR at night' + \
        ' without using all the navigational aids and information' + \
        ' available to him and his deviation from the pre-planned route' + \
        ' without adequate positioning information.',
            "Adverse weather conditions"),
    ("The aircraft crashed short of the runway in fog while on approach" + \
     " to Christchurch Airport. The plane crashed two kilometers from the" + \
     " airport, hitting a farm hedge and sliding across a paddock before" + \
     " smashing into a row of trees.", 'Adverse weather conditions'),
    ('The charter aircraft crashed into a steep hillside on south' + \
     ' Thormanby Island 19 minutes after taking off and exploded into' + \
     ' flames. Controlled flight into terrain caused by poor weather' + \
     ' conditions and the decision by the pilot to fly in such conditions.',
        'Adverse weather conditions'),
    ('The plane struck the side of El Yunque mountain 2,310 feet, east of' + \
     ' San Juan in heavy fog.', 'Adverse weather conditions'),
    ("Crashed during a severe thunderstorm.", 'Adverse weather conditions'),
    ('The aircraft collided with rising terrain at 1,100 ft. after' + \
     ' executing a go-around. Failure of the pilot to follow proper IFR' + \
     ' procedures.', 'Recklessness of the pilot'),
    ('Crashed into an 850 meter high peak while on approach to Puerto' + \
     ' Plata.', 'Low flight'),
    ('While en route, the aircraft went into a steep dive and crashed to' + \
     ' the ground.', 'Low flight'),
    ('The sightseeing plane hit a mountainside at an elevation of 4,500' + \
     ' ft., 200 ft. below the summit. The weather was clear at the time' + \
     ' of the accident.', 'Low flight'),
    ('The plane crashed after its right wing clipped a mountaintop while' + \
     ' en route.', 'Low flight'),
    ('An electrical fire forced the cargo planes pilot to attempt an' + \
     ' emergency landing in a rice field when the plane crashed, broke' + \
     ' into pieces, and burst into flames.', 'Conflagration'),
    ('The cargo plane experienced an engine failure 5 minutes after' + \
     ' taking off causing the aircraft to crash.', 'Engine failure'),
    ('There was an explosion in the center fuel tank while the aircraft' + \
     ' was being pushed back for flight. Ignition of vapors in the empty' + \
     ' center tank probably resulted from faulty wiring. Several causes' + \
     ' have been presumed including chafed insulation on the wiring for' + \
     ' the center fuel tank float level switch and damaged insulation on' + \
     ' the wiring of the nearby wing anti-ice valve.', 'Conflagration'),
    ('?', 'Unknown')
]

class ReasonClassifier():

    def __init__(self):
        self.classifier = NaiveBayesClassifier(train_set)

    def classify(self, summary_str):
        return self.classifier.classify(summary_str)
