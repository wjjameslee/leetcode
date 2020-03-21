# * recordError()
# * getErrorCount()

# Write the implementation of the two functions such that you can efficiently fetch
# the number of errors occurring in the last 60 seconds.

# The recordError() function is called from external code with no arguments -
# say, every time a specific error event occurs, like a server issuing a 500.
# getErrorsCount() should return a count, a single integer that represents the # of errors

# ---------- Example -----------

# getErrorCount() => 0
# recordError()
# recordError()

# # 30 seconds pass

# getErrorCount() => 2
# recordError()

# 31 seconds pass (61 since initial calls)

# getErrorCount() => 1

# 30 seconds pass
# getErrorCount() => 0

class error():
  
  def __init__(self, num_err):
    self.num_err = num_err
    self.time_stack = []
  
  def recordError(self, t):
    self.time_stack.append(t)
    self.num_err += 1
    
  
  def getErrorCount(self, t):
    res = self.num_err
    l_stack = len(self.time_stack)
    diff = t
    i = 0
    while i < l_stack:
        if diff - self.time_stack[i] > 60:
            
            self.num_err -= 1
            self.time_stack.pop(i)
            l_stack -= 1
        i += 1
    return self.num_err
  
e = error(0)
e.recordError(0)
e.recordError(15)
e.recordError(30)
print(e.getErrorCount(45))
print(e.getErrorCount(60))
print(e.getErrorCount(75))
print(e.getErrorCount(76))
print(e.getErrorCount(91))