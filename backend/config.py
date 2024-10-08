from enum import Enum
import os

DATA_DIRECTORY = os.path.join(os.getcwd(), "export_data")
HEALTH_ELEMENTS_DIRECTORY = os.path.join(DATA_DIRECTORY, "health_records")
HEALTH_ELEMENTS_VITALS_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "vitals")
HEALTH_ELEMENTS_HEALTH_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "health")
HEALTH_ELEMENTS_ACTIVITY_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "activity")
HEALTH_ELEMENTS_AUDIO_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "audio")
HEALTH_ELEMENTS_MOBILITY_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "mobility")
HEALTH_ELEMENTS_ENVIRONMENT_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "environment")
HEALTH_ELEMENTS_SLEEP_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "sleep")
HEALTH_ELEMENTS_SYMPTOMS_DIRECTORY = os.path.join(
    HEALTH_ELEMENTS_DIRECTORY, "symptoms")


ELECTROCARDIOGRAM_ELEMENTS_DIRECTORY = os.path.join(
    DATA_DIRECTORY, "electrocardiograms")
WORKOUT_ELEMENTS_DIRECTORY = os.path.join(DATA_DIRECTORY, "workout_records")
WORKOUT_ROUTE_ELEMENTS_DIRECTORY = os.path.join(
    WORKOUT_ELEMENTS_DIRECTORY, "workout-routes")

HEALTH_EXPORT_DIRECTORIES = [
    DATA_DIRECTORY,
    HEALTH_ELEMENTS_DIRECTORY,
    ELECTROCARDIOGRAM_ELEMENTS_DIRECTORY,
    WORKOUT_ELEMENTS_DIRECTORY,
    WORKOUT_ROUTE_ELEMENTS_DIRECTORY,
    HEALTH_ELEMENTS_VITALS_DIRECTORY,
    HEALTH_ELEMENTS_ACTIVITY_DIRECTORY,
    HEALTH_ELEMENTS_AUDIO_DIRECTORY,
    HEALTH_ELEMENTS_MOBILITY_DIRECTORY,
    HEALTH_ELEMENTS_ENVIRONMENT_DIRECTORY,
    HEALTH_ELEMENTS_SLEEP_DIRECTORY,
    HEALTH_ELEMENTS_SYMPTOMS_DIRECTORY,
    HEALTH_ELEMENTS_HEALTH_DIRECTORY
]

ACTIVITY_SUMMARY_FILE_NAME = 'ActivitySummaries.csv'
WORKOUTS_SUMMARY_FILE_NAME = 'Workouts.csv'


HEALTH_RECORDS = [
    "BodyFatPercentage",
    "BodyMass",
    "BodyMassIndex",
    "DietaryWater",
    "HandwashingEvent",
    "ToothbrushingEvent",
    "Height",
    "DietaryCaffeine",
    "MindfulSession",
    "WaistCircumference"
]


VITAL_SIGN_RECORDS = [
    "HeartRate",
    "RestingHeartRate",
    "WalkingHeartRateAverage",
    "HeartRateVariabilitySDNN",
    "HeartRateRecoveryOneMinute",
    "AtrialFibrillationBurden",
    "OxygenSaturation",
    "BodyTemperature",
    "HighHeartRateEvent",
    "IrregularHeartRhythmEvent",
    "LowHeartRateEvent",
    "BloodPressureDiastolic",
    "BloodPressureSystolic",
    "RespiratoryRate",
    "VO2Max"
]

ACTIVITY_RECORDS = [
    "StepCount",
    "DistanceWalkingRunning",
    "RunningGroundContactTime",
    "RunningPower",
    "RunningSpeed",
    "RunningStrideLength",
    "RunningVerticalOscillation",
    "DistanceCycling",
    "PushCount",
    "DistanceWheelchair",
    "SwimmingStrokeCount",
    "DistanceSwimming",
    "DistanceDownhillSnowSports",
    "BasalEnergyBurned",
    "ActiveEnergyBurned",
    "FlightsClimbed",
    "NikeFuel",
    "AppleExerciseTime",
    "AppleMoveTime",
    "AppleStandTime",
    "AppleStandHour",
    "PhysicalEffort"
]

AUDIO_RECORDS = [
    "EnvironmentalAudioExposure",
    "HeadphoneAudioExposure",
    "EnvironmentalSoundReduction",
    "AudioExposureEvent",
    "HeadphoneAudioExposureEvent",
]

MOBILITY_RECORDS = [
    "AppleWalkingSteadiness",
    "SixMinuteWalkTestDistance",
    "WalkingSpeed",
    "WalkingStepLength",
    "WalkingAsymmetryPercentage",
    "WalkingDoubleSupportPercentage",
    "StairAscentSpeed",
    "StairDescentSpeed",
    "AppleWalkingSteadinessEvent"
]

ENVIRONMENTAL_RECORDS = [
    "UVExposure",
    "UnderwaterDepth",
    "WaterTemperature",
    "TimeInDaylight",
]

SLEEP_RECORDS = [
    "AppleSleepingWristTemperature",
    "SleepAnalysis",
    "SleepDurationGoal"
]

SYMPTOM_RECORDS = [
    "RapidPoundingOrFlutteringHeartbeat",
    "AbdominalCramps",
    "Bloating",
    "Constipation",
    "Diarrhea",
    "Heartburn",
    "Nausea",
    "Vomiting",
    "AppetiteChanges",
    "Chills",
    "Dizziness",
    "Fainting",
    "Fatigue",
    "Fever",
    "GeneralizedBodyAche",
    "HotFlashes",
    "ChestTightnessOrPain",
    "Coughing",
    "ShortnessOfBreath",
    "SkippedHeartbeat",
    "Wheezing",
    "LowerBackPain",
    "Headache",
    "MemoryLapse",
    "MoodChanges",
    "LossOfSmell",
    "LossOfTaste",
    "RunnyNose",
    "SoreThroat",
    "SinusCongestion",
    "BreastPain",
    "PelvicPain",
    "VaginalDryness",
    "Acne",
    "DrySkin",
    "HairLoss",
    "NightSweats",
    "SleepChanges",
    "BladderIncontinence",
    "ECGOtherSymptom",
]


class AppleHealthPrefix(Enum):
    """Enum of all the Apple Health prefixes"""
    BIOLOGICAL_SEX = "HKBiologicalSex"
    BLOOD_TYPE = "HKBloodType"
    CATEGORY_TYPE_IDENTIFIER = "HKCategoryTypeIdentifier"
    CHARACTERISTIC_TYPE_IDENTIFIER = "HKCharacteristicTypeIdentifier"
    FITZPATRICK_SKIN_TYPE = "HKFitzpatrickSkinType"
    HEALTH_KIT = "HK"
    METADATA_KEY = "HKMetadataKey"
    QUANTITY_TYPE_IDENTIFIER = "HKQuantityTypeIdentifier"
    WORKOUT_ACTIVITY_TYPE = "HKWorkoutActivityType"
    WORKOUT_EVENT_TYPE = "HKWorkoutEventType"
    HEALTH_KIT_DATA_TYPE = "HKDataType"


class HeartRateMotionContext(Enum):
    """Enum of all the heart rate location options"""
    NOT_SET = 0
    SEDENTARY = 1
    ACTIVE = 2

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


# https://developer.apple.com/documentation/healthkit/hkvo2maxtesttype
class VO2MaxTestType(Enum):
    """Enum of all the V02 Max Test Types"""
    MAX_EXERCISE = 1
    PREDICTION_SUB_MAX_EXERCISE = 2
    PREDICTION_NON_EXERCISE = 3

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


class PhysicalEffortEstimationType(Enum):
    """Enum of all the physical effort estimation types"""
    ACTIVITY_LOOKUP = 1
    DEVICE_SENSED = 2

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


# https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype
class SwimmingLocations(Enum):
    """Enum of all the swimming location options"""
    UNKNOWN = 0
    POOL = 1
    OPEN_WATER = 2

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


# https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle
class SwimmingStrokeStyles(Enum):
    """Enum of all the swimming stroke styles"""
    UNKNOWN = 0
    MIXED = 1
    FREESTYLE = 2
    BACKSTROKE = 3
    BREASTSTROKE = 4
    BUTTERFLY = 5
    KICK_BOARD = 6

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name.replace('_', ' ')


# https://developer.apple.com/documentation/healthkit/hkworkoutsessiontype
class WorkoutSessionType(Enum):
    """Enum of all the workout session types"""
    PRIMARY = 0
    MIRRORED = 1

    @ classmethod
    def from_value(cls, value: int) -> str:
        return cls(value).name

# https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate

# https://developer.apple.com/documentation/healthkit/hkworkouteventtype
