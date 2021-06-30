[![CI](https://github.com/sontt22791/mlops-01-github-actions/actions/workflows/main.yml/badge.svg)](https://github.com/sontt22791/mlops-01-github-actions/actions/workflows/main.yml)

# mlops-01-github-actions
create first github actions project


## create new virtualenv
```python3 -m venv ~/.venv```
(~/.venv => . o truoc de hide folder env di
~ la dir HOME)

source it
```source ~/.venv/bin/activate```


create requirements.txt
```
touch requirements.txt
vim requirements.txt
=> add library
```

create Makefile
```co the su dung lai cho cac project khac```

code
```tao hello.py va test_hello.py```

git push
```
git status => check
git add => add file da modified
git commit -m "haha" => commit
git push
git pull
```

tao github actions
```
sau khi push len github => vao github actions => create workflows
```

NOTE:
```
- co the tao nhieu github action tren 1 project bang cach new 1 workflow moi
- Makefile co the dat ten cac action, vd: install, install-gcp, install-aws
```
