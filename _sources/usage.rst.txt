Usage
=====

.. _installation:

Installation
------------

To use lumache, first install it using pip:

.. code-block:: console

   (.venv) $ uv pip install lumache


Creating recipes
----------------

.. To retrieve a list of random ingredients,
.. you can use the ``lumache.get_random_ingredients()`` function:

.. .. py:function:: lumache.get_random_ingredients(kind=None)

..    Return a list of random ingredients as strings.

..    :param kind: Optional "kind" of ingredients.
..    :type kind: list[str] or None
..    :raise lumache.InvalidKindError: If the kind is invalid.
..    :return: The ingredients list.
..    :rtype: list[str]

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: error.InvalidKindError


>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']