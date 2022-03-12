import re
a = input()

pattern = r'\W*\d*[A-Z]*(?P<naiti>[a-z]+_[a-z]+)\W*\d*[A-Z]*'

print(re.search(pattern, a).group('naiti')) if re.search(pattern, a) != None else print('Ne naideno')
#aa_sksks ----- aa_sksks
#Ajassj_alsksk --- jassj_alsksk
#AAa_aslA ---- a_asl
#==-ALAals_alqoq --- als_alqoq
#==ASKKsall_aal==1  ---- sall_aal