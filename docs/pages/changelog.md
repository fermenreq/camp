# CAMP Versions

Below is the list of CAMP versions, along with a quick summary of the
changes that were made.

*   Development


*   CAMP v0.3

    *   CAMP v0.3.6 (Apr. 29, 2019)

        *   Fix [Issue
            48](https://github.com/STAMP-project/camp/issues/48) about
            the `camp realize` command, which failed when a variable
            substitution targeted a file nested in a subdirectory of a
            component template.

    *   CAMP v0.3.5 (Apr. 25, 2019)

        *   Fix [Issue
            46](https://github.com/STAMP-project/camp/issues/46) about
            failing string concatenation in the UI during `camp
            execute`.

    *   CAMP v0.3.4 (Apr. 12, 2019)

        *   Expose the parameter of CAMP execute in the CAMP model.

        *   Add a new Python example following the Java Greetings example.

        *   Move to Green 2.15.0, which generates JUnit reports (see
            [Issue 104](https://guthub.com/cleancut/green/issue/104)).

        *   Drop the tecor tool that was in the repository under the
            `modules` directory. This is replaced by CAMP execute.

    *   CAMP v0.3.3 (Apr. 9, 2019)

        *   Move to Green 2.14.2. Fix [Issue
            203](https://github.com/cleancut/green/issues/203) about the
            'GreenStream' object that had no attribute 'encoding' when
            capturing tests's output.

        *   Port to Python 3.5. Runs now on both Python 2.7 and 3.5.

    *   CAMP v0.3.2 (Apr. 3, 2019)

        *   Merge with [Pull Request
            38](https://github.com/STAMP-project/camp/pull/38) that
            contains the case-study from ActiveEon.

        *   Test CAMP against multiple versions of Z3 (4.8.4, 4.7.1 and
            4.6) using Travis Matrix Build.

    *   CAMP v0.3.1 (Apr. 1, 2019)

        *   Fix [Issue
            35](https://github.com/STAMP-project/camp/issues/35) by
            using `docker cp` to fetch test reports, instead of
            mounting volumes.

        *   Fix [Issue
            27](https://github.com/STAMP-project/camp/issues/27) with
            revision of the installation documentation that pointed to
            CAMP v1.0.0, which does not exists yet.

        *   Fix [Issue
            33](https://github.com/STAMP-project/camp/issues/33) by
            taking into account the presence of `settings.xml` to
            avoid Maven to create local repository in a directory that
            does not exist.

        *   Fix [Issue
            32](https://github.com/STAMP-project/camp/issues/32) and
            move dependencies from `requirements.txt` to
            `setup.py`. Add an alternative installation procedure,
            which does not requires docker.

        *   Fix [Issue
            28](https://github.com/STAMP-project/camp/issues/28) about
            libgomp that fails the Docker build process.

    *   CAMP v0.3.0 (Mar. 21, 2019)

        *   New version of the `camp execute` command that deploys
            generated configuration, runs tests, and collect and
            aggregates test reports.

        *   Fix [Security Issue
            CVE-2017-18342](https://nvd.nist.gov/vuln/detail/CVE-2017-18342)
            on PyYAML before version 4.1

	    *   Fix reporting of missing configurations (similar to [Issue
		    25](https://github.com/STAMP-project/camp/issues/25)).

*   CAMP v0.2

	*   CAMP v0.2.3 (Nov. 22, 2018)

		*   Fix reporting of missing CAMP model, as per [Issue
			25](https://github.com/STAMP-project/camp/issues/25)

	*  CAMP v0.2.2 (Nov. 20, 2018)

		*   Update the documentation of the CityGo case to explain why
			there are only 10 possible configurations, as noted in
			[Issue
			24](https://github.com/STAMP-project/camp/issues/24)

		*   Fix the generation of the `build_images.sh` script as per
			[Issue
			23](https://github.com/STAMP-project/camp/issues/23)

		*   New documentation page that explains how to contribute to
			the code and documentation.

	*   CAMP v0.2.1 (Nov. 19, 2018)

		*   Fix issue in the setup.py that prevented building a correct
			Docker imag

	*   CAMP v0.2.0 (Nov. 19, 2018)

		*   Consolidated input files (now only one, as per [Issue
			19](https://github.com/STAMP-project/camp/issues/19))

		*   Input Validation (as per [Issue
			20](https://github.com/STAMP-project/camp/issues/20) and
			[Issue 21](https://github.com/STAMP-project/camp/issues/21))

		*   Support for coverage over integer variables (see Atos case-study,
			[Issue 22](https://github.com/STAMP-project/camp/issues/22))

		*   Integrate the solution of both case-study, so that both are solved
			with the same code.

		*   Revised the documentation ([Issue
			18](https://github.com/STAMP-project/camp/issues/18))

*   CAMP v0.1 (Oct. 23, 2018)

	*    First complete draft

	*    Common command line interface for all three commands,
         generate, realize and execute.
