*sphinxcontrib-fsharp* is a `Sphinx <http://www.sphinx-doc.org/>`_ (1.6.3+)
extension to document `F# <https://fsharp.org/>`_ libraries. It
provides a Sphinx `domain
<http://www.sphinx-doc.org/en/stable/domains.html>`_ for F# and
`autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_-like
directives to generate documentation from source code (not ported to F#
yet).

It's licensed under the `MIT license <http://choosealicense.com/licenses/mit/>`_.
It's available on the `Python package index <http://pypi.python.org/pypi/sphinxcontrib-fsharp>`_.
Its `documentation <http://jacquev6.github.io/sphinxcontrib-ocaml>`_
and its `source code <https://github.com/dbrattli/sphinxcontrib-fsharp>`_ are on GitHub.

Questions? Remarks? Bugs? Want to contribute? `Open an issue
<https://github.com/dbrattli/sphinxcontrib-fsharp/issues>`__!

Status
======

sphinxcontrib-fsharp is a fork of spinxcontrib-ocaml and still highly
experimental. Interfaces may be changed unannounced. We welcome all
contributions so please feel free to submit PRs.

Quick start
===========

Install both packages::

    $ pip3 install sphinxcontrib-fsharp

Enable and configure the Sphinx extension in your ``conf.py`` file::

    extensions.append("sphinxcontrib.fsharp")
    primary_domain = "fsharp"  # Optional
    fsharp_source_directories = ["src"]
    fsharp_findlib_packages = ["batteries", "js_of_fsharp"]

And document your module (in an ``.rst`` file)::

    .. autoocamlmodule:: MyModule
