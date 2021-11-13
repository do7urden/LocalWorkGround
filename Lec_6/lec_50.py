# Bir key birden fazla value yu işaret edemez. Key ler biricik olmalı.

# Master mind nedir araştır. Dictonary de bunu kullancağız.

sample_dict_list = [{'Hits': 1, 'Name': 'A'}, {'Hits': 2, 'Name': 'B'}, {'Hits': 3, 'Name': 'C'}, {'Hits': 4, 'Name': 'D'}, {'Hits': 5, 'Name': 'E'}, {'Hits': 6, 'Name': 'NONE'}]


result = {x['Name'] : x['Hits'] for x in sample_dict_list if x['Name'] != 'NONE'}
print(result)

print('###break##')