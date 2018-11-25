from khayyam import JalaliDate
from modules.day_counter import daycounter
from modules.shift_counter import ShiftCounter

start = JalaliDate(1397,9, 3)
end = JalaliDate(1397, 9, 30)
res = daycounter(start, end)
interns = ['amir', 'omid', 'pari', 'raoof', 'erfan', 'rahim', 'karim', 'ali', 'ashkan']
a = ShiftCounter(len(res['holidays']), len(res['pre holidays']), interns, 28, 2, ipd=True)
