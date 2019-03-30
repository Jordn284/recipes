# Recipes
Set of Jinja2-Templates to generate a recipes website

To prepare, run `make init`. This will clone the awesome [material-kit](https://demos.creative-tim.com/material-kit/index.html) and you can adjust the theme to your liking.
To add a recipe, just create a new `.yml` file in the recipes directory and run `make` again. This will compile the jinja templyte and output some html files in the out folder. In addition, this creates a zip containing the out folder for easy deployment to a web hoster.
