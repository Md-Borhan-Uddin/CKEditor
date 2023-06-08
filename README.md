# django-ckeditor

in this project I use django-ckeditor. I create post app there i create post model and in this model I use ckeditor

## Process of add ckeditor in django project

## Installation

Install django-ckeditor with [pip](https://pip.pypa.io/en/stable/)

```bash
  pip install django-ckeditor
  
```
## Uses

in your models.py file add

```python
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    discription = RichTextField()

```


## Authors

- [linkedin](https://www.linkedin.com/in/mdborhanuddin-python/)

- [twitter](https://twitter.com/MdBorhanUdin)

- [reddit](https://www.reddit.com/user/md_borhan)

