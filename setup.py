from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='uniswapfeecalculator',
    version='0.1.2',
    description='Useful tools to calculate the Fee APR in any Uniswap V3 pool',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Johnny Chuang',
    author_email='johntzuyang@gmail.com',
    keywords=['Uniswap', 'Fee', 'Uniswap V3'],
    url='https://github.com/ZooWallet/Uniswap-Fee-Calculator',
    download_url='https://pypi.org/project/uniswapfeecalculator/'
)

install_requires = [
    'pandas>=1.4.3',
    'requests>=2.28.1'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
