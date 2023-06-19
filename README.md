<a name="readme-top"></a>
# Qanat Examples

This repository is a collection of examples for [Qanat](https://github.com/AmmarMian/qanat) experiment management system. It is constructed to references several git repositories as submodules[^1] with different projects to showcase the versatility of the tool. 

This is still a Work in Progress and documentation is in progress.

[^1]: Indeed a Qanat project must be a git repository to track the code running experiments.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#readme-top">About The Project</a>
    </li>
    <li><a href="#documentation">Documentation</a></li>
    <li>
      <a href="#installation">Installation</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#settinguptheproject">Setting up the project</a></li>
      </ul>
    </li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>


## Documentation

Documentation available at https://ammarmian.github.io/qanat/.
**Still in progress**.

## Installation

### Prerequisites

* python >= 3.6
* htcondor (for HTcondor runner)
* an emoji friendly terminal
* [Qanat](https://github.com/AmmarMian/qanat)

### Setting up the projects

You can fetch all the examples projects thanks to:

```bash
git clone --recurse-submodules https://github.com/AmmarMian/qanat-examples
cd qanat-examples
```

or a specific project by cloning the corresponding submodule.

For every example, you can setup the configuration with:

```bash
doit initialize_example
```

which will initialize the qanat repertory and add relevant experiments and datasets.


## Authors

Ammar Mian, Associate professor at LISTIC, Université Savoie Mont-Blanc
  * :envelope: mail: ammar.mian@univ-smb.fr
  * :house: web: https://ammarmian.github.io

