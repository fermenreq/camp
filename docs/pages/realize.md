---
layout: default
---

# CAMP Realize

CAMP also builds the docker images and the *docker-compose* file that
we need to run the configurations that we generated using `camp
generate`. We explain here:
 1. How to [use the `camp realize` command](#usage);
 2. How to [organize the template orchestration](#template);
 3. How to [specify the components' implementation ](#implementation); 
 4. How to [specify the variables' realization](#variables).


## Usage
<a name="usage"/>

To implement the configurations we have generated, and provided we
have completed the `model.yml` file, we simply invoke the command:

```bash
$> camp realize -d .
```

CAMP then generates new Dockerfiles, properly chained together
according to the configurations generated by `camp generate`. In
addition, CAMP injects the proper variables' value in each
configuration. It generates as well the service orchestration as a
`docker-compose` file.

To work, `camp realize` needs three things:

 1. Some configurations generated using `camp generate`. CAMP will
	search for directories named like `./config_1`, `./config_2`, that
	must contains a file `configuration.yml` that CAMP generates.

 1. A `camp.yml` files that includes information about the
	implementation of each component. This information includes:

	* A template deployment, including the implementation of each
	  component, and the configuration of the orchestration. So far,
	  CAMP only supports the [Docker](https://www.docker.com/)
	  technology.

	* Details about how CAMP must realize the variables.


## Template Deployment
<a name="template"/>

Below is a sample directory structure for a CAMP project. Note that
the command `camp generate` would add another `out` directory, which
we did not show here.

```bash
$ tree 
├── camp.yml
└── template
    ├── docker-compose.yml
    ├── postgres
    │   ├── Dockerfile
    │   └── postgresql-template.conf
    └── showcase
        ├── Dockerfile
        ├── mpm_prefork-template.conf
        └── mpm_worker-template.conf
```

The `template` directory contains a directory named after **each
component defined in the CAMP model** (i.e., the file `camp.yml`),
that contains a `Dockerfile`. It also contains a `docker-compose.yml`
as a template orchestration.

Note that additional file may be added along with the Dockerfile, for
confiuration purpose for instance.

--- 

**Note.** The names of the files directories matter. CAMP expects to
find directory named `template` inside which it will search for a
`docker-compose.yml` file and directory ndmes after the components
defined in the CAMP model, each containing a `Dockerfile`.

---


## Component Implementation
<a name="implementation"/>

### Using Dockerfile
<a name="docker-file"/>

The first thing we must add in our `model.yml` is the implementation of
each component. For instance, if we have implemented the `tests`
component with a Dockerfile, we must specify this as follows:

```yaml
components:
   tests:
      provide_services: [ Tests ]
      require_services: [ Awesome ]
      variables:
         threads:
            values:
               range: [10, 50] # in GB
               coverage: 40
      implementation:
         docker:
            file: repo/tests/Dockerfile
```

Note that if there are other resources such as configuration files,
they could stay with the Dockerfile and they would be copied in each
generated configuration.

### Using a Docker Image
<a name="docker-image"/>

Alternatively, some components may be implemented by existing docker
images, such as database or application servers for instance. In our
*Awesome* example, we added the following implementation:

```yaml
components:
   postgres:
      provide_services: [ DB ]
      implementation:
         docker:
            image: postgres:10.6-alpine
```
CAMP will fetch the image `postgres:10.6-alpine` from Docker Hub.


## Variable Realization
<a name="variables"/>

As we've seen CAMP let you define variables  whose value
may vary from one configuration to another. For instance, in our
*Awesome* example, we found the following definition:

```yaml
components:
   tests:
      provide_services: [ Tests ]
      require_services: [ Awesome ]
      variables:
         threads:
            values:
               range: [10, 50] # in GB
               coverage: 40
```

This defines a variable named `threads` whose value ranges from 10
to 50. See the [`camp generate` documentation for more
details](generate.html).

In order to realize the `tests` component, we must tell CAMP where
it must place the values of this `threads` variable. In the following
example, we ask CAMP to substitute the `threads` value in the
Dockerfile.

```yaml
components:
   tests:
      provide_services: [ Tests ]
      require_services: [ Awesome ]
      variables:
         threads:
            values:
               range: [10, 50] # in GB
               coverage: 40
            realization:
               - targets: [ repor/tests/Dockerfile ]
                 pattern: MAX_THREADS=4
                 replacements: [ "MAX_THREADS={value}" ]
```

Note that the `realization` entry may lists several substitutions
(though only one is given here). Each substitution will be carried out
on every file listed in the `targets` entry. Each time, CAMP will
replace the given `pattern` with the given `replacement`, where
`{value}` stands for the actual value. For instance, if CAMP
assigns 10 to the `threads` variable, the Dockerfile will eventually
contains the text "MAX_THREAD=10".

---

**Note** Subtitutions may target any files, including the
docker-compose file, or other configurations files.

---
