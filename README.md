# Flower Language API

flower meanings source: https://www.almanac.com/flower-meanings-language-flowers

```
git clone https://github.com/kritserv/flower_language_api.git
```

---

### Condensed documentation

| GET path               | Result                                 | Params                               |
| :--------------------- | :------------------------------------- | :----------------------------------- |
| `/get-flower`          | return all flowers                     |                                      |
| `/get-flower/flower=`  | return flower with specified `name`    | `flower={text}`                      |
| `/get-flower/meaning=` | return flower with specified `meaning` | `meaning={text}`                     |
| `/get-flower/random=`  | get random flower(s)                     | _optional_ `random={integer <= 135}` |
| `/get-flower/id=`      | return flower with specified `id`      | `id={integer <= 135}`                |

---

Examples:

```
pip install -r requirements.txt
```

```
py main.py
```

Get the Meaning of Hibiscus:

http://127.0.0.1:5000/get-flower/flower=hibiscus

Get All Flowers with Word "Friend" in Meaning:

http://127.0.0.1:5000/get-flower/meaning=friend

Get 10 Random Flowers:

http://127.0.0.1:5000/get-flower/random=10

Get 1 Random Flower:

http://127.0.0.1:5000/get-flower/random
