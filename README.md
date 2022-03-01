Tagname to follow ta-lib python version

```
docker build -t joshteng/m1test .
docker push joshteng/m1test
```

```
docker pull joshteng/m1test
docker run -it joshteng/m1test
```

Requirements
```
Python > 3.9
brew install ta-lib
```

Run it
```python
pip install -r requirements.txt
python start.py
```