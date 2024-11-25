#!/usr/bin/env python3

# Rosalind prtm exercise

# from util import read_input -> had some issues, so I just copy pasted the string from the txt

sample = "SIAYNVWTGWAFPWGASTCVFALKVCVLKVNWSRTWGPCRQSAFQNCWSWSMFERTYFAAVICPEHVTAMKNTIQFSWRVPQDAEIMIEWWQLRSLMIGCCMDQCSRIIRYFRKLKIHRQMIYFGCVAWDALSYQGHPRLGLEGMEMGMALRCDCISGLLGRIQQSSPKVQYGGIHMSKYHHTMHIKKIEFDLMHSCCGGVLPCGTVRTDREMAHFHCAMGNHSDSQWEQQIVFQDPRNECFHVMGDYLFSEPKMVPVTLVLGWFFKGCCRVKYWDMIHGYWVKTFTLEEDIMDNENVYKKVISDPGGPEQCIIKNSKGNDSMMYLELCAYINNQHTFYGICPRPLMDERISNHFDDGAQCEYPGIEQWQFHIRGLGEATIRQDETPTPDMRNGDLCRTRFASYSDAKQQQAAASGDPCESGDDNHWGIWSCILHTLNEDRETHSHVTKLNAHQDWVDKVFIRINVTFRIWWVTHIPAQWTLTPPSTNQNQKIVDPGYCISKHHFAGAHRKDPFSRPIQVHQKEEIAMLMIWFMVWSTPRIHEYPSWCWTSEVGMYFGVRCVFWDVVSHEAAFGYDTSFALIGYSWPMQSQEQDAPDEYLSHLTGKAKNRLEVDVRYYSWYCNWKLVDCEPGWFAIMDECLCKTMDHDTGCCLVYAKANTQVVELTQADIGHLFHNKSFYTHCQPVLAERNVSKFICDDPQPNMISRNPHTGSDEQEVMIPKGYTIRMMIEWINCRDFVTTWCAMRVEYGGCDNQYRCYHWLDNYITNYVFTCITVQISCFYEYLDPLQALESDKYKGGGEFNDWPFSPPQDWEHWIKQSVPLWASYACRAPGRRCAFSEGKHERTDDDAQTNDGNRFLEGKYYYSKPQAFYIMRINRFQAYCMCMQVAGNLNEAEKRNVMNVFTVHRAWPKPAHWHPTFLDCISVMWNWTYIKCPRAWWDSAKPMKCENMWAGPI"

protein = sample

# I mostly did what we did for the last exercise, first a dictionary

weight_dict = {
"A": "71.03711",
"C": "103.00919",
"D": "115.02694",
"E": "129.04259",
"F": "147.06841",
"G": "57.02146",
"H": "137.05891",
"I": "113.08406",
"K": "128.09496",
"L": "113.08406",
"M": "131.04049",
"N": "114.04293",
"P": "97.05276",
"Q": "128.05858",
"R": "156.10111",
"S": "87.03203",
"T": "101.04768",
"V": "99.06841",
"W": "186.07931",
"Y": "163.06333" }

# then almost the same for loop, but with spaces added for the weight string output
# That was neccessary, because otherwise the output string was one long noodle of all the numbers put together
weight = ""

for start in range(0, len(protein)):
    codon = protein[start:start+1]
    aminoacid = weight_dict[codon]
    weight += aminoacid + " "

# The final thing with which I struggled after I made the string output work, was how to get python to add the numbers together (or even read them as numbers).
# turns out, it was needed to turn them into floats! Also, what I had no idea about, was that I needed to use .split to have the weight numbers be seperate. 
# Then, everything finally worked! The biggeset challenge was figuring out how to get the string converted into numbers (took some research but here we are)

weight_sum = [float((weight_number) for weight_number in weight.split())]

print(sum(weight_sum))
