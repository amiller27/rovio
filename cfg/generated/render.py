#!/usr/bin/env python3

from jinja2 import Template

with open('noise_template.yaml') as f:
    template = Template(f.read())

params = {
    'imu_noise': 'false',
    'x': 0,
    'image_noise': 'false',
    'p': 0,
    'sap_noise': 'false',
    'sap_p': 0
}

for i, x in enumerate((1, 5, 10, 15)):
    with open(f'noise_imu_{i}.yaml', 'w') as f:
        new_params = params.copy()
        new_params['imu_noise'] = 'true'
        new_params['x'] = x
        print(template.render(new_params), file=f)

for i, p in enumerate((0, 20, 40, 60, 80)):
    with open(f'noise_img_{i}.yaml', 'w') as f:
        new_params = params.copy()
        new_params['image_noise'] = 'true'
        new_params['p'] = p
        print(template.render(new_params), file=f)

for i, p in enumerate((0, 0.01, 0.05)):
    with open(f'noise_sap_{i}.yaml', 'w') as f:
        new_params = params.copy()
        new_params['sap_noise'] = 'true'
        new_params['sap_p'] = p
        print(template.render(new_params), file=f)
