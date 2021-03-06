# PDDL-PARSER

This is a small tool to create a deterministic transition system from given the classic planning problem described by the PDDL files.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Python 3.x

* Visit https://www.python.org/downloads/ to download the latest suitable Python 3.x version according to your OS (we used Python 3.5 on Ubuntu 16.04)

### Installing

The following Python packages are required:

1. pandas
2. pickle
   
You can run the following command to install the package.
```
pip install pandas
pip install pickle
```

You can download the tool using the following command. 

```
git clone https://github.com/leelening/pddl-parser.git
```

## Running the example

We provide a running example in the example dictionary. You can find **domain.pddl** and **problem.pddl**. These files are generated by the [MulVALTOPDDL](https://github.com/leelening/MulVALTOPDDL.git).

You can create a deterministic transition system described by **transitions.pickle** by running the following commend.
```
python constructor.py ./examples/domain.pddl ./examples/problem.pddl
```

## Authors

* **Lening Li** - *Initial work* - [leelening](https://github.com/leelening)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The code is referenced by [pddl-parser](https://github.com/pucrs-automated-planning/pddl-parser)