
# HowTo

```
for i in ~/devel/quasartest/konto/Kontoumsaetze_*; \
do \
  echo "${i}"; venv/bin/python3 fix_trans_2019.py "${i}" > "${i/Konto/Fixed__Konto}"; \
done
```

