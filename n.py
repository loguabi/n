>>>def binary_to_decimal(binary):
decimal=0
for i in range(len(str(binary))):
power=len(str(binary))-(i+1)
decimal+=int(str(binary)[i])*(2**power)
return decimal
