from setuptools import setup, find_packages

setup(
    name='pofium', 
    version='0.1.8',  
    description='Pacote para download e processamento dos microdados da POF do IBGE.',
    long_description=open('README.md', encoding='utf-8').read(),  # Certifique-se de que o README.md existe
    long_description_content_type='text/markdown',
    author='Gustavo G. Ximenez',
    author_email='ggximenez@gmail.com',
    url='https://github.com/ggximenez/pofium',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'unidecode',
        # Adicione outras dependências necessárias
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
