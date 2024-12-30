import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-equipment-request",
    description="Meta package for open-synergy-ssi-equipment-request Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_equipment_request',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
