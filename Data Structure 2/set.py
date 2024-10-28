s1={"Air India","Air Asia","Indigo","Vistara","Emirates","Etihad","SpiceJet","Srilankan Airline","Bathik Airline","Singapore Airline","Qatar Airways"}
print(s1,type(s1))
s2={"Air India","Air Asia","Gulf Airways","Oman Airways"}
s2.add("Kuwait Airways")
print(s2)
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
