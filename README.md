# Work Time Calculator
Small tool to calculate the exact business time between two dates.

## Features
- Aims for performance
- Multiple ways to define working hours
- Considers holidays from a list

## Install
```pip install work-time-calc```

## Quick example
Just create a calculator and call it to get the difference:
```python
from work_time_calc.calc import WorkTimeCalculator

calc = WorkTimeCalculator(9, 18, 'mon tue thu fri sat')
delta = calc("2050-02-10T10:30:00", "2050-03-10T18:15:00")

print(delta.seconds)    # 675000.0
print(delta.as_dhms)    # {'days': 7, 'hours': 19, 'minutes': 30, 'seconds': 0}
print(delta.as_hms)     # {'hours': 187, 'minutes': 30, 'seconds': 0}
```

## Constructor examples
```python
calc = WorkTimeCalculator(8, 15)
calc = WorkTimeCalculator(8, 15, '1100100')
calc = WorkTimeCalculator(8, 15, 'sat tue thu mon sun')
calc = WorkTimeCalculator("08:30", "18:30")
calc = WorkTimeCalculator(9, "17:45")
calc = WorkTimeCalculator(datetime.time(8, 30), datetime.time(18, 30))
calc = WorkTimeCalculator(detail=[(8, 16), (8, 16), (8, 16), (8, 16), (8, 10), None, None])
calc = WorkTimeCalculator(detail=[(8, "16:30"), ("17:15", 20), None, None, None, None, None])
```

## To do
- Overnight shifts (spanning two days)
- Small performance improvements
