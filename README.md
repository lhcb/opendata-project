# An everware demo

Everware demo repository. It contains various demonstrations of what
you can do with everware, jupyter notebooks, and integrating it with
the CERN infrastructure.


# Running it on Everware

If you have access to an [`everware`](//github.com/everware/everware) instance
you can try out this repository by pasting a link to this repository.


# Running it locally

You can execute this demo locally with the `run_local.sh` script. This
is particularly useful during development. You will have to install
[docker](http://docker.io) on your machine.

For this to work you will have to build the docker container first with

```
docker build -t betatim/everware-demo .
```


# Credits

The `cms-jpsi.ipynb` notebook is from [`everware/everware-dimuon-example`](https://github.com/everware/everware-dimuon-example)
and was written by [Noel Dawe](https://github.com/ndawe).

The `RooFit-tutorial.ipynb` notebook is from [`betatim/roofit_tutorial_solutions`](https://github.com/betatim/roofit_tutorial_solutions).
