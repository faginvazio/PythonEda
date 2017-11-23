# make a function for matching the string

N="TAG"
K="L"
D="E"

g4 = 'NKXD'
protein = 'MASEIHMTGPMCLIENTNGRLMANPEALKILSAITQPMVVVAIVGLYRTGKSYLMNKLAGKKKGFSLGSTVQSHTKGIWMWCVPHPKKPGHILVLLDTEGLGDVEKGDNQNDSWIFALAVLLSSTFVYNSIGTINQQAMDQLYYVTELTHRIRSKSSPDENENEVEDSADFVSFFPDFVWTLRDFSLDLEADGQPLTPDEYLTYSLKLKKGTSQKDETFNLPRLCIRKFFPKKKCFVFDRPVHRRKLAQLEKLQDEELDPEFVQQVADFCSYIFSNSKTKTLSGGIQVNGPRLESLVLTYVNAISSGDLPCMENAVLALAQIENSAAVQKAIAHYEQQMGQKVQLPTETLQELLDLHRDSEREAIEVFIRSSFKDVDHLFQKELAAQLEKKRDDFCKQNQEASSDRCSALLQVIFSPLEEEVKAGIYSKPGGYRLFVQKLQDLKKKYYEEPRKGIQAEEILQTYLKSKESMTDAILQTDQTLTEKEKEIEVERVKAESAQASAKMLQEMQRKNEQMMEQKERSYQEHLKQLTEKMENDRVQLLKEQERTLALKLQEQEQLLKEGFQKESRIMKNEIQDLQTKMRRRKACTIS'

def g4_match(g4,protein):

    N = "NTAG"
    K = "KLQ"
    D = "DE"

    spl_mismatch = 0
    mismatch = 0
    for x,y in zip(g4,protein):
        if not (y in "NKD"):
            if (y in N):
                spl_mismatch+=1
            elif (y in K):
                spl_mismatch+=1
            elif (y in D):
                spl_mismatch+=1
            else:
                mismatch+=1

    if mismatch > 0 or spl_mismatch > 0:
        return False

    return True

print g4_match(g4,protein)