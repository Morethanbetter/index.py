
index.py
========

中文 | `English <https://github.com/abersheeran/index.py/tree/master/README-en.md>`_


.. image:: https://github.com/abersheeran/index.py/workflows/Test/badge.svg
   :target: https://github.com/abersheeran/index.py/actions?query=workflow%3ATest
   :alt: Github Action Test


.. image:: https://github.com/abersheeran/index.py/workflows/Build%20setup.py/badge.svg
   :target: https://github.com/abersheeran/index.py/actions?query=workflow%3A%22Build+setup.py%22
   :alt: Build setup.py


.. image:: https://github.com/abersheeran/index.py/workflows/Publish%20PyPi/badge.svg
   :target: https://github.com/abersheeran/index.py/actions?query=workflow%3A%22Publish+PyPi%22
   :alt: Publish PyPi


.. image:: https://img.shields.io/pypi/v/index.py
   :target: https://pypi.org/project/index.py/
   :alt: PyPI


.. image:: https://img.shields.io/pypi/pyversions/index.py
   :target: https://img.shields.io/pypi/pyversions/index.py
   :alt: PyPI - Python Version


一个基于 ASGI 协议的高性能 web 框架。\ `Index.py 文档 <https://abersheeran.github.io/index.py/>`_


* 灵活且高效的路由系统 (基于 Radix Tree)
* 自动解析请求 & 生成文档 (基于 ``pydantic``\ )
* 可视化 API 接口 (基于 ``ReDoc``\ , 针对中文字体优化)
* 现代化的测试组件 (基于 ``pytest`` 与 ``requests``\ )
* 非常简单的部署 (基于 ``uvicorn`` 与 ``gunicorn``\ )
* 挂载 ASGI/WSGI 应用 (比 ``starlette`` 更易用)
* 更好用的 background tasks
* 可使用任何可用的 ASGI 生态

Install
-------

.. code-block:: bash

   pip install -U index.py

或者直接从 Github 上安装最新版本（不稳定）

.. code-block:: bash

   pip install -U git+https://github.com/abersheeran/index.py@setup.py
