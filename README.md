# Boilerplate for KITDM mapping-service plugins

Ever wrote a python script or CLI to convert some data input to some data output? And being happy with the result you wanted to provide it to an end user, but they rejected the idea of installing python or to run a CLI at all?

Ever wanted a simple magic button for your script and its configuration? 

Then this may be the project for you.

The [kit-datamanager/mapping-service](https://github.com/kit-data-manager/mapping-service) provides a generic web interface for mapping between documents and formats. The mapping functionalities can be provided as task specific plugins.
This repository intends to work as a boilerplate for python plugins.

## Features

- Boilerplate plugin that may work for most use cases without any adaption. Everything concerning the python code can be put behind the `plugin_wrapper.py`
- Preconfigured CI workflows. Your plugin can be automatically tested against specified and the latest version of the mapping-service. Providing additional `hurl` tests is recommended.
- Automatic version alignment of python code and java plugin
- Standardized building blocks and tool chains. Works seamlessly with open source best practice tools such as [somesy](https://github.com/Materials-Data-Science-and-Informatics/somesy).

## Caveats

- Using the same class name multiple times in the same mapping service instance can cause problems. It is highly recommended to adapt the package name and the class name of the plugin.