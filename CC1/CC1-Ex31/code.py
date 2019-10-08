str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
host = str[atpos+1 : ]
host_float = float(host)
print(host_float)
