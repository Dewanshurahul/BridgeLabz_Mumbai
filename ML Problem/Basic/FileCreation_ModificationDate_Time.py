import os.path, time
print("Created: %s" % time.ctime(os.path.getctime("Experiment.py")))
print("Last modified: %s" % time.ctime(os.path.getmtime("Experiment.py")))