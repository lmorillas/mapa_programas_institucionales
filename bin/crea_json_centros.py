import json
import itertools

pros = json.load(open('programas.json')).get('items')
pros.sort(key=lambda x: x['cproy'])
centros = dict([[k, ','.join([x['ccentro'] for x in v])] for k,v in itertools.groupby(pros, key=lambda x: x['cproy'])])

json.dump(centros, open('proycentros.json', 'w'))
