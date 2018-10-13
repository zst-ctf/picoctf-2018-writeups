from collections import Counter
import json
import statistics

with open("./incidents.json") as f:
  json_data = f.read()
  data = json.loads(json_data)

# What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
src_ip = list(map(lambda x: x['src_ip'], data['tickets']))
print("Most common", Counter(src_ip).most_common(1)[0][0])
print()

# How many unique destination IP addresses were targeted by the source IP address xxx?
src_ip = input('Input source IP: ').strip()
uniq_ip = list(filter(lambda x: x['src_ip'] == src_ip, data['tickets']))
uniq_ip_2 = set(map(lambda x: x['dst_ip'], uniq_ip))
print('Unique dest', len(uniq_ip_2))
print()

# What is the average number of unique destination IP addresses that were sent a file with the same hash?
# Your answer needs to be correct to 2 decimal places.
hashes = set(map(lambda x: x['file_hash'], data['tickets']))
to_average = []
for hash in hashes:
  uniq_ip = list(filter(lambda x: x['file_hash'] == hash, data['tickets']))
  uniq_ip_2 = set(map(lambda x: x['dst_ip'], uniq_ip))
  to_average.append(len(uniq_ip_2))
print("Average unique dest:", statistics.mean(to_average))
print()


