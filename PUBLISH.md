# Publishing

1. Create Distribution:
   
   - Major Release (off of `dev` Branch)
   
   - Minor Release (off of `release-*` Branch)
     
     ```bash
     [~]$ ./build.sh --cut-release
     ```

2. Upload the Distribution:
   
   - To [Test PyPI](https://packaging.python.org/guides/using-testpypi/) and verify things look right:
     
     ```bash
     [~]$ twine upload -r testpypi dist/*
     ```
   
   - To [PyPI](https://pypi.org/):
     
     ```bash
     [~]$ twine upload dist/*
     ```
