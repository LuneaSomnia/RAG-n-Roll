import pkg_resources

required_packages = [
    'streamlit',
    'fastapi',
    'mistralai',
    'snowflake-connector-python',
    'cortex-search',
    'plotly',
    'sqlalchemy',
    'python-multipart',
    'pydantic'
]

def verify_installations():
    installed = [pkg.key for pkg in pkg_resources.working_set]
    return all(package in installed for package in required_packages)
