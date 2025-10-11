t = int(input("Quanto tempo em segundos demora esse evento? L"))
h = t/3600
m = (t%3600)//60 
s = (t%3600)%60 


print(f" O tempo desse evento é {int(h)}h {m}min {s}s")

