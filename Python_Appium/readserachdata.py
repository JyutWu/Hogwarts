import yaml

with open('./searchdata.yaml') as f:
    data = yaml.safe_load(f)
    print(data)
