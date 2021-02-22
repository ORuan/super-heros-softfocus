# SuperHero(back-end)

### Instalação
- obs: o node/npm e python devem estar instaladas na máquina


O back-end e o front-end foram migrados para repositórios diferentes, para facilitar
o deploy posteriormente.
Sendo assim, esse é o backend['heroku'] e o [frontend-react](https://github.com/ORuansoft-focus-sh-frontend)

```
git clone https://github.com/ORuan/super-heros-softfocus
cd super-heros-softfocus; git checkout dev-heroku-deploy
python3 -m venv .env; source .env/bin/active
pip install -r requirements.txt
python3 manage.py runserver
```
---
Agora o frontend
```
git clone https://github.com/ORuan/soft-focus-sh-frontend
cd soft-focus-sh-frontend
npm i; npm start
```
### Vua lá
Abra seu navegador na url[*] http://localhost:3000/