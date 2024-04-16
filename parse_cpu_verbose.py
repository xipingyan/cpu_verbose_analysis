
from typing import Any


class CPU_Verbose:
  def __init__(self, line):
    itms = line.split(',')
    self.name = itms[3]
    self.kernel = itms[4]
    self.params = itms[5]
    self.tm = float(str(itms[7]).removesuffix('ms\n'))

    # Name with line NO.
    # For example: LSTMSequence_537:RNNSeq:Default -> LSTMSequence:RNNSeq:Default
    items = str(self.name).split(':')
    if len(items) > 0:
       names = str(items[0]).split('_')
       if (len(names) > 0):
          self.new_name = names[0]
          for i in range(len(items)):
             if i == 0:
                continue
             self.new_name = self.new_name + ":" + str(items[i])
    else:
       self.new_name = self.name

  def __str__(self):
    return f"{self.name}, {self.kernel}, {self.params}, {self.tm}"
  
  def __sub__(self, other):
     ret = other
     ret.tm = self.tm - other.tm
     return ret

def sort_verbs(verbs, enable_abs = False):
    if enable_abs:
        return sorted(verbs, key=lambda x: abs(x.tm))   
    else:
        return sorted(verbs, key=lambda x: x.tm)

def read_verbose(fn):
    # Using readline()
    file1 = open(fn, 'r')
    count = 0
    
    verbs = []
    while True:
        count += 1
    
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            break
        
        if line.startswith('['):
            continue
        
        verb = CPU_Verbose(line)
        verbs.append(verb)
        # print("Line{}: {}\n".format(count, line.strip()))
        # print(f'{verb}')
    
    file1.close()
    return verbs

# Unit test
if 0:
    fn='../master/openvino/build/cpu_verbose_dna.log'
    verbs = read_verbose(fn)
    verbs=sort_verbs(verbs)
    for v in verbs:
        print(f'{v}')
