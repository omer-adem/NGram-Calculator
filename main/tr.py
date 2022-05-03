import re
def lower(self):
    self = re.sub(r'İ', 'i', self)
    self = re.sub(r'I', 'ı', self)
    self = self.lower()
    return self

def upper(self):
    self = re.sub(r'i', 'İ', self)
    self = self.upper()
    return self