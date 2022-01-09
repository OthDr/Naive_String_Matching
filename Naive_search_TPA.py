print'Naive String Matching \n \n'

def search(pat, txt):                # -------fonction de type void 

	M = len(pat)         	    # longueure du pattern (mot desire) .
	N = len(txt)  		   # longueure du texte .
	 
	for i in range(N - M + 1): # boucle pour parcourir pat[] case par case
		j = 0
		
		# pour l'actuelle valeur de l'index i, verifier pour pattern match
		while(j < M): 

			if (txt[i + j] != pat[j]): 
				break
			j += 1

		if (j == M): 
			print("Pattern found at the index ", i) 

# --------- -------------Test de l'Algorithme ---------------------------------
 
txt = "TAPTPAAPTPAPTAAATPAA"
pat = "TPA"
print'*--Your text: ',txt
print'*---Your pattern:',pat
search(pat, txt)
