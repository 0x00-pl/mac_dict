import csv


def load_mac_dict(filename, ret=None):
  ret = ret or {}

  if type(filename) == type([]):
    for i in filename:
      ret = load_mac_dict(i, ret) 
  else:
    with open(filename, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        ret[row[1]] = row
  return ret


def get_info(d, mac):
  mac = mac.upper()
  for i in range(len(mac), 0, -1):
    submac = mac[0:i]
    if d.get(submac) is not None:
      return d.get(submac)
  return None


if __name__ == "__main__":
  d = load_mac_dict(["oui.csv", "oui36.csv", "mam.csv"])
  r = get_info(d, "f0761ce8c784")
  print(r)
