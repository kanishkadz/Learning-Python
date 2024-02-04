Engg
-- __init__.py
-- years
  -- __init__.py
   -- sem.py
-- main.py



# Engg/years/sem.py

def staff():
    print("Function: staff in sem module")

def student():
    print("Function: student in sem module")


# main.py

from Engg.years import sem

# Using functions from sem module
sem.staff()
sem.student()
