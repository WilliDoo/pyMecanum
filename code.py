import vex
# Configured devices
# Controller/ Name: Controller1/ config: LA directions RA turn zr/ zl claw  
# Drivetrain/ Name: drivetrain/ config: 4 motor Mecanum drivetrain, offers more mobility but slightly less speed because 
# Motor Group/ Name: claw/ config: REV RM, FOR LM

while True:
  if Controller1.axis1 != 0 or Controller1.axis2 != 0:
    wait(20, MM)
   
