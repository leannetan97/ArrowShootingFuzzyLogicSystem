# Arrow Shooting Fuzzy Logic System <br> (Soft Computing MidTerm Test WIX3001)
This is a Arrow Shooting Fuzzy Logic System using SkFuzzy Library.

In this system, the velocity is a constant value:
  > v = 30

The target standing point will be random generate within the [0, maximum_distance]:

  > maxmimum_distance = (v^2) * (sin(2*angle_in_radian))/ 9.81

## Crisp Input & Output and Fuzzy Input:
1. Crisp Input
    * Angle shoot by the shooter [45,90]
  
2. Crisp Output
    * Angle changed should be made for next attempt.
  
3. Fuzzy Input <b>[Take the crisp input to calculate the fuzzy input]</b>
    * The distance between the arrow landed and the target

## To install the dependencies:
1. Download the requirements.txt
2. Intsall using <b>pip install --no-cache-dir -r requirements.txt</b> or <b>pip install -r requirements.txt.</b>
