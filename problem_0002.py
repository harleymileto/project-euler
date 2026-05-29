terms = [1,2]
while (terms[-1]+terms[-2] <= 4000000):
  terms.append(terms[-1]+terms[-2])

even_terms = []
for term in terms:
  if term%2 == 0:
    even_terms.append(term)

print(sum(even_terms))