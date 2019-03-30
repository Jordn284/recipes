from os import listdir
from os.path import isfile, join

from jinja2 import Template, FileSystemLoader, Environment
import yaml

recipes_folder="./recipes"
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('recipe_template.j2')
yamls = [f for f in listdir(recipes_folder) if isfile(join(recipes_folder, f)) and f.endswith(".yml")]
recipes = []
for fn in yamls:
    print(fn)
    f = open(recipes_folder+"/"+fn,'r')
    fn = fn.split('.')[0]
    url = fn+".html"
    recipe = yaml.load(f.read())
    recipe['url']=url
    recipes.append(recipe)
    rendered = template.render(recipe)
    with open("./out/"+url, "w") as fh:
        fh.write(rendered)


index_template = env.get_template('index_template.j2')
content={}
content['recipes']=recipes
index_rendered = index_template.render(content)
with open("./out/"+"index.html", "w") as fh:
    fh.write(index_rendered)
